from PyQt6.QtWidgets import QHBoxLayout, QLabel
from PyQt6.QtCore import  Qt
from packet import PacketWidget

class IPPacketWidget(PacketWidget):
    def __init__(self, parent=None, packet=None, packet_number=0):
        super().__init__(parent)
        self.protocol = "IP"
        self.version = 4
        
        self.packet = packet
        self.packet_number = packet_number
        self.ihl = 5
        self.tos = 0
        self.len = 0
        self.id = 1
        self.flags = 0
        self.frag = 0
        self.ttl = 64
        self.proto = 0
        self.checksum = None
        self.options = None

        self.number_of_packet = 5
        self.source_ip_address = "192.168.1.236"
        self.destination_ip_address = "192.168.1.236"
        self.payload = "Hello World!"

        # Label
        self.top_layout = QHBoxLayout()
        self.top_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)

        # Create and add the labels for the source and destination IP addresses
        self.packet_number_label = QLabel("No. {}".format(self.packet_number))
        self.src_label = QLabel("Src: {}".format(packet["srcIP"]))
        self.dst_label = QLabel("Dst: {}".format(packet["dstIP"]))

        self.src_label.setStyleSheet("color: black")
        self.dst_label.setStyleSheet("color: black")
        self.packet_number_label.setStyleSheet("color: black")

        self.top_layout.addWidget(self.packet_number_label)
        self.top_layout.addWidget(self.src_label)
        self.top_layout.addWidget(self.dst_label)
        self.layout.addLayout(self.top_layout)

    def send_packets_signal(self):
        self.generate_packet(self.packet)
