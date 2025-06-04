class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

def main():
    print("Animal Inheritance Example")
    my_dog = Dog("Buddy")
    my_cat = Cat("Whiskers")

    my_dog.speak()  # Output: Buddy says Woof!
    my_cat.speak()  # Output: Whiskers says Meow!

if __name__ == "__main__":
    main()
