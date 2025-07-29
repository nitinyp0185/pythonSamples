import sys
from PyQt6.QtWidgets import QApplication, QPushButton

def greet():
   print("Hello, PyQt!")

app = QApplication(sys.argv)
button = QPushButton("Click Me")
button.clicked.connect(greet)
button.show()
sys.exit(app.exec())