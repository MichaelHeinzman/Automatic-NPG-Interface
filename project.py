import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget
import WelcomeScreen.WelcomeScreen as WelcomeScreen

app = QApplication(sys.argv)
welcome = WelcomeScreen.WelcomeScreen()
widget = QStackedWidget()
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.addWidget(welcome)
widget.show()

try: 
    sys.exit(app.exec())
except:
    print("Exiting")
