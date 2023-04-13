from PyQt6.QtCore import QThreadPool, QRunnable

class PacketSender(QRunnable):
    def __init__(self, packet):
        super().__init__()
        self.packet = packet
        
    def run(self):
        self.packet.send_packet()