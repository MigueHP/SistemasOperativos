import sys
import time

from PyQt6.QtCore import QCoreApplication, QTimer
from PySide6 import QtWidgets
from PySide6.QtCore import QEventLoop
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem
from ui_mainwindow import Ui_Dialog
from table import Ui_Table
from Proceso import Proceso


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ou = Ui_Table()
        validator = QIntValidator(self)
        self.ui.lineEdit.setValidator(validator)
        self.table = QtWidgets.QMainWindow()
        self.ou.setupUi(self.table)
        self.habilitar_interfaz(False)
        self.ui.pushButton.clicked.connect(self.cargar_procesos)
        self.ui.pushButton_2.clicked.connect(self.ejecutar_proceso)
        self.ou.Iniciar.clicked.connect(self.s)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.iteracion_actual = 0
        self.procesos = []
        self.seconds = 0
        self.ids_usados = []


        self.ui.no_procesos_4.setValue(1)


    def startTimer(self):
        self.timer.start(1000)  # Inicia el único temporizador

    def updateTimer(self):
        self.seconds += 1
        self.ou.lcdNumber_2.display(self.seconds)

    def detener_cronometro(self):
        self.timer.stop()

    def habilitar_interfaz(self, estado):
        # Habilitar o deshabilitar widgets según el estado
        self.ui.lineEdit.setEnabled(estado)
        self.ui.lineEdit_2.setEnabled(estado)
        self.ui.no_procesos.setEnabled(estado)
        self.ui.no_procesos_3.setEnabled(estado)
        self.ui.no_procesos_4.setEnabled(estado)
        self.ui.comboBox.setEnabled(estado)
        self.ui.pushButton_2.setEnabled(estado)


    def cargar_procesos(self):
        datos = Proceso()

        datos.no_proceso = self.ui.no_procesos_2.text()
        valor_entero = int(datos.no_proceso)

        if valor_entero == 0:
            QtWidgets.QMessageBox.warning(self, 'Advertencia', 'Ingrese la cantidad de procesos.')
            return

        valor_entero = int(datos.no_proceso)
        v_ = valor_entero
        self.ui.no_procesos_2.setValue(v_)
        self.ui.no_procesos_2.setEnabled(False)
        self.habilitar_interfaz(True)

    def iniciar_proceso(self):
        self.iteracion_actual = 0
        self.timer.start(1000)

    def ejecutar_proceso(self):

        if self.iteracion_actual < self.ui.no_procesos_2.value():
            datos = Proceso()
            self.ui.no_procesos_4.setValue(1)
            datos.nombre = self.ui.lineEdit_2.text()
            datos.num1 = self.ui.no_procesos.value()
            datos.operador = self.ui.comboBox.currentText()
            datos.num2 = self.ui.no_procesos_3.value()
            datos.id = self.ui.lineEdit.text()
            datos.time = self.ui.no_procesos_4.value()
            #Validar 0 / 0
            if datos.num1 == 0 and datos.num2 == 0 and datos.operador == '/':
                mensaje_box = QMessageBox()
                mensaje_box.setText(f"No es posible dividir 0 entre 0")
                mensaje_box.exec()
                return
            if datos.num2 == 0 and datos.operador =='/':
                mensaje_box = QMessageBox()
                mensaje_box.setText(f"No es posible dividir entre 0")
                mensaje_box.exec()
                return
            if datos.num1 == 0 and datos.num2 == 0 and datos.operador == '%':
                mensaje_box = QMessageBox()
                mensaje_box.setText(f"No es posible residuo 0 entre 0")
                mensaje_box.exec()
                return
            if datos.num2 == 0 and datos.operador =='%':
                mensaje_box = QMessageBox()
                mensaje_box.setText(f"No es posible residuo entre 0")
                mensaje_box.exec()
                return

            # Validar si el ID ya está en uso
            if datos.id in self.ids_usados:
                mensaje_box = QMessageBox()
                mensaje_box.setText("El ID '{}' ya está en uso.".format(datos.id))
                mensaje_box.exec()
                self.ui.lineEdit.clear()
                return


            if datos.id == '' :
                mensaje_box = QMessageBox()
                mensaje_box.setText(f"ID vacio, no valido")
                mensaje_box.exec()

                return

            if datos.nombre == '':
                mensaje_box = QMessageBox()
                mensaje_box.setText(f"Nombre vacio, no valido")
                mensaje_box.exec()
                return


            self.ids_usados.append(datos.id)

            proceso = {
                "nombre": datos.nombre,
                "num1": datos.num1,
                "operador": datos.operador,
                "num2": datos.num2,
                "id": datos.id,
                "tiempo": datos.time
            }

            self.procesos.append(proceso)



            # Limpiar los campos después de agregar un proceso
            self.ui.lineEdit_2.clear()
            self.ui.no_procesos.setValue(0)
            self.ui.no_procesos_3.setValue(0)
            self.ui.lineEdit.clear()
            self.ui.no_procesos_4.setValue(0)

            self.iteracion_actual += 1
            self.ui.lcdNumber.display(self.iteracion_actual)
            self.ui.no_procesos_4.setValue(1)
        if self.iteracion_actual == self.ui.no_procesos_2.value():
            self.timer.stop()
            self.table.show()

            mensaje_box = QMessageBox()
            mensaje_box.setText("Procesos completados.")
            mensaje_box.exec()

    def s(self):
        self.startTimer()
        i = len(self.procesos)
        # CREACION DE TABALAS
        self.ou.Tabla_trabajando.setColumnCount(2)
        self.ou.Tabla_trabajando.setRowCount(4)
        self.ou.Tabla_ejecucion.setColumnCount(4)

        self.ou.tabla_terminados.setColumnCount(4)

        if i % 4 == 0:
            self.x = i / 4
            self.ou.lcdNumber.display(self.x)
        elif i % 4 >= 1:
            self.x = int(i / 4) + 1
            self.ou.lcdNumber.display(self.x)

        # INICIA CICLO mostrar todos
        for i, proceso_actual in enumerate(self.procesos):
            nombre = proceso_actual.get('nombre', '')
            tiempo = proceso_actual.get('tiempo', 0)

            self.ou.Tabla_trabajando.setItem(i, 0, QTableWidgetItem(nombre))
            self.ou.Tabla_trabajando.setItem(i, 1, QTableWidgetItem(str(tiempo)))

        no_lote = 1
        p = 0
        for i, p_a in enumerate(self.procesos):

            nombre = p_a.get('nombre', '')
            id = p_a.get('id', '')
            tiempo = p_a.get('tiempo', 0)
            op1 = p_a.get('num1', '')
            op2 = p_a.get('num2', '')
            op = p_a.get('operador', '')
            operacion = f"{op1} {op} {op2}"
            resultado = self.calcular_resultado(op1, op2, op)

            loop = QEventLoop()
            self.ou.Tabla_ejecucion.setRowCount(2)
            self.ou.Tabla_ejecucion.setItem(1, 0, QTableWidgetItem(str(id)))
            self.ou.Tabla_ejecucion.setItem(1, 1, QTableWidgetItem(nombre))
            self.ou.Tabla_ejecucion.setItem(1, 2, QTableWidgetItem(str(operacion)))
            self.ou.Tabla_ejecucion.setItem(1, 3, QTableWidgetItem(str(tiempo)))

            self.ou.Tabla_trabajando.removeRow(p)

            QTimer.singleShot(tiempo * 1000, loop.exit)
            loop.exec_()
            self.ou.Tabla_ejecucion.clearContents()
            self.ou.tabla_terminados.setRowCount(i+1)
            self.ou.tabla_terminados.setItem(i, 0, QTableWidgetItem(str(f"Lote: {no_lote}")))
            self.ou.tabla_terminados.setItem(i, 1, QTableWidgetItem(str(id)))
            self.ou.tabla_terminados.setItem(i, 2, QTableWidgetItem(str(operacion)))
            self.ou.tabla_terminados.setItem(i, 3, QTableWidgetItem(str(resultado)))


            if i > 0 and (i + 1) % 4 == 0:
                no_lote += 1
                self.ou.Tabla_trabajando.clearContents()
                z =self.x -1
                self.ou.lcdNumber.display(z)
                contador = 0
                for j in range(i + 1, min(len(self.procesos), i + 5)):
                    self.ou.Tabla_trabajando.setColumnCount(2)
                    self.ou.Tabla_trabajando.setRowCount(4)
                    nombre = self.procesos[j]["nombre"]
                    tiempo = self.procesos[j]["tiempo"]

                    self.ou.Tabla_trabajando.setItem(contador, 0, QTableWidgetItem(nombre))
                    self.ou.Tabla_trabajando.setItem(contador, 1, QTableWidgetItem(str(tiempo)))
                    contador += 1



        QtWidgets.QMessageBox.warning(self, 'Advertencia', 'Ejecucion Terminada.')
        self.detener_cronometro()

       # QApplication.instance().exit()
        QCoreApplication.processEvents()

    def calcular_resultado(self, op_1, op_2, operando):
        if operando == '+':
            return op_1 + op_2
        elif operando == '-':
            return op_1 - op_2
        elif operando == '*':
            return op_1 * op_2
        elif operando == '/':
            return op_1 / op_2
        elif operando == '%':
            return op_1 % op_2
        else:
            return None


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
