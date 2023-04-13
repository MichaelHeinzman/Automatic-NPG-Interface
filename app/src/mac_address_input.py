from PyQt6 import QtGui, QtCore
from input import Input
class MacAddressInput(Input):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.validate_mac_inputs()

    # Validate MAC Inputs
    def validate_mac_inputs(self):
        self.setMaxLength(17)
        self.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')))
        self.setPlaceholderText('00:11:22:33:44:55')