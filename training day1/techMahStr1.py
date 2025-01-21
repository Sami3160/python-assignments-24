# str1="OqPputLE"
str1="iamneo@"
# str1="OqPputLE"

vowel=['a','e','i','o','u']
str1=str1.lower()
c=0
for i in range( 1,len(str1)):
    if(str1[i-1] in vowel and str1[i] not in vowel and str1[i].isalpha()):
        c+=1
print(c)