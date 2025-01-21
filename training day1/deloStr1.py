# 10 mob
# 1 gen

# last second 2 age
# last 2 seat
l1=["1234567898F5965","1234567898F7065","1234567898F6265"]
# l1=[]
# n=int(input("n: "))
# for i in range(n):
#     rec=input("records : ")
#     l1.append(rec)
# c=0
# for l in l1:
#     if(int(l[11:13])>60):
#         c+=1
# print(c)

# for i in range(len(l1)):
#     rec=input("records : ")
#     l1.append(rec)
c=0
for l in l1:
    if(int(l[-4:-2])>60):
        c+=1
print(c)