from os import system, name
import psycopg2

sql = "INSERT INTO products(name, category) VALUES(%s,%s)"

#establishing the connection
conn = psycopg2.connect(
   database="wms", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
)

cursor = conn.cursor()

PRODUCTS_FILE = "towary.txt"
PACKING_DOCUMENTS_FILE = "wydania.txt"
PICKUP_DOCUMENTS_FILE = "przyjecia.txt"

def User_choice(section):
    global user_choice
    for n, value in enumerate(navigation[section]):
        print(str(n + 1) + ":", value) 

    user_choice = input()
    system('clear')

def Add_product(name, label, color, prize):
    product_summary = "\n" + product_name + ";" + product_label + ";" + product_color + ";" + product_prize
    with open(PRODUCTS_FILE, "a") as products:
        products.write(product_summary)

def Add_packing_document(number, client):
    product_summary = "\n" + number + ";" + client
    with open(PACKING_DOCUMENTS_FILE, "a") as products:
        products.write(product_summary)        

navigation = {"Menu":["Wydania", "Przyjecia", "Inwentaryzacja", "Towary", "Wyjscie"],
        "Wydania":["Utworz", "Zakoncz", "Wyjscie"],        
        "Przyjecia":["Utworz", "Zakoncz", "Wyjscie"],
        "Towary":["Wyswietl", "Dodaj", "Import CSV", "Cofnij"]
        }

def main_menu():
    global user_choice
    User_choice("Menu")

    if user_choice == "1":
        User_choice("Wydania")
        if user_choice == "1":
            document_number = input("Podaj numer: ")
            document_client = input("Podaj dane kontrahenta: ")
            Add_packing_document(document_number, document_client)
            main_menu()
    elif user_choice == "2":
        User_choice("Przyjecia")
    elif user_choice == "3":
        User_choice("Inwentaryzacja")    
    elif user_choice == "4":
        User_choice("Towary")
        if user_choice == "1": #view
            while True:
                system("clear")
                file_read = open(PRODUCTS_FILE, "r")
                print(file_read.read())
                user_choice = input("Q - wyjscie: ")
                if user_choice.upper() == "Q":
                    system("clear")
                    file_read.close()
                    main_menu()   
        elif user_choice == "2": #add
            product_name = input("Podaj nazwe: ")
            product_label = input("Podaj marke: ")
            product_color = input("Podaj kolor: ")
            product_prize = input("podaj cene: ")
            records_to_insert = product_name, product_label
            #Add_product(product_name, product_label, product_color, product_prize)
            cursor.execute(sql,records_to_insert)
            conn.commit()
            system("clear")    
            main_menu()
        elif user_choice == "3": #import CSV
            path = input("Podaj sciezke do pliku: ")
            file_read = open("/home/kamil/Desktop/test.txt", "r")
            file_write = open(PRODUCTS_FILE , "a")
            for line in file_read:
                file_write.write(line)
            file_read.close()
            file_write.close()
            main_menu()
        else:
            main_menu()
    elif user_choice == "5":
        exit()  

main_menu()

conn.close()