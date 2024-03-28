from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPixmap

class SegmentationResultsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graphics view example")
        self.setGeometry(100, 100, 800, 600)

        # Create a QGraphicsView to display the images
        self.graphics_view = QGraphicsView()
        self.setCentralWidget(self.graphics_view)

        # Create a QGraphicsScene to hold the images
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.scene.clear()  # Clear the scene before adding a new image
        self.scene.addPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication([])

    # Example usage:
    window = SegmentationResultsWindow()
    window.display_image("image path")
    window.show()

    app.exec()