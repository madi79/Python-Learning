import re
str1 = 'Portchannel1.189     192.168.189.254    YES    CONFIG    up'
s2 = re.findall('\S+',str1)
print('%-10s'%'接口'+r':'+s2[0])
print('%-10s'%'IP地址'+r':'+s2[1])
print('%-10s'%'状态'+r':'+s2[4])
