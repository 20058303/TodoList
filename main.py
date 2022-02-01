from objectives import Objective


class ToDoList:
    def __init__(self):
        self.objective_list = []
        self.main_loop()

    def main_loop(self):
        print("What would you like to do?\n 1: Show all Objectives\n 2: Add new objective\n 3: Edit objective \n 4: Remove objective")
        choice = input("> ")
        if choice == "1":
            self.display_all()
        elif choice == "2":
            self.add_objective()
        elif choice == "3":
            if len(self.objective_list) > 0:
                self.edit_objective()
            else:
                print("\n ## No objectives to be edited!\n")
                self.main_loop()
        elif choice == "4":
            if len(self.objective_list) > 0:
                self.remove_objective()
            else:
                print("\n ## No objectives to be removed!\n")
                self.main_loop()
        else:
            print("\n ##Invalid input, please try again!\n")
            self.main_loop()

    def add_objective(self):
        name = ''
        description = ''
        while True:
            name = input("What do you want to name this Todo? > ")
            if len(name) > 1:
                break
            else:
                print('\n ## Name too short, please try again!\n')

        while True:
            description = input("What do you want the objective to be? > ")
            if len(description) > 1:
                break
            else:
                print('\n ## Description too short, please try again!\n')

        new_obj = Objective(name, description)
        self.objective_list.append(new_obj)
        self.main_loop()

    def edit_objective(self):
        try:
            number = input("Which objective would you like to edit? (index only) > ")
            if int(number) > len(self.objective_list):
                print("\n ## Number out of range, please try again!\n")
                self.edit_objective()
            else:
                obj_to_edit = self.objective_list[int(number)-1]
                name = obj_to_edit.name
                description = obj_to_edit.description

                name = input(f"What do you want to rename this Todo?\n (Current: {name})\n > ")

                description = input(f"What do you want the new objective to be?\n (Current: {description})\n > ")
                obj_to_edit.name = name
                obj_to_edit.description = description
                print('Updated successfully!')
                self.main_loop()

        except ValueError:
            print("\n## Input is not a number, please try again!\n")
            self.edit_objective()

    def remove_objective(self):
        try:
            number = input("Which objective would you like to remove? (index only) > ")
            if int(number) > len(self.objective_list):
                print("\n ## Number out of range, please try again!\n")
                self.remove_objective()
            else:
                self.objective_list.pop(int(number)-1)
                self.main_loop()
        except ValueError:
            print("\n## Input is not a number, please try again!\n")
            self.remove_objective()

    def display_all(self):
        print("\nAll Todo Objectives: ")
        if len(self.objective_list) > 0:
            index = 1
            for obj in self.objective_list:
                print(f" [{index}] {obj}")
                index += 1
            print("\n")
        else:
            print("\n## No objectives saved!\n")

        self.main_loop()


td = ToDoList()

