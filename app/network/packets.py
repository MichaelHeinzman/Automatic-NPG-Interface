
__all__ = ['create_ARP_who_has', 'create_IP', 'create_DNS']

from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.l2 import *
from scapy.layers.dns import DNS, DNSQR
from error_handling import handle_error


# Creates an ARP response and request packet.
@handle_error
def create_ARP_who_has(packet_info):
    pdst = packet_info.get('pdst', '')
    psrc = packet_info.get('psrc', '')

    arp_packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=ARP.who_has, pdst=pdst, psrc=psrc)

    ARP.show(arp_packet)
    return arp_packet
    
# Creates an IP packet.
@handle_error
def create_IP(packet_info):
    src_IP = packet_info.get("srcIP")
    dst_IP = packet_info.get("dstIP")
    payload = packet_info.get("payload")

    ip_packet = IP(src=src_IP, dst=dst_IP)
    ip_packet = ip_packet/payload if payload else ip_packet

    IP.show(ip_packet)
    return ip_packet


# Create a DNS packet.
@handle_error
def create_DNS (packet_info):
    id = packet_info.get("id")
    qr = packet_info.get("qr")
    qdcount = packet_info.get("qdcount")
    ancount = packet_info.get("ancount")
    nscount = packet_info.get("nscount")
    arcount = packet_info.get("arcount")
    qname = packet_info.get("qname")

    question_record = DNSQR(qname=qname)
    dns_packet = DNS(id = id, qr = qr, qdcount = qdcount, ancount = ancount, nscount = nscount, arcount = arcount, qd=question_record)

    dns_packet.show()
    return dns_packet