import os
#from __future__import print_function
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    ping_result = os.popen('ping ' + ' 172.16.1.1 ' + ' -c 1').read()
    fo = open('result.txt','r+')
    fo.write(ping_result)
    fo.close()
    # 将要运行的代码加到这里
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)