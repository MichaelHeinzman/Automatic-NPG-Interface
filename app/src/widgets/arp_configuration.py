from PyQt6.QtWidgets import QWidget, QLineEdit, QRadioButton,QStackedWidget,QGridLayout
from network.packet_info import  ARP_PACKET_INFO
from widgets.packet_ARP import ARPPacketWidget

class ARPConfigurationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.packet = ARP_PACKET_INFO

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

    def setup_radio_buttons(self):
        self.arp_is_at_radio = self.findChild(QRadioButton, "arp_is_at_radio")
        self.arp_who_has_radio = self.findChild(QRadioButton, "arp_who_has_radio")
        self.arp_is_at_radio.clicked.connect(self.handle_arp_type_change)
        self.arp_who_has_radio.clicked.connect(self.handle_arp_type_change)

    def setup_inputs(self):
        # Radio Button
        self.setup_radio_buttons()

        # Get IP Inputs and store references in dictionary
        input_names = ["pdst", "number"]
        input_ids = ["destination_ip_address_arp_input", "number_arp_input"]
        
        for name, widget_id in zip(input_names, input_ids):
            self.handle_input(name, widget_id)

    def handle_input(self, name, widget_id):
        widget = self.findChild(QLineEdit, widget_id)
        widget.setText(str(self.packet[name]))
        widget.textChanged.connect(lambda value, key=name: self.update_packet(value, key))
        self.input_widgets[name] = widget

    def handle_arp_type_change(self):
        if self.arp_who_has_radio.isChecked():
            self.packet["op"] = "who-has"
        elif self.arp_is_at_radio.isChecked():
            self.packet["op"] = "is-at"

    def add_packet_clicked(self, parent):
        # Create a copy of the current packet
        packet_copy = dict(self.packet)
        item_widget = ARPPacketWidget(packet=packet_copy, packet_number=parent.packet_number, add_to_summary=parent.add_to_summary)
        parent.add_packet_to_send_list(item_widget)