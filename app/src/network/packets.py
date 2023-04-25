
__all__ = ['create_ARP', 'create_IP', 'create_DNS']

from scapy.all import  get_if_hwaddr, get_if_addr, get_working_if, Raw, RandShort
from scapy.layers.inet import IP,ICMP, TCP, UDP
from scapy.layers.l2 import *
from scapy.layers.dns import DNS, DNSQR
from .error_handling import handle_error


# Creates an ARP response and request packet.
@handle_error
def create_ARP(packet_info):
    pdst = packet_info.get('pdst', '192.168.1.1')
    hwdst = packet_info.get('hwdst', 'ff:ff:ff:ff:ff:ff')
    srcIP = packet_info.get('srcIP', get_if_addr(get_working_if()))
    hwsrc = packet_info.get('hwsrc', get_if_hwaddr(get_working_if()))

    arp_packet = Ether(dst=hwdst)/ARP(op=1,pdst=pdst, psrc=srcIP, hwsrc=hwsrc)
    return arp_packet
    
@handle_error
def create_IP(packet_info):
    src_IP = packet_info.get("srcIP", get_if_addr(get_working_if()))
    dst_IP = packet_info.get("dstIP")
    ttl = packet_info.get("ttl", 64)
    payload = packet_info.get("payload", '')
    options = packet_info.get("options")
    if options is None:
        options = {}

    # create the IP packet object
    ip_packet = IP(src=src_IP, dst=dst_IP, ttl=ttl)
    
    # check the value of "proto" and add the appropriate layer
    proto = packet_info.get("proto", 6)
    if proto == 1:
        ip_packet /= ICMP()
    elif proto == 6:
        ip_packet /= TCP(sport=packet_info.get("sport", 0), dport=packet_info.get("dport", 80),flags=packet_info.get("tcp_type", "S"),seq=packet_info.get("seq", None), ack=packet_info.get("ack", None))/Raw(load=payload)
    elif proto == 17:
        ip_packet /= UDP(sport=packet_info.get("sport", 12345), dport=packet_info.get("dport", 54321))/Raw(load=payload)

    # calculate the checksum
    ip_packet.chksum = None
    ip_packet = IP(bytes(ip_packet))

    return ip_packet


# Create a DNS packet.
@handle_error
def create_DNS (packet_info):
    qname = packet_info.get("qname", 'example.com')

    dns_packet = IP(dst='8.8.8.8')/UDP(sport=RandShort(),dport=53)/DNS(rd=1, qd=DNSQR(qname=qname))

    return dns_packet