from scapy.all import *
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import ARP

# Creates an ARP response and request packet.
def create_ARP (ARP_type, hwsrc, psrc, hwdst, pdst):
    if ARP_type == 0:
        arp_packet = ARP(op=ARP.who_has, pdst = pdst)
    if ARP_type == 1:
        arp_packet = ARP(op=ARP.is_at, hwsrc = hwsrc, psrc = psrc, hwdst = hwdst, pdst = pdst)
        
    ARP.show(arp_packet)
    if arp_packet:
        return arp_packet
    else:
        return None