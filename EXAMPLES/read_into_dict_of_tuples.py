from pprint import pprint

knight_info = {}  # create empty dict

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value

print(knight_info)
print()

pprint(knight_info)
print()

# for KEY, VALUE in DICT.items():
for name, info in knight_info.items():
    print(info[0], name)

print()
print(knight_info['Robin'])
print(knight_info['Robin'][2])
