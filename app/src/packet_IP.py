from PyQt6.QtWidgets import QHBoxLayout, QLabel,QSpacerItem,QSizePolicy,QWidget
from PyQt6.QtCore import  Qt,pyqtSignal
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


        # Top Layout
        self.top_layout = QHBoxLayout()
        self.top_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.top_layout.setSpacing(10)

        # Create and add the labels for the source and destination IP addresses
        self.packet_number_label = QLabel("No. {}".format(self.packet_number))
        self.src_label = QLabel("Src: {}".format(packet["srcIP"]))
        self.dst_label = QLabel("Dst: {}".format(packet["dstIP"]))

        self.src_label.setStyleSheet(self.textStyle)
        self.dst_label.setStyleSheet(self.textStyle)
        self.packet_number_label.setStyleSheet(self.textStyle)

        # Add Spacing 
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.top_layout.addWidget(self.packet_number_label)
        self.top_layout.addItem(spacer)
        self.top_layout.addWidget(self.src_label)
        self.top_layout.addItem(spacer)
        self.top_layout.addWidget(self.dst_label)
        self.top_layout.addItem(spacer)
        self.layout.addLayout(self.top_layout)
    
    def send_packet(self):
        self.generate_packet(self.packet)
        self.__del__()
        self.remove_packet.emit()

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
