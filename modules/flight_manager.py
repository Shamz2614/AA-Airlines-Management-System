from modules.utils import load_data, save_data, clear_screen
from datetime import datetime

FLIGHT_FILE = "data/flights.json"

def menu():
    while True:
        clear_screen()
        print("=== Flight Management ===")
        print("1. View Flights")
        print("2. Add Flight")
        print("3. Edit Flight")
        print("4. Archive Flight")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_flights()
        elif choice == "2":
            add_flight()
        elif choice == "3":
            edit_flight()
        elif choice == "4":
            archive_flight()
        elif choice == "5":
            break
        else:
            input("Invalid choice. Press Enter to continue...")

def view_flights():
    flights = load_data(FLIGHT_FILE)
    clear_screen()
    print("=== Flight Records ===")
    if not flights:
        print("No flight records found.")
    else:
        for f in flights:
            status = "Archived" if f.get("archived") else "Active"
            print(f"{f['passenger']} | {f['departure']} → {f['arrival']} | {f['date']} | {status}")
    input("\nPress Enter to continue...")

def add_flight():
    flights = load_data(FLIGHT_FILE)
    passenger = input("Enter passenger name: ")
    departure = input("Enter departure airport code: ").upper()
    arrival = input("Enter arrival airport code: ").upper()
    date = input("Enter date/time (YYYY(Year)-MM(Month)-DD(Day) HH(Hour):MM(Minutes)): ")

    try:
        datetime.strptime(date, "%Y-%m-%d %H:%M")
    except ValueError:
        input("Invalid date format. Press Enter to continue...")
        return

    flights.append({
        "passenger": passenger,
        "departure": departure,
        "arrival": arrival,
        "date": date,
        "archived": False
    })
    save_data(FLIGHT_FILE, flights)
    input("Flight added successfully. Press Enter to continue...")

def edit_flight():
    flights = load_data(FLIGHT_FILE)
    passenger = input("Enter passenger name of flight to edit: ")

    for f in flights:
        if f["passenger"].lower() == passenger.lower():
            new_departure = input(f"New departure ({f['departure']}): ") or f["departure"]
            new_arrival = input(f"New arrival ({f['arrival']}): ") or f["arrival"]
            new_date = input(f"New date ({f['date']}): ") or f["date"]
            f["departure"], f["arrival"], f["date"] = new_departure, new_arrival, new_date
            save_data(FLIGHT_FILE, flights)
            input("Flight updated successfully. Press Enter to continue...")
            return
    input("Flight not found. Press Enter to continue...")

def archive_flight():
    flights = load_data(FLIGHT_FILE)
    passenger = input("Enter passenger name of flight to archive: ")
    for f in flights:
        if f["passenger"].lower() == passenger.lower():
            f["archived"] = True
            save_data(FLIGHT_FILE, flights)
            input("Flight archived successfully. Press Enter to continue...")
            return
    input("Flight not found. Press Enter to continue...")
