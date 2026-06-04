# calcwindow.py
import csv
import os
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QFileDialog, QHeaderView
from PyQt6 import uic

from report_generator import generate_order_document

def generate_name_index(fio):
    """Генерирует именной индекс (например, Волков М. В. -> ВМВ)"""
    parts = fio.replace('.', ' ').split()
    index = ""
    for part in parts:
        if part:
            index += part[0].upper()
    return index if index else "КС"

def calculate_equipment(fio, head, height, chest, waist, shoe, finger_len, wrist_circ, arm_len, leg_len):
    name_index = generate_name_index(fio)

    shl_size = "1" if head < 58 else "2"

    base_size = int(round(chest / 2))
    if base_size % 2 != 0:
        base_size += 1
    base_size = max(44, min(base_size, 62))

    def size_by_length(val, borders):
        if val <= borders[0]:
            return 1
        elif val <= borders[1]:
            return 2
        elif val <= borders[2]:
            return 3
        return 4

    r_arm = size_by_length(arm_len, [62, 66, 70])
    r_leg = size_by_length(leg_len, [90, 96, 102])

    if waist <= 82:
        r_torso = 2
    elif waist <= 92:
        r_torso = 3
    else:
        r_torso = 4

    if height >= 182 and r_torso < 4:
        r_torso += 1

    suit_size = f"{base_size}-{r_arm}-{r_leg}-{r_torso}"

    if wrist_circ <= 17 and finger_len <= 7.5:
        gloves_gp = "1"
    elif wrist_circ <= 20 and finger_len <= 8.5:
        gloves_gp = "2"
    else:
        gloves_gp = "3"

    underwear_base = max(44, base_size - 2)
    if height < 165:
        underwear_height = 3
    elif height < 178:
        underwear_height = 4
    else:
        underwear_height = 5
    underwear_size = f"{underwear_base}/{underwear_height}"

    if shoe <= 39:
        socks_size = "25"
    elif shoe <= 43:
        socks_size = "27"
    else:
        socks_size = "29"

    gloves_start = "12" if wrist_circ >= 18 or finger_len >= 9.5 else "11"

    boots_size = str(max(37, min(int(shoe), 47)))
    insoles_size = str(max(36, int(boots_size) - 1))

    return {
        "name_index": name_index,
        "suit_size": suit_size,
        "shl_size": shl_size,
        "underwear_size": underwear_size,
        "gloves_gp": gloves_gp,
        "gloves_start": gloves_start,
        "socks_size": socks_size,
        "boots_size": boots_size,
        "insoles_size": insoles_size
    }

