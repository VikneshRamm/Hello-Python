try:
    rf = open(r'D:\Viknesh Ramm\Python Programs\Assignments\Day-6\readfile.txt','r')
    wr = open(r'D:\Viknesh Ramm\Python Programs\Assignments\Day-6\writefile.txt','w')
    wline = []
    lno = 1
    for line in rf:
        li = str(lno)+":"+line.strip()+"\n"
        print li
        wr.write(li)
        lno += 1
    wr.close()
except IOError,var:
    print str(var)
