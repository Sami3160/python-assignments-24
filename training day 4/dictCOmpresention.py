s="liril"
d={}
for p in s:
    d[p]=s.count(p)
print(d)


#another method
d={p:s.count(p) for p in s}
print(d)


l=[1,2,3,4,1,4,1,2,5,1,2,21,4,3,1]
d={p:l.count(p) for p in l}
print(d)


#another
l=[1,2,3,4,1,4,1,2,5,1,2,21,4,3,1]
d={p:d.get(p,0)+1 for p in l}


#another
l=[1,2,3,4,1,4,1,2,5,1,2,21,4,3,1]
d={p:d.get(p,0)+1 for p in l}
for p in l:
    if p not in d:
        d[p]=1
    else:
        d[p]+=1
print(d)