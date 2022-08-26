from collections import defaultdict

x, y = map(int, input().split())

group_A = defaultdict(list)

for i in range(1, x+1):
    group_A[input()].append(i)
    
group_b = [input() for i in range(0, y)]

for i in group_b:
    print("-1") if not i in group_A else print(*group_A[i])
