__all__ = ['create_packet']

from packets import create_ARP, create_IP
from error_handling import handle_error

# Creates a packet based on type and data.
@handle_error
def create_packet(packet_info):
    switcher = {
        "ARP-who-has": handle_create_ARP_packet,
        "IP": handle_create_IP_packet
    }

    type = packet_info.get("type", "")
    generate_packet = switcher.get(type)

    if not generate_packet:
        raise ValueError(f"Unsupported packet type: {type}")

    new_packet = generate_packet(packet_info) or None

    return new_packet

# Handle calling create_Packets with packet_info.
@handle_error
def handle_create_ARP_packet(packet_info):
    return create_ARP(0, packet_info.get("hwsrc",""), packet_info.get("pdst",""), packet_info.get("hwdst",""), packet_info.get("psrc",""))

@handle_error
def handle_create_IP_packet(packet_info):
    return create_IP(packet_info.get("srcIP",""), packet_info.get("dstIP",""), packet_info.get("payload",""))
