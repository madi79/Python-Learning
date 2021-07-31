import logging, telnetlib, time

class TelnetClient:

    def __init__(self):
        self.tn = telnetlib.Telnet()

    def login_host(self, host_ip, username, password):
        try:
            self.tn.open(host_ip, port=23)
        except:
            logging.warning(u'\u7f51\u7edc\u8fde\u63a5\u5931\u8d25,\u8bf7\u8054\u7cfbEric')
            return False
            self.tn.read_until('login: ', timeout=10)
            self.tn.write(username.encode('ascii') + '\n')
            self.tn.read_until('Password: ', timeout=10)
            self.tn.write(password.encode('ascii') + '\n')
            time.sleep(2)
            command_result = self.tn.read_very_eager().decode('ascii')
            if 'Login incorrect' not in command_result:
                logging.warning(u'\u767b\u5f55\u6210\u529f\uff0c\u5f00\u59cb\u6d4b\u8bd5')
                return True
            logging.warning(u'\u767b\u5f55\u5931\u8d25\uff0c\u8bf7\u8054\u7cfb\u5f20\u6c38\u53ec/\u738b\u4eae')
            return False

    def execute_some_command(self, command, ctime):
        self.tn.write(command.encode('ascii') + '\n')
        time.sleep(ctime)
        command_result = self.tn.read_very_eager().decode('ascii')
        return command_result

    def exit_host(self):
        self.tn.write('exit\n')


if __name__ == '__main__':
    ip_dic = {1:u'ebgp-tm\u65b9\u5411',  2:u'ebgp-\u539f\u751fHE\u65b9\u5411',  3:u'ebgp-HGC\u65b9\u5411',  6:u'ebgp-HE\u65b9\u5411',  7:u'\u4e0a\u6d77\u7535\u4fe1cn2\u65b9\u5411',  8:u'gbgp-\u9646\u7f06\u5fb7\u56fd\u65b9\u5411',  9:u'jbgp-\u65e5\u672c\u65b9\u5411',  12:u'Hbgp-HKBN \u5c9b\u5185\u65b9\u5411',  15:u'Hbgp-HKBN \u5c9b\u5185\u65b9\u5411'}
    test_ip = input(u'\u9700\u8981\u6d4b\u8bd5\u7684ip\u5730\u5740:')
    host_ip = '210.22.148.197'
    username = 'zhangyongzhao'
    password = 'cnlink-sh'
    command0 = 'conf t \n ip route ' + test_ip + ' 255.255.255.255 10.161.1.2'
    command2 = 'ping ' + test_ip + ' source lo '
    command3 = 'conf t \n no ip route ' + test_ip + ' 255.255.255.255 10.161.1.2'
    telnet_client = TelnetClient()
    if telnet_client.login_host(host_ip, username, password):
        print(u'+++++++\u8def\u7531\u5f00\u59cb\u65b0\u589e' + test_ip + u'\u8def\u7531++++++++')
        telnet_client.execute_some_command(command=command0, ctime=1)
        telnet_client.exit_host()
        print(u'+++++++\u65b0\u589e\u6210\u529f++++++++++')
        for i in ip_dic.keys():
            print('+++++++++++++++++++++Eric.zhang+++++++' + ip_dic[i] + '+++++++++++++++++++++')
            text = telnet_client.execute_some_command(command=(command2 + str(i)), ctime=12)
            print(ip_dic[i] + ':' + text[text.rfind('min/avg/max ='):])

        print(u'+++++++\u5220\u9664\u8def\u7531+++++++')
        telnet_client.execute_some_command(command=command3, ctime=1)
        telnet_client.exit_host()
        telnet_client.exit_host()
    while 1:
        out = input(u'\u8c22\u8c22\u4f7f\u7528\uff0c\u8f93\u5165exit\u9000\u51fa')
        if out == 'exit':
            exit()