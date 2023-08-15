# unique values
dict=[{"v":"s001"},{"v1":"s002"},{"v11":"s005"},{"v111":"s005"}]
c=[]
for i in dict:
    c.append(dict)
d=[]
for i in c:
    if i not in d:
       d.append(i)
print(dict(d))
    