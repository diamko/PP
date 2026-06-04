import psycopg2
from psycopg2.extras import DictCursor
from config import DB_CONFIG

class DatabaseManager:
    def _get_connection(self):
        conn = psycopg2.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            cursor.execute('SET search_path TO "AstroDate";')
        return conn

    def add_astronaut(self, last_name, first_name, patronymic, gender):
        query = """
            INSERT INTO astronauts (last_name, first_name, patronymic, gender)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (last_name, first_name, patronymic, gender))
                    new_id = cursor.fetchone()[0]
                conn.commit()
                return new_id
        except Exception as e:
            print(f"Ошибка при добавлении космонавта: {e}")
            return None

    def delete_astronaut(self, astronaut_id):
        """Удаление космонавта по ID."""
        query = "DELETE FROM astronauts WHERE id = %s;"
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (astronaut_id,))
                conn.commit()
                return True
        except Exception as e:
            print(f"Ошибка при удалении космонавта: {e}")
            return False

    def get_astronauts(self, search_text=""):
        query = """
            SELECT id, CONCAT_WS(' ', last_name, first_name, patronymic) AS fio, gender
            FROM astronauts
            WHERE CONCAT_WS(' ', last_name, first_name, patronymic) ILIKE %s
            ORDER BY last_name;
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute(query, (f"%{search_text}%",))
                    return cursor.fetchall()
        except Exception as e:
            print(f"Ошибка получения данных: {e}")
            return []
    def get_card_data(self, astronaut_id):
        """Получает сохраненную антропометрию из БД для карточки"""
        query = """
            SELECT suit_modification, head_circumference, height,
                   chest_circumference, waist_circumference, feet_size,
                   finger_len, wrist_circ, arm_len, leg_len
            FROM anthropometry
            WHERE astronaut_id = %s;
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute(query, (astronaut_id,))
                    return cursor.fetchone()
        except Exception as e:
            print(f"Ошибка получения данных карты: {e}")
            return None

    def save_card_data(self, astronaut_id, anthro, equip):
        # 1. Запрос для антропометрии (все 4 новых параметра перенесены сюда)
        q_anthro = """
            INSERT INTO anthropometry (
                astronaut_id, suit_modification, head_circumference, height,
                chest_circumference, waist_circumference, feet_size,
                finger_len, wrist_circ, arm_len, leg_len
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (astronaut_id) DO UPDATE SET
                suit_modification = EXCLUDED.suit_modification,
                head_circumference = EXCLUDED.head_circumference,
                height = EXCLUDED.height,
                chest_circumference = EXCLUDED.chest_circumference,
                waist_circumference = EXCLUDED.waist_circumference,
                feet_size = EXCLUDED.feet_size,
                finger_len = EXCLUDED.finger_len,
                wrist_circ = EXCLUDED.wrist_circ,
                arm_len = EXCLUDED.arm_len,
                leg_len = EXCLUDED.leg_len;
        """

        # 2. Запрос для снаряжения (остается чистым, без антропометрии)
        q_equip = """
            INSERT INTO equipment_selection (
                astronaut_id, suit_size, gp7s_qty, shl10sa_qty,
                underwear_size, socks_size, insoles_size, gloves_size, boots_size
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (astronaut_id) DO UPDATE SET
                suit_size = EXCLUDED.suit_size,
                gp7s_qty = EXCLUDED.gp7s_qty,
                shl10sa_qty = EXCLUDED.shl10sa_qty,
                underwear_size = EXCLUDED.underwear_size,
                socks_size = EXCLUDED.socks_size,
                insoles_size = EXCLUDED.insoles_size,
                gloves_size = EXCLUDED.gloves_size,
                boots_size = EXCLUDED.boots_size;
        """

        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                # Передаем старые + 4 новых параметра из словаря anthro
                cursor.execute(q_anthro, (
                    astronaut_id,
                    anthro['mod'],
                    anthro['head'],
                    anthro['height'],
                    anthro['chest'],
                    anthro['waist'],
                    anthro['shoe'],
                    anthro.get('finger_len', 0),  # Используем .get() на случай, если ключа нет
                    anthro.get('wrist_circ', 0),
                    anthro.get('arm_len', 0),
                    anthro.get('leg_len', 0)
                ))

                # Передаем данные снаряжения
                cursor.execute(q_equip, (
                    astronaut_id,
                    equip['suit_size'],
                    equip['gp7s_qty'],
                    equip['shl10sa_qty'],
                    equip['underwear_size'],
                    equip['socks_size'],
                    equip['insoles_size'],
                    equip['gloves_size'],
                    equip['boots_size']
                ))
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()