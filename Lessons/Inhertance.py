class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(animal):
    pass
class cat(animal):
    pass
class mouse(animal):
    pass

dog = dog("Toffik")
cat = cat("Alex")
mouse = mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()