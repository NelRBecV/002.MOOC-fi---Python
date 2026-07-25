# Write your solution here:
class MagicPotion:
    """Creates a magic potion recipe."""
  
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []
 
    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))
 
    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")
 
class SecretMagicPotion(MagicPotion):
    """Creates a magic potion recipe protected by password."""
  
    def __init__(self,name: str, password: str):
        super().__init__(name)        
        self._password = password
        
    def check_password(self, pwrd:str):
        if pwrd == self._password:
            return True
        return False
    
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if self.check_password(password):
            self._ingredients.append((ingredient,amount,password))
        else:
            raise ValueError("wrong password!!!")
    
    def print_recipe(self, password: str):
        if self.check_password(password):
            super().print_recipe()
        else:
            raise ValueError("wrong password!!!")
 
if __name__ == "__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")
 
    diminuendo.print_recipe("pocushocus") # WRONG password!



