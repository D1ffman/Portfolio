def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1, 5, 2))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Egor", "Egooor")
print(
    )

def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_adress(street="Ovchinikova", 
             city="Chelybinsk", 
             Number_home="7")