a=input()
l=len(a)
b=0
for i in range(l):
    if(a[i]!=a[l-i-1]):
        print("not palindrome")
        b=1
        break
if(b==0):
    print("palindrome")