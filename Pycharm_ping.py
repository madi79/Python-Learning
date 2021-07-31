import os
ping_result=''
if os.system("ping -n 1 172.16.100.1") == 0:
    print("host appears to be up.")
else :
    print("host not appears.")
ping_result = os.popen('ping ' + ' 172.16.1.1 ' + ' -n 1').read()
print(ping_result)