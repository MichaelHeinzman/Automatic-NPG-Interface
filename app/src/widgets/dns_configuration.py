from PyQt6.QtWidgets import QWidget, QLineEdit, QRadioButton,QStackedWidget,QGridLayout
from network.packet_info import  DNS_PACKET_INFO
from widgets.packet_DNS import DNSPacketWidget

class DNSConfigurationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.packet = DNS_PACKET_INFO

        # Dictionary to store references to input widgets
        self.input_widgets = {}

        # Call the setup_inputs method to initialize the input widgets
        if (parent):
            self.setup_inputs()
            self.add_packet_signal.connect(self.add_packet, parent)

    # Updates the current packet with changed values.
    def update_packet(self, value, index):
        if index in {'number'}:
            value = int(value)
        self.packet[index] = value

    def setup_inputs(self):
        # Get IP Inputs and store references in dictionary
        input_names = ["qname", "number", "srcIP"]
        input_ids = ["dns_query_name_input", "dns_packet_number_input", "dns_source_ip_address_input"]
        
        for name, widget_id in zip(input_names, input_ids):
            self.handle_input(name, widget_id)

    def handle_input(self, name, widget_id):
        widget = self.findChild(QLineEdit, widget_id)
        widget.setText(str(self.packet[name]))
        widget.textChanged.connect(lambda value, key=name: self.update_packet(value, key))
        self.input_widgets[name] = widget
            
    def add_packet_clicked(self, parent):
        # Create a copy of the current packet
        packet_copy = dict(self.packet)
        item_widget = DNSPacketWidget(packet=packet_copy, packet_number=parent.packet_number, add_to_summary=parent.add_to_summary)
        parent.add_packet_to_send_list(item_widget)