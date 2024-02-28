from PySide6.QtWidgets import QApplication,QTextEdit,QDateEdit,QTimeEdit,QCheckBox,QComboBox, QMainWindow,QWidget,QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QSizePolicy
from PySide6.QtGui import  QDoubleValidator, QShortcut, QImageReader, QPixmap, QIcon, Qt, QDesktopServices 
from PySide6 import QtCore
from PySide6.QtCore import QUrl
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("PyCorr")

        widget = QWidget()
        Push_button = QPushButton("click me!")
        Push_button.clicked.connect(self.gotowebsite)
        layout = QGridLayout()
        layout.addWidget(Push_button, 0,0)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def gotowebsite(self):
        QDesktopServices.openUrl(QUrl("https://www.irt-m2p.fr/fr"))

app = QApplication(sys.argv)
w = MainWindow()
app.exec()