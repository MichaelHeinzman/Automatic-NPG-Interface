from PyQt6.QtWidgets import QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QWidget,QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from widgets.packet import PacketWidget
from scapy.layers.inet import TCP,IP
from network.tcp_handshake import tcp_handshake

class IPPacketWidget(PacketWidget):
    # Signals
    send_packet_signal = pyqtSignal()

    def __init__(self, parent=None, packet=None, packet_number=0):
        super().__init__(parent)
        # Initialize variables
        self.protocol = "IP"
        self.packet = packet
        self.packet_number = packet_number
        self.payload = packet.get("payload", "")

        # Create Bottom Layout
        self.bottom_layout = QVBoxLayout()
        self.bottom_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.bottom_layout.setSpacing(10)
        
        # Create top-level horizontal layout
        self.top_layout = QHBoxLayout()
        self.top_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.top_layout.setSpacing(10)


        # Add protocol label if applicable
        if packet["proto"] == 6:
            if packet.get("tcp_type"):
                if packet["tcp_type"] == "S":
                    tcp_type_text = "SYN"
                elif packet["tcp_type"] == "A":
                    tcp_type_text = "ACK"
                elif packet["tcp_type"] == "SA":
                    tcp_type_text = "SYN-ACK"
                elif packet["tcp_type"] == "FA":
                    tcp_type_text = "FIN-ACK"
                elif packet["tcp_type"] == "R":
                    tcp_type_text = "RST"
                else:
                    tcp_type_text = "TCP"
                protocol_label_text = "TCP ({})".format(tcp_type_text)
            else:
                protocol_label_text = "TCP"
        elif packet["proto"] == 17:
            protocol_label_text = "UDP"
        elif packet["proto"] == 1:
            protocol_label_text = "ICMP"
        else:
            protocol_label_text = "Protocol {}".format(packet["proto"])

        # Create and add the labels for the source and destination IP addresses
        self.packet_number_label = QLabel("No. {}".format(self.packet_number))
        self.src_label = QLabel("Src: {}".format(packet["srcIP"]))
        self.dst_label = QLabel("Dst: {}".format(packet["dstIP"]))
        self.protocol_label = QLabel(protocol_label_text)
        self.protocol_label.setStyleSheet(self.textStyle)
        self.src_label.setStyleSheet(self.textStyle)
        self.dst_label.setStyleSheet(self.textStyle)
        self.packet_number_label.setStyleSheet(self.textStyle)

        # Add spacing 
        self.top_layout.addWidget(self.packet_number_label)
        self.top_layout.addWidget(self.src_label)
        self.top_layout.addWidget(self.dst_label)
        self.top_layout.addWidget(self.protocol_label)
        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.bottom_layout)
        self.packet_selected.connect(self.on_packet_selected)
        
    # Sends the generated packet
    def send_packet(self):
        if self.packet["proto"] == 6:
            return tcp_handshake(self.packet)
        else:
            return self.generate_packet(self.packet)


    def on_packet_selected(self):
        if self.selected:
            # Change Style  of top layout
            self.src_label.setStyleSheet(self.selectedTopLayout)
            self.dst_label.setStyleSheet(self.selectedTopLayout)
            self.protocol_label.setStyleSheet(self.selectedTopLayout)
            self.packet_number_label.setStyleSheet(self.selectedTopLayout)

            # show details
            self.version_label = QLabel("Version: {}".format(self.packet["version"]))
            self.version_label.setStyleSheet(self.textStyle)
            self.proto_label = QLabel("Protocol: {}".format(self.packet["proto"]))
            self.proto_label.setStyleSheet(self.textStyle)
            self.payload_label = QLabel("Payload: {}".format(self.packet["payload"]))
            self.payload_label.setStyleSheet(self.textStyle)
            self.number_of_packets = QLabel("Number of Packets: {}".format(self.packet["number"]))
            self.number_of_packets.setStyleSheet(self.textStyle)
            self.bottom_layout.addWidget(self.version_label)
            self.bottom_layout.addWidget(self.proto_label)
            self.bottom_layout.addWidget(self.payload_label)
            self.bottom_layout.addWidget(self.number_of_packets)
        else:
            # Change Style  of top layout
            self.src_label.setStyleSheet(self.textStyle)
            self.dst_label.setStyleSheet(self.textStyle)
            self.protocol_label.setStyleSheet(self.textStyle)
            self.packet_number_label.setStyleSheet(self.textStyle)

            # hide details
            if self.version_label is not None:
                self.version_label.deleteLater()
                self.version_label = None
            if self.proto_label is not None:
                self.proto_label.deleteLater()
                self.proto_label = None
            if self.payload_label is not None:
                self.payload_label.deleteLater()
                self.payload_label = None
            if self.number_of_packets is not None:
                self.number_of_packets.deleteLater()
                self.number_of_packets = None
    
    # Deletes the widget and its layout
    def __del__(self):
        if self.top_layout is not None:
            for i in reversed(range(self.top_layout.count())):
                item = self.top_layout.itemAt(i)

                if isinstance(item, QSpacerItem):
                    self.top_layout.removeItem(item)
                elif isinstance(item, QWidget):
                    widget = item.widget()

                    if widget is not None:
                        widget.deleteLater()
                    else:
                        self.top_layout.removeItem(item)
                else:
                    self.top_layout.removeItem(item)

            self.top_layout.deleteLater()

        self.packet_number_label = None
        self.src_label = None
        self.dst_label = None
        self.top_layout = None