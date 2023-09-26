N, K= map(int,input().split())
death = []
for _ in range(N):
    death.append(int(input()))

target = 0
cnt = 0
for i in range(N):
    target = death[target]
    cnt+=1
    if K==target:
        print(cnt)
        break
else:
    print(-1)