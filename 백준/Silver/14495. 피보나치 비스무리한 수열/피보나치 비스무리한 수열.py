n = int(input())

sequence = [1,1,1]

for i in range(3,117):
    sequence.append(sequence[i-1] + sequence[i-3])

print(sequence[n-1])