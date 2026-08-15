#function    

#def name(x, price):
 #   print(f"qq {x}")
  #  print("who u?")
 #   print(f"u price? {price}")

#name("Egor", 30)
#name("joe", 20)




#def display_invoice(name, amount, due_data):
 #   print(f"hello {name}")
    #print(f"u bill of ${amount:.2f} is due {due_data}")
    #print()

#display_invoice("Egor", 43.2222, "01.01")
#display_invoice("Jor", 43.2222, "01.01")
#display_invoice("Igor", 43.2222, "01.01")


#return

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def mult(x, y):
    z = x * y
    return z

def dele(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(mult(21, 3))
print(dele(5, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

ful_name = create_name("Egor", "GG")

print(ful_name)