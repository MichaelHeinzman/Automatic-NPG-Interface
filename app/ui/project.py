import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication,QStackedWidget,QDialog, QComboBox,  QLineEdit, QPushButton, QVBoxLayout,QListWidgetItem
from PyQt6.uic import loadUi
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from network.packet_info import IP_PACKET_INFO, ARP_PACKET_INFO, DNS_PACKET_INFO
import network.packet_processing as packet_processing
from packet_generator_thread import PacketGeneratorThread
from packet_item import PacketItemWidget


# Screen 1, packet creation.
class PacketCreationScreen (QDialog):
    def __init__(self):
        super(PacketCreationScreen, self).__init__()

        loadUi("welcomescreen.ui", self)

        # Important Variables
        self.packet = {}
        self.packet_thread = None
        self.packet_result = None

        # Store Important UI Elements in variables.
        self.current_packet_type_select = self.findChild(QComboBox, "ProtocolSelectionInput")
        self.current_packet_type_select.currentTextChanged.connect(self.on_selection_changed)
        self.protocol_details_stacked = self.findChild(QStackedWidget, "ProtocolsContainer")
        self.send_packet_button = self.findChild(QPushButton, "SendPacketButton")
        self.destination_mac_IP = None
        self.payload_IP = None
        
        # Validate and Format Inputs (MAC, IP, etc...).
        self.validate_inputs()
        self.on_selection_changed("IP")

        # On Send Packet Button Push, handle packet sending and validating. 
        self.send_packet_button.clicked.connect(self.send_packet)


    def send_packet(self):
        if self.packet_thread is not None and self.packet_thread.isRunning():
            self.packet_thread.terminate()
        
        self.send_packet_button.setText("Sending Packet...")
        self.packet_thread = PacketGeneratorThread(self.packet)
        self.packet_thread.started.connect(self.on_thread_started)
        self.packet_thread.finished.connect(self.on_thread_finished)
        self.packet_thread.packet_generated.connect(self.on_packet_generated)
        self.packet_thread.start()

    def on_thread_started(self):
        self.send_packet_button.setDisabled(True)

    def on_thread_finished(self):
        self.send_packet_button.setDisabled(False)
        self.send_packet_button.setText("Send Packet")

    def on_packet_generated(self, result):
        self.packet_result = result
        processed_packets = packet_processing.process_packets(result)
        self.packets_list = self.findChild(QVBoxLayout, "packets_list")

        # Add items to the model
        for packet in processed_packets:
            item_widget = PacketItemWidget(packet)
            self.packets_list.addWidget(item_widget)


    # Validate and Format inputs.
    def validate_inputs(self):
        self.validate_mac_inputs()
        self.validate_ip_inputs()

    # Validate MAC Inputs
    def validate_mac_inputs(self):
        for widget in self.findChildren(QLineEdit):
            if  widget.property('MAC_ADDRESS'):
                widget.setMaxLength(17)
                widget.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')))
                widget.setPlaceholderText('00:11:22:33:44:55')

    # Validate IP Inputs
    def validate_ip_inputs(self):
        for widget in self.findChildren(QLineEdit):
            if  widget.property('IP'):
                widget.setMaxLength(15)
                widget.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression('^([0-9]{1,3}\.){3}[0-9]{1,3}$')))
                widget.setPlaceholderText('192.168.0.1')

    # On Protocol Change present different packet details forms.
    def on_selection_changed(self, value):
            if value == "IP":
                # Set the current page to IP Details.
                self.protocol_details_stacked.setCurrentIndex(0)

                # Set the packet to default IP Packet Info.
                self.packet = IP_PACKET_INFO

                # Get IP Inputs
                self.source_mac_IP = self.findChild(QLineEdit, "SourceMacAddressInput_8")
                self.destination_mac_IP = self.findChild(QLineEdit, "SourceMacAddressInput_9")
                self.payload_IP = self.findChild(QLineEdit, "PayloadInput_5")

                # Set IP Values
                self.source_mac_IP.setText(IP_PACKET_INFO["srcIP"])
                self.destination_mac_IP.setText(IP_PACKET_INFO["dstIP"])
                self.payload_IP.setText(IP_PACKET_INFO["payload"])

                # Update packet values with changed IP values.
                self.source_mac_IP.textChanged.connect(lambda value: self.update_packet("srcIP", value))
                self.destination_mac_IP.textChanged.connect(lambda value: self.update_packet("dstIP", value))
                self.payload_IP.textChanged.connect(lambda value: self.update_packet("payload", value))
                
                return 
            elif value == "DNS":
                self.protocol_details_stacked.setCurrentIndex(1)
                self.packet = DNS_PACKET_INFO
                return
            elif value == "ARP":
                self.protocol_details_stacked.setCurrentIndex(2)
                self.packet = ARP_PACKET_INFO
                return
            else:
                return

    # Updates the current packet with changed values.
    def update_packet (self, index, value):
        self.packet[index] = value

# Launch Application
app = QApplication(sys.argv)
packetCreation = PacketCreationScreen()
widget = QStackedWidget()
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.addWidget(packetCreation)
widget.show()

try: 
    sys.exit(app.exec())
except:
    print("Exiting")




