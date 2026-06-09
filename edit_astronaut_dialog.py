from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic


class EditAstronautDialog(QDialog):
    def __init__(self, astronaut_id, last_name, first_name, patronymic, gender, db_manager, parent=None):
        super().__init__(parent)
        uic.loadUi("edit_astronaut_dialog.ui", self)   # загружаем новый файл
        self.db = db_manager
        self.astronaut_id = astronaut_id

        # Заполнение полей
        self.lineEditLastName.setText(last_name)
        self.lineEditFirstName.setText(first_name)
        self.lineEditPatronymic.setText(patronymic)
        index = self.comboBoxGender.findText(gender)
        if index >= 0:
            self.comboBoxGender.setCurrentIndex(index)

    def accept(self):
        last_name = self.lineEditLastName.text().strip()
        first_name = self.lineEditFirstName.text().strip()
        patronymic = self.lineEditPatronymic.text().strip()
        gender = self.comboBoxGender.currentText()

        if not last_name or not first_name:
            QMessageBox.warning(self, "Предупреждение", "Фамилия и имя обязательны!")
            return

        success = self.db.update_astronaut(self.astronaut_id, last_name, first_name, patronymic, gender)
        if success:
            QMessageBox.information(self, "Успех", "Данные обновлены")
            super().accept()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось обновить запись")