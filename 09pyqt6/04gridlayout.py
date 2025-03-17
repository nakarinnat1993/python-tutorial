from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        
        grid = QGridLayout(self)
        
        btn1 = QPushButton("G1")
        btn2 = QPushButton("G2")
        btn3 = QPushButton("G3")
        btn4 = QPushButton("G4")
        
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 1, 0)
        grid.addWidget(btn4, 1, 1)
        
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()