from packet_creator import create_packet
from packet_sending import send_created_packets

# Handles creating and sending of packets. Packet Generation based on packet info.
def generate_packets (packet_info):
    new_packet = create_packet(packet_info)
    send_created_packets(new_packet, packet_info)

# Packet Info.
IP_packet_info = {"type":"IP", "srcIP":"192.168.1.236", "dstIP":"192.168.1.236", "payload":"Hello", "number": 5}
ARP_packet_info = {"type": "ARP-who-has", "pdst":"192.168.1.1", "hwdst":"ff:ff:ff:ff:ff:ff", "hwsrc": "00-05-1B-33-F7-46", "psrc": "192.168.1.236", "number": 1}

# Call generate_packets to generate multiple packets based on the packet info passed.
generate_packets(ARP_packet_info)