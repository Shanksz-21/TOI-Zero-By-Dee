N = int(input())
high = map(int,input().split())
high = list(high)
bird = 0
for i in high:
      if N > 1000 or N < 1:
            print("N ไม่อยู่ใน [1,1000]")
            break
      elif i > 1000000 or i < 1:
            print("H ไม่อยู่ใน [1,1000000]")
            break
else:
      if N == len(high):
            for x in range(N):
                  if high[x-1] < high[x] and high[x] > high[x+1]:
                        bird += 1
      elif N < len(high):
            print("จำนวนของ Hเกินที่กำหนด")
      elif N > len(high):
            print("จำนวนของ H ไม่ถึงที่กำหนด")
print(bird)