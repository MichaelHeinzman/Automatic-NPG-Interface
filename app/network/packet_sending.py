
__all__ = ['send_packet']

from scapy.all import *
from error_handling import handle_error

# Sends multiple of the same packet. 
@handle_error
def send_packet (packet, packet_info):
    if packet is None or packet_info is None:
        return None

    number_of_packets = packet_info.get("number")

    if number_of_packets is None: return None

    send_method = check_packet_type_assign_send_method(packet, packet_info)
    ans, unans = send_method(packet * number_of_packets, timeout = 10)
    print_packet_summary(ans, unans)

@handle_error
def check_packet_type_assign_send_method(packet, packet_info):
    if packet is None or packet_info is None:
        return None

    packet_type = packet_info.get("type")

    send_method_dict = {
        "IP": sr,
        "ARP-who-has": srp
    }

    send_method = send_method_dict.get(packet_type, sr)

    return send_method
    
@handle_error
def print_packet_summary(ans, unans):
    if ans:
        print("Answered Packets: ")
        print(ans.summary())
    if unans:
        print("Unanswered Packets: ")
        print(unans.summary())