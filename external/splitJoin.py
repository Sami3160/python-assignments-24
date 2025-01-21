string="Sami:28 may,Atharv:31 Dec,Amar:26 feb"
print(string.split(','))
di=dict(pair.split(':') for pair in string.split(','))
# print(di)
# print(','.join(f"{name}:{date}" for name, date in di.items()))

di=dict({'a':2,'b':1,'c':0,'d':5,'e':8})
print(sorted(di.items(), key=lambda item:item[1]))