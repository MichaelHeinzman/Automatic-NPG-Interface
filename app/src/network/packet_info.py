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
    "proto": 0,
    "chksum": None,
    "srcIP": "192.168.1.236",
    "dstIP": "192.168.1.236",
    "options": None,
    "payload": "Hello World!",
    "number": 5
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
