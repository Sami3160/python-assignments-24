str1=input()
vow={"a":"e", "e":"i", "i":"o", "o":"u","u":"a"}
newStr=""
for i in range(len(str1)):
    if(str1[i] in vow.keys()):
        newStr+=(vow[str1[i]])
    else:
        newStr+=(str1[i])
print(newStr)
# print(str1)