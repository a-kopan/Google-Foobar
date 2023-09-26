n = int(input(">>>"))


def solution(n):
    cache = []

    for x in range(n):
        cache.append([-1]*n)
        
    def part(n,k):
        if cache[n-1][k]>0:
            return cache[n-1][k]
        if n<=k:
            return 0
        else:
            s=1
            for i in range(k+1, n):
                s += part(n-i, i)
            cache[n-1][k]=s
            return s
    ans = part(n,0)-1
    return ans

print(solution(n))

