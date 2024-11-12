students = {
    "Amit": 21,
    "Priya": 22,
    "Raj": 20,
    "Sneha": 23
}

age_amit = students["Amit"]

students["Vijay"] = 24

students["Priya"] = 23

del students["Raj"]

is_sneha_present = "Sneha" in students

for name in students:
    print(name)

for age in students.values():
    print(age)

for name, age in students.items():
    print(name, age)

num_students = len(students)

students.clear()
