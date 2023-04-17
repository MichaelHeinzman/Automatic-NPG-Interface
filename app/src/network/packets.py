
__all__ = ['create_ARP_who_has', 'create_IP', 'create_DNS']

from scapy.all import *
from scapy.layers.inet import IP
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
    
# Creates an IP packet.
@handle_error
def create_IP(packet_info):
    src_IP = packet_info.get("srcIP", get_if_addr(get_working_if()))
    dst_IP = packet_info.get("dstIP")
    id = packet_info.get("id", 1)
    flags = packet_info.get("flags", 0)
    frag = packet_info.get("frag", 0)
    ttl = packet_info.get("ttl", 64)
    proto = packet_info.get("proto", 6)
    chksum = packet_info.get("chksum")
    payload = packet_info.get("payload", '')
    options = packet_info.get("options")
    if options is None:
        options = {}

    # encode the payload as bytes
    payload_bytes = payload.encode('iso-8859-1')

    # set the length field in packet_info
    packet_info['len'] = len(payload_bytes) + 20

    ip_packet = IP(src=src_IP, dst=dst_IP, id=id, flags=flags, frag=frag, ttl=ttl, proto=proto, chksum=chksum, options=options, len=packet_info['len'])

    try:
        ip_packet = ip_packet/payload_bytes if payload_bytes else ip_packet
        return ip_packet
    except Exception as e:
        print(f"Error: {e}")
        return None


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