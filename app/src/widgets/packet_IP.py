from PyQt6.QtWidgets import QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QWidget,QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from widgets.packet import PacketWidget

class IPPacketWidget(PacketWidget):
    # Signals
    send_packet_signal = pyqtSignal()

    def __init__(self, parent=None, packet=None, packet_number=0, add_to_summary=None):
        super().__init__(parent)
        self.add_to_summary = add_to_summary
        # Initialize variables
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

        # Create Bottom Layout
        self.bottom_layout = QVBoxLayout()
        self.bottom_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.bottom_layout.setSpacing(10)
        
        # Create top-level horizontal layout
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

        # Add spacing 
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.top_layout.addWidget(self.packet_number_label)
        self.top_layout.addItem(spacer)
        self.top_layout.addWidget(self.src_label)
        self.top_layout.addItem(spacer)
        self.top_layout.addWidget(self.dst_label)
        self.top_layout.addItem(spacer)
        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.bottom_layout)
        self.packet_selected.connect(self.on_packet_selected)
        
    # Sends the generated packet
    def send_packet(self):
        result = self.generate_packet(self.packet)
        if (result):
            self.__del__()
            self.add_to_summary(result)
        


    def on_packet_selected(self):
        if self.selected:
            # Change Style  of top layout
            self.src_label.setStyleSheet(self.selectedTopLayout)
            self.dst_label.setStyleSheet(self.selectedTopLayout)
            self.packet_number_label.setStyleSheet(self.selectedTopLayout)

            # show details
            self.version_label = QLabel("Version: {}".format(self.version))
            self.version_label.setStyleSheet(self.textStyle)
            self.protocol_label = QLabel("Protocol: {}".format(self.protocol))
            self.protocol_label.setStyleSheet(self.textStyle)
            self.payload_label = QLabel("Payload: {}".format(self.payload))
            self.payload_label.setStyleSheet(self.textStyle)
            self.number_of_packets = QLabel("Number of Packets: {}".format(self.number_of_packet))
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