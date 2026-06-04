from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic

class AddAstronautDialog(QDialog):
    def __init__(self, db_manager, parent=None):
        super().__init__(parent)
        uic.loadUi("add_astronaut.ui", self)
        self.db = db_manager

    def accept(self):
        last_name = self.lineEditLastName.text().strip()
        first_name = self.lineEditFirstName.text().strip()
        patronymic = self.lineEditPatronymic.text().strip()
        gender = self.comboBoxGender.currentText()

        if not last_name or not first_name:
            QMessageBox.warning(self, "Предупреждение", "Поля 'Фамилия' и 'Имя' обязательны!")
            return

        new_id = self.db.add_astronaut(last_name, first_name, patronymic, gender)

        if new_id:
            QMessageBox.information(self, "Успех", "Космонавт успешно добавлен.")
            super().accept()
        else:
            QMessageBox.critical(self, "Ошибка", "Ошибка сохранения в базу данных.")