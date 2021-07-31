import re
result = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
r1 = re.findall('\S+',result)
print('%-12s'%'VLAN ID'+r': '+r1[0])
print('%-12s'%'MAC'+r': '+r1[1])
print('%-12s'%'Type'+r': '+r1[2])
print('%-12s'%'Interface'+r': '+r1[3])

