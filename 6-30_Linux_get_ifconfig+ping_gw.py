import re
import os
ifconfig_result = """ ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
              inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
              inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
              ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
              RX packets 174598769 bytes 1795658527217 (1.6 TiB)
              RX errors 1 dropped 24662 overruns 0 frame 0
              TX packets 51706604 bytes 41788673420 (38.9 GiB)
              TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
"""
r1 = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",ifconfig_result)
mac_result= re.findall(r'(?:\w\w\:\w\w\:\w\w\:\w\w\:\w\w\:\w\w)',ifconfig_result)
ip_result = []
for i in range (0,len(r1)-1):
    if r1[i].split('.')[3] != '0':
        if r1[i].split('.')[3] !='255':
            ip_result.append(r1[i])
tmp_ip= str(ip_result[0]).split('.')
tmp_ip[3]='254'
ipv4_gw = ('.'.join(tmp_ip))
print('%-12s'% 'ipv4_add'+r':'+r1[0])
print('%-12s'% 'netmask'+r':'+r1[1])
print('%-12s'% 'broadcacst'+r':'+r1[2])
print('%-12s'% 'mac_address'+r':'+mac_result[0])
print('\n我们假设网关IP地址为最后一位为254，因此网关IP地址为：' + ipv4_gw + '\n')
ping_result = os.popen('ping '+ ipv4_gw + ' -n 1').read()
re_ping_resutl = re.sub('\D','',re.search(r'[(].*?[)]',ping_result).group(0))
if int(re_ping_resutl) == 100:
    print('网关不可达')
else:
    print('网关可达')