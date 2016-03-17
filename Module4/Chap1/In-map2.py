import sys
H = {}
for line in sys.stdin:
    for token in line.strip().split(" "):
        H.update({token: H.setdefault(token, 0)+1})
for i in H:
    print(i+'\t'+str(H.get(i)))
