arr = [9, 16, 12, 5, 15]
brr = [14, 7, 22, 5, 32, 77]
k = 9
# arr_max = len([x for x in arr if x > k])
# brr_max = len([x for x in arr if x < k])
# print(arr_max if arr_max > brr_max else brr_max)


c=0
for i in arr:
   if i>k:
       c+=1
d=0
for i in brr:
   if i<k:
       d+=1 
print(max(c,d))