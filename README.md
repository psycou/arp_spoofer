# arp_spoofer

In computer networking, ARP spoofing, ARP cache poisoning, or ARP poison routing, is a technique by which an attacker sends (spoofed) Address Resolution Protocol (ARP) messages onto a local area network. Generally, the aim is to associate the attacker's MAC address with the IP address of another host, such as the default gateway, causing any traffic meant for that IP address to be sent to the attacker instead.

ARP spoofing may allow an attacker to intercept data frames on a network, modify the traffic, or stop all traffic. Often the attack is used as an opening for other attacks, such as denial of service, man in the middle, or session hijacking attacks.

The attack can only be used on networks that use ARP, and requires attacker have direct access to the local network segment to be attacked.


With this python arp spoofer any one can achieve Spoofing arp


requierment: 

scapy: follow This insctruction to install scapy

root@root:~$ pip install --pre scapy[basic]

Usage 

root@root:~$ sudo python arp_spoofer.py -t || --targer <Tareget> -g || --gateaway <Router IP Adress>
