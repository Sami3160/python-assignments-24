str1="leetcode"
def check(s):
    map={}
    for i in s:
        if( i in map):
            map[i]+=1
        else:
            map[i]=1

    for i in range(len(s)):
        if map[s[i]]==1 :
            # print(i)
            return i
    return -1
print(check(str1))
