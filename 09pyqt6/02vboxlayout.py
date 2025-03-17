from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Box Layout")
        
        vbox = QVBoxLayout(self)
        self.setLayout(vbox)
        
        v_btn1 = QPushButton("V1")
        v_btn2 = QPushButton("V2")
        
        vbox.addWidget(v_btn1)
        vbox.addWidget(v_btn2)
        
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()