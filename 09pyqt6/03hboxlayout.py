from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        
        hbox = QHBoxLayout(self)
        
        h_btn1 = QPushButton("H1")
        h_btn2 = QPushButton("H2")
        
        hbox.addWidget(h_btn1)
        hbox.addWidget(h_btn2)
        
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()