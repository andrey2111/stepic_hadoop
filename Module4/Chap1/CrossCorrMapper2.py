import sys
for line in sys.stdin:
    M = line.strip().split(' ')
    for i in M:
        H = {}
        for j in M:
            if i != j:
                H.update({i: H.setdefault(i, "")+j+':'+str(M.count(j))+','})
        print(i+'\t'+(','.join(str(k) for k in set(H.get(i)[:-1].split(',')))))
