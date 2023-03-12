
__all__ = ['create_packet']

from packets import create_ARP, create_IP

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

# Handle calling create_Packets with packet_info.
def handle_create_ARP_packet (packet_info):
    return create_ARP(0, packet_info.get("hwsrc",""), packet_info.get("pdst",""), packet_info.get("hwdst",""), packet_info.get("psrc",""))

def handle_create_IP_packet (packet_info):
    return create_IP(packet_info.get("srcIP",""), packet_info.get("dstIP",""), packet_info.get("payload",""))

