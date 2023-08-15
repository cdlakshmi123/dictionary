# riginal dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]

# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

n= {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x=list(n.keys())
i=0
d=dict()
while i<len(n):
    x.sort()
    d.append(x[i])
    i=i+1
print(d)
    
    
    

