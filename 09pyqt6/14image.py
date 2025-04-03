from PyQt6.QtCore import QCoreApplication, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image")
        # self.setFixedSize(400, 200)
        
        vbox = QVBoxLayout(self)
        
        image_path = os.path.join(os.path.dirname(__file__), '14image.png')
        img = QPixmap(image_path)
        label = QLabel()
        label.setPixmap(img)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        vbox.addWidget(label)
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()