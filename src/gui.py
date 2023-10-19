from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import clientsocket

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Transmisión Punto-Punto")
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
        clientsocket.setParams(self.origin_input, self.destination_input, self.quantity_input)
        global origin_input, destination_input, quantity_input
        origin_input = self.origin_input
        destination_input = self.destination_input
        quantity_input = self.quantity_input
        self.close()

    def closeGUI(self):
        self.close()

class ResultsWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ResultsWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Transmisión Punto-Punto")
        layout = QVBoxLayout()

        results = QLabel(response_toshow)
        
        close = QPushButton("CLOSE")
        close.clicked.connect(self.closeGUI)

        widgets = [
            results,
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
        clientsocket.setParams(self.origin_input, self.destination_input, self.quantity_input)
        global origin_input, destination_input, quantity_input
        origin_input = self.origin_input
        destination_input = self.destination_input
        quantity_input = self.quantity_input
        self.close()

    def closeGUI(self):
        self.close()

def startGUI():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()

def showResults(r):
    app = QApplication(sys.argv)
    global response
    response = r
    window = ResultsWindow()
    window.show()
    app.exec_()