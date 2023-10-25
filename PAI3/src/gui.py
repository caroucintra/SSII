from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Transmisión Punto-Punto")
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        layout = QVBoxLayout()

        origin = QLineEdit()
        self.origin_input = ""
        origin.textEdited.connect(self.origin_edited)

        destination = QLineEdit()
        self.destination_input = ""
        destination.textEdited.connect(self.destination_edited)

        quantity = QLineEdit()
        self.quantity_input = ""
        quantity.textEdited.connect(self.quantity_edited)

        run = QPushButton("RUN")
        run.clicked.connect(self.run)

        close = QPushButton("CLOSE")
        close.clicked.connect(self.closeGUI)

        widgets = [
            QLabel("Cuenta Origen"),
            origin,
            QLabel("Cuenta Destino"),
            destination,
            QLabel("Cantidad"),
            quantity,
            run,
            close,
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def origin_edited(self, s):
        self.origin_input = s

    def destination_edited(self, s):
        self.destination_input = s

    def quantity_edited(self, s):
        self.quantity_input = s

    def run(self):
        global origin_input, destination_input, quantity_input
        origin_input = self.origin_input
        destination_input = self.destination_input
        quantity_input = self.quantity_input
        global running
        running = True
        self.close()

    def closeGUI(self):
        global running
        running = False
        self.close()

class ResultsWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ResultsWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Transmisión Punto-Punto")
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        
        layout = QVBoxLayout()

        results = QLabel(response)
        
        restart = QPushButton("RESTART")
        restart.clicked.connect(self.restartGUI)

        widgets = [
            results,
            restart,
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def restartGUI(self):
        global running
        running = True
        self.close()

def startGUI():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    return running

def showResults(r):
    app = QApplication(sys.argv)
    global response
    response = r
    window = ResultsWindow()
    window.show()
    app.exec_()
    return running