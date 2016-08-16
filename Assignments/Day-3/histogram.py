def histogram(li):
    for i in li:
        s = ''
        for k in range(i):
            s += '*'
        print s    
histogram([4,9,7])
        