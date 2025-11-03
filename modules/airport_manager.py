import os
from modules.utils import load_data, save_data, clear_screen

AIRPORT_FILE = "data/airports.json"

def menu():
    while True:
        clear_screen()
        print("=== Airport Management ===")
        print("1. View Airports")
        print("2. Add Airport")
        print("3. Edit Airport")
        print("4. Delete Airport")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_airports()
        elif choice == "2":
            add_airport()
        elif choice == "3":
            edit_airport()
        elif choice == "4":
            delete_airport()
        elif choice == "5":
            break
        else:
            input("Invalid choice. Press Enter to continue...")

def view_airports():
    airports = load_data(AIRPORT_FILE)
    clear_screen()
    print("=== Airport Codes ===")
    if not airports:
        print("No airport codes found.")
    else:
        for a in airports:
            print(f"- {a['code']}: {a['name']}")
    input("\nPress Enter to continue...")

def add_airport():
    airports = load_data(AIRPORT_FILE)
    code = input("Enter new airport code (e.g., PPS): ").upper()
    name = input("Enter airport name: ")
    airports.append({"code": code, "name": name})
    save_data(AIRPORT_FILE, airports)
    input("Airport added successfully. Press Enter to continue...")

def edit_airport():
    airports = load_data(AIRPORT_FILE)
    code = input("Enter airport code to edit: ").upper()
    for a in airports:
        if a["code"] == code:
            new_name = input(f"Enter new name for {code} ({a['name']}): ")
            a["name"] = new_name
            save_data(AIRPORT_FILE, airports)
            input("Airport updated successfully. Press Enter to continue...")
            return
    input("Airport not found. Press Enter to continue...")

def delete_airport():
    airports = load_data(AIRPORT_FILE)
    code = input("Enter airport code to delete: ").upper()
    airports = [a for a in airports if a["code"] != code]
    save_data(AIRPORT_FILE, airports)
    input("Airport deleted (if it existed). Press Enter to continue...")
