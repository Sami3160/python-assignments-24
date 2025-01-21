m=int(input())
l1=list(map(int, input().split()))[:m+1]
l1.sort()
l2=[]
i=0
j=len(l1)-1
while(i<j):
    l2.append(l1[i])
    l2.append(l1[j])
    i+=1
    j-=1
if(len(l1)%2==1):
    l2.append(l1[i])
print(l2)
