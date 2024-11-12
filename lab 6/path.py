import os

os.makedirs('./india/delhi')
os.makedirs('./india/mumbai')
os.makedirs('./india/chennai')

print(os.listdir('india'))

os.rename('india/chennai', 'india/kolkata')

print(os.path.exists('india/kolkata'))

os.rmdir('india/kolkata')

for root, dirs, files in os.walk('india'):
    print(root, dirs, files)

print(os.getcwd())

os.chdir('india/delhi')
print(os.getcwd())

with open('rahul.txt', 'w') as f:
    f.write('Hello Rahul')

with open('rahul.txt', 'r') as f:
    print(f.read())

os.remove('rahul.txt')

os.chdir('../..')
print(os.getcwd())

os.rmdir('india/delhi')
os.rmdir('india/mumbai')
os.rmdir('india')
