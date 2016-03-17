import sys
(k1, v1) = sys.stdin.readline().split("\t")
sum = int(v1.split(';')[0])
cnt = 1
k = ""
for line in sys.stdin:
    (k, v) = line.strip().split("\t")
    if k == k1:
        sum += int(v.split(';')[0])
        cnt += 1
    else:
        print(k1+'\t'+str(sum)+';'+str(cnt))
        sum = int(v.split(';')[0])
        cnt = 1
        k1 = k
print(k+'\t'+str(sum)+';'+str(cnt))
