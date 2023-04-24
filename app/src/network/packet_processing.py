__all__ = ['process_packets']
from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.layers.l2 import ARP
from scapy.layers.dns import DNS
from .error_handling import handle_error

@handle_error
def process_packets(result):
    packet_data = []
    for i, resp in enumerate(result):
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
            data['version'] = resp[1][IP].version
            data['ihl'] = resp[1][IP].ihl
            data['tos'] = resp[1][IP].tos
            data['len'] = resp[1][IP].len
            data['id'] = resp[1][IP].id
            data['flags'] = resp[1][IP].flags
            data['frag'] = resp[1][IP].frag
            data['ttl'] = resp[1][IP].ttl
            data['proto'] = resp[1][IP].proto
            data['chksum'] = resp[1][IP].chksum
            data['srcIP'] = resp[1][IP].src
            data['dstIP'] = resp[1][IP].dst
            if resp[1].haslayer(TCP):
                data['payload'] = resp[1][TCP].payload.load
                data['sport'] = resp[1][TCP].sport
                data['dport'] = resp[1][TCP].dport
                flags = resp[1][TCP].flags
                if flags == 0x02:  # SYN packet
                    data['tcp_type'] = 'S'
                elif flags == 0x12:  # SYN-ACK packet
                    data['tcp_type'] = 'SA'
                elif flags == 0x10:  # ACK packet
                    data['tcp_type'] = 'A'
                elif flags == 0x11:  # FIN-ACK packet
                    data['tcp_type'] = 'FA'
                elif flags == 0x04:  # RST packet
                    data['tcp_type'] = 'R'
            elif resp[1].haslayer(UDP):
                data['sport'] = resp[1][UDP].sport
                data['dport'] = resp[1][UDP].dport
                data['payload'] = resp[1][UDP].payload.load
            elif resp[1].haslayer(ICMP):
                data['payload'] = resp[1][ICMP].payload.load
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

        data['number'] = 1
        packet_data.append(data)

    return packet_data