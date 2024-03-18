from PySide6.QtWidgets import QApplication,QTabWidget, QMainWindow,QWidget,QGridLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import  QPixmap, QIcon, Qt

class irtm2p(QWidget):
    """IRT M2P Window"""
    def __init__(self, logo_path):
        super().__init__()
        self.setWindowTitle("IRT M2P")
        #self.setGeometry(100,100,200,100)
        
        pixmap = QPixmap(logo_path)
        resizedPixmap = pixmap.scaled(64, 64)
        self.setWindowIcon(QIcon(resizedPixmap))

    
        logo_about = QLabel()
        logo_about.setPixmap(pixmap)
        logo_about.setScaledContents(True)
        logo_about.setFixedSize(200,60) #Adjust the size

        Text = QLabel("<b>DES COMPÉTENCES ET DES ÉQUIPEMENTS AU SERVICE DE LA RECHERCHE INDUSTRIELLE</b>\
                      <p>L’Institut de Recherche Technologique Matériaux Métallurgie et Procédés (IRT M2P) met son expertise, ses équipements et son réseau de laboratoires académiques au service des projets de R&D des industriels. Les pilotes industriels de M2P permettent notamment le développement plus rapide de produits et procédés dans un environnement représentatif des contraintes des entreprises partenaires. La mutualisation des développements entre industriels de différents secteurs d’activité accélère également la maturation d’innovations via M2P. L’offre de technologies et les plateformes sont au service de tout industriel au travers de prestations sur-mesure, de projets de R&D privée ou de projets multipartenaires avec un cofinancement privé/public. Les moyens de M2P sont également accessibles pour la formation professionnelle. Depuis 2013, l'IRT M2P est soutenu par le Programme d'Investissements d'Avenir (PIA) avec un cofinancement attractif des projets initiés par les industriels.</p>")
        Text.setWordWrap(True) #permet de passer à la ligne automatiquement
        Text.setAlignment(Qt.AlignJustify)

        layout = QGridLayout()
        #First column
        layout.addWidget(logo_about, 0, 0)
        layout.addWidget(Text, 1, 0)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    #the main window class 
    def __init__(self):
        super().__init__()
        button = QPushButton("Click")
        button.clicked.connect(self.open_tabs)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QGridLayout(self.central_widget)
        layout.addWidget(button, 0,0)
    
        # Set the window's size and title
        self.resize(400, 300)
        self.setWindowTitle('Example')

    def open_tabs(self): 
        # Create the tab widget
        self.window_with_tabs = QTabWidget()
        self.window_with_tabs.setWindowTitle("Tabbed window")

        # Create the first tab content
        # Adding a logo path 
        self.logo_path = "/Users/issamhammadi/Documents/GitHub/code/app_with_skimageV2/Assets/logo irt m2p.png"
        
        self.tab1 = irtm2p(self.logo_path)
        self.window_with_tabs.addTab(self.tab1, "Tab 1")

        # Create the second tab content
        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout(self.tab2)
        
        image1_path = "/Users/issamhammadi/Documents/GitHub/main_code/Assets/assemblage.png"
        pixmap = QPixmap(image1_path)
        
        image1 = QLabel()
        image1.setPixmap(pixmap)
        self.tab2_layout.addWidget(image1)

        self.window_with_tabs.addTab(self.tab2, "Tab 2")

        # Create the 3rd tab content
        self.tab3 = QWidget()
        self.tab3_layout = QVBoxLayout(self.tab3)

        image2_path = "/Users/issamhammadi/Documents/GitHub/main_code/Assets/TS mécanique.png"
        pixmap = QPixmap(image2_path)
        
        image2 = QLabel()
        image2.setPixmap(pixmap)
        self.tab3_layout.addWidget(image2)

        self.window_with_tabs.addTab(self.tab3, "Tab 3")

        # You can create more tabs in the same way
        self.window_with_tabs.resize(500, 400)
        self.window_with_tabs.show()
# Run the GUI 
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()