__all__ = ['create_packet']

from packets import create_ARP_who_has, create_IP,create_DNS
from error_handling import handle_error

# Creates a packet based on type and data.
@handle_error
def create_packet(packet_info):
    switcher = {
        "ARP-who-has": create_ARP_who_has,
        "IP": create_IP,
        "DNS": create_DNS,
    }

    type = packet_info.get("type", "")
    generate_packet = switcher.get(type)

    if not generate_packet:
        raise ValueError(f"Unsupported packet type: {type}")

    new_packet = generate_packet(packet_info) or None

    return new_packet
