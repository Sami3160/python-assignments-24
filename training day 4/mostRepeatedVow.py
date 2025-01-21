s="abeaicaidao"
vow="aeiou"

d={}
for i in s:
    if i in vow:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
maxVal=0
maxVow=""
for i,j in d.items():
     if(maxVal<j):
         maxVal=j
         maxVow=i
print(maxVow, maxVal)