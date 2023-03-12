from packets import handle_create_ARP_packet, handle_create_IP_packet
from packet_sending import send_generated_packet

# Creates a packet based on type and data.
def create_packet (packet_info):
    switcher = {
        "ARP-who-has": handle_create_ARP_packet,
        "IP": handle_create_IP_packet
    }

    type = packet_info.get("type", "")
    generate_packet = switcher.get(type)

    new_packet = generate_packet(packet_info) or None

    return new_packet
    
# Handles creating and sending of packets. Packet Generation based on packet info.
def generate_packets (packet_info):
    new_packet = create_packet(packet_info)
    send_generated_packet(new_packet, packet_info)

# Packet Info.
IP_packet_info = {"type":"IP", "srcIP":"192.168.1.236", "dstIP":"192.168.1.236", "payload":"Hello", "number": 5}
ARP_packet_info = {"type": "ARP-who-has", "pdst":"192.168.1.1", "hwdst":"ff:ff:ff:ff:ff:ff", "hwsrc": "00-05-1B-33-F7-46", "psrc": "192.168.1.236", "number": 1}

# Call generate_packets to generate multiple packets based on the packet info passed.
generate_packets(ARP_packet_info)