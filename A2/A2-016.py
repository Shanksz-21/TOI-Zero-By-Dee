alplot,numlot = map(str,input().split())
myalplot,mynumlot = map(str,input().split())

pos = [numlot[i]==mynumlot[i] for i in range(5)]

if alplot==myalplot:
    if all(pos):
        print("คุณได้เงินรางวัล 1,000,000 บาท")
    elif pos[-1] and pos[-2]:
        if pos[-3]:
            print("คุณได้เงินรางวัล 2,000 บาท")
        else:
            print("คุณได้เงินรางวัล 1,000 บาท")
    else:
        print("คุณได้เงินรางวัล 20 บาท")
else:
    if all(pos):
        print("คุณได้เงินรางวัล 100,000 บาท")
    elif pos[-1] and pos[-2]:
        if pos[-3]:
            print("คุณได้เงินรางวัล 200 บาท")
        else:
            print("คุณได้เงินรางวัล 100 บาท")
    else:
        print("ขอแสดงความเสียใจ คุณโดนแดกกกกก")