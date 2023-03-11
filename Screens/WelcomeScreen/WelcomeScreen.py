import sys
from PyQt6 import QtWidgets,QtGui
from PyQt6.QtWidgets import QDialog, QWidget
from PyQt6.uic import loadUi

class WelcomeScreen (QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()

        loadUi("welcomescreen.ui", self)



