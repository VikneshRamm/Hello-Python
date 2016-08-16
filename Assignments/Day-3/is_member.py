def is_member(x,list):
    for i in list:
        if x == i:
            return True
    return False

print is_member(3,[1,2,3,4,5])