names = ("Amit", "Raj", "Priya", "Anjali")
ages = (25, 30, 22, 28)

first_name = names[0]
last_age = ages[-1]

middle_names = names[1:3]

combined = names + ages

repeated_names = names * 2

is_amit_in_names = "Amit" in names

names_length = len(names)

nested_tuple = (names, ages)

(name1, name2, name3, name4) = names

single_element_tuple = ("Suresh",)

mixed_tuple = ("Ravi", 35, True)

for name in names:
    print(name)

def get_person():
    return "Vijay", 40

person_name, person_age = get_person()
