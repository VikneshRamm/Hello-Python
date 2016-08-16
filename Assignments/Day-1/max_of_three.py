def max(val1,val2,val3):
    if val1 > val2 and val1 > val3:
        return val1
    elif val2 > val3 and val2 > val1:
        return val2
    return val3
x = input('Enter three values:\n')
y = input()
z = input()
print 'The maximum value is %d' %(max(x,y,z))
