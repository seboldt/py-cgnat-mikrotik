from ipaddress import IPv4Network, IPv4Interface

def interfaces_cgnat(public_ip):
    # Cria as interfaces de Loopback conforme a quantidade de IPs Públicos
    interfaces_output = list()    
    for key, addr in enumerate(public_ip):
        interfaces_output.append(f'interface bridge add name=loopback{key} \n')
    return interfaces_output

def ipaddress_cgnat(public_ip):
    # Adiciona os IPs Públicos a interface de Loopback
    ipaddress_output = list()
    for key, addr in enumerate(public_ip):
        ipaddress_output.append(f'ip address add address={addr}/32 interface=loopback{key} \n')
    return ipaddress_output


def firewall_cgnat(cgnat, public_ip):
    # Cria as Regras de Firewall com 1 IP Público para cada /29 de CGNAT
    firewall_output = list()    
    for cgnat_29, addr in zip(cgnat.subnets(new_prefix=29), public_ip):    
        firewall_output.append(f'ip firewall nat add action=src-nat chain=srcnat out-interface=sfp-sfpplus1 src-address={cgnat_29} to-addresses={addr} \n')
    return firewall_output

