from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QHBoxLayout,QRadioButton,QStackedWidget
from PyQt6.QtCore import Qt
from network.packet_info import  TCP_IP_PACKET, ICMP_IP_PACKET, UDP_IP_PACKET
from widgets.packet_IP import IPPacketWidget

class IPConfigurationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.packet = ICMP_IP_PACKET

        # Dictionary to store references to input widgets
        self.input_widgets = {}

        # Call the setup_inputs method to initialize the input widgets
        if (parent):
            self.setup_inputs()
            self.add_packet_signal.connect(self.add_packet, parent)

    # Updates the current packet with changed values.
    def update_packet(self, value, index):
        if index in {'number', 'ttl'}:
            value = int(value)
        self.packet[index] = value

    def setup_ip_stacked(self):
        self.ip_stacked = self.findChild(QStackedWidget, "ip_types_stacked_widget")
        
    def setup_radio_buttons(self):
        self.icmp_radio = self.findChild(QRadioButton, "icmp_radio")
        self.tcp_radio = self.findChild(QRadioButton, "tcp_radio")
        self.udp_radio = self.findChild(QRadioButton, "udp_radio")

        self.icmp_radio.clicked.connect(self.handle_ip_type_change)
        self.tcp_radio.clicked.connect(self.handle_ip_type_change)
        self.udp_radio.clicked.connect(self.handle_ip_type_change)

    def setup_inputs(self):
        self.setup_ip_stacked()
        self.setup_radio_buttons()
        # Get IP Inputs and store references in dictionary
        input_names = ["srcIP", "dstIP", "ttl", "payload", "number"]
        input_ids = ["source_ip_address_input", "destination_ip_address_input", "time_to_live_ip_input",
                    "ip_payload_input", "number_ip_input"]
        
        for name, widget_id in zip(input_names, input_ids):
            widget = self.findChild(QLineEdit, widget_id)
            widget.setText(str(self.packet[name]))
            widget.textChanged.connect(lambda value, key=name: self.update_packet(value, key))
            self.input_widgets[name] = widget

    def handle_ip_type_change (self):
        if self.icmp_radio.isChecked():
            self.packet = ICMP_IP_PACKET
            self.ip_stacked.setCurrentIndex(1)
            self.ip_stacked.hide()
        elif self.tcp_radio.isChecked():
            self.packet = TCP_IP_PACKET
            self.ip_stacked.setCurrentIndex(0)
            self.ip_stacked.show()
        elif self.udp_radio.isChecked():
            self.packet = UDP_IP_PACKET
            self.ip_stacked.setCurrentIndex(2)
            self.ip_stacked.hide()

        self.update_input_fields()
        
    def update_input_fields(self):
        for name, widget in self.input_widgets.items():
            widget.setText(str(self.packet[name]))
    def add_packet_clicked(self, parent):
        item_widget = IPPacketWidget(packet=self.packet, packet_number=parent.packet_number, add_to_summary=parent.add_to_summary)
        parent.add_packet_to_send_list(item_widget)