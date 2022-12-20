from os import system, name

def User_choice(section):
    global user_choice
    for n, value in enumerate(navigation[section]):
        print(str(n + 1) + ":", value) 

    user_choice = input()
    system('clear')

navigation = {"Menu":["Wydania", "Przyjecia", "Inwentaryzacja", "Towary", "Wyjscie"],
        "Wydania":["Utworz", "Zakoncz", "Wyjscie"],        
        "Przyjecia":["Utworz", "Zakoncz", "Wyjscie"],
        "Towary":["Wyswietl", "Dodaj", "Import CSV", "Cofnij"]
        }

User_choice("Menu")

if user_choice == "1":
    User_choice("Wydania")
elif user_choice == "2":
    User_choice("Przyjecia")
elif user_choice == "3":
    User_choice("Inwentaryzacja")    
elif user_choice == "4":
    User_choice("Towary")
    if user_choice == "1":
        file_read = open("towary.txt", "r")
        print(file_read.read())
        file_read.close()
        input()
    elif user_choice == "3":
        path = input("Podaj sciezke do pliku: ")
        file_read = open("/home/kamil/Desktop/test.txt", "r")
        file_write = open("towary.txt", "a")
        
        for line in file_read:
            file_write.write(line)

        file_read.close()
        file_write.close()    
elif user_choice == "5":
    exit()    

