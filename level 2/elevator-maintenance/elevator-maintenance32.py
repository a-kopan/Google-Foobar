def solution(l):
    l = [x.split('.') for x in l]
    #change each string to int
    for x in range(len(l)):
        for y in range(len(l[x])):
            l[x][y] = int(l[x][y])
    #add -1 as revision if there is none
    for arr in l:
        while len(arr)!=3:
            arr.append(-1)
    #sort by each number one by one
    l = sorted(l, key=lambda x: (x[0],x[1],x[2]))
    #filter the revision -1s
    for arr in l:
        while(arr[-1]==-1):
            arr.pop(-1)
    #change the arrays contents back into strings
    for x in range(len(l)):
        for y in range(len(l[x])):
            l[x][y] = str(l[x][y])
    for x in range(len(l)):
        l[x] = '.'.join(l[x])
    return l