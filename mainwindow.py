# mainwindow.py
import sys
import os
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt6 import uic
from database import DatabaseManager
from add_astronaut_dialog import AddAstronautDialog
from calcwindow import CardDialog

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)

        self.db = DatabaseManager()

        # Привязка системных действий
        self.lineEdit.textChanged.connect(self.load_data)
        self.btnDeleteAstronaut.clicked.connect(self.delete_selected_astronaut)
        self.btnOpenOrdersLog.clicked.connect(self.export_to_csv)
        self.btnAddAstronaut.clicked.connect(self.open_add_dialog)
        self.btnOpenCard.clicked.connect(self.open_card)

        # Двойной клик по ячейке также может вызывать карточку расчетов
        self.tableAstronauts.cellDoubleClicked.connect(self.open_card)

        self.load_data()

    def open_add_dialog(self):
        dialog = AddAstronautDialog(self.db, self)
        if dialog.exec():
            self.load_data()

    def load_data(self):
        search_text = self.lineEdit.text()
        astronauts = self.db.get_astronauts(search_text)

        self.tableAstronauts.setRowCount(0)
        if not astronauts:
            return

        self.tableAstronauts.setRowCount(len(astronauts))
        for row_idx, data in enumerate(astronauts):
            item_id = QTableWidgetItem(str(data['id']))
            self.tableAstronauts.setItem(row_idx, 0, item_id)
            self.tableAstronauts.setItem(row_idx, 1, QTableWidgetItem(data['fio']))
            item_id.setData(100, data['gender'])

    def open_card(self, row=None, column=None):
        """Открытие карточки (работает и по кнопке, и по двойному клику)."""
        current_row = self.tableAstronauts.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Внимание", "Выберите космонавта из списка!")
            return

        ast_id = int(self.tableAstronauts.item(current_row, 0).text())
        fio = self.tableAstronauts.item(current_row, 1).text()
        gender = self.tableAstronauts.item(current_row, 0).data(100)

        # Скрываем главное окно и открываем карточку расчетов
        self.hide()
        self.card_window = CardDialog(ast_id, fio, gender, self.db, parent=self)
        self.card_window.show()

    def delete_selected_astronaut(self):
        current_row = self.tableAstronauts.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Внимание", "Выберите кого удалить!")
            return

        ast_id = int(self.tableAstronauts.item(current_row, 0).text())
        fio = self.tableAstronauts.item(current_row, 1).text()

        confirm = QMessageBox.question(
            self, "Удаление", f"Вы уверены, что хотите удалить космонавта {fio} и все его параметры?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            if self.db.delete_astronaut(ast_id):
                QMessageBox.information(self, "Успех", "Запись успешно удалена.")
                self.load_data()
            else:
                QMessageBox.critical(self, "Ошибка", "Не удалось удалить запись из СУБД.")

    def export_to_csv(self):
        if self.tableAstronauts.rowCount() == 0:
            QMessageBox.warning(self, "Экспорт", "Таблица пуста, нечего экспортировать.")
            return

        current_dir = os.path.dirname(os.path.abspath(__file__))
        default_path = os.path.join(current_dir, "реестр_экипажа.csv")

        path, _ = QFileDialog.getSaveFileName(self, "Сохранить отчет", default_path, "CSV Files (*.csv)")
        if not path:
            return

        try:
            with open(path, 'w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file, delimiter=';')
                headers = [self.tableAstronauts.horizontalHeaderItem(i).text() for i in range(self.tableAstronauts.columnCount())]
                writer.writerow(headers)

                for row in range(self.tableAstronauts.rowCount()):
                    row_data = []
                    for col in range(self.tableAstronauts.columnCount()):
                        item = self.tableAstronauts.item(row, col)
                        row_data.append(item.text() if item else "")
                    writer.writerow(row_data)

            QMessageBox.information(self, "Успех", f"Данные сохранены в файл:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Критический сбой экспорта: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())