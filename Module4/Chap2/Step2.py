import sys
for line in sys.stdin:
    a = line.strip().split("\t")
    if a[1] == "user10":
        print('\t'.join(i for i in a))
