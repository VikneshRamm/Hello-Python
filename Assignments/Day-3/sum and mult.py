def sum(lis):
    return reduce(lambda x,y:x+y,lis)
def multiply(lis):
    return reduce(lambda x,y:x*y,lis)

print sum([1,2,3,4])
print multiply([1,2,3,4])
