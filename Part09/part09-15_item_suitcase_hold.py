# Write your solution here:
class Item:
    def __init__(self,name,weight):
        self.__name = name
        self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
 
    def name(self):
        return self.__name
 
    def weight(self):
        return self.__weight
 
class Suitcase:
    def __init__(self,max_weight:int):
        self.__max_weight = max_weight
        self.__items = {}
 
    def add_item(self, item:Item):
        weight = 0
        for obj, weigh in self.__items.items():
            weight += weigh
        if (weight + item.weight()) < self.__max_weight:
            self.__items[item] = item.weight()
    
    def __str__(self):
        sing = "item" if len(self.__items) == 1 else "items"
        return f"{len(self.__items)} {sing} ({sum(self.__items.values())} kg)"
 
    def weight(self):
        return sum(self.__items.values())
    
    def print_items(self):
        for i in self.__items.keys():
            print(i)
 
    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        max_weight = max(self.__items.values())
        for obj, weight in self.__items.items():
            if weight == max_weight:
                return obj 
 
class CargoHold:
    def __init__(self,max_weight):
            self.__max_weight = max_weight
            self.__cargo = []
 
    def add_suitcase(self, suit_case:Suitcase):
        weight = 0
        for w in self.__cargo:
            weight += w.weight()
        if (weight + suit_case.weight()) < self.__max_weight:
            self.__cargo.append(suit_case)
 
    def __str__(self):
        sing = "suitcase" if len(self.__cargo) == 1 else "suitcases"
        weight = 0
        for weigh in self.__cargo:
            weight += weigh.weight()
        space = self.__max_weight - weight
        return f"{len(self.__cargo)} {sing}, space for {space} kg"
 
    def print_items(self):
        for item in self.__cargo:
            item.print_items()
 
if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)
 
    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)
 
    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)
 
    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)
 
    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()



