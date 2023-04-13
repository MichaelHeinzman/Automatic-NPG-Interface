from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QLineEdit
from widgets.input import Input

class NumberLineEdit(Input):
    """
    A custom widget that extends the Input widget and allows only integer input.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setValidator(QIntValidator())  # Set validator to only allow integers

    def text(self) -> str:
        """
        Override the QLineEdit text() method to return an empty string if input is invalid.
        """
        text = super().text()
        if self.hasAcceptableInput():
            return text
        return ""

    def value(self) -> int:
        """
        Convert the input text to an integer.
        """
        return int(self.text() or 0)