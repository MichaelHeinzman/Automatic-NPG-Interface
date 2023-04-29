
__all__ = ['send_packet']

import netifaces
from scapy.all import *
from .error_handling import handle_error

# Sends multiple of the same packet. 
@handle_error
def send_packet(packet, packet_info, iface=None):
    if packet is None or packet_info is None:
        return None

    number_of_packets = packet_info.get("number", 1)

    if number_of_packets is None:
        return None

    send_method = check_packet_type_assign_send_method(packet, packet_info)
    iface = get_default_interface_name()
    result = send_method(packet * number_of_packets, timeout=10, iface=iface, filter=None, verbose=0, chainCC=0, retry=0, multi=0)
    time.sleep(.1)

    # Extract answered and unanswered packets from the result variable
    answered, unanswered = result

    # Print sent packets
    sent_packets = packet * number_of_packets
    print(f"Sent {number_of_packets} packets:")
    for i in range(number_of_packets):
        print(sent_packets[i].summary())

    # Print answered packets
    print(f"\nReceived {len(answered)} packets, got {len(answered)} answers:")
    for pkt in answered:
        if isinstance(pkt, tuple):
            # if the packet is a tuple, it contains the packet and the answer
            pkt, ans = pkt
            pkt.time = ans.time
        print(pkt.summary())

    # Print unanswered packets
    if len(unanswered) > 0:
        print(f"\n{len(unanswered)} packets were not answered:")
        for pkt in unanswered:
            print(pkt.summary())
    else:
        print("\nAll packets were answered.")

    print("\n")
    
    # Create a new tuple to include the sent packets
    result = (answered, unanswered, sent_packets)
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

def get_default_interface_name():
    """
    Returns the name of the default network interface on the system.
    """
    # Get the addresses of all available network interfaces
    interfaces = netifaces.interfaces()

    # Find the default interface, which has a 0.0.0.0 IP address
    for iface in interfaces:
        addresses = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addresses:
            ipv4_addresses = addresses[netifaces.AF_INET]
            for addr in ipv4_addresses:
                if addr['addr'] == '0.0.0.0':
                    return iface

    # If the default interface was not found, return None
    return None