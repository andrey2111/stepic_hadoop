import sys
import string
for line in sys.stdin:
    (id, content) = line.split(":", 1)
    for c in string.punctuation:
        content = content.replace(c, " ")
    content = ' '.join(content.split(' '))
    content = content.split()
    for word in content:
        print(word+'#'+id+'\t'+str(1))
