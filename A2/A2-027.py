unit = int(input())
score_List = []
for i in range(unit):
    score = int(input())
    score_List.append(score)
topScore = max(score_List)
count = 0
for j in range(unit):
      if topScore == score_List[j]:
            count += 1
print(f"คะแนนสูงสุด:{topScore}\nจำนวน:{count}")