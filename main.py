from PySide6.QtWidgets import QApplication,QTextEdit,QDateEdit,QTimeEdit,QCheckBox,QComboBox, QMainWindow,QWidget,QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QSizePolicy
from PySide6.QtGui import  QDoubleValidator, QShortcut, QImageReader, QPixmap, QIcon, Qt, QDesktopServices 
from PySide6 import QtCore
from PySide6.QtCore import QUrl
import sys
import pandas as pd
from numpy import nan

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("PyCorr")
        self.init_ui()
    
        widget = QWidget()
        Push_button = QPushButton("click me!")
        Push_button.clicked.connect(self.gotowebsite)

        echantillon_label = QLabel("Échantillon :")
        
        L_label = QLabel("L (mm) :") 
        l_label = QLabel("L (mm) :") 
        e_label = QLabel("e (mm) :") 
        

        self.L_edit = QLineEdit()

        self.l_edit = QLineEdit()

        self.e_edit = QLineEdit() 

        self.update_edit_lines(0)

        layout = QGridLayout()
        layout.addWidget(Push_button, 0,0)
        layout.addWidget(echantillon_label, 1,0)
        layout.addWidget(self.drop_nuances, 1,1)
        layout.addWidget(L_label, 0,2)
        layout.addWidget(l_label, 0,3)
        layout.addWidget(e_label, 0,4)
        layout.addWidget(self.L_edit, 1,2)
        layout.addWidget(self.l_edit, 1,3)
        layout.addWidget(self.e_edit, 1,4)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def update_edit_lines(self, index):
        # Update the QLineEdit widgets with the selected sample's dimensions
        self.L_edit.setText(str(self.df.iloc[index]['Longueur (mm)']))
        #replacing nan values with empty strings
        self.L_edit.setText('' if pd.isna(self.df.iloc[index]['Longueur (mm)']) else str(self.df.iloc[index]['Longueur (mm)']))
        self.l_edit.setText(str(self.df.iloc[index]['Largeur (mm)']))
        self.l_edit.setText('' if pd.isna(self.df.iloc[index]['Largeur (mm)']) else str(self.df.iloc[index]['Largeur (mm)']))
        self.e_edit.setText(str(self.df.iloc[index]['épaisseur (mm)']))
        self.e_edit.setText('' if pd.isna(self.df.iloc[index]['épaisseur (mm)']) else str(self.df.iloc[index]['épaisseur (mm)']))

    def gotowebsite(self):
        QDesktopServices.openUrl(QUrl("https://www.irt-m2p.fr/fr"))
        
    def init_ui(self):
        
        # Read data from Excel
        self.excel_file = '/Users/issamhammadi/Documents/GitHub/code/app_with_skimageV2/nuances.xlsx'  # Update this to your Excel file path
        self.df = pd.read_excel(self.excel_file, sheet_name=0)

        self.df.dropna(subset=[self.df.columns[0]], inplace=True)
        self.drop_nuances = QComboBox()
        self.drop_nuances.addItems(self.df.iloc[:, 0].astype(str).tolist())
        self.drop_nuances.currentIndexChanged.connect(self.update_edit_lines)  # Link to update function

app = QApplication(sys.argv)
W = MainWindow()
W.show()

app.exec()