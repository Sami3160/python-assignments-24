a=[1,2,3,4,5,4,3,9,1,5,3,6]
b=a.copy()
print(a.insert(2,30))
print(a.index(3))
print(a.index(3, 3))
print(a.index(3, 3, 6))
print(a.pop())
print(a.remove(3))
print(a.reverse())
print(a.sort())
del a[0]
print(a)
print(a.clear())

print(a)
print(b)