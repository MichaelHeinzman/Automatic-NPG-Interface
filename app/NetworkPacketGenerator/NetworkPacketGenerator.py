from Packets import create_ARP,create_IP
from scapy.all import *


# Sends multiple of the same packet. 
def send_generated_packet (packet, number_of_packets):
    if number_of_packets == None:
        return None
    
    if packet == None:
        return None
    
    sendp(packet * number_of_packets)


# Creates a packet based on type and data.
def create_packet (packet_info):
    switcher = {
        ("ARP-who-has",): lambda: create_ARP(0, packet_info["hwsrc"], packet_info["pdst"], packet_info["hwdst"], packet_info["psrc"]),
        ("IP",): lambda: create_IP(packet_info["srcIP"], packet_info["dstIP"], packet_info["payload"])
    }

    generate_packet = switcher.get((packet_info["type"],))

    if generate_packet: 
        new_packet = generate_packet()
    else:
        new_packet = None
    return new_packet
    
# Handles creating and sending of packets. Packet Generation based on packet info.
def generate_packets (packet_info):
    new_packet = create_packet(packet_info)
    send_generated_packet(new_packet, packet_info["number"])


# Packet Info.
IP_packet_info = {"type":"IP", "srcIP":"192.168.1.236", "dstIP":"192.168.1.236", "payload":"", "number": 5}
ARP_packet_info = {"type": "ARP-who-has", "pdst":"192.168.1.236", "hwdst":"192.168.1.236", "hwsrc": "", "psrc": "", "number": 10}

# Call generate_packets to generate multiple packets based on the packet info passed.
generate_packets(IP_packet_info)