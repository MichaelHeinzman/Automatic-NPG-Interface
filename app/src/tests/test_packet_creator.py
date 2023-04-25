import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from network.packet_creator import create_packet
from scapy.all import *

def test_create_packet():
    # Test creating an ARP packet
    packet_info = {
        "type": "ARP",
        "hwsrc": "00:11:22:33:44:55",
        "hwdst": "ff:ff:ff:ff:ff:ff",
        "srcIP": "192.168.1.100",
        "dstIP": "192.168.1.1",
    }
    packet = create_packet(packet_info)
    assert packet.haslayer("ARP")
    assert packet[0].hwsrc == packet_info["hwsrc"]
    assert packet[0].hwdst == packet_info["hwdst"]
    assert packet[0].psrc == packet_info["srcIP"]
    assert packet[0].pdst == packet_info["dstIP"]

    # Test creating an IP packet
    packet_info = {
        "type": "IP",
        "srcIP": "192.168.1.100",
        "dstIP": "8.8.8.8",
        "ttl": 64,
        "proto": 17,
        "payload": b"hello world",
    }
    packet = create_packet(packet_info)
    assert packet.haslayer("IP")
    assert packet[IP].src == packet_info["srcIP"]
    assert packet[IP].dst == packet_info["dstIP"]
    assert packet[IP].ttl == packet_info["ttl"]
    assert packet.haslayer("UDP")
    assert packet[UDP].sport == 12345
    assert packet[UDP].dport == 54321
    assert packet.haslayer("Raw")
    assert packet[Raw].load == packet_info["payload"]

    # Test creating a DNS packet
    packet_info = {
        "type": "DNS",
        "qname": "example.com",
    }
    packet = create_packet(packet_info)
    assert packet.haslayer("IP")
    assert packet[IP].dst == "8.8.8.8"
    assert packet.haslayer("UDP")
    assert packet[UDP].sport > 0
    assert packet[UDP].dport == 53
    assert packet.haslayer("DNS")
    assert packet[DNS].rd == 1
    assert packet.haslayer("DNSQR")
    assert packet[DNSQR].qname == packet_info["qname"]