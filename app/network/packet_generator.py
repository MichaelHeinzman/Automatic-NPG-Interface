__all__ = ['generate_packets']

from packet_creator import create_packet
from packet_sending import send_created_packets


# Handles creating and sending of packets. Packet Generation based on packet info.
def generate_packets (packet_info):
    new_packet = create_packet(packet_info)
    send_created_packets(new_packet, packet_info)