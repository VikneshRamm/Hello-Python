import re
def sent_splitting():
    f = open(r'D:\Viknesh Ramm\Python Programs\senttext.txt','r+')
    ss = f.read()
    t = ('Mr','Mrs','Dr','Jr','Prof')
    str = re.sub(r'\n',r' ',ss)
    #str = 'Hai all. I am going to teach you python Today with and Prof. Man.M.E.Phd., the link www.google.com. Have fun!!! My name is Mr. Viknesh.'
    str = re.sub(r'([?!])( )([A-Z0-9])',r'\1\n\3',str)
    #print re.sub(r'([^'+'| '.join(t)+']*[\.?!])( )([A-Z0-9])',r'\1\n\3',str)
    s = re.findall(r'(\w*\.*)\. [A-Z0-9]',str)
    for i in s:
        if i not in t:
            str = re.sub(r'(%s\.)( )(.*)' %(i),r'\1\n\3',str)
    print str
    f.close()
    
sent_splitting()    
    
