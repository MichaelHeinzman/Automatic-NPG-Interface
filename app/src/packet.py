from PyQt6.QtWidgets import QWidget,QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt6.QtCore import pyqtSignal, Qt
import network.packet_generator as packet_generator

class PacketWidget(QWidget):
    packet_clicked = pyqtSignal()
    packet_selected = pyqtSignal()
    packet_generation_completed = pyqtSignal(object)
    remove_packet = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.selected = False
        self.protocol = "undefined"
        self.number_of_packet = 1
        self.textStyle = '''
            position: absolute;
            width: 122px;
            max-height: 32px;
            padding: 10px;
            left: 700px;
            top: 161px;
            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 16px;
            line-height: 19px;
            text-align: center;
            color: #363C4B;
            background-color: rgba(217, 217, 217, 1);
        '''
        self.packet_clicked.connect(self.on_packet_clicked)

        # Layout.
        self.setMaximumHeight(300)

        # Create the top-level vertical layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setObjectName("packet_item")
        self.setStyleSheet("#packet_item:hover {background-color: lightgrey;}")
        
        # Connect the click signal to show/hide the details label
        self.adjustSize()
        
    # Functions
    def on_packet_clicked(self):
        self.selected = not self.selected
        self.packet_selected.emit()

    def mousePressEvent(self, event):
        self.packet_clicked.emit()
        super().mousePressEvent(event)
    
    def generate_packet(self, packet):
        result = packet_generator.generate_packets(packet)
        self.packet_generation_completed.emit(result)



