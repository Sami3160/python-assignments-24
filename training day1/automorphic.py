n=int(input())
# print("its automorphic") if(n==((n*n)%(10**(len(str(n))))))else print("its not automorphic")
# else:
    
b=str(n*n)
a=str(n)
if(b.endswith(a)):
    print("automorphic")
else:
    print("not automorphic")