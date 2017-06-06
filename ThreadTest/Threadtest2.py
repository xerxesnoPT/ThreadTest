# -*- coding: utf-8 -*-
from threading import Thread
import threading

def execute(name):
    for i in range(0, 5):
        print('我的名字是 %s ' % name+threading.current_thread().name)

def main():
    t1 = Thread(target=execute, name='1', args=('jack',))
    t2 = Thread(target=execute, name='2', args=('Tom',))
    t1.start()
    t1.join()
    t2.start()

if __name__ == '__main__':
    main()
