a={"a":50,"b":80,"c":100,"d":59,"e":70}
x=list(a.keys())
d=dict()
x.sort(reverse=True)
x=x[:3]
print(x)