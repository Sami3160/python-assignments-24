str1="hello world"
a=str1.split()
for i in range(len(str1.split())):
    for j in range(len(str1.split()[i])):
        l=len(str1.split()[i])
        d=str1[l-j-1]
        str1[l-j-1]=str1[j]
        str1[j]=d
print(str1)
        
        
    	
    
