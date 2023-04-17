# Import necessary modules
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import (
    QApplication, QStackedWidget, QMainWindow, QComboBox, QPushButton,
    QVBoxLayout)
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSignal, Qt, QThreadPool
from widgets.ip_packet_configuration import IPConfigurationWidget
from widgets.packet_sender import PacketSender


# Define PacketCreationScreen class
class PacketCreationScreen(QMainWindow):
    # Define custom signals
    add_packet_signal = pyqtSignal()
    send_packets_signal = pyqtSignal()
    
    # Initialize the class
    def __init__(self):
        super(PacketCreationScreen, self).__init__()

        # Load the UI file
        loadUi("./ui/main.ui", self)

        # Initialize variables
        self.packet = {}
        self.packet_thread = None
        self.packet_result = None
        self.packet_number = 1
        self.packets_to_send = []

        # Set up UI elements
        self.setup_configuration_pages()
        self.setup_protocol_selection()
        self.to_send_packets_list = self.findChild(QVBoxLayout, "to_send_packets_list")
        self.to_send_packets_list.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.send_packets_button = self.findChild(QPushButton, "send_packets_button")
        self.add_packet_button = self.findChild(QPushButton, "add_packet_button")
        
        # Connect button signals to functions
        self.add_packet_button.clicked.connect(self.add_packet_clicked)
        self.send_packets_button.clicked.connect(self.send_packets_button_clicked)

    # Function to handle "Add Packet" button click
    def add_packet_clicked(self):
        # Get the index of the selected protocol configuration page
        index = self.protocol_details_stacked.currentIndex()
        
        # Call the appropriate function based on the selected protocol
        if index == 0: 
            return self.ip_page.add_packet_clicked(self)
        elif index == 1: 
            print("ARP")
            return
        elif index == 2:
            print("DNS")
            return
        else:
            return
    
    # Function to add a packet to the list of packets to be sent
    def add_packet_to_send_list(self, packet):
        self.packets_to_send.append(packet)
        self.to_send_packets_list.addWidget(packet)
        self.packet_number += 1

    # Function to handle "Send Packets" button click
    def send_packets_button_clicked(self):
        # Reset packet number
        self.packet_number = 1
        
        # Get the global thread pool instance
        threadpool = QThreadPool.globalInstance()
        
        # Start a new thread for each packet to be sent
        for packet in self.packets_to_send:
            runnable = PacketSender(packet)
            threadpool.start(runnable)
            
            # Remove packet from UI list after sending
            self.to_send_packets_list.removeWidget(packet)
            packet.__del__()
        
        # Clear the list of packets to be sent
        self.packets_to_send.clear()

    # Function to update the current packet with changed values
    def update_packet(self, index, value):
        self.packet[index] = value

    # Function to set up the protocol configuration pages
    def setup_configuration_pages(self):
        # Store Important UI Elements in variables.
        self.ip_page = self.findChild(IPConfigurationWidget, "ip_page")
        self.ip_page.setup_inputs(self)

    # Function to set up the protocol selection combo box
    def setup_protocol_selection(self):
        self.protocol_details_stacked = self.findChild(QStackedWidget, "protocol_types_configuration_pages")
        self.protocol_selection = self.findChild(QComboBox, "protocol_input")
        self.protocol_selection.protocol_details_stacked = self.protocol_details_stacked
        self.protocol_selection.setup()


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




