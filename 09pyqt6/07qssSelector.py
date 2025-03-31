from PyQt6.QtCore import QCoreApplication, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Style Sheets")
        self.setFixedSize(400, 200)
        
        vbox = QVBoxLayout(self)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label = QLabel("Label with Qt Style Sheets");
        button_a = QPushButton("A")
        button_b = QPushButton("B")
        button_c = QPushButton("C")
        button_c.setObjectName("text_red")
        label.setObjectName("text_red")
        
        vbox.addWidget(label)
        vbox.addWidget(button_a)
        vbox.addWidget(button_b)
        vbox.addWidget(button_c)
        
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
    qss_path = os.path.join(os.path.dirname(__file__), '07qssSelector.qss')
    with open(qss_path, 'r') as style:
        qss = style.read()
        app.setStyleSheet(qss)
window = MainWindow()
window.show()
app.exec()