from os import system, name

def User_choice(section):
    global user_choice
    for n, value in enumerate(navigation[section]):
        print(str(n + 1) + ":", value) 

    user_choice = input()
    system('clear')

navigation = {"Menu":["Wydania", "Przyjecia", "Inwentaryzacja", "Wyjscie"],
        "Wydania":["Utworz", "Zakoncz", "Wyjscie"],        
        "Przyjecia":["Utworz", "Zakoncz", "Wyjscie"]
        }

User_choice("Menu")

if user_choice == "1":
    User_choice("Wydania")
elif user_choice == "2":
    User_choice("Przyjecia")



