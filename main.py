from ipaddress import IPv4Network, IPv4Interface
from getpass import getpass

from config_cgnat import interfaces_cgnat, ipaddress_cgnat, firewall_cgnat

file_save = open('cgnat.txt', 'a')

cgnat = IPv4Network('100.64.0.0/20')
public_ip = IPv4Network('192.168.0.0/23')

interfaces_output = interfaces_cgnat(public_ip)
ipaddress_output = ipaddress_cgnat(public_ip)
firewall_output = firewall_cgnat(cgnat, public_ip)

file_save.writelines(interfaces_output)
file_save.writelines(ipaddress_output)
file_save.writelines(firewall_output)
file_save.close()