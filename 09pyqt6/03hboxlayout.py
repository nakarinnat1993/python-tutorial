from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        
        hbox = QHBoxLayout(self)
        
        for message in ["A", "B", "C"]:
            self.display_button(message, hbox)
    
    def display_button(self, text, layout):
        button = QPushButton(text)
        button.setFixedSize(100, 50)
        layout.addWidget(button)
        
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()