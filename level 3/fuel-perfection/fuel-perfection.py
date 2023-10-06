a = input(">")

def solution(n):
    n = int(n)
    steps = 0
    while n>1:
        temp = bin(n)
        if temp[-1]=='0': n = n>>1 
        elif temp[-2:]=='01': n-=1
        #check if the number has '11' at the end and is not bin(3)
        elif temp[-2:]=='11' and len(temp)>4: n+=1
        else: n-=1
        steps+=1
    return steps

print(solution(a))
