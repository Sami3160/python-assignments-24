num=int(input())
s=list(str(num))
s.sort()
c=0
ans=[]
for i in s:
    if(i=='0'):
        c+=1
        continue
    ans.append(i)
while(c!=0):
    ans.insert(1,'0')
    c-=1
print(int(''.join(ans)))
# print(s)