import sys
H = {}
for line in sys.stdin:
    (k, v) = line.strip().split("\t")
    H.update({k: H.setdefault(k, "")+v})
for i in sorted(H):
    if len(H.get(i)) == 1:
        print(i)
