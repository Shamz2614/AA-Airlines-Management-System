from modules.utils import load_data, save_data, clear_screen

PASSENGER_FILE = "data/passengers.json"

def menu():
    while True:
        clear_screen()
        print("=== Passenger Management ===")
        print("1. View Passengers")
        print("2. Add Passenger")
        print("3. Edit Passenger")
        print("4. Archive Passenger")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_passengers()
        elif choice == "2":
            add_passenger()
        elif choice == "3":
            edit_passenger()
        elif choice == "4":
            archive_passenger()
        elif choice == "5":
            break
        else:
            input("Invalid choice. Press Enter to continue...")

def view_passengers():
    passengers = load_data(PASSENGER_FILE)
    clear_screen()
    print("=== Passenger List ===")
    if not passengers:
        print("No passengers found.")
    else:
        for p in passengers:
            status = "Archived" if p.get("archived") else "Active"
            print(f"- {p['name']} ({status})")
    input("\nPress Enter to continue...")

def add_passenger():
    passengers = load_data(PASSENGER_FILE)
    name = input("Enter passenger name: ")
    contact = input("Enter contact info: ")
    passengers.append({"name": name, "contact": contact, "archived": False})
    save_data(PASSENGER_FILE, passengers)
    input("Passenger added successfully. Press Enter to continue...")

def edit_passenger():
    passengers = load_data(PASSENGER_FILE)
    name = input("Enter passenger name to edit: ")
    for p in passengers:
        if p["name"].lower() == name.lower():
            new_name = input(f"Enter new name ({p['name']}): ") or p["name"]
            new_contact = input(f"Enter new contact ({p['contact']}): ") or p["contact"]
            p["name"], p["contact"] = new_name, new_contact
            save_data(PASSENGER_FILE, passengers)
            input("Passenger updated successfully. Press Enter to continue...")
            return
    input("Passenger not found. Press Enter to continue...")

def archive_passenger():
    passengers = load_data(PASSENGER_FILE)
    name = input("Enter passenger name to archive: ")
    for p in passengers:
        if p["name"].lower() == name.lower():
            p["archived"] = True
            save_data(PASSENGER_FILE, passengers)
            input("Passenger archived successfully. Press Enter to continue...")
            return
    input("Passenger not found. Press Enter to continue...")
