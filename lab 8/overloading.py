class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

    def multiply(self, a, b, c=1):
        return a * b * c

class Person:
    def greet(self, name=None):
        if name is not None:
            return f"Namaste, {name}!"
        else:
            return "Namaste!"

class Area:
    def calculate(self, length, breadth=None):
        if breadth is not None:
            return length * breadth
        else:
            return length * length

math_ops = MathOperations()
print(math_ops.add(10, 20))
print(math_ops.add(10, 20, 30))
print(math_ops.multiply(2, 3))
print(math_ops.multiply(2, 3, 4))

person = Person()
print(person.greet())
print(person.greet("Amit"))

area = Area()
print(area.calculate(5))
print(area.calculate(5, 10))