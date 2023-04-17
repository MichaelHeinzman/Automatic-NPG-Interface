
__all__ = ['send_packet']

from scapy.all import *
from .error_handling import handle_error

# Sends multiple of the same packet. 
@handle_error
def send_packet (packet, packet_info):
    if packet is None or packet_info is None:
        return None

    number_of_packets = packet_info.get("number", 1)

    if number_of_packets is None: return None

    send_method = check_packet_type_assign_send_method(packet, packet_info)
    result = send_method(packet * number_of_packets, timeout = 10)
    time.sleep(.1)
    return result

@handle_error
def check_packet_type_assign_send_method(packet, packet_info):
    if packet is None or packet_info is None:
        return None

    packet_type = packet_info.get("type")

    send_method_dict = {
        "IP": sr,
        "ARP-who-has": srp,
        "DNS": sr,
    }

    send_method = send_method_dict.get(packet_type, sr)

    return send_method