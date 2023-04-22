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
        self.textChanged.connect(self._on_text_changed)

    def _on_text_changed(self, text):
        """
        Convert the input text to an integer.
        """
        if text:
            try:
                value = int(text)
            except ValueError:
                pass
            else:
                self.setText(str(value))

    def value(self) -> int:
        """
        Return the integer value of the input text.
        """
        return int(self.text() or 1)