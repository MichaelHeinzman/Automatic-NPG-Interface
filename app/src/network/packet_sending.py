import netifaces

__all__ = ['send_packet']

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

    send_method, iface = check_packet_type_assign_send_method(packet, packet_info, iface)
    result = send_method(packet * number_of_packets, timeout=10, iface=iface, filter=None, verbose=None, chainCC=0, retry=0, multi=0)
    time.sleep(.1)
    return result

@handle_error
def check_packet_type_assign_send_method(packet, packet_info, iface=None):
    if packet is None or packet_info is None:
        return None

    packet_type = packet_info.get("type")

    send_method_dict = {
        "IP": sr,
        "ARP-who-has": srp,
        "DNS": sr,
    }

    send_method = send_method_dict.get(packet_type, sr)

    if iface is None:
        iface = get_default_interface_name()

    return send_method, iface

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