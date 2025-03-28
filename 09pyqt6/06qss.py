from PyQt6.QtCore import QCoreApplication, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Style Sheets")
        self.setFixedSize(800, 600)
        
        hbox = QHBoxLayout(self)
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hbox.setSpacing(30)
        
        for message in ["A", "B", "C"]:
            self.display_button(message, hbox)
    
    def display_button(self, text, layout):
        button = QPushButton(text)
        button.setFixedSize(100, 50)
        button.setStyleSheet('color:white; background-color:green; font-size:20px; font-weight:bold')
        layout.addWidget(button)
        
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()