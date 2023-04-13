from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QComboBox
from network.packet_info import  ARP_PACKET_INFO, DNS_PACKET_INFO

class ProtocolSelection(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.protocol_details_stacked = None

    def setup (self):
        self.currentTextChanged.connect(self.on_selection_changed)
        self.on_selection_changed("IP")

    # On Protocol Change present different packet details forms.
    def on_selection_changed(self, value):
        if value == "IP":
            # Set the current page to IP Details.
            self.protocol_details_stacked.setCurrentIndex(0)
            return
        elif value == "DNS":
            self.protocol_details_stacked.setCurrentIndex(1)
            self.packet = DNS_PACKET_INFO
            return
        elif value == "ARP":
            self.protocol_details_stacked.setCurrentIndex(2)
            self.packet = ARP_PACKET_INFO
            return
        else:
            return
