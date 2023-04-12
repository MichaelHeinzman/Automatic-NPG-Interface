import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication,QStackedWidget,QMainWindow, QComboBox,  QPushButton, QVBoxLayout
from PyQt6.uic import loadUi
from network.packet_info import  ARP_PACKET_INFO, DNS_PACKET_INFO
from PyQt6.QtCore import pyqtSignal
from ip_packet_configuration import IPConfigurationWidget

# Screen 1, packet creation.
class PacketCreationScreen (QMainWindow):
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

        # Store Important UI Elements in variables.
        self.ip_page = self.findChild(IPConfigurationWidget, "ip_page")
        self.ip_page.setup_inputs(self)
        self.add_packet_signal.connect(lambda: self.ip_page.add_packet_signal(self))
        self.current_packet_type_select = self.findChild(QComboBox, "protocol_input")
        self.current_packet_type_select.currentTextChanged.connect(self.on_selection_changed)
        self.protocol_details_stacked = self.findChild(QStackedWidget, "protocol_types_configuration_pages")
        self.send_packets_button = self.findChild(QPushButton, "send_packets_button")
        self.add_packet_button = self.findChild(QPushButton, "add_packet_button")
        self.on_selection_changed("IP")

        self.add_packet_button.clicked.connect(self.add_packet_button_clicked)
        self.send_packets_button.clicked.connect(self.send_packets_button_clicked)

    def send_packets_button_clicked(self):
        self.send_packets_signal.emit()
        self.packet_number = 1

    def add_packet_button_clicked(self):
        self.add_packet_signal.emit()

    # On Protocol Change present different packet details forms.
    def on_selection_changed(self, value):
            if value == "IP":
                # Set the current page to IP Details.
                self.protocol_details_stacked.setCurrentIndex(0)
                self.ip_page.send_packets_signal = self.send_packets_signal
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




