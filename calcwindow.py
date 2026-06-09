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

def calculate_equipment(fio, head, height, chest, waist, foot_size, finger_len, wrist_circ, arm_len, leg_len):
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

    r_arm_len = size_by_length(arm_len, [62, 66, 70])
    r_leg_len = size_by_length(leg_len, [90, 96, 102])

    if waist <= 82:
        r_torso = 2
    elif waist <= 92:
        r_torso = 3
    else:
        r_torso = 4

    if height >= 182 and r_torso < 4:
        r_torso += 1

    suit_size = f"{base_size}-{r_arm_len}-{r_leg_len}-{r_torso}"

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

    if foot_size <= 39:
        socks_size = 25
    elif foot_size <= 43:
        socks_size = 27
    else:
        socks_size = 29

    gloves_start = 12 if wrist_circ >= 18 or finger_len >= 9.5 else 11
    boots_size = max(37, min(int(foot_size), 47))
    insoles_size = max(36, int(boots_size) - 1)

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

        self.equipment_id = None

        self.labelAstranautName.setText(f"Космонавт: {fio}")
        self.tableResultKit.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        # Переназначаем спинбоксы на новые осмысленные имена элементов из UI
        self.all_spins = [
            self.doubleSpinBox_head, self.doubleSpinBox_height, self.doubleSpinBox_chest,
            self.doubleSpinBox_waist, self.doubleSpinBox_foot_size, self.doubleSpinBox_wrist_circ,
            self.doubleSpinBox_finger_len, self.doubleSpinBox_arm_len, self.doubleSpinBox_leg_len
        ]

        for spin in self.all_spins:
            spin.valueChanged.connect(self.auto_calculate)

        # Подвязываем обновленные ComboBox'ы (модификация, подгузники/трусы, кольчужные перчатки)
        self.comboBox_mod.currentTextChanged.connect(self.auto_calculate)
        self.comboBox_trousers_size.currentTextChanged.connect(self.auto_calculate)
        self.comboBox_surgical_chainmail_gloves_size.currentTextChanged.connect(self.auto_calculate)

        self.btnSaveAllToDb.clicked.connect(self.save_to_database)
        self.btnResetInputs.clicked.connect(self.reset_inputs)
        self.btnCreateOrder.clicked.connect(self.create_word_order)
        self.btnExportAnthroCsv.clicked.connect(self.export_anthro_to_csv)
        self.btnExportSpecCsv.clicked.connect(self.export_spec_to_csv)

        self.load_or_reset_data()


    def load_or_reset_data(self):
        """Загружает данные из БД с учетом новой структуры."""
        data = self.db.get_card_data(self.astronaut_id)
        if data:
            # Блокируем сигналы, чтобы избежать лавинообразных пересчетов во время инициализации полей
            for s in self.all_spins:
                s.blockSignals(True)
            self.comboBox_mod.blockSignals(True)

            self.comboBox_mod.setCurrentText(data['suit_modification'])
            self.doubleSpinBox_head.setValue(data['head_circumference'])
            self.doubleSpinBox_height.setValue(data['height'])
            self.doubleSpinBox_chest.setValue(data['chest_circumference'])
            self.doubleSpinBox_waist.setValue(data['waist_circumference'])
            self.doubleSpinBox_foot_size.setValue(data['foot_size'])

            self.doubleSpinBox_wrist_circ.setValue(data['wrist_circ'] if data['wrist_circ'] is not None else 15)
            self.doubleSpinBox_finger_len.setValue(data['finger_len'] if data['finger_len'] is not None else 5)
            self.doubleSpinBox_arm_len.setValue(data['arm_len'] if data['arm_len'] is not None else 0)
            self.doubleSpinBox_leg_len.setValue(data['leg_len'] if data['leg_len'] is not None else 0)
            self.comboBox_trousers_size.setCurrentText(data['trousers_size'] or 'M')
            self.comboBox_surgical_chainmail_gloves_size.setCurrentText(data['surgical_chainmail_gloves_size'] or 'M')

            self.equipment_id = data.get('equipment_id')
            for s in self.all_spins:
                s.blockSignals(False)
            self.comboBox_mod.blockSignals(False)
            self.auto_calculate()

        else:
            self.reset_inputs()

    def auto_calculate(self):
        """Заполнение таблицы строго по параметрам интерфейса"""
        head = self.doubleSpinBox_head.value()
        height = self.doubleSpinBox_height.value()
        chest = self.doubleSpinBox_chest.value()
        waist = self.doubleSpinBox_waist.value()
        foot_size = self.doubleSpinBox_foot_size.value()
        wrist_circ = self.doubleSpinBox_wrist_circ.value()
        finger_len = self.doubleSpinBox_finger_len.value()
        arm_len = self.doubleSpinBox_arm_len.value()
        leg_len = self.doubleSpinBox_leg_len.value()

        res = calculate_equipment(self.fio, head, height, chest, waist, foot_size, finger_len, wrist_circ, arm_len, leg_len)

        # Вытаскиваем значения из новых комбобоксов
        res["trousers_size"] = self.comboBox_trousers_size.currentText()
        res["surgical_chainmail_gloves_size"] = self.comboBox_surgical_chainmail_gloves_size.currentText()

        self.calculated_data = res
        self.tableResultKit.setRowCount(1)

        product_id = str(self.equipment_id) if self.equipment_id else "-"

        data_fields = [
            product_id,                  # 1. № Изделия
            res["name_index"],          # 2. Именной индекс
            res["suit_size"],           # 3. Размер оболочки
            res["gloves_gp"],           # 4. ГП-7С
            res["shl_size"],            # 5. ШЛ-10СА
            res["underwear_size"],      # 6. Белье
            res["socks_size"],          # 7. Носки
            res["insoles_size"],        # 8. Стельки
            res["gloves_start"],        # 9. Перчатки стартовые
            res["boots_size"]           # 10. Обувь стартовая
        ]

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
            'head': self.doubleSpinBox_head.value(), 'height': self.doubleSpinBox_height.value(),
            'chest': self.doubleSpinBox_chest.value(), 'waist': self.doubleSpinBox_waist.value(),
            'foot_size': self.doubleSpinBox_foot_size.value(), 'finger_len': self.doubleSpinBox_finger_len.value(),
            'wrist_circ': self.doubleSpinBox_wrist_circ.value(), 'arm_len': self.doubleSpinBox_arm_len.value(),
            'leg_len': self.doubleSpinBox_leg_len.value()
        }

        calculated_data_for_report = self.calculated_data.copy()
        calculated_data_for_report["product_id"] = self.equipment_id if self.equipment_id else 0
        try:
            generate_order_document(
                path=path,
                astronaut_id=self.astronaut_id,
                fio=self.fio,
                gender=self.gender,
                suit_mod=self.comboBox_mod.currentText(),
                anthro_params=anthro_params,
                calculated_data=calculated_data_for_report
            )
            QMessageBox.information(self, "Успех", f"Документ успешно сгенерирован!\nПуть: {path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сформировать документ: {e}")

    def reset_inputs(self):
        self.doubleSpinBox_head.setValue(55)
        self.doubleSpinBox_height.setValue(158)
        self.doubleSpinBox_chest.setValue(96)
        self.doubleSpinBox_waist.setValue(82)
        self.doubleSpinBox_foot_size.setValue(37)
        self.doubleSpinBox_wrist_circ.setValue(15)
        self.doubleSpinBox_finger_len.setValue(5)
        self.doubleSpinBox_arm_len.setValue(0)
        self.doubleSpinBox_leg_len.setValue(0)

        self.comboBox_trousers_size.setCurrentIndex(0)
        self.comboBox_surgical_chainmail_gloves_size.setCurrentIndex(0)
        self.auto_calculate()

    def save_to_database(self):
        anthro = {
            'mod': self.comboBox_mod.currentText(),
            'head': self.doubleSpinBox_head.value(),
            'height': self.doubleSpinBox_height.value(),
            'chest': self.doubleSpinBox_chest.value(),
            'waist': self.doubleSpinBox_waist.value(),
            'foot_size': self.doubleSpinBox_foot_size.value(),
            'wrist_circ': self.doubleSpinBox_wrist_circ.value(),
            'finger_len': self.doubleSpinBox_finger_len.value(),
            'arm_len': self.doubleSpinBox_arm_len.value(),
            'leg_len': self.doubleSpinBox_leg_len.value()
        }
        try:
            # Формируем словарь под новые колонки СУБД
            legacy_calculated = {
                "suit_size": self.calculated_data["suit_size"],
                "gp7s_qty": 1,
                "shl10sa_qty": 1,
                "underwear_size": self.calculated_data["underwear_size"],
                "socks_size": self.calculated_data["socks_size"],
                "insoles_size": self.calculated_data["insoles_size"],
                "gloves_size": int(self.calculated_data["gloves_gp"]),
                "boots_size": self.calculated_data["boots_size"],
                # Новые параметры:
                "surgical_chainmail_gloves_size": self.calculated_data["surgical_chainmail_gloves_size"],
                "trousers_size": self.calculated_data["trousers_size"]
            }
            equip_id = self.db.save_card_data(self.astronaut_id, anthro, legacy_calculated)
            if equip_id:
                self.equipment_id = equip_id
                QMessageBox.information(self, "Успех", "Данные сохранены в СУБД.")
                self.auto_calculate()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка СУБД", f"Критический сбой: {e}")

    def export_anthro_to_csv(self):
        """Экспорт текущих значений антропометрии в CSV"""
        path, _ = QFileDialog.getSaveFileName(self, "Экспорт антропометрии", "", "CSV Files (*.csv)")
        if not path:
            return
        headers = ["Параметр", "Значение"]
        rows = [
            ("Обхват головы, см", self.doubleSpinBox_head.value()),
            ("Рост, см", self.doubleSpinBox_height.value()),
            ("Обхват груди, см", self.doubleSpinBox_chest.value()),
            ("Обхват талии, см", self.doubleSpinBox_waist.value()),
            ("Размер стопы", self.doubleSpinBox_foot_size.value()),
            ("Обхват кисти, см", self.doubleSpinBox_wrist_circ.value()),
            ("Длина 3-го пальца, см", self.doubleSpinBox_finger_len.value()),
            ("Длина руки, см", self.doubleSpinBox_arm_len.value()),
            ("Длина ноги по боку, см", self.doubleSpinBox_leg_len.value()),
            ("Модификация скафандра", self.comboBox_mod.currentText()),
        ]
        with open(path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(headers)
            writer.writerows(rows)
        QMessageBox.information(self, "Успех", f"Антропометрия сохранена в {path}")

    def export_spec_to_csv(self):
        """Экспорт таблицы с результатами подбора в CSV"""
        path, _ = QFileDialog.getSaveFileName(self, "Экспорт спецификации", "", "CSV Files (*.csv)")
        if not path:
            return
        headers = [self.tableResultKit.horizontalHeaderItem(i).text() for i in range(self.tableResultKit.columnCount())]
        row_data = []
        for col in range(self.tableResultKit.columnCount()):
            item = self.tableResultKit.item(0, col)
            row_data.append(item.text() if item else "")
        with open(path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(headers)
            writer.writerow(row_data)
        QMessageBox.information(self, "Успех", f"Спецификация сохранена в {path}")

    def closeEvent(self, event):
        if self.main_window:
            self.main_window.show()
        event.accept()