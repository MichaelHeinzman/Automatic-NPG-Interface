from PyQt6.QtCore import pyqtSignal, QThread
import network.packet_generator as packet_generator

class PacketGeneratorThread(QThread):
    packet_generated = pyqtSignal(bytes)
    packet_generation_progress = pyqtSignal(int)

    def __init__(self, packet_info):
        super(PacketGeneratorThread, self).__init__()
        self.packet_info = packet_info
        self.packet_result = ""

    def run(self):
        ans, unans = packet_generator.generate_packets(self.packet_info)
        if ans:
            self.packet_result += "Answered Packets: \n" + (ans.summary() or "")
        if unans:
            self.packet_result += "Unanswered Packets: \n" + (unans.summary() or "")

        self.packet_generated.emit(self.packet_result.encode())