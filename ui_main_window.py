# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.tableAstronauts = QTableWidget(self.centralwidget)
        if (self.tableAstronauts.columnCount() < 2):
            self.tableAstronauts.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableAstronauts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableAstronauts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableAstronauts.setObjectName(u"tableAstronauts")
        self.tableAstronauts.setSortingEnabled(True)
        self.tableAstronauts.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableAstronauts)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAddAstronaut = QPushButton(self.centralwidget)
        self.btnAddAstronaut.setObjectName(u"btnAddAstronaut")

        self.horizontalLayout.addWidget(self.btnAddAstronaut)

        self.btnEditAstronaut = QPushButton(self.centralwidget)
        self.btnEditAstronaut.setObjectName(u"btnEditAstronaut")

        self.horizontalLayout.addWidget(self.btnEditAstronaut)

        self.btnOpenCard = QPushButton(self.centralwidget)
        self.btnOpenCard.setObjectName(u"btnOpenCard")

        self.horizontalLayout.addWidget(self.btnOpenCard)

        self.btnDeleteAstronaut = QPushButton(self.centralwidget)
        self.btnDeleteAstronaut.setObjectName(u"btnDeleteAstronaut")

        self.horizontalLayout.addWidget(self.btnDeleteAstronaut)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.btnOpenOrdersLog = QPushButton(self.centralwidget)
        self.btnOpenOrdersLog.setObjectName(u"btnOpenOrdersLog")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnOpenOrdersLog.sizePolicy().hasHeightForWidth())
        self.btnOpenOrdersLog.setSizePolicy(sizePolicy1)
        self.btnOpenOrdersLog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.btnOpenOrdersLog)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tableAstronauts.cellDoubleClicked.connect(MainWindow.open_card)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0435\u0441\u0442\u0440 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0418\u0421\u041a", None))
        ___qtablewidgetitem = self.tableAstronauts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tableAstronauts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.btnAddAstronaut.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0433\u043e \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.btnEditAstronaut.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.btnOpenCard.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043a\u0430\u0440\u0442\u0443 \u043f\u043e\u0434\u0431\u043e\u0440\u0430", None))
        self.btnDeleteAstronaut.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 \u0440\u0435\u0435\u0441\u0442\u0440\u0430", None))
        self.btnOpenOrdersLog.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0436\u0443\u0440\u043d\u0430\u043b \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u044f\u0432\u043e\u043a", None))
    # retranslateUi

