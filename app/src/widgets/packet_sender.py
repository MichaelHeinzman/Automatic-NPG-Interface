from PyQt6.QtCore import QRunnable,pyqtSignal, QObject

class PacketSenderSignals(QObject):
    finished = pyqtSignal(object, object)

class PacketSender(QRunnable):
    def __init__(self, packet):
        super().__init__()
        self.signals = PacketSenderSignals()
        self.packet = packet
        
    def run(self):
        # Call send_packet method of the packet object
        result = self.packet.send_packet()
        if result:
            self.signals.finished.emit(result, self.packet)