# Automatic Network Packet Generator User Interface
This is my 2023 Spring Project. It's a python application that allows for someone to generate network packets. I haven't completed this project yet, but it will be done by May 2023 before I graduate.


You can view the full documentation / report by clicking the link below.
https://github.com/MichaelHeinzman/Automatic-NPG-Interface/blob/master/Documents/Project%20Proposal.pdf


## **Details**     
  Language : **Python**     
  Libraries : **PyQt, Scapy, Qtest**          
  Design Tool : **Figma**   

## **Structure**     
  app: The main application.    
    network: A package I created that contains modules for packet generation.     
      packet_generator: Receives packet_info and creates and sends a packet.     
      packet_creator: Receives packet_info from packet_generator and creates a packet based on packet type.    
      packets: Is called by the packet_creator to generate packets of different types.     
      packet_sending: Receives a packet from the packet_generator and sends it to the destination.   
     
    screens: Contains the screen UI for the application.  
  
  Documents: The documents of the project.
  
  
