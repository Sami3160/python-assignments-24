a=input()
print(a[::-1])
l=len(a)
print("palindrome") if(a==a[::-1]) else print("not palindrome")
# print("palindrome") if(a[:l//2]==a[l//2:][::-1]) else print("not palindrome")
# print(a[:l//2])
# print(a[l//2:])