v="w3source"
i=0
d={}
while i<len(v):
    r=v.count(v[i])
    if v[i] not in d:
        d[v[i]]=r
    i=i+1
print(d)