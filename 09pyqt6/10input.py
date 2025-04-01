from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QInputDialog 
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog")
        self.setFixedSize(400, 200)
        
        vbox = QVBoxLayout(self)
        
        self.button_name = QPushButton("Input name")
        self.button_address = QPushButton("Input address")
        self.button_gender = QPushButton("Input gender")
        
        vbox.addWidget(self.button_name)
        vbox.addWidget(self.button_address)
        vbox.addWidget(self.button_gender)
        
        self.button_name.clicked.connect(self.show_message)
        self.button_address.clicked.connect(self.show_message)
        self.button_gender.clicked.connect(self.show_message)
        
    # slot
    def show_message(self):
        sender = self.sender()
        if sender==self.button_name:
            text, submit = QInputDialog.getText(self, "Input", "Please input name")
            if submit:
                QMessageBox.information(self, "Name", "Hi!, "+text)
        elif sender==self.button_address:
            text, submit = QInputDialog.getMultiLineText(self, "Input", "Please input address")
            if submit:
                QMessageBox.information(self, "Address", "Your address is "+text)
        elif sender==self.button_gender:
            items = ["Male", "Female", "Not specify"]
            text, submit = QInputDialog.getItem(self, "Gender", "Please select gender", items)
            if submit:
                QMessageBox.information(self, "Gender", "Your gender is "+text)
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()