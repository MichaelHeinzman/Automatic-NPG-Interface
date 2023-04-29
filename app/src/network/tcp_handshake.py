
__all__ = ['tcp_handshake']
from network.packet_generator import generate_packets
from scapy.layers.inet import TCP,IP
from .error_handling import handle_error

@handle_error
def tcp_handshake(packet):
    print("Starting TCP Handshake \n")
    # SYN packet
    if packet["tcp_type"] == "S":  
        # SYN ACK Response (Has multiple packets if sent multiple of the same packet.)
        syn_ack = generate_packets(packet)
        if not syn_ack[0]:
            return syn_ack
        
        # SYN ACK Packet.
        syn_ack_packet = syn_ack[0][0]
        ack_packet_info = {
            "type": "IP",
            "proto": 6,
            "srcIP": syn_ack_packet[0][IP].src,
            "dstIP": syn_ack_packet[0][IP].dst,
            "sport": syn_ack_packet[0][TCP].sport,
            "dport": syn_ack_packet[0][TCP].dport,
            "seq": syn_ack_packet[0][TCP].ack,
            "ack": syn_ack_packet[0][TCP].seq + 1,
            "tcp_type": "A"
        }

        print("Sending ACK TCP Packet... \n")

        # Send ACK and receive result if any.
        ack_result = generate_packets(ack_packet_info)

        print("TCP Handshake Finished \n")

        # Return sent, answered packets.
        return (syn_ack[0] + ack_result[0], syn_ack[1] + ack_result[1], syn_ack[2] + ack_result[2])
    else: return generate_packets(packet)


