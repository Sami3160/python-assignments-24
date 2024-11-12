class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title

    def introduce(self):
        return f"My name is {self.name} and I am a {self.job_title}"

class Manager(Employee):
    def __init__(self, name, job_title, department):
        super().__init__(name, job_title)
        self.department = department

    def introduce(self):
        return f"My name is {self.name}, I am a {self.job_title} and I manage the {self.department} department"

person = Person("Amit")
employee = Employee("Ravi", "Software Engineer")
manager = Manager("Priya", "Project Manager", "IT")

print(person.introduce())
print(employee.introduce())
print(manager.introduce())