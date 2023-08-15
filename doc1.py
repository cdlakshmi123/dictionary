a={"a":100,"b":200,"c":300}
b={"a":100,"b":200,"c":400}
i=0
x=list(a)
y=list(b)
c={}
while i<len(a):
    if x[i] in y[i]:
        c[x[i]]=a[x[i]]+b[y[i]]
    else:
        c[x[i]]=x[i]=a[x[i]]
        c[y[i]]=y[i]=b[y[i]]
    i=i+1
print(c)
        
    