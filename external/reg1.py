import re
pattern="[bat|bit|but|hat|hit|hut]{3}"

a="hathut"

if re.match(pattern, a):
    print("pass")
else:
    print("no pass")
    
    pattern = r"\b(bat|bit|but|hat|hit|hut)\b"

    test_strings = ["bat", "bit", "but", "hat", "hit", "hut", "hathut", "batman"]

    for string in test_strings:
        if re.match(pattern, string):
            print(f"{string}: pass")
        else:
            print(f"{string}: no pass")