str1="a1b2igh3"
p1=0
p2=len(str1)-1
str2=""
while(p1<len(str1) or p2>=0):
    if(str1[p1].isalpha()):
        if(str1[p2].isalpha()):
            str2+=str1[p2]
            p2-=1
            p1+=1
        else:
            p2-=1
    else:
        str2+=str1[p1]
        p1+=1
    
    
print(str2)