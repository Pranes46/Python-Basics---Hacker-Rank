from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    deq=input().split()
    if deq[0]=="append":
        d.append(int(deq[1])) 
    elif deq[0]=="appendleft":
        d.appendleft(int(deq[1]))
    elif deq[0]=="pop":
        d.pop()
    elif deq[0]=="popleft":
        d.popleft()
print(*d)
