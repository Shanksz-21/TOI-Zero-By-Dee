try:
    N = int(input())
    if N < 1 or N > 100000:
        raise ValueError
    else:
        i = 0
        status = True
        mem = []
        while status:
            if i**2 < N <= (i+1)**2:
                mem = [j+1 for j in range(i**2,(i+1)**2)]
                status = False
            else:
                i += 1
        if N == 1:
            print("0")
        else:
            index = mem.index(N)
            if index % 2 == 0:
                smash = 2*i
            else:
                smash = (2*i)-1
            print(smash)
except ValueError:
    print("1<=N<=100,000")