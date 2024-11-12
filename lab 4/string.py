name = "Amit"
greeting = 'Namaste'
multiline = """This is a
multiline string"""

full_greeting = greeting + ", " + name

repeated_greeting = greeting * 3

first_char = name[0]
last_char = name[-1]

substring = name[1:3]

length = len(name)

upper_case = name.upper()
lower_case = name.lower()
title_case = name.title()
capitalized = name.capitalize()
swapped_case = name.swapcase()

index_of_a = name.find('a')
index_of_i = name.index('i')
count_of_m = name.count('m')

replaced_name = name.replace('A', 'S')

split_greeting = greeting.split()
split_by_comma = full_greeting.split(',')

joined_string = ' '.join(split_greeting)

whitespace_string = "   Hello   "
stripped_string = whitespace_string.strip()
left_stripped = whitespace_string.lstrip()
right_stripped = whitespace_string.rstrip()

starts_with_nam = greeting.startswith('Nam')
ends_with_te = greeting.endswith('te')

is_alpha = name.isalpha()
is_digit = name.isdigit()
is_alnum = name.isalnum()
is_lower = name.islower()
is_upper = name.isupper()
is_title = name.istitle()
is_space = "   ".isspace()

formatted_string = f"{greeting}, {name}!"
formatted_with_format = "{}, {}!".format(greeting, name)
formatted_with_percent = "%s, %s!" % (greeting, name)
