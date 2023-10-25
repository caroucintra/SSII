from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("BYODSEC")
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        layout = QVBoxLayout()

        usuario = QLineEdit()
        self.usuario_input = ""
        usuario.textEdited.connect(self.usuario_edited)

        contrasena = QLineEdit()
        self.contrasena_input = ""
        contrasena.textEdited.connect(self.contrasena_edited)

        mensaje = QLineEdit()
        self.mensaje_input = ""
        mensaje.textEdited.connect(self.mensaje_edited)

        run = QPushButton("RUN")
        run.clicked.connect(self.run)

        close = QPushButton("CLOSE")
        close.clicked.connect(self.closeGUI)

        widgets = [
            QLabel("usuario"),
            usuario,
            QLabel("contraseña"),
            contrasena,
            QLabel("mensaje"),
            mensaje,
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

    def usuario_edited(self, s):
        self.usuario_input = s

    def contrasena_edited(self, s):
        self.contrasena_input = s

    def mensaje_edited(self, s):
        self.mensaje_input = s

    def run(self):
        global usuario_input, contrasena_input, mensaje_input
        usuario_input = self.usuario_input
        contrasena_input = self.contrasena_input
        mensaje_input = self.mensaje_input
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

        self.setWindowTitle("BYODSEC")
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