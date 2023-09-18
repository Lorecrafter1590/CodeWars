def kebabize(st):
    counter = 0 
    st = ''.join([i for i in st if not i.isdigit()]) 
    for x in range(1, len(st)):
        if st[x].isupper() == True:
            counter += 1
    for x in range(1,len(st) + counter):
        if st[x-1] == '-':
            continue
        if st[x].isupper() == True:
            st = st[:x] + '-' + st[x:]
    st = st.lower()                   
    return st

print(kebabize("HakunaMatata"))