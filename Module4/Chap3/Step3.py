import sys
(k1, v1) = sys.stdin.readline().split('\t')
cnt = 1
for line in sys.stdin:
    (k, v) = line.split('\t')
    if k != k1:
        (word, id) = k1.split('#')
        print(word+'\t'+str(id)+'\t'+str(cnt))
        k1 = k
        cnt = 1
    else:
        cnt += 1
(word, id) = k1.split('#')
print(word+'\t'+str(id)+'\t'+str(cnt))
