from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from network.packet_info import IP_PACKET_INFO
from packet_IP import IPPacketWidget

class IPConfigurationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.packet = IP_PACKET_INFO

        # Dictionary to store references to input widgets
        self.input_widgets = {}

        # Call the setup_inputs method to initialize the input widgets
        if (parent):
            self.setup_inputs(parent)
            self.add_packet_signal.connect(self.add_packet, parent)

    # Updates the current packet with changed values.
    def update_packet(self, value, index):
        self.packet[index] = value

    def setup_inputs(self, parent):
        # Get IP Inputs and store references in dictionary
        self.input_widgets["source_mac_IP"] = parent.findChild(QLineEdit, "source_ip_address_input")
        self.input_widgets["destination_mac_IP"] = parent.findChild(QLineEdit, "destination_ip_address_input")
        self.input_widgets["time_to_live_IP"] = parent.findChild(QLineEdit, "time_to_live_ip_input")
        self.input_widgets["protocol_IP"] = parent.findChild(QLineEdit, "protocol_ip_input")
        self.input_widgets["flags_IP"] = parent.findChild(QLineEdit, "flags_ip_input")
        self.input_widgets["fragmentation_offset_IP"] = parent.findChild(QLineEdit, "fragmentation_offset_ip_input")
        self.input_widgets["identification_IP"] = parent.findChild(QLineEdit, "identification_ip_input")
        self.input_widgets["payload_IP"] = parent.findChild(QLineEdit, "ip_payload_input")
        
        input_names = ["srcIP", "dstIP", "ttl", "proto", "flags", "frag", "id", "payload"]
        input_ids = ["source_ip_address_input", "destination_ip_address_input", "time_to_live_ip_input",
                    "protocol_ip_input", "flags_ip_input", "fragmentation_offset_ip_input", "identification_ip_input",
                    "ip_payload_input"]
        
        for name, widget_id in zip(input_names, input_ids):
            widget = self.findChild(QLineEdit, widget_id)
            widget.setText(str(self.packet[name]))
            widget.textChanged.connect(lambda value, key=name: self.update_packet(value, key))
            self.input_widgets[name] = widget

    def add_packet_clicked(self, parent):
        item_widget = IPPacketWidget(packet=self.packet, packet_number=parent.packet_number)
        parent.add_packet_to_send_list(item_widget)