import sys
queries = {}
urls = {}
for line in sys.stdin:
    (k, v) = line.strip().split("\t")
    (tag, value) = v.split(':')
    if tag == "query":
        queries.update({k: queries.setdefault(k, "")+value+';'})
    if tag == "url":
        urls.update({k: urls.setdefault(k, "")+value+';'})
for k in sorted(queries.keys()):
    for q in queries.get(k)[:-1].split(';'):
        if urls.get(k):
            for u in urls.get(k)[:-1].split(';'):
                print(k+'\t'+q+'\t'+u)
