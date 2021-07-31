import re
import os
n1 = os.popen('route -n').read()
rn2 = re.findall(r'(?:.*?\n)',n1)
t1=[]
for x in range(len(rn2)):
    rn2[x]=rn2[x].split()
    for y in range(len(rn2[x])):
        if rn2[x][y] == 'UG':
            if rn2[x][0] == '0.0.0.0':
                t1 = rn2[x]

print('\u7f51\u5173\u4e3a\uff1a'+t1[1])
