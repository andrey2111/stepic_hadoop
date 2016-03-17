import sys
H = {}
for line in sys.stdin:
    (k, v) = line.strip().split("\t")
    H.update({k: H.setdefault(k, "")+v})
    if H.get(k) == "AB":
        print(k)
