# s="bbadbbababb"
s="liril"
replacement="t"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
maxVal=0
maxChar=""
for i,j in d.items():
    if(maxVal<j):
         maxVal=j
         maxChar=i
for i,j in d.items():
    if j==maxVal:
        if(ord(maxChar)>ord(i)):
            maxChar=i
            
            
s=list(s)
for i in range(len(s)):
    if(s[i]==maxChar):
        s[i]=replacement
s=''.join(s)
print(s)





# tip
# sorted(d, key=d.get)
# print(d)
# get max key from dict by value
# res=max(d, key=d.get)

