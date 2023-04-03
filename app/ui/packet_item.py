from PyQt6.QtWidgets import  QVBoxLayout, QHBoxLayout, QLabel, QWidget,QListWidget
from PyQt6.QtCore import Qt, pyqtSignal,QSize

class PacketItemWidget(QWidget):
    packet_clicked = pyqtSignal()
    def __init__(self, data, parent=None):
        super().__init__(parent)
        
        self.setMaximumHeight(100)

        # Create the top-level vertical layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setObjectName("packet_item")
        self.setStyleSheet("#packet_item:hover {background-color: lightgrey;}")

        # Create the horizontal layout for the source and destination IP addresses
        self.src_dst_layout = QHBoxLayout()
        self.src_dst_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Create and add the labels for the source and destination IP addresses
        self.src_label = QLabel("Src: {}".format(data["srcIP"]))
        self.dst_label = QLabel("Dst: {}".format(data["dstIP"]))
        self.src_dst_layout.addWidget(self.src_label)
        self.src_dst_layout.addWidget(self.dst_label)

        # Create the details label and add it to the layout
        self.details_label = QLabel(self.get_details_text(data))
        self.details_label.setStyleSheet("color: grey;")
        self.layout.addLayout(self.src_dst_layout)
        self.layout.addWidget(self.details_label)
        self.details_label.hide()

        # Connect the click signal to show/hide the details label
        self.packet_clicked.connect(self.show_hide_details)
        self.adjustSize()

    def adjust_item_size_hint(self):
        item = self.parent()
        if item:
            self.adjustSize()
        self.size_changed.emit(item)

    def get_details_text(self, data):
        if data["type"] == "IP":
            return data["payload"]
        elif data["type"] == "DNS":
            return "DNS packet: id={}, qname={}".format(data["id"], data["qname"])
        elif data["type"] == "ARP":
            return "ARP packet: hwsrc={}, hwdst={}, psrc={}, pdst={}, op={}".format(
                data["hwsrc"], data["hwdst"], data["psrc"], data["pdst"], data["op"]
            )
        else:
            return "Unknown packet type"


    def show_hide_details(self):
        if self.details_label.isHidden():
            self.details_label.show()
            self.setMaximumHeight(self.sizeHint().height())  # Set maximum height
        else:
            self.details_label.hide()
            self.setMaximumHeight(16777215)

        self.adjustSize()

    def mousePressEvent(self, event):
        self.packet_clicked.emit()
        super().mousePressEvent(event)