def is_overlap(list1,list2):
    'checks for overlapping'
    for x1 in list1:
        for x2 in list2:
            if x1 == x2:
                return True

    return False
list1 = [1,2,3,4,5]
list2 = [1,7,8,9,6]
print "Do list ovarlap: ",is_overlap(list1,list2)
