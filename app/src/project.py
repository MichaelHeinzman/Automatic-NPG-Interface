import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication,QStackedWidget,QMainWindow, QComboBox,  QPushButton, QVBoxLayout
from PyQt6.uic import loadUi
from network.packet_info import  ARP_PACKET_INFO, DNS_PACKET_INFO
from PyQt6.QtCore import pyqtSignal,Qt,QThreadPool
from widgets.ip_packet_configuration import IPConfigurationWidget
from widgets.packet_sender import PacketSender

# Screen 1, packet creation.
class PacketCreationScreen(QMainWindow):
    add_packet_signal = pyqtSignal()
    send_packets_signal = pyqtSignal()
    
    def __init__(self):
        super(PacketCreationScreen, self).__init__()

        loadUi("./ui/main.ui", self)

        # Important Variables
        self.packet = {}
        self.packet_thread = None
        self.packet_result = None
        self.packet_number = 1
        self.packets_to_send = []

        self.setup_configuration_pages()
        self.setup_protocol_selection()

        self.to_send_packets_list = self.findChild(QVBoxLayout, "to_send_packets_list")
        self.to_send_packets_list.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.current_packet_type_select = self.findChild(QComboBox, "protocol_input")
        self.current_packet_type_select.protocol_details_stacked = self.protocol_details_stacked

        self.send_packets_button = self.findChild(QPushButton, "send_packets_button")
        self.add_packet_button = self.findChild(QPushButton, "add_packet_button")
        

        self.add_packet_button.clicked.connect(self.add_packet_clicked)
        self.send_packets_button.clicked.connect(self.send_packets_button_clicked)

    def add_packet_clicked(self):
        index = self.protocol_details_stacked.currentIndex()
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
        
    def add_packet_to_send_list(self, packet):
        self.packets_to_send.append(packet)
        self.to_send_packets_list.addWidget(packet)
        self.packet_number += 1

    def send_packets_button_clicked(self):
        self.packet_number = 1
        threadpool = QThreadPool.globalInstance()
        for packet in self.packets_to_send:
            runnable = PacketSender(packet)
            threadpool.start(runnable)
            # remove packet from UI list after sending
            self.to_send_packets_list.removeWidget(packet)
            packet.__del__()
        self.packets_to_send.clear()

    # Updates the current packet with changed values.
    def update_packet(self, index, value):
        self.packet[index] = value

    def setup_configuration_pages(self):
        # Store Important UI Elements in variables.
        self.ip_page = self.findChild(IPConfigurationWidget, "ip_page")
        self.ip_page.setup_inputs(self)

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




