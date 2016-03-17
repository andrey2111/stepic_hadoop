import sys
for line in sys.stdin:
    g = line.strip().split(",")[1]
    print(g+'\t'+str(1))
