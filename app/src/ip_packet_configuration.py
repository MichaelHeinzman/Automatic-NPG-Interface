from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout,QHBoxLayout
from network.packet_info import IP_PACKET_INFO
from packet_IP import IPPacketWidget

class IPConfigurationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.packet = IP_PACKET_INFO

    # Updates the current packet with changed values.
    def update_packet (self, index, value):
        self.packet[index] = value

    def setup_inputs (self, parent):
        # Get IP Inputs
        self.source_mac_IP = parent.findChild(QLineEdit, "source_ip_address_input")
        self.destination_mac_IP = parent.findChild(QLineEdit, "destination_ip_address_input")
        self.payload_IP = parent.findChild(QLineEdit, "ip_payload_input")

        # Set IP Values
        self.source_mac_IP.setText(IP_PACKET_INFO["srcIP"])
        self.destination_mac_IP.setText(IP_PACKET_INFO["dstIP"])
        self.payload_IP.setText(IP_PACKET_INFO["payload"])

        # Update packet values with changed IP values.
        self.source_mac_IP.textChanged.connect(lambda value: self.update_packet("srcIP", value))
        self.destination_mac_IP.textChanged.connect(lambda value: self.update_packet("dstIP", value))
        self.payload_IP.textChanged.connect(lambda value: self.update_packet("payload", value)) 

    # Add current packet to list of packets to send.
    def add_packet_signal(self, parent):
        self.to_send_packets_list = parent.findChild(QVBoxLayout, "to_send_packets_list")
        item_widget = IPPacketWidget(packet=self.packet)
        self.send_packets_signal.connect(item_widget.send_packets_signal)
        self.to_send_packets_list.addWidget(item_widget)