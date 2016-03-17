import sys
fg1 = sys.stdin.readline().split("\t")[0]
for line in sys.stdin:
    fg = line.strip().split("\t")[0]
    if fg != fg1:
        print(fg1)
        fg1 = fg
print(fg)
