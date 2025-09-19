N,S = map(int,input().split())
try:
    if 1<=N<=1000 and 1<=S<=N:
        into = []
        S -= 1
        for n in range(N):
            a = int(input())
            into.append(a-1)
        count = 0
        status = True
        while count<N and status:
            S = into[S]
            if S == -1:
                count += 1
                status = False
            else:
                count+=1
        print(count)
    else:
        raise ValueError()
except ValueError:
    print("check\
          \n1<=N<=1000 and 1<=S<=N")
