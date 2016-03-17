import sys
(k1, v1) = sys.stdin.readline().split("\t")
sum = int(v1)
cnt = 1
k = ""
for line in sys.stdin:
    (k, v) = line.strip().split("\t")
    if k == k1:
        sum += int(v)
        cnt += 1
    else:
        print(k1+'\t'+str(int(sum/cnt)))
        sum = int(v)
        cnt = 1
        k1 = k
print(k+'\t'+str(int(sum/cnt)))
