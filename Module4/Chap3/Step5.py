import sys
H = {}
A = []
for line in sys.stdin:
    (k, v) = line.strip().split('\t')
    (id, tf, one) = v.split(';')
    A.append(k+'#'+id+'\t'+tf)
    H.update({k: H.setdefault(k, 0)+1})
for i in A:
    (k, v) = i.split('#')
    print(i+'\t'+str(H.get(k)))
