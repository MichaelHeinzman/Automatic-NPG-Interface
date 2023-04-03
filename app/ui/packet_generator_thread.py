from PyQt6.QtCore import pyqtSignal, QThread
import network.packet_generator as packet_generator
class PacketGeneratorThread(QThread):
    packet_generated = pyqtSignal(object)
    packet_generation_progress = pyqtSignal(int)

    def __init__(self, packet_info):
        super(PacketGeneratorThread, self).__init__()
        self.packet_info = packet_info

    def run(self):
        result = packet_generator.generate_packets(self.packet_info)
        self.packet_generated.emit(result)