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
    arp_packet = ARP(op=ARP.who_has, pdst = pdst) if ARP_type == 0 else ARP(op=ARP.is_at, hwsrc = hwsrc, psrc = psrc, hwdst = hwdst, pdst = pdst)

    ARP.show(arp_packet)

    return arp_packet or None
    
# Creates an IP packet.
def create_IP (srcIP, dstIP, payload):
    ip_packet = IP(src=srcIP, dst=dstIP)
        
    packet = ip_packet/payload if payload else ip_packet

    IP.show(packet)

    return packet or None
