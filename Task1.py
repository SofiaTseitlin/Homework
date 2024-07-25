import random
class Animal:
    def __init__(self, species, size, diet, habitat, lifespan, sex, satiety=100, age=14):
        self.species = species
        self.size = size
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.sex = sex
        self.satiety = satiety
        self.age = age

    def __repr__(self):
        return f'Вид: {self.species}, Размер: {self.size}, Тип питания: {self.diet}, Среда обитания: {self.habitat},' \
               f'Продолжительность жизни: {self.lifespan}, Возраст: {self.age}, Сытость: {self.satiety}, Пол: {self.sex}\n'


class Ecosystem:
    def __init__(self, animals = [], plant_food = 100):
        self.animals = animals
        self.plant_food = plant_food

    def __repr__(self):
        return f'Животные:\n {self.animals}'

    def add_animal(self, animal):
        self.animals.append(animal)

    def change_plant_food(self, raise_plant_food):
        self.plant_food += raise_plant_food

    def dead_animale(self):
        dead_animals = []
        alive_animals = []
        for i in range(len(self.animals)):
            self.animals[i].age += 1
            if self.animals[i].age == self.animals[i].lifespan:
                if self.animals[i].size == "Крупный":
                    ecosystem.change_plant_food(30)
                elif self.animals[i].size == "Средний":
                    ecosystem.change_plant_food(20)
                else:
                    ecosystem.change_plant_food(10)
                dead_animals.append(self.animals[i])
        for element in self.animals:
            if element not in dead_animals:
                alive_animals.append(element)
        self.animals = alive_animals

    def change_year(self):
        dead_animals = []
        alive_animals = []
        for i in range(len(self.animals)):
            self.animals[i].age += 1
            if self.animals[i].age == self.animals[i].lifespan:
                if self.animals[i].size == "Крупный":
                    ecosystem.change_plant_food(30)
                elif self.animals[i].size == "Средний":
                    ecosystem.change_plant_food(20)
                else:
                    ecosystem.change_plant_food(10)
                dead_animals.append(self.animals[i])
        for element in self.animals:
            if element not in dead_animals:
                alive_animals.append(element)
        self.animals = alive_animals
        for element in self.animals:
            if element.diet == "Растительная пища" and self.plant_food > 0:
                self.plant_food -= 1
                element.satiety += 26
            else:
                element.satiety -= 9
        print(self.animals)
        for element in self.animals:
            if element.diet == "Плотоядный":
                if random.randrange(0, 2) >= 0.5:
                    eaten_animal = random.choice(self.animals)
                    if eaten_animal.habitat == element.habitat and eaten_animal.diet == "Растительная пища":
                        element.satiety += 53
                        self.animals.remove(eaten_animal)
                else:
                    element.satiety -= 16
        for element in self.animals:
            if element.satiety < 10:
                self.animals.remove(element)




    def reproduction(self, animal1, animal2):
        if animal1.species == animal2.species and animal1.sex != animal2.sex:
            if animal1.habitat == "Вода"  and animal2.habitat == "Вода" and animal1.satiety > 50 and animal2.satiety > 50:
                for i in range(5):
                    animal = Animal(animal1.species, animal1.size, animal1.diet, animal1.habitat, animal1.lifespan, "м", 23, 0)
                    self.add_animal(animal)
                for i in range(5):
                    animal = Animal(animal1.species, animal1.size, animal1.diet, animal1.habitat, animal1.lifespan, "ж", 23, 0)
                    self.add_animal(animal)
            elif animal1.habitat == "Воздух" and animal2.habitat == "Воздух" and animal1.satiety > 42 and animal2.satiety > 42 and animal1.age > 3 and animal2.age > 3:
                for i in range(2):
                    animal = Animal(animal1.species, animal1.size, animal1.diet, animal1.habitat, animal1.lifespan, "м", 64, 0)
                for i in range(2):
                    animal = Animal(animal1.species, animal1.size, animal1.diet, animal1.habitat, animal1.lifespan, "ж", 64, 0)
                    self.add_animal(animal)
            elif animal1.habitat == "Земля" and animal2.habitat == "Земля" and animal1.satiety > 20 and animal2.satiety > 20 and animal1.age > 5 and animal2.age > 5:
                animal = Animal(animal1.species, animal1.size, animal1.diet, animal1.habitat, animal1.lifespan, "м", 73, 0)
                self.add_animal(animal)
                animal = Animal(animal1.species, animal1.size, animal1.diet, animal1.habitat, animal1.lifespan, "ж", 73, 0)
                self.add_animal(animal)
        else:
            print('Животные не подходят')


