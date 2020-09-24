#!/usr/bin/env python
import scapy.ass as scapy

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    #( answered_list, unanswered_list ) = scapy.srp(arp_broadcast_packet,1,verbose=False)
    answered_list = scapy.srp(arp_broadcast_packet,1,verbose=False)[0]
    print(answered_list)

scan("192.168.0.1/24")
