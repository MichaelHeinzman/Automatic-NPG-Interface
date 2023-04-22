from PyQt6.QtWidgets import QWidget, QVBoxLayout, QWidget
from PyQt6.QtCore import pyqtSignal, Qt
import network.packet_generator as packet_generator


class PacketWidget(QWidget):
    # Define signals that this widget will emit
    packet_clicked = pyqtSignal()
    packet_selected = pyqtSignal()
    remove_packet = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize variables to be used later
        self.selected = False
        self.protocol = "undefined"
        self.number_of_packet = 1

        # Define a style string that will be used to style the widget
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

        self.selectedTopLayout = '''
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
            background-color: #FFD600;
        '''

        # Connect the packet_clicked signal to the on_packet_clicked method
        self.packet_clicked.connect(self.on_packet_clicked)

        # Set the maximum height of this widget to 300
        self.setMaximumHeight(300)

        # Create a vertical layout for this widget
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Set the object name and style sheet for this widget
        self.setObjectName("packet_item")
        self.setStyleSheet("#packet_item:hover {background-color: lightgrey;}")

        # Call adjustSize() to resize the widget based on its contents
        self.adjustSize()

    # Function that will be called when the widget is clicked
    def on_packet_clicked(self):
        self.selected = not self.selected
        # Emit the packet_selected signal
        self.packet_selected.emit()

    # Override the mousePressEvent to emit the packet_clicked signal
    def mousePressEvent(self, event):
        self.packet_clicked.emit()
        super().mousePressEvent(event)

    # Function to generate a packet using the packet_generator module
    def generate_packet(self, packet):
        return packet_generator.generate_packets(packet)
