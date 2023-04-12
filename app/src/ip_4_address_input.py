from PyQt6.QtWidgets import  QLineEdit
from PyQt6 import QtGui, QtCore

class IPAddressInput(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.validate_ip_input()

    # Validate MAC Inputs
    def validate_ip_input(self):
        self.setMaxLength(15)
        self.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('^([0-9]{1,3}\.){3}[0-9]{1,3}$')))
        self.setPlaceholderText('192.168.0.1')