class Person:
    def __init__(self, name, surname, age, height, weight, blood_group):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.blood_group = blood_group

    def introduce(self):
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Age:", self.age)
        print("Height:", self.height, "cm")
        print("Weight:", self.weight, "kg")
        print("Blood Group:", self.blood_group)


# Creating an object
person1 = Person(
    "Muhammed",
    "Suenu",
    20,
    175,
    70,
    "O+"
)

# Display the person's information
person1.introduce()