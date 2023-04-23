from PyQt6.QtWidgets import QWidget, QLineEdit, QRadioButton,QStackedWidget,QGridLayout
from network.packet_info import  TCP_IP_PACKET, ICMP_IP_PACKET, UDP_IP_PACKET
from widgets.packet_IP import IPPacketWidget

class IPConfigurationWidget(QWidget):
    TCP_FLAG_MAP = {
    "tcp_ack_radio": "A",
    "tcp_fin_radio": "F",
    "tcp_finack_radio": "FA",
    "tcp_psh_radio": "P",
    "tcp_rst_radio": "R",
    "tcp_syn_radio": "S",
    "tcp_synack_radio": "SA",
    "tcp_urg_radio": "U"
    }

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
        if index in {'number', 'ttl', "sport", "dport"}:
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

        self.handle_input('sport', "tcp_source_port_input")
        self.handle_input('dport', "tcp_destination_port_input")
        self.handle_input('sport', "udp_source_port_input")
        self.handle_input('dport', "udp_destination_port_input")
        self.handle_ip_type_change()

        self.tcp_ack_radio = self.findChild(QRadioButton, "tcp_ack_radio")
        self.tcp_fin_radio = self.findChild(QRadioButton, "tcp_fin_radio")
        self.tcp_finack_radio = self.findChild(QRadioButton, "tcp_finack_radio")
        self.tcp_psh_radio = self.findChild(QRadioButton, "tcp_psh_radio")
        self.tcp_rst_radio = self.findChild(QRadioButton, "tcp_rst_radio")
        self.tcp_syn_radio = self.findChild(QRadioButton, "tcp_syn_radio")
        self.tcp_synack_radio = self.findChild(QRadioButton, "tcp_synack_radio")
        self.tcp_urg_radio = self.findChild(QRadioButton, "tcp_urg_radio")

        self.tcp_ack_radio.clicked.connect(lambda: self.handle_tcp_type_change(self.tcp_ack_radio))
        self.tcp_fin_radio.clicked.connect(lambda: self.handle_tcp_type_change(self.tcp_fin_radio))
        self.tcp_finack_radio.clicked.connect(lambda: self.handle_tcp_type_change(self.tcp_finack_radio))
        self.tcp_psh_radio.clicked.connect(lambda: self.handle_tcp_type_change(self.tcp_psh_radio))
        self.tcp_rst_radio.clicked.connect(lambda: self.handle_tcp_type_change(self.tcp_rst_radio))
        self.tcp_syn_radio.clicked.connect(lambda: self.handle_tcp_type_change(self.tcp_syn_radio))
        self.tcp_synack_radio.clicked.connect(lambda: self.handle_tcp_type_change(self.tcp_synack_radio))
        self.tcp_urg_radio.clicked.connect(lambda: self.handle_tcp_type_change(self.tcp_urg_radio))

    def setup_inputs(self):
        self.tcp_types_grid = self.findChild(QGridLayout, "tcp_types_grid")
        self.setup_ip_stacked()
        self.setup_radio_buttons()
        # Get IP Inputs and store references in dictionary
        input_names = ["srcIP", "dstIP", "ttl", "payload", "number"]
        input_ids = ["source_ip_address_input", "destination_ip_address_input", "time_to_live_ip_input",
                    "ip_payload_input", "number_ip_input"]
        
        for name, widget_id in zip(input_names, input_ids):
            self.handle_input(name, widget_id)

    def handle_input(self, name, widget_id):
        widget = self.findChild(QLineEdit, widget_id)
        widget.setText(str(self.packet[name]))
        widget.textChanged.connect(lambda value, key=name: self.update_packet(value, key))
        self.input_widgets[name] = widget

    def handle_tcp_type_change(self, checked_button):
        button_name = checked_button.objectName()
        if button_name in self.TCP_FLAG_MAP:
            self.packet['tcp_type'] = self.TCP_FLAG_MAP[button_name]
            
    def handle_ip_type_change(self):
        if self.icmp_radio.isChecked():
            self.packet = ICMP_IP_PACKET
            self.ip_stacked.setCurrentIndex(2)
            self.ip_stacked.hide()
        elif self.tcp_radio.isChecked():
            self.packet = TCP_IP_PACKET
            self.ip_stacked.setCurrentIndex(0)
            self.ip_stacked.show()
        elif self.udp_radio.isChecked():
            self.packet = UDP_IP_PACKET
            self.ip_stacked.setCurrentIndex(1)
            self.ip_stacked.show()

        self.update_input_fields()

    def update_input_fields(self):
        for name, widget in self.input_widgets.items():
            widget.setText(str(self.packet[name]))

    def add_packet_clicked(self, parent):
        # Create a copy of the current packet
        packet_copy = dict(self.packet)
        item_widget = IPPacketWidget(packet=packet_copy, packet_number=parent.packet_number, add_to_summary=parent.add_to_summary)
        parent.add_packet_to_send_list(item_widget)