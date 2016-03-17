import sys
current = sys.stdin.readline().strip().split('\t')
for line in sys.stdin:
    s = line.strip().split('\t')
    if s[1] == 'INF':
        s[1] = float('inf')
    if s[0] == current[0]:
        current[1] = str(min([float(s[1]), float(current[1])]))
        if len(s[2]) > 2:
            current[2] = s[2]
    else:
        if current[1] == 'inf':
            current[1] = 'INF'
        else:
            current[1] = int(float(current[1]))
        print('\t'.join(str(i) for i in current))
        current = s

if current[0] == s[0]:
    if current[1] == float('inf') or current[1] == 'INF' or current[1] == 'inf':
        current[1] = 'INF'
    else:
        current[1] = int(float(current[1]))
    print('\t'.join(str(i) for i in current))
else:
    if s[1] == float('inf') or s[1] == 'INF' or s[1] == 'inf':
        s[1] = 'INF'
    else:
        s[1] = int(float(s[1]))
    print('\t'.join(str(i) for i in s))

