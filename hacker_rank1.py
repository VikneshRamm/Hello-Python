
''' https://www.hackerrank.com/challenges/bigger-is-greater/copy-from/26027453 
Link for the question '''
def check(char,*lit):
    '''Checks whether a character in lit is lexichographically
    greater than char'''
    for i in sorted(lit[0]):
        if i > char:
            return i
    return 'none'    
n = input()
li = []
for i in range(n):
    li.append(raw_input())
for i in li:
    if len(i) == 2:
        if i[::-1] > i:
            print i[::-1]
        else:
            print 'no answer'
        continue
    j = len(i) - 2
    while(j >= 0):
        m = check(i[j],i[j+1:]) 
        if(m <> 'none'):
            st = ''.join(i[:j]) + m
            lis = list(i[j+1:])
            lis.remove(m)
            lis.append(i[j])
            st += ''.join(sorted(lis))
            print st
            break
        j = j-1
    if j < 0:
        print 'no answer'