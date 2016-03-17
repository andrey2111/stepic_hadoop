import sys
i1 = sys.stdin.readline().split('\t')[0]
for line in sys.stdin:
    i = line.strip().split("\t")[0]
    if i != i1:
        print(str(i1))
        i1 = i
print(i)
