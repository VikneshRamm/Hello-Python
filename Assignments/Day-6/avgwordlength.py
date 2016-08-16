try:
    f = open(r'D:\Viknesh Ramm\Python Programs\Assignments\Day-6\readfile.txt','r')
    wlist = f.read().split('.')
    wlist = ''.join(wlist).split()
    print reduce(lambda x,y:x+y,map(len,wlist))/float(len(wlist))
except IOError,var:
    print str(var)
finally:
        f.close()