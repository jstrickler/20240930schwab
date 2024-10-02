
function_list = []

def deco(original_function):
    function_list.append(original_function)
    return original_function

@deco
def spam():
    print("spam spam spam")

@deco
def ham():
    print("ham ham ham ham and ham")

# spam = deco(spam)

print(f"{spam = }")
print(f"{type(spam) = }")
spam()

print(f"{function_list = }")
