from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QLabel, QPushButton, QMessageBox
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RadioButton")
        self.setFixedSize(400, 200)
        
        vbox = QVBoxLayout(self)
        
        self.male = QRadioButton("Male")
        self.female = QRadioButton("Female")
        self.label_status = QLabel("Gender")
        button_save = QPushButton("Save")
        
        button_save.clicked.connect(self.save_data)
        
        vbox.addWidget(self.label_status)
        vbox.addWidget(self.male)
        vbox.addWidget(self.female)
        vbox.addWidget(button_save)
        
    # slot
    def save_data(self):
        if self.male.isChecked():
            QMessageBox.information(self, "Data", "Gender is "+self.male.text())
        if self.female.isChecked():
            QMessageBox.information(self, "Data", "Gender is "+self.female.text())
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()