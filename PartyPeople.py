def party_people(lst):
    lst.sort()
    for x in range(len(lst)-1,-1,-1):
        if lst[x] > len(lst):
            del lst[x]              
    return len(lst)
