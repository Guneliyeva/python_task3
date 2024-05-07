class cartoon:
    def __init__(self, name, age, caracter, start):
        self.name = name
        self.age = age
        self.caracter = caracter
        self.start = start

    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("caracter:", self.caracter)
        print("start:", self.start)


caracter1 = cartoon("Olaf", 3, "Snowman", 2013)
caracter2 = cartoon("Garfield", 25, "Cat", 1960)
caracter3 = cartoon("Bugs Bunny", 39, "Bunny: Naber cınım", 1930)
caracter4 = cartoon("Tom and Jerry", 77, "Cat and mouse", 1940)
caracter5 = cartoon("Donald Duck", 83, "Duck", 1934)
caracter6 = cartoon("Tweety & Sylvester", 75, "Bird and cat :Bi kedi gordum sanki", 1942)
caracter7 = cartoon("Road Runner & Wile E. Coyote", 68, "Miq-miq", 1949)


print("Cartoon caracter: ")
caracter3.display()
print("Cartoon caracter:")
caracter6.display()
print("Cartoon caracter:")
caracter7.display()


def caracter_age(self):
    if self.age < 10:
        return "Child"
    elif 18<self.age < 30:
        return "Young"
    elif 30<self.age < 60:
        return "Middle age"
    else:
        return "Old Dad"


print(f"{caracter1.name} {caracter1.age} yasinda ve {caracter_age(caracter1)} sayilir")
print(f"{caracter6.name} {caracter6.age} yasinda ve {caracter_age(caracter6)} sayilir")

