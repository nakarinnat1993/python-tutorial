from PyQt6.QtCore import QCoreApplication, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message box")
        self.setFixedSize(400, 200)
        
        vbox = QVBoxLayout(self)
        
        self.button_information = QPushButton("Information")
        self.button_warning = QPushButton("Warning")
        self.button_critical = QPushButton("Critical")
        
        vbox.addWidget(self.button_information)
        vbox.addWidget(self.button_warning)
        vbox.addWidget(self.button_critical)
        
        self.button_information.clicked.connect(self.show_message)
        self.button_warning.clicked.connect(self.show_message)
        self.button_critical.clicked.connect(self.show_message)
        
    # slot
    def show_message(self):
        sender = self.sender()
        if sender==self.button_information:
            QMessageBox.information(self, "Information", "This is an information message", QMessageBox.StandardButton.Ok)
        elif sender==self.button_warning:
            QMessageBox.warning(self, "Warning", "This is a warning message", QMessageBox.StandardButton.Ok)
        elif sender==self.button_critical:
            QMessageBox.critical(self, "Critical", "This is a critical message", QMessageBox.StandardButton.Ok)
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()