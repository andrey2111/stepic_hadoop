w = {} #веса рёбер
AL = {} #Список смежностей

(v, r) = [int(i) for i in input().split()]
for i in range(r):
    s = [int(i) for i in input().split()]
    w[(s[0], s[1])] = s[2]
    if s[0] in AL:
        AL[s[0]].append(s[1])
    else:
        AL[s[0]] = [s[1]]

(start, end) = [int(i) for i in input().split()]

V = []
d = {}
for i in range(1, v+1):
    V.append(i)
    d[i] = float('inf')
d[start] = 0
Q = d.copy()
while len(Q) != 0:
    u = [k for k, v in Q.items() if v == min(Q.values())][0]
    if Q[u] == float('inf'):
        break
    Q.pop(u)
    if u not in AL:
        continue
    for i in AL[u]:
        if d[i] > d[u] + w[(u, i)]:
            d[i] = d[u] + w[(u, i)]
    for i in Q:
        Q[i] = d[i]
    print(d)

if d[end] == float('inf'):
    print(-1)
else:
    print(d[end])
