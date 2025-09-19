N,K,T = map(int, input().split())
num = [n for n in range(N)]
status = True
i = 1
while status:
    if (i*K)%N == 0:
        print(i)
        status = False
    elif (i*K)%N == T-1:
        print(i+1)
        status = False
    i+=1