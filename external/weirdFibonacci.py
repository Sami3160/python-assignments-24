def fibonacci(limit):
    a,b =1,2
    total =0
    while a <=limit:
        if a%2==0:
            total+=a
        a,b=b,a+b
    print(total)

limit = 4000000
# fibonacci(limit)

# print(result)


def trace_birthday(birthdays, name):
    return birthdays.get(name, "Birthday not found")

# Example usage
birthdays = {
    "Alice": "1990-01-01",
    "Bob": "1992-02-02",
    "Charlie": "1993-03-03"
}

# Using split and join methods
birthday_string = "Alice:1990-01-01,Bob:1992-02-02,Charlie:1993-03-03"
birthday_list = birthday_string.split(',')
birthdays = {item.split(':')[0]: item.split(':')[1] for item in birthday_list}

name_to_trace = "Bob"
# print(f"{name_to_trace}'s birthday is {trace_birthday(birthdays, name_to_trace)}")



def combine_lists(keys, values):
    return dict(zip(keys, values))

# Example usage
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = combine_lists(keys, values)
print(result)