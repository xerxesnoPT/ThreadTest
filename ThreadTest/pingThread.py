#-*- ecoding:utf-8 -*-
import os
import subprocess
import threading
def ping (ip):
    result = subprocess.call('ping -n 1 -w 1 '+ip)
    with open('F:/result.txt', 'a') as f:
        if result:
            f.write('%s  death \n' %ip)
        else:
            f.write('%s alive \n' %ip)

# class PingThread(threading.Thread):
#     def __init__(self,ip):
#         super(PingThread, self).__init__()
#         self.ip = ip
#     def run(self):
#         result = os.system("ping -n 1 -w 1 "+self.ip)
#         if result:
#             print('%s death' %ip)
#         if not result:
#             print('%s alive' %ip)




# ping('www.baidu.com')
#
#
#
if __name__ == '__main__':
    ip = input("请输入网段前三位地址")
    iplist = []
    result = []
    for i in range(0, 240):
        iplist.append(ip+'.'+str(i))
    for ip in iplist:
        t = threading.Thread(target=ping, args=(ip,))
        t.start()

