from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QMessageBox
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox")
        self.setFixedSize(400, 200)
        
        vbox = QVBoxLayout(self)
        
        self.items = ["JS", "PHP", "CSS"]
        self.combo_box = QComboBox()
        self.combo_box.addItems(self.items)
        
        self.combo_box.currentIndexChanged.connect(self.save_data)
        
        vbox.addWidget(self.combo_box)
        
    # slot
    def save_data(self):
        print(self.combo_box.currentIndex())
        QMessageBox.information(self, "Data", "Stack language is "+self.combo_box.currentText())
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()