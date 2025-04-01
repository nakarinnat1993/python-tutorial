from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QLabel, QPushButton, QMessageBox
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox")
        self.setFixedSize(400, 200)
        
        vbox = QVBoxLayout(self)
        
        self.check_youtube = QCheckBox("YouTube")
        self.check_facebook = QCheckBox("Facebook")
        self.label_status = QLabel("Status")
        self.button_save = QPushButton("Save")
        
        self.check_youtube.stateChanged.connect(self.check_status)
        self.check_facebook.stateChanged.connect(self.check_status)
        self.button_save.clicked.connect(self.save_data)
        
        vbox.addWidget(self.check_youtube)
        vbox.addWidget(self.check_facebook)
        vbox.addWidget(self.label_status)
        vbox.addWidget(self.button_save)
        
    # slot
    def check_status(self):
        sender = self.sender()
        self.label_status.setText("Status " + sender.text() + " is " + str(sender.isChecked()))
        
    def save_data(self):
        items = []
        if self.check_youtube.isChecked():
            items.append(self.check_youtube.text())
        if self.check_facebook.isChecked():
            items.append(self.check_facebook.text())
            
        text = "List \n" + ",".join(items);
        QMessageBox.information(self, "Data", text)
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()