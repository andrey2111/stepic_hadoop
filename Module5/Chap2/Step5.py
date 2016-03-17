import sys
for line in sys.stdin:
    s = line.strip().split('\t')
    print('\t'.join(i for i in s))
    c = s[2][1:-1].split(',')
    if c != ['']:
        for i in c:
            if s[1] != 'INF':
                print(i+'\t'+str(int(s[1])+1)+'\t'+'{}')
            else:
                print(i+'\t'+'INF'+'\t'+'{}')
