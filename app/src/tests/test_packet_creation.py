import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from network.packets import create_ARP, create_IP, create_DNS
from scapy.all import *

def test_create_ARP():
    packet_info = {'pdst': '192.168.1.1', 'hwdst': 'ff:ff:ff:ff:ff:ff'}
    packet = create_ARP(packet_info)
    assert packet.haslayer(Ether)
    assert packet[Ether].dst == packet_info['hwdst']
    assert packet.haslayer(ARP)
    assert packet[ARP].op == 1
    assert packet[ARP].pdst == packet_info['pdst']


def test_create_IP():
    packet_info = {'srcIP': '192.168.1.100', 'dstIP': '8.8.8.8', 'ttl': 64,
                   'proto': 17, 'payload': 'hello world'}
    packet = create_IP(packet_info)
    assert packet.haslayer(IP)
    assert packet[IP].src == packet_info['srcIP']
    assert packet[IP].dst == packet_info['dstIP']
    assert packet[IP].ttl == packet_info['ttl']
    assert packet.haslayer(UDP)
    assert packet[UDP].sport == 12345
    assert packet[UDP].dport == 54321


def test_create_DNS():
    packet_info = {'qname': 'example.com'}
    packet = create_DNS(packet_info)
    assert packet.haslayer(IP)
    assert packet[IP].dst == '8.8.8.8'
    assert packet.haslayer(UDP)
    assert packet[UDP].sport > 0
    assert packet[UDP].dport == 53
    assert packet.haslayer(DNS)
    assert packet[DNS].rd == 1
    assert packet.haslayer(DNSQR)
    assert packet[DNSQR].qname == packet_info['qname'].encode()