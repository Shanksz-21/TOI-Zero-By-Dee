N,M = map(int,input().split())
red = map(int,input().split())
blue = map(int,input().split())
reds = list(red)
blues = list(blue)
reds.insert(0,0)
blues.insert(0,0)
if len(reds) == N+1 and len(blues) == M+1:
    count = 1
    for i in range(N):
        for j in range(M+1):
            if reds[i] < blues[j] <= reds[i+1]:
                count += 1
            else:
                pass
    print(count)
else:
    print("Error")