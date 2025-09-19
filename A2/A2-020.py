N1 = int(input())
N2 = int(input())
N3 = int(input())
N4 = int(input())
N5 = int(input())
N6 = int(input())

N = [1,2,3,4,5,6]
NInvers = [[N1,1],[N2,2],[N3,3],[N4,4],[N5,5],[N6,6]]
inters = {0}
start = 0
while start == 0 or len(inters) < 7:
    for i in range(6):
        j=0
        while j < 6:
            if N[i] == NInvers[j][0]:
                N[i] = NInvers[j][1]
                j = 6
            j+=1
    for k in range(6):
        A = k+1
        B = N[k]
        if A == B:
            inters.add(A)
    start = 1
    print(N)