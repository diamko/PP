# utils.py
from PyQt6.QtWidgets import QApplication

def center_window(window):
    screen_center = QApplication.primaryScreen().geometry().center()
    window.move(screen_center - window.rect().center())