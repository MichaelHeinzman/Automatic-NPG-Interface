
__all__ = ['create_ARP', 'create_IP']

from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.l2 import *
from error_handling import handle_error


# Creates an ARP response and request packet.
@handle_error
def create_ARP(ARP_type, hwsrc, pdst, hwdst, psrc):
    arp_packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=ARP.who_has, pdst=pdst, psrc=psrc) if ARP_type == 0 else ARP(op=ARP.is_at, hwsrc=hwsrc, psrc=psrc, hwdst=hwdst, pdst=pdst)
    ARP.show(arp_packet)

    return arp_packet
    
# Creates an IP packet.
@handle_error
def create_IP(srcIP, dstIP, payload):
    ip_packet = IP(src=srcIP, dst=dstIP)
    packet = ip_packet/payload if payload else ip_packet
    IP.show(packet)

    return packet
