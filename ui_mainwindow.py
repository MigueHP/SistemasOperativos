# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLCDNumber, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(406, 300)
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #333;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #444;\n"
"    color: #fff;\n"
"    border: 1px solid #666;\n"
"    selection-background-color: #555;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #555;\n"
"    color: #fff;\n"
"    border: 1px solid #666;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    color: #fff;\n"
"}\n"
"\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    background-color: #444;\n"
"    border: 1px solid #666;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked, QRadioButton::indicator:unchecked {\n"
"    background-color: #333;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    background-color: #555;\n"
"    border: 1px solid #666;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: #333;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: #333;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-c"
                        "olor: #555;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #444;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: #444;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #555;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #777;\n"
"}\n"
"\n"
"QFrame#separatorLine {\n"
"    background-color: #666;\n"
"    width: 2px;  /* Ajusta el ancho de la l\u00ednea seg\u00fan tus preferencias */\n"
"    margin: 0 5px;  /* Ajusta los m\u00e1rgenes seg\u00fan tus preferencias */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.no_procesos = QSpinBox(Dialog)
        self.no_procesos.setObjectName(u"no_procesos")
        self.no_procesos.setGeometry(QRect(70, 160, 42, 22))
        self.no_procesos_2 = QSpinBox(Dialog)
        self.no_procesos_2.setObjectName(u"no_procesos_2")
        self.no_procesos_2.setGeometry(QRect(110, 10, 42, 22))
        self.no_procesos_3 = QSpinBox(Dialog)
        self.no_procesos_3.setObjectName(u"no_procesos_3")
        self.no_procesos_3.setGeometry(QRect(240, 160, 42, 22))
        self.no_procesos_4 = QSpinBox(Dialog)
        self.no_procesos_4.setObjectName(u"no_procesos_4")
        self.no_procesos_4.setGeometry(QRect(100, 250, 42, 22))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 200, 113, 20))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 130, 211, 20))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(140, 160, 69, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 20))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 40, 75, 31))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 47, 13))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 61, 16))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 200, 47, 13))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 250, 91, 16))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 250, 81, 16))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 10, 47, 13))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 240, 131, 51))
        self.lcdNumber = QLCDNumber(Dialog)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(290, 10, 64, 23))
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 100, 401, 16))
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Simulador de Procesos", None))
        self.lineEdit_2.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"+", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"-", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"*", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"/", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"%", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"No. Procesos", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Operacion", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Tiempo Estimado", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"segundos", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Proceso", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
    # retranslateUi

