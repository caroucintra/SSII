from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import config


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("HIDS App")
        layout = QVBoxLayout()

        directories = QLineEdit()
        self.directories_input = ""
        directories.textEdited.connect(self.directories_edited)

        function = QComboBox()
        function.addItems(["md5", "sha1", "sha256"]),
        self.function_input = "sha256"
        function.setCurrentText("sha256")
        function.currentTextChanged.connect(self.function_edited)

        email = QLineEdit()
        self.email_input = ""
        email.textEdited.connect(self.email_edited)

        scan = QSpinBox()
        scan.setMinimum(1)
        scan.setMaximum(3)
        self.scan_input = 3
        scan.setValue(3)
        scan.valueChanged.connect(self.scan_edited)
        log = QSpinBox()
        log.setMinimum(1)
        log.setMaximum(3)
        self.log_input = 3
        log.setValue(3)
        log.valueChanged.connect(self.log_edited)

        run = QPushButton("RUN")
        run.clicked.connect(self.run)

        default = QPushButton("Continue with default config")
        default.clicked.connect(self.default)

        widgets = [
            QLabel("directories_to_scan"),
            directories,
            QLabel("hash_function"),
            function,
            QLabel("email_to_notify"),
            email,
            QLabel("scan_interval: (1=cada minuto, 2=cada hora, 3=diario)"),
            scan,
            QLabel("log_interval: (1=cada 10 minutos, 2=diario, 3=mensual)"),
            log,
            run,
            default,
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def directories_edited(self, s):
        self.directories_input = s

    def email_edited(self, s):
        self.email_input = s

    def function_edited(self, s):
        self.function_input = s

    def scan_edited(self, i):
        self.scan_input = i

    def log_edited(self, i):
        self.log_input = i

    def run(self):
        # print(self.email_input)
        config.editConfig(
            self.directories_input,
            self.function_input,
            self.email_input,
            self.scan_input,
            self.log_input,
        )
        start()
        self.close()

    def default(self):
        config.writeDefaultConfig()
        start()
        self.close()


def start():
    print("App started.")

def startGUI():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()