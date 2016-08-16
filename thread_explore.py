import threading,time
count = 0
class MyThread(threading.Thread):
    def __init__(self,name):
       super(MyThread,self).__init__()
       #super(MyThread,self).setdaemon(True)
       self.name = name
    def run(self):
        
        print 'Child Thread %s' %(self.name)
        loop1(self.name)
        
def loop1(name):
    global count
    for i in range(5):
        
        count += i
        print "%s %d" %(name,count)
        time.sleep(1)
        
lock = threading.Lock()    
#t = MyThread("Viknesh")
t1 = MyThread("Ramm")
t1.setDaemon(True)
#t.start()
t1.start()
#t.join()
for i in range(5):
        print "%s %d" %('Main Thread',i)
        if i == 3:
            break
        time.sleep(1)
print t1.isDaemon()



    
    
        