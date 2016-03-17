import sys
for line in sys.stdin:
    s = line.strip().split('\t')
    print('\t'.join(i for i in s))
    c = s[2][1:-1].split(',')
    for i in c:
        x = str(round(float(s[1])/len(c), 3))
        if len(x) < 4:
            for j in range(5-len(x)):
                x += '0'
        print(i+'\t'+x+'\t{}')
