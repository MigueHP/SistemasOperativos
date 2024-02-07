import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton
from PyQt5.QtCore import QTimer


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Contador de Segundos")

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(7)  # Configura el número máximo de dígitos que se pueden mostrar
        self.lcd.display(0)

        self.start_button = QPushButton("Iniciar")
        self.start_button.clicked.connect(self.startTimer)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lcd)
        self.layout.addWidget(self.start_button)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.seconds = 0

        self.setLayout(self.layout)

    def startTimer(self):
        self.timer.start(1000)  # Disparar el temporizador cada 1000 ms (1 segundo)

    def updateTimer(self):
        self.seconds += 1
        self.lcd.display(self.seconds)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
