from PyQt6.QtWidgets import QHBoxLayout, QLabel
from PyQt6.QtCore import  Qt
from packet import PacketWidget

class IPPacketWidget(PacketWidget):
    def __init__(self, parent=None, packet=None):
        super().__init__(parent)
        self.protocol = "IP"
        self.version = 4
        
        self.packet = packet
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

        # Create the horizontal layout for the source and destination IP addresses
        self.src_dst_layout = QHBoxLayout()
        self.src_dst_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # Create and add the labels for the source and destination IP addresses
        self.src_label = QLabel("Src: {}".format(packet["srcIP"]))
        self.dst_label = QLabel("Dst: {}".format(packet["dstIP"]))
        self.src_label.setStyleSheet("color: black")
        self.dst_label.setStyleSheet("color: black")
        self.src_dst_layout.addWidget(self.src_label)
        self.src_dst_layout.addWidget(self.dst_label)
        self.layout.addLayout(self.src_dst_layout)

    def send_packets_signal(self):
        self.generate_packet(self.packet)
