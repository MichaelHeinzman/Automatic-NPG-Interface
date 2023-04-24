
__all__ = ['process_packets']
from scapy.all import *
from scapy.layers.inet import IP, ARP,ICMP
from scapy.layers.dns import DNS
from .error_handling import handle_error

@handle_error
def process_packets(result):
    packet_data = []
    for resp in result:
        data = {}
        if resp[1].haslayer(DNS):
            data['type'] = 'DNS'
            data['id'] = resp[1][DNS].id
            data['qr'] = resp[1][DNS].qr
            data['qdcount'] = resp[1][DNS].qdcount
            data['ancount'] = resp[1][DNS].ancount
            data['nscount'] = resp[1][DNS].nscount
            data['arcount'] = resp[1][DNS].arcount
            data['qname'] = resp[1][DNS].qd.qname.decode('utf-8')
            data['srcIP'] = resp[1][DNS].an.rdata
            data['dstIP'] = resp[1][IP].dst
        elif resp[1].haslayer(IP):
            data['type'] = 'IP'
            data['srcIP'] = resp[1][IP].src
            data['dstIP'] = resp[1][IP].dst
            if not resp[1].haslayer(ICMP):
                data['payload'] = resp[1][IP].payload.load.decode('utf-8')
        elif resp[1].haslayer(ARP):
            print("ARP RECEIVED")
            data['type'] = 'ARP'
            data['hwsrc'] = resp[1][ARP].hwsrc
            data['hwdst'] = resp[1][ARP].hwdst
            data['psrc'] = resp[1][ARP].psrc
            data['pdst'] = resp[1][ARP].pdst
            data['op'] = resp[1][ARP].op
        else: 
            print("Unknown")

        packet_data.append(data)

    return packet_data


