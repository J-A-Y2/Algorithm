n = int(input()) #상근이가 배달해야할 Nkg 설탕 무게

noAns = -1 

for fiveCount in range(n//5, -1, -1):
    threeCount = (n - fiveCount*5) // 3
    if fiveCount*5 + threeCount*3 == n:
        print(fiveCount + threeCount)
        break
else:
    print(noAns)