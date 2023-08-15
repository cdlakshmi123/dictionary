# max 3
dict={"a":20,"b":45,"c":61,"d":98,"e":100}
a=list(dict.values())
a.sort(reverse=True)
a=a[0:3]
print(a)