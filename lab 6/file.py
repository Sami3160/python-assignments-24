import os

with open('example.txt', 'w') as file:
    file.write('Hello, my name is Rajesh.\n')
    file.write('I live in Mumbai.\n')

with open('example.txt', 'a') as file:
    file.write('I love programming.\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

with open('example.txt', 'r') as file:
    file.seek(0)
    print(file.tell())
    print(file.read(5))
    print(file.tell())

with open('example.txt', 'r') as file:
    print(file.read())

with open('example.bin', 'wb') as file:
    file.write(b'Hello, my name is Sita.\n')

with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

if os.path.exists('example.txt'):
    print('File exists')
else:
    print('File does not exist')

if os.path.exists('example.txt'):
    os.remove('example.txt')
    print('File deleted')
else:
    print('File does not exist')
