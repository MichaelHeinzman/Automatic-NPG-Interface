__all__ = ['generate_packets']

from packet_creator import create_packet
from packet_sending import send_packet
from error_handling import handle_error

# Handles creating and sending of packets. Packet Generation based on packet info.
@handle_error
def generate_packets (packet_info):
    new_packet = create_packet(packet_info)
    send_packet(new_packet, packet_info)


dns_packet_info = {
    "type": "DNS",
    "id": 0xAAA,
    "qr": 0,
    "qdcount": 1,
    "ancount": 0,
    "nscount": 0,
    "arcount": 0,
    "qname": "www.google.com",
}

generate_packets(dns_packet_info)