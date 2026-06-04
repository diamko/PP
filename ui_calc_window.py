# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1223, 348)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelAstranautName = QLabel(Form)
        self.labelAstranautName.setObjectName(u"labelAstranautName")

        self.verticalLayout.addWidget(self.labelAstranautName)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_14 = QVBoxLayout(self.tab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(300, 20, 300, 0)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.comboBox_mod = QComboBox(self.tab)
        self.comboBox_mod.addItem("")
        self.comboBox_mod.addItem("")
        self.comboBox_mod.addItem("")
        self.comboBox_mod.setObjectName(u"comboBox_mod")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_mod.sizePolicy().hasHeightForWidth())
        self.comboBox_mod.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.comboBox_mod)


        self.verticalLayout_14.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 30, -1, 30)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_4)

        self.doubleSpinBox_head = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_head.setObjectName(u"doubleSpinBox_head")

        self.verticalLayout_3.addWidget(self.doubleSpinBox_head)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_5)

        self.doubleSpinBox_height = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_height.setObjectName(u"doubleSpinBox_height")

        self.verticalLayout_4.addWidget(self.doubleSpinBox_height)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_6)

        self.doubleSpinBox_chest = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_chest.setObjectName(u"doubleSpinBox_chest")

        self.verticalLayout_5.addWidget(self.doubleSpinBox_chest)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_7)

        self.doubleSpinBox_waist = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_waist.setObjectName(u"doubleSpinBox_waist")

        self.verticalLayout_6.addWidget(self.doubleSpinBox_waist)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_8)

        self.doubleSpinBox_foot_size = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_foot_size.setObjectName(u"doubleSpinBox_foot_size")

        self.verticalLayout_7.addWidget(self.doubleSpinBox_foot_size)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label)

        self.doubleSpinBox_wrist_circ = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_wrist_circ.setObjectName(u"doubleSpinBox_wrist_circ")

        self.verticalLayout_8.addWidget(self.doubleSpinBox_wrist_circ)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_2)

        self.doubleSpinBox_finger_len = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_finger_len.setObjectName(u"doubleSpinBox_finger_len")

        self.verticalLayout_10.addWidget(self.doubleSpinBox_finger_len)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_11)

        self.doubleSpinBox_arm_len = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_arm_len.setObjectName(u"doubleSpinBox_arm_len")

        self.verticalLayout_11.addWidget(self.doubleSpinBox_arm_len)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_12)

        self.doubleSpinBox_leg_len = QDoubleSpinBox(self.tab)
        self.doubleSpinBox_leg_len.setObjectName(u"doubleSpinBox_leg_len")

        self.verticalLayout_13.addWidget(self.doubleSpinBox_leg_len)


        self.horizontalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_14.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btnResetInputs = QPushButton(self.tab)
        self.btnResetInputs.setObjectName(u"btnResetInputs")
        sizePolicy2.setHeightForWidth(self.btnResetInputs.sizePolicy().hasHeightForWidth())
        self.btnResetInputs.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.btnResetInputs)

        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.btnExportAnthroCsv = QPushButton(self.tab)
        self.btnExportAnthroCsv.setObjectName(u"btnExportAnthroCsv")
        sizePolicy2.setHeightForWidth(self.btnExportAnthroCsv.sizePolicy().hasHeightForWidth())
        self.btnExportAnthroCsv.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.btnExportAnthroCsv)


        self.verticalLayout_14.addLayout(self.horizontalLayout_15)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.tableResultKit = QTableWidget(self.tab_2)
        if (self.tableResultKit.columnCount() < 10):
            self.tableResultKit.setColumnCount(10)
        font = QFont()
        font.setPointSize(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font)
        self.tableResultKit.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableResultKit.rowCount() < 1):
            self.tableResultKit.setRowCount(1)
        self.tableResultKit.setObjectName(u"tableResultKit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(10)
        sizePolicy3.setHeightForWidth(self.tableResultKit.sizePolicy().hasHeightForWidth())
        self.tableResultKit.setSizePolicy(sizePolicy3)
        self.tableResultKit.setMinimumSize(QSize(0, 40))
        self.tableResultKit.setStyleSheet(u"QHeaderView::section {\n"
"white-space: normal;\n"
"text-align: center;\n"
"}")
        self.tableResultKit.setLineWidth(1)
        self.tableResultKit.setSortingEnabled(True)
        self.tableResultKit.setRowCount(1)
        self.tableResultKit.horizontalHeader().setMinimumSectionSize(100)
        self.tableResultKit.horizontalHeader().setDefaultSectionSize(118)
        self.tableResultKit.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableResultKit.horizontalHeader().setStretchLastSection(True)
        self.tableResultKit.verticalHeader().setVisible(False)
        self.tableResultKit.verticalHeader().setMinimumSectionSize(40)
        self.tableResultKit.verticalHeader().setDefaultSectionSize(41)
        self.tableResultKit.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableResultKit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setMargin(0)

        self.horizontalLayout.addWidget(self.label_10)

        self.comboBox_surgical_chainmail_gloves_size = QComboBox(self.tab_2)
        self.comboBox_surgical_chainmail_gloves_size.addItem("")
        self.comboBox_surgical_chainmail_gloves_size.addItem("")
        self.comboBox_surgical_chainmail_gloves_size.addItem("")
        self.comboBox_surgical_chainmail_gloves_size.setObjectName(u"comboBox_surgical_chainmail_gloves_size")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(20)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox_surgical_chainmail_gloves_size.sizePolicy().hasHeightForWidth())
        self.comboBox_surgical_chainmail_gloves_size.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.comboBox_surgical_chainmail_gloves_size)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.comboBox_trousers_size = QComboBox(self.tab_2)
        self.comboBox_trousers_size.addItem("")
        self.comboBox_trousers_size.addItem("")
        self.comboBox_trousers_size.addItem("")
        self.comboBox_trousers_size.setObjectName(u"comboBox_trousers_size")
        sizePolicy4.setHeightForWidth(self.comboBox_trousers_size.sizePolicy().hasHeightForWidth())
        self.comboBox_trousers_size.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.comboBox_trousers_size)

        self.horizontalSpacer_6 = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btnExportSpecCsv = QPushButton(self.tab_2)
        self.btnExportSpecCsv.setObjectName(u"btnExportSpecCsv")

        self.horizontalLayout_10.addWidget(self.btnExportSpecCsv)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.btnCreateOrder = QPushButton(self.tab_2)
        self.btnCreateOrder.setObjectName(u"btnCreateOrder")

        self.horizontalLayout_10.addWidget(self.btnCreateOrder)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btnSaveAllToDb = QPushButton(Form)
        self.btnSaveAllToDb.setObjectName(u"btnSaveAllToDb")

        self.horizontalLayout_13.addWidget(self.btnSaveAllToDb)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.btnCancelAndBack = QPushButton(Form)
        self.btnCancelAndBack.setObjectName(u"btnCancelAndBack")

        self.horizontalLayout_13.addWidget(self.btnCancelAndBack)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        QWidget.setTabOrder(self.tabWidget, self.comboBox_mod)
        QWidget.setTabOrder(self.comboBox_mod, self.doubleSpinBox_head)
        QWidget.setTabOrder(self.doubleSpinBox_head, self.doubleSpinBox_height)
        QWidget.setTabOrder(self.doubleSpinBox_height, self.doubleSpinBox_chest)
        QWidget.setTabOrder(self.doubleSpinBox_chest, self.doubleSpinBox_waist)
        QWidget.setTabOrder(self.doubleSpinBox_waist, self.doubleSpinBox_foot_size)
        QWidget.setTabOrder(self.doubleSpinBox_foot_size, self.btnExportAnthroCsv)
        QWidget.setTabOrder(self.btnExportAnthroCsv, self.tableResultKit)
        QWidget.setTabOrder(self.tableResultKit, self.btnSaveAllToDb)
        QWidget.setTabOrder(self.btnSaveAllToDb, self.btnExportSpecCsv)
        QWidget.setTabOrder(self.btnExportSpecCsv, self.btnCreateOrder)
        QWidget.setTabOrder(self.btnCreateOrder, self.btnResetInputs)
        QWidget.setTabOrder(self.btnResetInputs, self.btnCancelAndBack)

        self.retranslateUi(Form)
        self.btnCancelAndBack.clicked.connect(Form.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelAstranautName.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0441\u043a\u0430\u0444\u0430\u043d\u0434\u0440\u0430:", None))
        self.comboBox_mod.setItemText(0, QCoreApplication.translate("Form", u"\u0420\u0414\u0421\u041f-3\u041c", None))
        self.comboBox_mod.setItemText(1, QCoreApplication.translate("Form", u"\u0420\u0414\u0421\u041f-3\u041c-01", None))
        self.comboBox_mod.setItemText(2, QCoreApplication.translate("Form", u"\u0420\u0414\u0422-1", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0445\u0432\u0430\u0442 \u0433\u043e\u043b\u043e\u0432\u044b, \u0441\u043c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0420\u043e\u0441\u0442, \u0441\u043c", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0445\u0432\u0430\u0442 \u0433\u0440\u0443\u0434\u0438", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0445\u0432\u0430\u0442 \u0442\u0430\u043b\u0438\u0438", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0441\u0442\u043e\u043f\u044b", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0445\u0432\u0430\u0442 \u043a\u0438\u0441\u0442\u0438, \u0441\u043c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u043d\u0430 3-\u0433\u043e \u043f\u0430\u043b\u044c\u0446\u0430, \u0441\u043c", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u043d\u0430 \u0440\u0443\u043a\u0438 (\u0440\u0443\u043a\u0430\u0432\u0430),\u0441\u043c", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u043d\u0430 \u043d\u043e\u0433\u0438 \u043f\u043e \u0431\u043e\u043a\u0443, \u0441\u043c", None))
        self.btnResetInputs.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.btnExportAnthroCsv.setText(QCoreApplication.translate("Form", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0430\u043d\u0442\u0440\u043e\u043f\u043e\u043c\u0435\u0442\u0440\u0438\u0438 (CSV)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0412\u0445\u043e\u0434\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0438 \u0420\u0430\u0441\u0447\u0435\u0442", None))
        ___qtablewidgetitem = self.tableResultKit.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u2116\u0418\u0437\u0434", None))
        ___qtablewidgetitem1 = self.tableResultKit.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u0435\u043d\u043d\u043e\u0439 \u0438\u043d\u0434\u0435\u043a\u0441", None))
        ___qtablewidgetitem2 = self.tableResultKit.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043e\u0431\u043e\u043b\u043e\u0447\u043a\u0438", None))
        ___qtablewidgetitem3 = self.tableResultKit.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0413\u041f-7\u0421", None))
        ___qtablewidgetitem4 = self.tableResultKit.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0428\u041b-10\u0421\u0410", None))
        ___qtablewidgetitem5 = self.tableResultKit.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0411\u0435\u043b\u044c\u0435", None))
        ___qtablewidgetitem6 = self.tableResultKit.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0441\u043a\u0438", None))
        ___qtablewidgetitem7 = self.tableResultKit.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0435\u043b\u044c\u043a\u0438", None))
        ___qtablewidgetitem8 = self.tableResultKit.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0447\u0430\u0442\u043a\u0438 \u0441\u0442\u0430\u0440\u0442\u043e\u0432\u044b\u0435", None))
        ___qtablewidgetitem9 = self.tableResultKit.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0443\u0432\u044c \u0441\u0442\u0430\u0440\u0442\u043e\u0432\u0430\u044f", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0447\u0430\u0442\u043a\u0438 \u043a\u043e\u043b\u044c\u0447\u0443\u0436\u043d\u044b\u0435 \u0445\u0438\u0440\u0443\u0440\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0435 - \u0440\u0430\u0437\u043c\u0435\u0440", None))
        self.comboBox_surgical_chainmail_gloves_size.setItemText(0, QCoreApplication.translate("Form", u"M", None))
        self.comboBox_surgical_chainmail_gloves_size.setItemText(1, QCoreApplication.translate("Form", u"L", None))
        self.comboBox_surgical_chainmail_gloves_size.setItemText(2, QCoreApplication.translate("Form", u"S", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"\u042d\u043b\u0430\u0441\u0442\u0438\u0447\u043d\u044b\u0435 \u0432\u043f\u0438\u0442\u044b\u0432\u0430\u044e\u0449\u0438\u0435 \u0442\u0440\u0443\u0441\u044b - \u0440\u0430\u0437\u043c\u0435\u0440", None))
        self.comboBox_trousers_size.setItemText(0, QCoreApplication.translate("Form", u"M", None))
        self.comboBox_trousers_size.setItemText(1, QCoreApplication.translate("Form", u"L", None))
        self.comboBox_trousers_size.setItemText(2, QCoreApplication.translate("Form", u"S", None))

        self.btnExportSpecCsv.setText(QCoreApplication.translate("Form", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0441\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 (CSV)", None))
        self.btnCreateOrder.setText(QCoreApplication.translate("Form", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u043e\u0434\u0431\u043e\u0440\u0430", None))
        self.btnSaveAllToDb.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0411\u0414", None))
        self.btnCancelAndBack.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434 \u043a \u0440\u0435\u0435\u0441\u0442\u0440\u0443", None))
    # retranslateUi

