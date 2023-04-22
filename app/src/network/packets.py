
__all__ = ['create_ARP_who_has', 'create_IP', 'create_DNS']

from scapy.all import *
from scapy.layers.inet import IP,ICMP, TCP, UDP
from scapy.layers.l2 import *
from scapy.layers.dns import DNS, DNSQR
from .error_handling import handle_error


# Creates an ARP response and request packet.
@handle_error
def create_ARP_who_has(packet_info):
    pdst = packet_info.get('pdst', 'ff:ff:ff:ff:ff:ff')
    hwdst = packet_info.get('hwdst', '00:00:00:00:00:00')
    hwsrc = packet_info.get('hwsrc', get_if_hwaddr(get_working_if()))
    psrc = packet_info.get('psrc', get_if_addr(get_working_if()))

    arp_packet = Ether(dst=hwdst)/ARP(op=ARP.who_has, pdst=pdst, hwdst=hwdst, hwsrc=hwsrc, psrc=psrc)

    ARP.show(arp_packet)
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
        ip_packet /= TCP()/Raw(load=payload)
    elif proto == 17:
        ip_packet /= UDP(sport=packet_info.get("sport", 12345), dport=packet_info.get("dport", 54321))/Raw(load=payload)

    # calculate the checksum
    ip_packet.chksum = None
    ip_packet = IP(bytes(ip_packet))

    return ip_packet


# Create a DNS packet.
@handle_error
def create_DNS (packet_info):
    id = packet_info.get("id", 1)
    qr = packet_info.get("qr", 0)
    qdcount = packet_info.get("qdcount", 1)
    ancount = packet_info.get("ancount", 0)
    nscount = packet_info.get("nscount", 0)
    arcount = packet_info.get("arcount", 0)
    qname = packet_info.get("qname", 'example.com')

    question_record = DNSQR(qname=qname)
    dns_packet = DNS(id=id, qr=qr, qdcount=qdcount, ancount=ancount, nscount=nscount, arcount=arcount, qd=question_record)

    dns_packet.show()
    return dns_packet