current_animals = []
current_animals.append(Animal("Тигр", "Крупный", "Плотоядный", "Земля", 15, "м"))
current_animals.append(Animal("Тигр", "Крупный", "Плотоядный", "Земля", 15, "ж"))
current_animals.append(Animal("Ястреб", "Средний", "Плотоядный", "Воздух", 18, "м"))
current_animals.append(Animal("Ястреб", "Средний", "Плотоядный", "Воздух", 18, "ж"))
current_animals.append(Animal("Акула", "Крупный", "Плотоядный", "Вода", 30, "м"))
current_animals.append(Animal("Акула", "Крупный", "Плотоядный", "Вода", 30, "ж"))
current_animals.append(Animal("Жираф", "Крупный", "Растительная пища", "Земля", 25, "м"))
current_animals.append(Animal("Жираф", "Крупный", "Растительная пища", "Земля", 25, "ж"))
current_animals.append(Animal("Попугай", "Маленький", "Всеядный", "Воздух", 50, "м"))
current_animals.append(Animal("Попугай", "Маленький", "Всеядный", "Воздух", 50, "ж"))
current_animals.append(Animal("Черепаха", "Средний", "Растительная пища", "Вода", 80, "м"))
current_animals.append(Animal("Черепаха", "Средний", "Растительная пища", "Вода", 80, "ж"))

ecosystem = Ecosystem(current_animals, 1000)

print(ecosystem)
answer = ''
while answer != 'выйти':
    print("Хотите добавить животное? Если да, введите'добавить особь'")
    print("Хотите добавить количество растительной пищи? Если да, введите 'добавить количество растительной пищи'")
    print("Хотите просмотреть текущие характеристики каждой особи? Если да, введите 'просмотреть текущие характеристики каждой особи'")
    print("Хотите смоделировать процесс размножения особей одного вида? Если да, введите 'смоделировать процесс размножения особей'")
    print("Хотите смоделировать движение времени на 1 единицу? Если да, введите 'смоделировать движение времени'")
    print("Хотите завершить игру? Введите 'выйти'")
    answer = input()
    if answer == 'добавить особь':
        species = input("Введите название особи: ")
        size = input("Введите размер особи: ")
        diet = input("Введите тип питания особи: ")
        habitat = input("Введите среду обитания особи: ")
        lifespan = input("Введите продолжительность жизни особи: ")
        sex = input("Введите пол особи: ")
        ecosystem.add_animal(Animal(species, size, diet, habitat, lifespan, sex))
        print("Животное добавлено")
    elif answer == 'добавить количество растительной пищи':
        raise_plant_food = int(input("Введите увеличение колиества пищи: "))
        ecosystem.change_plant_food(raise_plant_food)
        print(f'Количество растительной пищи на данный момент составляет: {ecosystem.plant_food}')
    elif answer == 'просмотреть текущие характеристики каждой особи':
        print(ecosystem)
    elif answer == 'смоделировать процесс размножения особей':
        print(ecosystem)
        animal1 = ecosystem.animals[int(input("Введите номер животного из списка: ")) - 1]
        animal2 = ecosystem.animals[int(input("Введите номер животного из списка: ")) - 1]
        ecosystem.reproduction(animal1, animal2)
        print(ecosystem)
    elif answer == 'смоделировать движение времени':
        ecosystem.change_year()