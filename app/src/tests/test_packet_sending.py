import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from unittest.mock import MagicMock, patch
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP
from scapy.layers.dns import DNS, DNSQR
from network.packet_sending import send_packet, check_packet_type_assign_send_method

# Test send_packet function with a single packet
def test_send_packet_single():
    packet = Ether() / IP(dst="8.8.8.8") / DNS(rd=1, qd=DNSQR(qname="www.google.com"))
    packet_info = {"type": "DNS", "number": 1}
    result = send_packet(packet, packet_info)
    assert result[0] is not None  # Check that there is at least one answered packet
    assert result[1] is not None  # Check that there are no unanswered packets
    assert len(result[2]) == 5  # Check that all packets were sent

# Test send_packet function with multiple packets
def test_send_packet_multiple():
    packet = Ether() / IP(dst="8.8.8.8") / DNS(rd=1, qd=DNSQR(qname="www.google.com"))
    packet_info = {"type": "DNS", "number": 5}
    result = send_packet(packet, packet_info)
    assert result[0] is not None  # Check that there is at least one answered packet
    assert result[1] is not None  # Check that there are no unanswered packets
    assert len(result[2]) == 5  # Check that all packets were sent

# Test check_packet_type_assign_send_method function with a valid packet type
def test_check_packet_type_assign_send_method_valid():
    packet = Ether() / IP(dst="8.8.8.8") / DNS(rd=1, qd=DNSQR(qname="www.google.com"))
    packet_info = {"type": "DNS", "number": 1}
    send_method, iface = check_packet_type_assign_send_method(packet, packet_info)
    assert send_method.__name__ == "sr"  # Check that the correct send method was assigned
    assert iface is not None  # Check that the interface is not None

# Test check_packet_type_assign_send_method function with an invalid packet type
def test_check_packet_type_assign_send_method_invalid():
    packet = Ether() / IP(dst="8.8.8.8") / DNS(rd=1, qd=DNSQR(qname="www.google.com"))
    packet_info = {"type": "HTTP", "number": 1}
    send_method, iface = check_packet_type_assign_send_method(packet, packet_info)
    assert send_method.__name__ == "sr"  # Check that the default send method was assigned
    assert iface is not None  # Check that the interface is not None
