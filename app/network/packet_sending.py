from scapy.all import *

__all__ = ['send_generated_packet']

# Sends multiple of the same packet. 
def send_generated_packet (packet, packet_info):
    if packet is None or packet_info is None:
        return None

    number_of_packets = packet_info.get("number")

    if number_of_packets is None: return None

    send_method = check_packet_type_assign_send_method(packet, packet_info)
    ans, unans = send_method(packet * number_of_packets, timeout = 10)
    print(ans.summary())

    print("Unanswered Packets: ")
    print(unans.summary())


def check_packet_type_assign_send_method (packet, packet_info):
    if packet is None or packet_info is None:
        return None
    
    type = packet_info.get("type")

    if type == "IP": 
        return sr
    if type == "ARP-who-has":
        return srp
    else:
        return sr
    