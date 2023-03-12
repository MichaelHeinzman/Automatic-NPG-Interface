# Automatic Network Packet Generator

## **Introduction**
This is my 2023 Spring Project. Automatic Network Packet Generator is a tool to generate and send different types of network packets. This tool is useful for network administrators, penetration testers and security professionals who want to generate and send packets for testing purposes.     

This project contains a user interface that allows the user to configure and generate different types of network packets. The project also includes a network package that holds four files for creating and sending packets.    

## **Installation**
To install the Automatic Network Packet Generator, follow these steps:   
1. Clone the repository from GitHub    
2. Install the required packages:    
``` 
pip install -r requirements.txt
```
3. Run the project.py file:
``` 
python app/project.py
```

## **Usage**
When the Automatic Network Packet Generator user interface is launched, the user can select the type of packet to generate from a drop-down list. After selecting the packet type, the user can enter the packet details such as the source IP, destination IP, and payload.     

Once the user enters the packet details, they can click the "Generate Packet" button to generate the packet. The user can then click the "Send Packet" button to send the generated packet.     

The user interface also includes a summary of the sent and unsent packets.  


## **Network Package**
The network package contains four files:   

1. packet_creator: This file handles the creation of packets based on the packet type and data.   
2. packets: This file contains functions for creating ARP and IP packets.   
3. packet_sending: This file handles the sending of packets and includes functions for checking the packet type and assigning a send method.   
4. packet_generator: This file handles the creation and sending of packets based on packet info.     

## **Examples**
The Automatic Network Packet Generator tool can be used for different scenarios such as testing network security or checking network performance.    

Example 1: Generate and send multiple ARP packets   
```python
from packet_generator import generate_packets

ARP_packet_info = {"type": "ARP-who-has", "pdst":"192.168.1.1", "hwdst":"ff:ff:ff:ff:ff:ff", "hwsrc": "00-05-1B-33-F7-46", "psrc": "192.168.1.236", "number": 10}
generate_packets(ARP_packet_info)
```

Example 2: Generate and send multiple IP packets      
```python
from packet_generator import generate_packets

IP_packet_info = {"type":"IP", "srcIP":"192.168.1.236", "dstIP":"192.168.1.236", "payload":"Hello", "number": 5}
generate_packets(IP_packet_info)

```

## **Details**     
  Language : **Python**     
  Libraries : **PyQt, Scapy, Qtest**          
  Design Tool : **Figma**     

## **Conclusion**
The Automatic Network Packet Generator is a useful tool for network administrators, penetration testers, and security professionals who want to generate and send packets for testing purposes. The user interface allows the user to easily configure and generate packets. The network package includes functions for creating and sending different types of packets.   
   