class CardDialog(QWidget):
    def __init__(self, astronaut_id, fio, gender, db_manager, parent=None):
        super().__init__()
        self.main_window = parent
        uic.loadUi("calc_window.ui", self)

        self.db = db_manager
        self.astronaut_id = astronaut_id
        self.fio = fio
        self.gender = gender
        self.calculated_data = {}

        self.labelAstranautName.setText(f"Космонавт: {fio}")
        self.tableResultKit.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        # Добавил 8 и 9 спинбоксы в список, чтобы они тоже триггерили перерасчет
        all_spins = [self.spinBox, self.spinBox_2, self.spinBox_3, self.spinBox_4,
                     self.spinBox_5, self.spinBox_6, self.spinBox_7, self.spinBox_8, self.spinBox_9]
        for spin in all_spins:
            spin.valueChanged.connect(self.auto_calculate)

        self.comboBox_2.currentTextChanged.connect(self.auto_calculate)
        self.comboBox.currentTextChanged.connect(self.auto_calculate)
        self.comboBox_3.currentTextChanged.connect(self.auto_calculate)

        self.btnSaveAllToDb.clicked.connect(self.save_to_database)
        self.btnResetInputs.clicked.connect(self.reset_inputs)
        self.btnCreateOrder.clicked.connect(self.create_word_order)

        # Вызов загрузки данных из базы или сброса на минимум
        self.load_or_reset_data()

    def load_or_reset_data(self):
        """Загружает данные из БД. Если пусто — ставит минимумы."""
        data = self.db.get_card_data(self.astronaut_id)
        if data:
            # Отключаем сигналы на секунду, чтобы программа не пересчитывала таблицу 10 раз при заполнении
            spins = [self.spinBox, self.spinBox_2, self.spinBox_3, self.spinBox_4,
                     self.spinBox_5, self.spinBox_6, self.spinBox_7, self.spinBox_8, self.spinBox_9]
            for s in spins:
                s.blockSignals(True)
            self.comboBox_2.blockSignals(True)

            self.comboBox_2.setCurrentText(data['suit_modification'])
            self.spinBox.setValue(data['head_circumference'])
            self.spinBox_2.setValue(data['height'])
            self.spinBox_3.setValue(data['chest_circumference'])
            self.spinBox_4.setValue(data['waist_circumference'])
            self.spinBox_5.setValue(data['shoe_size'])

            # Ставим данные (с защитой от того, если в БД записался NULL)
            self.spinBox_6.setValue(data['wrist_circ'] if data['wrist_circ'] is not None else 15)
            self.spinBox_7.setValue(data['finger_len'] if data['finger_len'] is not None else 5)
            self.spinBox_8.setValue(data['arm_len'] if data['arm_len'] is not None else 0)
            self.spinBox_9.setValue(data['leg_len'] if data['leg_len'] is not None else 0)

            # Включаем сигналы обратно и делаем один итоговый расчет
            for s in spins:
                s.blockSignals(False)
            self.comboBox_2.blockSignals(False)
            self.auto_calculate()
        else:
            self.reset_inputs()

    def auto_calculate(self):
        """Заполнение таблицы строго по твоим 10 колонкам интерфейса"""
        head = self.spinBox.value()
        height = self.spinBox_2.value()
        chest = self.spinBox_3.value()
        waist = self.spinBox_4.value()
        shoe = self.spinBox_5.value()
        finger_len = self.spinBox_6.value()
        wrist_circ = self.spinBox_7.value()
        arm_len = self.spinBox_8.value()
        leg_len = self.spinBox_9.value()

        # Считаем параметры
        res = calculate_equipment(self.fio, head, height, chest, waist, shoe, finger_len, wrist_circ, arm_len, leg_len)

        res["seni_size"] = self.comboBox.currentText()
        res["gloves_chainmail"] = self.comboBox_3.currentText()

        self.calculated_data = res

        self.tableResultKit.setRowCount(1)

        # ВЫРАВНИВАНИЕ ПО КОЛОНКАМ ИЗ ТВОЕГО UI СНИМКА:
        # 1. № Изделия | 2. Именной индекс | 3. Размер оболочки | 4. ГП-7С | 5. ШЛ-10СА
        # 6. Белье | 7. Носки | 8. Стельки | 9. Перчатки стартовые | 10. Обувь стартовая

        # Получаем ID изделия из базы данных (если оно привязано к карте, иначе пишем дефолтный инвентарный номер)
        product_id = str(self.astronaut_id + 500)  # Пример генерации ID изделия для тестов под твои цифры 528, 529...

        data_fields = [
            product_id,                 # 1. № Изделия (ID изделия из склада)
            res["name_index"],          # 2. Именной индекс
            res["suit_size"],           # 3. Размер оболочки
            res["gloves_gp"],           # 4. ГП-7С
            res["shl_size"],            # 5. ШЛ-10СА
            res["underwear_size"],      # 6. Белье
            res["socks_size"],          # 7. Носки (ГОСТ 8541-2014)
            res["insoles_size"],        # 8. Стельки
            res["gloves_start"],        # 9. Перчатки стартовые
            res["boots_size"]           # 10. Обувь стартовая
        ]

        # Пушим в ячейки
        for col_idx, value in enumerate(data_fields):
            if col_idx < self.tableResultKit.columnCount():
                self.tableResultKit.setItem(0, col_idx, QTableWidgetItem(str(value)))

    def create_word_order(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        default_name = f"Заказ_Наряд_{self.calculated_data['name_index']}.docx"
        default_path = os.path.join(current_dir, default_name)

        path, _ = QFileDialog.getSaveFileName(self, "Сохранить Заказ-Наряд", default_path, "Word Documents (*.docx)")
        if not path:
            return

        anthro_params = {
            'head': self.spinBox.value(), 'height': self.spinBox_2.value(),
            'chest': self.spinBox_3.value(), 'waist': self.spinBox_4.value(),
            'shoe': self.spinBox_5.value(), 'finger': self.spinBox_6.value(),
            'wrist': self.spinBox_7.value()
        }

        try:
            generate_order_document(
                path=path,
                astronaut_id=self.astronaut_id,
                fio=self.fio,
                gender=self.gender,
                suit_mod=self.comboBox_2.currentText(),
                anthro_params=anthro_params,
                calculated_data=self.calculated_data
            )
            QMessageBox.information(self, "Успех", f"Документ успешно сгенерирован!\nПуть: {path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сформировать документ: {e}")
    def reset_inputs(self):
        # Устанавливаем новые минимальные значения из твоего списка
        self.spinBox.setValue(55)      # Обхват головы
        self.spinBox_2.setValue(158)   # Рост
        self.spinBox_3.setValue(96)    # Обхват груди
        self.spinBox_4.setValue(82)    # Обхват талии
        self.spinBox_5.setValue(37)    # Размер обуви

        self.spinBox_6.setValue(15)     # Обхват запястья
        self.spinBox_7.setValue(5)    # Длина 3-го пальца

        # Сброс комбобоксов гигиены
        self.comboBox.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

        # Новые параметры (рука и нога) сбрасываем в 0
        self.spinBox_8.setValue(0)     # Длина руки
        self.spinBox_9.setValue(0)     # Длина ноги

        # Пересчитываем таблицу автоматически после сброса
        self.auto_calculate()

    def save_to_database(self):
        anthro = {
            'mod': self.comboBox_2.currentText(),
            'head': self.spinBox.value(),
            'height': self.spinBox_2.value(),
            'chest': self.spinBox_3.value(),
            'waist': self.spinBox_4.value(),
            'shoe': self.spinBox_5.value(),
            'wrist_circ': self.spinBox_6.value(),
            'finger_len': self.spinBox_7.value(),
            'arm_len': self.spinBox_8.value(),
            'leg_len': self.spinBox_9.value()
        }
        try:
            legacy_calculated = {
                "suit_size": self.calculated_data["suit_size"],
                "gp7s_qty": 1, "shl10sa_qty": 1,
                "underwear_size": self.calculated_data["underwear_size"],
                "socks_size": self.calculated_data["socks_size"],
                "insoles_size": self.calculated_data["insoles_size"],
                "gloves_size": self.calculated_data["gloves_gp"],
                "boots_size": self.calculated_data["boots_size"]
            }
            if self.db.save_card_data(self.astronaut_id, anthro, legacy_calculated):
                QMessageBox.information(self, "Успех", "Данные сохранены в СУБД.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка СУБД", f"Критический сбой: {e}")

    def closeEvent(self, event):
        if self.main_window:
            self.main_window.show()
        event.accept()