import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLabel

class ConsoleOutput(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Replace the standard output stream with a custom stream
        sys.stdout = self

    def __del__(self):
        # Reset the standard output stream
        sys.stdout = sys.__stdout__

    # Override the write() method to capture console output
    def write(self, message):
        # Strip the captured message of any extra spaces or newlines
        self.setText(self.text() + message)

    # Override the flush() method to ensure all output is emitted
    def flush(self):
        pass