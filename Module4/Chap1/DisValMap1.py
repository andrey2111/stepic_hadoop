import sys
for line in sys.stdin:
    (f, g) = line.strip().split("\t")
    for i in g.split(','):
        print(f+','+i+'\t'+str(1))
