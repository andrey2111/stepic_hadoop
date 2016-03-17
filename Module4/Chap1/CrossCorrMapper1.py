import sys
for line in sys.stdin:
    M = line.strip().split(' ')
    for i in M:
        for j in M:
            if i != j:
                print(i+','+j+'\t'+str(1))
