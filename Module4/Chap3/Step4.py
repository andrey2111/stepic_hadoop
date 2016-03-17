import sys
for line in sys.stdin:
    (k, v1, v2) = line.strip().split('\t')
    print(k+'\t'+v1+';'+v2+';'+str(1))
