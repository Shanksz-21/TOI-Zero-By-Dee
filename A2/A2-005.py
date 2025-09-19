W,H,M,N = map(int,input().split())
X = map(int,input().split())
Y = map(int,input().split())
X = list(X)
Y = list(Y)
X.append(W)
X.append(0)
Y.append(H)
Y.append(0)
X.sort()
Y.sort()
area = []
for x in range(M+1):
      for y in range(N+1):
            A = (X[x+1]-X[x])*(Y[y+1]-Y[y])
            area.append(A)
area.sort()
print(f"{area[-1]} {area[-2]}")