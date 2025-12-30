class User_Class:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        if character_class == "1":
            self.health = 100
        elif character_class == "2":
            self.health = 85
        elif character_class == "3":
            self.health = 75

    def stats(self):
        print(f"name: {self.name}")
        print(f"Health: {self.health}")

def class_selection():
    class_choice = input("Select an option: ")
    if class_choice in ["1", "2", "3"]:
        return class_choice
def main_menu():
    name = input("Enter your name: ")
    character_class = class_selection()

    user = User_Class(name, character_class)
    user.stats()
main_menu()
