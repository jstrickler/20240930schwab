from card import Card

c = Card('A', 'Spades')
print(c)
print(f"{c = }")
print(f"{c.rank = }")
print(f"{c.suit = }\n")

attr_name = "rank"
a = getattr(c, attr_name)
print(f"{a = }")

b = getattr(c, "serial_number", None)
print(f"{b = }")

if hasattr(c, "serial_number"):
    serial_number = getattr(c, "serial_number")
    # process number here

# if hasattr(obj, "write")
