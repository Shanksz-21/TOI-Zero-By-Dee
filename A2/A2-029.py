N = int(input("N:"))
if N <= 3:
      for i in range(N):
            print("0 "*(i+1))
elif N > 3:
      print("0")
      n = N - 2
      for i in range(n):
            print(f'0 {'1 '*(i)}0')
      print("0 "*N)