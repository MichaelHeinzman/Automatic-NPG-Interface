from Packets import create_ARP
from scapy.all import *


# Sends multiple of the same packet. 
def send_generated_packet (packet, number_of_packets):
    if number_of_packets == None:
        return None
    
    if packet == None:
        return None
    
    sendp(packet * number_of_packets)


# Creates a packet based on type and data.
def create_packet (type, pdst, hwsrc = "", psrc = "", hwdst = "", number = 1):
    switcher = {
        ("ARP-who-has",): lambda: create_ARP(0, hwsrc, psrc, hwdst, pdst),
    }

    generate_packet = switcher.get((type,))

    if generate_packet: 
        new_packet = generate_packet()
    else:
        new_packet = None
    return new_packet
    
# Handles creating and sending of packets. Packet Generation based on packet info.
def generate_packets (packetInfo):
    new_packet = create_packet(**packetInfo)
    send_generated_packet(new_packet, packetInfo["number"])


packetInfo = {
    "type": "ARP-who-has",
    "pdst": "192.168.236",
    "hwsrc": "",
    "hwdst": "",
    "psrc": "",
    "number": 10,
}

generate_packets(packetInfo)