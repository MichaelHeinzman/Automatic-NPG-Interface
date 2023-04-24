# Import necessary modules
import os
import sys
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import (
    QApplication, QStackedWidget, QMainWindow, QComboBox, QPushButton,QTabWidget,QLabel,
    QVBoxLayout)
from PyQt6.uic import loadUi
from PyQt6.QtCore import pyqtSignal, Qt, QThreadPool
from widgets.ip_packet_configuration import IPConfigurationWidget
from widgets.dns_configuration import DNSConfigurationWidget
from widgets.arp_configuration import ARPConfigurationWidget
from widgets.packet_sender import PacketSender
from widgets.packet_ARP import ARPPacketWidget
from widgets.packet_IP import IPPacketWidget
from widgets.packet_DNS import DNSPacketWidget

from network import packet_processing, export

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
        self.packet_finished_number = 1
        self.packets_to_send = []
        self.packet_summary = []
        
        # Set up UI elements
        self.setup_tabs()
        self.setup_configuration_pages()
        self.setup_protocol_selection()
        self.to_send_packets_list = self.findChild(QVBoxLayout, "to_send_packets_list")
        self.to_send_packets_list.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.packets_list = self.findChild(QVBoxLayout, "packets_list")
        self.packets_list.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.send_packets_button = self.findChild(QPushButton, "send_packets_button")
        self.add_packet_button = self.findChild(QPushButton, "add_packet_button")
        self.export_to_wireshark_button = self.findChild(QPushButton, "export_to_wireshark_button")
        self.duration_packet_generation_value = self.findChild(QLabel, "duration_packet_generation_value")
        self.total_number_of_packets = self.findChild(QLabel, "total_number_of_packets")
        self.download_pcap_file_button = self.findChild(QPushButton, "download_pcap_file_button")

        # Connect button signals to functions
        self.add_packet_button.clicked.connect(self.add_packet_clicked)
        self.send_packets_button.clicked.connect(self.send_packets_button_clicked)
        self.export_to_wireshark_button.clicked.connect(self.export_to_wireshark)
        self.download_pcap_file_button.clicked.connect(self.download_pcap_file)

    def download_pcap_file(self):
        sent_packets, answered_packets, unanswered_packets = self.pcap_file_helper()
        if (answered_packets or unanswered_packets):
            export.download_pcap_file(answered_packets + unanswered_packets)
        else:
            export.download_pcap_file(sent_packets)
            
    def pcap_file_helper(self):
        sent_packets = []
        # Combine all the sent packets into one list
        sent_packets = []
        for result in self.packet_summary:
            sent_packets += result[2]

        # Combine all the answered and unanswered packets into one list
        answered_packets = []
        unanswered_packets = []
        for result in self.packet_summary:
            answered_packets += result[0]
            unanswered_packets += result[1]

        return (sent_packets, answered_packets, unanswered_packets)
    
    def export_to_wireshark(self):
        sent_packets, answered_packets, unanswered_packets = self.pcap_file_helper()
        if (answered_packets or unanswered_packets):
            export.export_to_wireshark(answered_packets + unanswered_packets)
        else:
            export.export_to_wireshark(sent_packets)


    # Function to handle "Add Packet" button click
    def add_packet_clicked(self):
        # Get the index of the selected protocol configuration page
        index = self.protocol_details_stacked.currentIndex()
        
        # Call the appropriate function based on the selected protocol
        if index == 0: 
            return self.ip_page.add_packet_clicked(self)
        elif index == 1: 
            return self.arp_page.add_packet_clicked(self)
        elif index == 2:
            return self.dns_page.add_packet_clicked(self)
        else:
            return
    
    # Function to add a packet to the list of packets to be sent
    def add_packet_to_send_list(self, packet):
        self.packets_to_send.append(packet)
        self.to_send_packets_list.addWidget(packet)
        self.packet_number += 1

    # Function to handle "Send Packets" button click
    def send_packets_button_clicked(self):
        # Clear Current packet_summary
        self.packet_summary.clear()

        # Remove packet from UI list after sending
        if (self.packets_list.count() > 0):
            for i in reversed(range(self.packets_list.count())):
                widget = self.packets_list.itemAt(i).widget()

                if widget is not None:
                    self.packets_list.removeWidget(widget)
                    widget.__del__()

        # Reset console output label.
        self.findChild(QLabel, "console_output_label").setText("")
        
        # Reset packet number
        self.packet_number = 1
        self.packet_finished_number = 1

        # Get the global thread pool instance
        threadpool = QThreadPool.globalInstance()
        
        # Start Time
        start_time = datetime.datetime.now()

        # Start a new thread for each packet to be sent
        for packet in self.packets_to_send:
            runnable = PacketSender(packet)
            runnable.signals.finished.connect(self.on_packet_finished_sending)
            threadpool.start(runnable)
        # Clear the list of packets to be sent
        self.packets_to_send.clear()

        # Wait for all threads to finish
        while threadpool.activeThreadCount() > 0:
            QApplication.processEvents()
        
        # Get End Time of Generation of Packets
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        total_time = f"{duration.total_seconds():.2f} seconds"
        self.duration_packet_generation_value.setText(total_time)

    def on_packet_finished_sending(self, result, sent_packet):
        self.packet_summary.append(result)

        # Remove from send List and add to packets_list
        self.to_send_packets_list.removeWidget(sent_packet)

        # process the packets in the summary
        processed_packets = packet_processing.process_packets(result[0])

        print(processed_packets)
        if not processed_packets:
            for i in range(sent_packet.packet["number"]):
                self.packets_list.addWidget(sent_packet)
                self.packet_finished_number += 1
        else:
            packet_type_to_widget_class = {
                "IP": IPPacketWidget,
                "ARP": ARPPacketWidget,
                "DNS": DNSPacketWidget,
            }

            for packet in processed_packets:
                packet_type = packet["type"]
                if packet_type in packet_type_to_widget_class:
                    sent = packet_type_to_widget_class[packet_type](
                        packet=sent_packet.packet, packet_number=self.packet_finished_number
                    )
                    self.packet_finished_number += 1
                    widget = packet_type_to_widget_class[packet_type](
                        packet=packet, packet_number=self.packet_finished_number
                    )
                    self.packets_list.addWidget(sent)
                    self.packets_list.addWidget(widget)
                    self.packet_finished_number += 1
                    self.total_number_of_packets.setText(str(self.packet_finished_number - 1))

    # Function to update the current packet with changed values
    def update_packet(self, index, value):
        self.packet[index] = value

    # Function to set up tabs or pages.
    def setup_tabs(self):
        self.tab_widget = self.findChild(QTabWidget, "tabWidget")

    # Function to set up the protocol configuration pages
    def setup_configuration_pages(self):
        # Store Important UI Elements in variables.
        self.ip_page = self.findChild(IPConfigurationWidget, "ip_page")
        self.ip_page.setup_inputs()

        self.dns_page = self.findChild(DNSConfigurationWidget, "dns_page")
        self.dns_page.setup_inputs()

        self.arp_page = self.findChild(ARPConfigurationWidget, "arp_page")
        self.arp_page.setup_inputs()

    # Function to set up the protocol selection combo box
    def setup_protocol_selection(self):
        self.protocol_details_stacked = self.findChild(QStackedWidget, "protocol_types_configuration_pages")
        self.protocol_selection = self.findChild(QComboBox, "protocol_input")
        self.protocol_selection.protocol_details_stacked = self.protocol_details_stacked
        self.protocol_selection.setup()

# Launch Application
app = QApplication(sys.argv)
packetCreation = PacketCreationScreen()
packetCreationWidget = QMainWindow()
packetCreationWidget.setWindowTitle("Automatic Network Packet Generator")
packetCreationWidget.setCentralWidget(packetCreation)
packetCreationWidget.show()

try: 
    sys.exit(app.exec())
except:
    print("Exiting")




