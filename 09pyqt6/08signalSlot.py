from PyQt6.QtCore import QCoreApplication, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal & Slot")
        self.setFixedSize(400, 200)
        
        vbox = QVBoxLayout(self)
        
        button_save = QPushButton("Save")
        # signal
        button_save.clicked.connect(self.show_name)
        vbox.addWidget(button_save)
        
        button_exit = QPushButton("Exit")
        # signal
        button_exit.clicked.connect(self.show_name)
        vbox.addWidget(button_exit)
        
    # slot
    def show_name(self):
        print(self.sender().text())
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()