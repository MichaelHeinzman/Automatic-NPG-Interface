from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QComboBox
from network.packet_info import ARP_PACKET_INFO, DNS_PACKET_INFO

class ProtocolSelection(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.protocol_details_stacked = None

    def setup(self):
        """
        Connects the currentTextChanged signal to the on_selection_changed method and sets the initial selection to "IP".
        """
        self.currentTextChanged.connect(self.on_selection_changed)
        self.on_selection_changed("IP")

    def on_selection_changed(self, value):
        """
        Displays the appropriate packet details form based on the selected protocol.
        """
        if value == "IP":
            self.protocol_details_stacked.setCurrentIndex(0)
        elif value == "DNS":
            self.protocol_details_stacked.setCurrentIndex(1)
            self.packet = DNS_PACKET_INFO
        elif value == "ARP":
            self.protocol_details_stacked.setCurrentIndex(2)
            self.packet = ARP_PACKET_INFO
        else:
            return