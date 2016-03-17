import sys
H = {}
A = []
for line in sys.stdin:
    (f, g) = line.strip().split("\t")
    A.append((f, g))
    A = list(set(A))
for i in A:
    H.update({i[1]: H.setdefault(i[1], 0)+1})
for i in H:
    print(i+'\t'+str(H.get(i)))
