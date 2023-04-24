from PyQt6.QtWidgets import QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QWidget,QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from widgets.packet import PacketWidget
from scapy.layers.inet import TCP

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

        # Create and add the labels for the source and destination IP addresses
        self.packet_number_label = QLabel("No. {}".format(self.packet_number))
        self.src_label = QLabel("Src: {}".format(packet["srcIP"]))
        self.dst_label = QLabel("Dst: {}".format(packet["dstIP"]))
        self.src_label.setStyleSheet(self.textStyle)
        self.dst_label.setStyleSheet(self.textStyle)
        self.packet_number_label.setStyleSheet(self.textStyle)

        # Add spacing 
        self.top_layout.addWidget(self.packet_number_label)
        self.top_layout.addWidget(self.src_label)
        self.top_layout.addWidget(self.dst_label)
        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.bottom_layout)
        self.packet_selected.connect(self.on_packet_selected)
        
    # Sends the generated packet
    def send_packet(self):
        if self.packet["proto"] == 6:
            if self.packet["tcp_type"] == "S":  # SYN packet
                syn_result = self.generate_packet(self.packet)
                syn_ack = syn_result[0]
                if syn_ack:
                    seq_num = syn_ack[TCP].ack
                    ack_num = syn_ack[TCP].seq + 1
                    self.packet["tcp_seq_num"] = seq_num
                    self.packet["tcp_ack_num"] = ack_num
                    
                    # Create an ACK packet
                    ack_packet = self.generate_packet(tcp_type="A")
                    return ack_packet
                else: return syn_result   
            elif self.packet["tcp_type"] == "F":  # FIN packet
                fin_result = self.generate_packet(self.packet)
                fin_ack = fin_result[0]
                if fin_ack:
                    seq_num = fin_ack[TCP].ack
                    ack_num = fin_ack[TCP].seq + 1
                    self.packet["tcp_seq_num"] = seq_num
                    self.packet["tcp_ack_num"] = ack_num
                    
                    # Create an ACK packet
                    ack_packet = self.generate_packet(tcp_type="A")
                    return ack_packet
                else: return fin_result
            elif self.packet["tcp_type"] == "A":  # ACK packet
                ack_result = self.generate_packet(self.packet)
                ack_resp = ack_result[0]
                if ack_resp:
                    seq_num = ack_resp[TCP].ack
                    ack_num = ack_resp[TCP].seq + 1
                    self.packet["tcp_seq_num"] = seq_num
                    self.packet["tcp_ack_num"] = ack_num
                else: return ack_result
            else:  # All other cases (e.g. PSH, RST, etc.)
                return self.generate_packet(self.packet)
                
        else:
            return self.generate_packet(self.packet)


    def on_packet_selected(self):
        if self.selected:
            # Change Style  of top layout
            self.src_label.setStyleSheet(self.selectedTopLayout)
            self.dst_label.setStyleSheet(self.selectedTopLayout)
            self.packet_number_label.setStyleSheet(self.selectedTopLayout)

            # show details
            self.version_label = QLabel("Version: {}".format(self.packet["version"]))
            self.version_label.setStyleSheet(self.textStyle)
            self.protocol_label = QLabel("Protocol: {}".format(self.packet["proto"]))
            self.protocol_label.setStyleSheet(self.textStyle)
            self.payload_label = QLabel("Payload: {}".format(self.packet["payload"]))
            self.payload_label.setStyleSheet(self.textStyle)
            self.number_of_packets = QLabel("Number of Packets: {}".format(self.packet["number"]))
            self.number_of_packets.setStyleSheet(self.textStyle)
            self.bottom_layout.addWidget(self.version_label)
            self.bottom_layout.addWidget(self.protocol_label)
            self.bottom_layout.addWidget(self.payload_label)
            self.bottom_layout.addWidget(self.number_of_packets)
        else:
            # Change Style  of top layout
            self.src_label.setStyleSheet(self.textStyle)
            self.dst_label.setStyleSheet(self.textStyle)
            self.packet_number_label.setStyleSheet(self.textStyle)

            # hide details
            if self.version_label is not None:
                self.version_label.deleteLater()
                self.version_label = None
            if self.protocol_label is not None:
                self.protocol_label.deleteLater()
                self.protocol_label = None
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