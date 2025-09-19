N = int(input())
valiable = []
for i in range(N):
    A,L,B,R = map(int,input().split())
    valiable.append([A,L,B,R])
balance = [[] for n in range(N)]
i = 0
for i in range(N):
    j = 0
    while j <= 2:
        if valiable[i][j] == 0:
            balance[i].append(f'index{valiable[i][j+1]-1}') #form index
        elif valiable[i][j] == 1:
            balance[i].append(valiable[i][j+1])
        j += 2
print(valiable)
print(balance)