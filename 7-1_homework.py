import re
import os
n1 = """Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.2.254   0.0.0.0         UG    100    0        0 ens160
10.0.0.0        10.200.244.161  255.0.0.0       UG    101    0        0 ens192
10.200.244.160  0.0.0.0         255.255.255.252 U     101    0        0 ens192
192.168.2.0     0.0.0.0         255.255.255.0   U     100    0        0 ens160
"""
rn2 = re.findall(r'(?:.*?\n)',n1)
t1=[]
for x in range(len(rn2)):
    rn2[x]=rn2[x].split()
    for y in range(len(rn2[x])):
        if rn2[x][y] == 'UG':
            if rn2[x][0] == '0.0.0.0':
                t1 = rn2[x]

print('网关为：'+t1[1])
