from modules import airport_manager, passenger_manager, flight_manager, predictor
from modules.utils import clear_screen

def main_menu():
    while True:
        clear_screen()
        print("=== AA Airlines Management System ===")
        print("1. Manage Airports")
        print("2. Manage Passengers")
        print("3. Manage Flights")
        print("4. Generate Predictions")
        print("5. View Change Logs")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            airport_manager.menu()
        elif choice == "2":
            passenger_manager.menu()
        elif choice == "3":
            flight_manager.menu()
        elif choice == "4":
            predictor.menu()
        elif choice == "5":
            predictor.view_changes()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
