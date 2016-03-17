import sys
current = ['1', '0.0', '{}']
for line in sys.stdin:
    s = line.strip().split('\t')
    if s[0] == current[0]:
        if s[2] == "{}":
            current[1] = str(float(current[1]) + float(s[1]))
        else:
            current[2] = s[2]
    else:
        current[1] = str(round(float(current[1]), 3))
        if len(current[1]) < 5:
            for j in range(5-len(current[1])):
                current[1] += '0'
        print('\t'.join(i for i in current))
        current[0] = s[0]
        if s[2] == "{}":
            current[1] = s[1]
        else:
            current[1] = '0.000'
            current[2] = s[2]

current[1] = str(round(float(current[1]), 3))
if len(current[1]) < 5:
    for j in range(5-len(current[1])):
        current[1] += '0'
print('\t'.join(i for i in current))

