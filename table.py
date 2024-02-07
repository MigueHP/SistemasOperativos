# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Table(object):
    def setupUi(self, Table):
        if not Table.objectName():
            Table.setObjectName(u"Table")
        Table.resize(971, 454)
        Table.setStyleSheet(u"")
        self.centralwidget = QWidget(Table)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Tabla_trabajando = QTableWidget(self.centralwidget)
        if (self.Tabla_trabajando.columnCount() < 2):
            self.Tabla_trabajando.setColumnCount(2)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        self.Tabla_trabajando.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setForeground(brush);
        self.Tabla_trabajando.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.Tabla_trabajando.setObjectName(u"Tabla_trabajando")
        self.Tabla_trabajando.setGeometry(QRect(10, 20, 241, 151))
        self.Tabla_trabajando.setStyleSheet(u"\n"
"    background-color:(214, 214, 214)\n"
"\n"
"\n"
"")
        self.Tabla_trabajando.setRowCount(0)
        self.Tabla_ejecucion = QTableWidget(self.centralwidget)
        if (self.Tabla_ejecucion.columnCount() < 4):
            self.Tabla_ejecucion.setColumnCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Tabla_ejecucion.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Tabla_ejecucion.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Tabla_ejecucion.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Tabla_ejecucion.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        self.Tabla_ejecucion.setObjectName(u"Tabla_ejecucion")
        self.Tabla_ejecucion.setGeometry(QRect(10, 200, 411, 211))
        self.Tabla_ejecucion.setStyleSheet(u"")
        self.tabla_terminados = QTableWidget(self.centralwidget)
        if (self.tabla_terminados.columnCount() < 4):
            self.tabla_terminados.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_terminados.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_terminados.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_terminados.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_terminados.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tabla_terminados.setObjectName(u"tabla_terminados")
        self.tabla_terminados.setGeometry(QRect(530, 10, 411, 381))
        self.tabla_terminados.setStyleSheet(u"")
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(380, 100, 64, 23))
        self.lcdNumber.setStyleSheet(u"background-color: black; color: green;")
        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(380, 50, 64, 23))
        self.lcdNumber_2.setStyleSheet(u"background-color: black; color: green;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 80, 101, 16))
        self.label.setStyleSheet(u"font: 8pt \"Segoe Print\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 20, 61, 16))
        self.label_2.setStyleSheet(u"font: 8pt \"Segoe Print\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 101, 16))
        self.label_3.setStyleSheet(u"font: 8pt \"Segoe Print\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 131, 16))
        self.label_4.setStyleSheet(u"font: 8pt \"Segoe Print\";")
        self.Iniciar = QPushButton(self.centralwidget)
        self.Iniciar.setObjectName(u"Iniciar")
        self.Iniciar.setGeometry(QRect(370, 150, 75, 23))
        Table.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Table)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 971, 21))
        Table.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Table)
        self.statusbar.setObjectName(u"statusbar")
        Table.setStatusBar(self.statusbar)

        self.retranslateUi(Table)

        QMetaObject.connectSlotsByName(Table)
    # setupUi

    def retranslateUi(self, Table):
        Table.setWindowTitle(QCoreApplication.translate("Table", u"MainWindow", None))
        ___qtablewidgetitem = self.Tabla_trabajando.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Table", u"Nombre", None));
        ___qtablewidgetitem1 = self.Tabla_trabajando.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Table", u"Tiempo", None));
        ___qtablewidgetitem2 = self.Tabla_ejecucion.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Table", u"ID", None));
        ___qtablewidgetitem3 = self.Tabla_ejecucion.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Table", u"Nombre", None));
        ___qtablewidgetitem4 = self.Tabla_ejecucion.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Table", u"Operacion", None));
        ___qtablewidgetitem5 = self.Tabla_ejecucion.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Table", u"Tiempo", None));
        ___qtablewidgetitem6 = self.tabla_terminados.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Table", u"Lote", None));
        ___qtablewidgetitem7 = self.tabla_terminados.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Table", u"ID", None));
        ___qtablewidgetitem8 = self.tabla_terminados.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Table", u"Operacion", None));
        ___qtablewidgetitem9 = self.tabla_terminados.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Table", u"Resultado", None));
        self.label.setText(QCoreApplication.translate("Table", u"Lotes Pendientes", None))
        self.label_2.setText(QCoreApplication.translate("Table", u"Contador", None))
        self.label_3.setText(QCoreApplication.translate("Table", u"Lote", None))
        self.label_4.setText(QCoreApplication.translate("Table", u"Proceso en ejecucion", None))
        self.Iniciar.setText(QCoreApplication.translate("Table", u"Iniciar", None))
    # retranslateUi

