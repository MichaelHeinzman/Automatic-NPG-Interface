# IP packet information dictionary
IP_PACKET_INFO = {
    "type": "IP",
    "version": 4,
    "ihl": 5,
    "tos": 0,
    "len": 0,
    "id": 1,
    "flags": 0,
    "frag": 0,
    "ttl": 64,
    "proto": 6,
    "chksum": None,
    "srcIP": "127.0.0.1",
    "dstIP": "127.0.0.1",
    "options": None,
    "payload": "HELLO",
    "number": 5
}

TCP_IP_PACKET = {
    "type": "IP",
    "version": 4,
    "ihl": 5,
    "tos": 0,
    "len": 64,
    "id": 54321,
    "flags": 0,
    "frag": 0,
    "ttl": 64,
    "proto": 6,
    "chksum": None,
    "srcIP": "127.0.0.1",
    "dstIP": "127.0.0.1",
    "options": None,
    "payload": "This is a TCP packet",
    "number": 1
}

UDP_IP_PACKET ={
    "type": "IP",
    "version": 4,
    "ihl": 5,
    "tos": 0,
    "len": 64,
    "id": 12345,
    "flags": 0,
    "frag": 0,
    "ttl": 64,
    "proto": 17,
    "chksum": None,
    "srcIP": "127.0.0.1",
    "dstIP": "127.0.0.1",
    "options": None,
    "payload": "This is a UDP packet",
    "number": 2
}

ICMP_IP_PACKET = {
    "type": "IP",
    "version": 4,
    "ihl": 5,
    "tos": 0,
    "len": 84,
    "id": 54321,
    "flags": 0,
    "frag": 0,
    "ttl": 64,
    "proto": 1,
    "chksum": None,
    "srcIP": "127.0.0.1",
    "dstIP": "127.0.0.1",
    "options": None,
    "payload": "This is an ICMP packet",
    "number": 1
}

# ARP packet information dictionary
ARP_PACKET_INFO = {
    "type": "ARP-who-has",
    "hwtype": 1,
    "ptype": 2048,
    "hwlen": 6,
    "plen": 4,
    "op": 1,
    "hwsrc": "",
    "psrc": "192.168.1.236",
    "hwdst": "ff:ff:ff:ff:ff:ff",
    "pdst": "192.168.1.236",
    "number": 10
}

# DNS packet information dictionary
DNS_PACKET_INFO = {
    "type": "DNS",
    "id": 0xAAA,
    "qr": 0,
    "opcode": 0,
    "aa": 0,
    "tc": 0,
    "rd": 1,
    "ra": 0,
    "z": 0,
    "ad": 0,
    "cd": 0,
    "rcode": 0,
    "qdcount": 1,
    "ancount": 0,
    "nscount": 0,
    "arcount": 0,
    "qd": [],
    "an": [],
    "ns": [],
    "ar": [],
    "qname": "www.example.com"
}
