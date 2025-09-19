N,K = map(int,input().split())
C_str = ''
for n in range(N):
    C = str(input())
    C_str += C
Wall = []
for i in range(K,N):
    for j in range(N-K+1):
        wall = C_str[j:i+j]
        if len(set(wall)) >= K:
            Wall.append(wall)
            print(Wall)
        print(j)
if len(set(C_str)) >= K:
    Wall.append(C_str)
Wall = set(Wall)
Wall = list(Wall)
print(len(Wall))