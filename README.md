# py-cgnat-mikrotik

- Script python para gerar a configuração de CGNAT em Mikrotik, usando de um IP Público para cada /29 de CGNAT.
- As configurações dos network fica no arquivo main.py, deve ser ajustado conforme a necessidade
- Caso seja preciso fazer para redes maiores, deve dentro do arquivo config_cgnat na função firewall_cgnat alterar o new_prefix para a rede desejada.
