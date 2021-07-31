import re
result = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
r1 = re.findall('\S+',result)
subr1 = re.sub(r'(\d+):(\d+):(\d+)',r"\1小时\2分钟\3秒",r1[6])
print('%-20s'%'protocal',':',r1[0])
print('%-20s'%'server',':',r1[1])
print('%-20s'%'idle',':',subr1[:-1])
print('%-20s'%'bytes',':',r1[8][:-1])
print('%-20s'%'flgs',':',r1[10])