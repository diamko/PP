# database.py
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
        """Удаление космонавта по ID. Благодаря ON DELETE CASCADE,
        связанные антропометрия и снаряжение удалятся автоматически."""
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
            SELECT a.suit_modification, a.head_circumference, a.height,
                   a.chest_circumference, a.waist_circumference, a.foot_size,
                   a.finger_len, a.wrist_circ, a.arm_len, a.leg_len,
                   e.trousers_size, e.surgical_chainmail_gloves_size, e.id AS equipment_id
            FROM anthropometry a
            LEFT JOIN equipment_selection e ON a.astronaut_id = e.astronaut_id
            WHERE a.astronaut_id = %s;
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
        # 1. Запрос для антропометрии (учитывая новые ENUM и названия колонок)
        q_anthro = """
            INSERT INTO anthropometry (
                astronaut_id, suit_modification, head_circumference, height,
                chest_circumference, waist_circumference, foot_size,
                finger_len, wrist_circ, arm_len, leg_len
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (astronaut_id) DO UPDATE SET
                suit_modification = EXCLUDED.suit_modification,
                head_circumference = EXCLUDED.head_circumference,
                height = EXCLUDED.height,
                chest_circumference = EXCLUDED.chest_circumference,
                waist_circumference = EXCLUDED.waist_circumference,
                foot_size = EXCLUDED.foot_size,
                finger_len = EXCLUDED.finger_len,
                wrist_circ = EXCLUDED.wrist_circ,
                arm_len = EXCLUDED.arm_len,
                leg_len = EXCLUDED.leg_len;
        """

        # 2. Запрос для снаряжения (добавлены 2 новые колонки: surgical_chainmail_gloves_size и trousers_size)
        q_equip = """
            INSERT INTO equipment_selection (
                astronaut_id, suit_size, gp7s_qty, shl10sa_qty,
                underwear_size, socks_size, insoles_size, surgical_chainmail_gloves_size,
                boots_size, gloves_size, trousers_size
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (astronaut_id) DO UPDATE SET
                suit_size = EXCLUDED.suit_size,
                gp7s_qty = EXCLUDED.gp7s_qty,
                shl10sa_qty = EXCLUDED.shl10sa_qty,
                underwear_size = EXCLUDED.underwear_size,
                socks_size = EXCLUDED.socks_size,
                insoles_size = EXCLUDED.insoles_size,
                surgical_chainmail_gloves_size = EXCLUDED.surgical_chainmail_gloves_size,
                boots_size = EXCLUDED.boots_size,
                gloves_size = EXCLUDED.gloves_size,
                trousers_size = EXCLUDED.trousers_size;
        """

        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                # Отправляем параметры антропометрии
                cursor.execute(q_anthro, (
                    astronaut_id,
                    anthro['mod'],
                    anthro['head'],
                    anthro['height'],
                    anthro['chest'],
                    anthro['waist'],
                    anthro['foot_size'],
                    anthro.get('finger_len', 0),
                    anthro.get('wrist_circ', 0),
                    anthro.get('arm_len', 0),
                    anthro.get('leg_len', 0)
                ))

                # Отправляем параметры снаряжения
                cursor.execute(q_equip, (
                    astronaut_id,
                    equip['suit_size'],
                    equip['gp7s_qty'],
                    equip['shl10sa_qty'],
                    equip['underwear_size'],
                    equip['socks_size'],
                    equip['insoles_size'],
                    equip['surgical_chainmail_gloves_size'],
                    equip['boots_size'],
                    equip['gloves_size'],
                    equip['trousers_size']
                ))
                cursor.execute("""
                    SELECT id FROM equipment_selection WHERE astronaut_id = %s
                """, (astronaut_id,))
                equip_id = cursor.fetchone()[0]

            conn.commit()
            return equip_id
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()