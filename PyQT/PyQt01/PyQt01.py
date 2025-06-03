import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
from app_controller import AppController
from sampleUi01 import Ui_MainWindow  # <-- import the class

app = QApplication([])

# window = QWidget()
# window.setWindowTitle("PyQt App")
# window.setGeometry(100, 100, 280, 80)
# helloMsg = QLabel("Hello, World!", parent=window)
# okButton = QPushButton("OK", parent=window)
# okButton.setGeometry(10, 40, 60, 30)

controller = AppController(app)  # <-- pass app to controller

# okButton.clicked.connect(controller.quitApp)
# helloMsg.move(60, 15)

# window.show()

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(controller)  # <-- pass controller to Ui_MainWindow
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
sys.exit(app.exec())