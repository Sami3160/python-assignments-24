s={"name":"Raju","Rno":433,"subject":"Python","marks":78}
print(s)

#access
print(s["name"])

#update
s["marks"]=90
print(s)

#keys
for i in s.keys():
    print(i)


#values
for i in s.values():
    print(i)


#items
for i in s.items():
    print(i)
for i,j in s.items():
    print(i,j)

l1=sorted(s.keys())
print(l1)

