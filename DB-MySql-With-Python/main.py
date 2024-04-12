from services import database
import os

def view_menu(db):
    print("- APLIKASI DATABASE PYTHON -")
    print("1. Add Data")
    print("2. Update Data")
    print("3. Show Data")
    print("4. Search Data")
    print("5. Delete Data")
    print("6. Exit Program")
    menu = input("Select Menu : ")

    # os.system('cls' if os.name == 'nt' else 'clear')

    if menu == "1":
        database.insertData(db)
    elif menu == "2":
        database.updateData(db)
    elif menu == "3":
        database.showData(db)
    elif menu == "4":
        database.searchData(db)
    elif menu == "5":
        database.deleteData(db)
    elif menu == "6":
        print("Program Berhenti, Terimakasih!")
        exit()
    else:
        print("Inputan tidak valid, Coba Lagi!")

def main():
    db = database.connect_to_db()
    view_menu(db)

if __name__ == "__main__":
    while True:
        main()