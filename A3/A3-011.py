import time as t
t1 = t.time()
try:
    N = int(input())
    P = map(int,input().split())
    P = list(P)
    n = len(P)
    checkS = [1<=P[k]<=100000 for k in range(n)]
    if len(P) == N and 1<=N<=100 and all(checkS):
        result = []
        for i in range(0,N):
            for j in range(0,N-i):
                pSum = sum(P[j:j+i+1])
                result.append(pSum)
        result = set(result)
        prob = len(result)
        print(prob)
    else:
        raise ValueError
except ValueError:
    print("check this\
    \n1<=N<=100\
    \n1<=P<=100000")
t2 = t.time()
t1 *= 10**(-3)
t2 *= 10**(-3)
print(f'time {t2-t1:.3f} seconds')