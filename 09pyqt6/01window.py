from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# app = QApplication([])
# window = QWidget()
# window.show()
# app.exec()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        
        label = QLabel("Hello World", self)
        label.move(50, 0)
        button = QPushButton("Click Me", self)
        button.move(50, 50)
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])
window = MainWindow()
window.show()
app.exec()