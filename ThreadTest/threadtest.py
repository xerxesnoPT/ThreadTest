# -*- coding: utf-8 -*-
from threading import Thread


class Threadtest(Thread):
    def __init__(self,name):
        super(Threadtest, self).__init__()
        self.name = name

    def run(self):
        for i in range(0, 5):
            print(self.name+str(i))



def main():
    threadpool = []
    for i in range(0, 4):
        t = Threadtest(str(i))
        threadpool.append(t)
    # t1 = Threadtest('i am no.1')
    # t2 = Threadtest('i am no.2')
    # t1.start()
    # t2.start()
    for t in threadpool:
        t.start()

if __name__ =='__main__':
    main()
