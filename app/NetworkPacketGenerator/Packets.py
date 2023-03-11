from scapy.all import *
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import ARP


# Handle calling create_Packets with packet_info.
def handle_create_ARP_packet (packet_info):
    return create_ARP(0, packet_info.get("hwsrc",""), packet_info.get("pdst",""), packet_info.get("hwdst",""), packet_info.get("psrc",""))

def handle_create_IP_packet (packet_info):
    return create_IP(packet_info.get("srcIP",""), packet_info.get("dstIP",""), packet_info.get("payload",""))

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
    
# Creates an IP packet.
def create_IP (srcIP, dstIP, payload):
    ip_packet = IP(src=srcIP, dst=dstIP)
        
    if payload:
        packet = ip_packet/payload
    else:
        packet = ip_packet

    IP.show(packet)
    if packet:
        return packet
    else:
        return None
