import unittest
from unittest.mock import patch
from app.src.network.packet_sending import send_packet


class TestSendPacket(unittest.TestCase):
    @patch('my_module.sr')
    def test_send_packet(self, mock_sr):
        # Create a fake packet and packet_info to send
        packet = b'fake packet'
        packet_info = {'type': 'IP', 'number': 1}

        # Call send_packet with the fake packet and packet_info
        send_packet(packet, packet_info)

        # Assert that sr was called with the correct arguments
        mock_sr.assert_called_with(packet * packet_info['number'], timeout=10, iface=None, filter=None, verbose=0, chainCC=0, retry=0, multi=0)

 
if __name__ == '__main__':
    unittest.main()
