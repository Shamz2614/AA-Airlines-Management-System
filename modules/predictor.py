from modules.utils import load_data, save_data, clear_screen
from datetime import datetime, timedelta
import random

PREDICTION_FILE = "data/predictions.json"
CHANGE_LOG = "data/changes_log.txt"

def menu():
    while True:
        clear_screen()
        print("=== Flight Prediction System ===")
        print("1. Generate Predictions")
        print("2. View Predictions")
        print("3. Record Change (+5% Modifier)")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_predictions()
        elif choice == "2":
            view_predictions()
        elif choice == "3":
            record_change()
        elif choice == "4":
            break
        else:
            input("Invalid choice. Press Enter to continue...")

def generate_predictions():
    predictions = load_data(PREDICTION_FILE)
    name = input("Enter customer name: ")

    today = datetime.now()
    for i in range(1, 6): 
        date = today + timedelta(days=365 * i)
        arrival_percent = random.randint(50, 75)
        departure_percent = random.randint(50, 75)
        predictions.append({
            "name": name,
            "date": date.strftime("%Y-%m-%d"),
            "arrival%": arrival_percent,
            "departure%": departure_percent
        })
    save_data(PREDICTION_FILE, predictions)
    input("Predictions generated successfully. Press Enter to continue...")

def view_predictions():
    predictions = load_data(PREDICTION_FILE)
    clear_screen()
    print("=== Stored Flight Predictions ===")
    if not predictions:
        print("No predictions found.")
    else:
        for p in predictions:
            print(f"{p['name']} | {p['date']} | Arrival: {p['arrival%']}% | Departure: {p['departure%']}%")
    input("\nPress Enter to continue...")

def record_change():
    modifier = input("Enter new +% modifier value: ")
    with open(CHANGE_LOG, "a") as f:
        f.write(f"{datetime.now()} - Modified prediction percentage to +{modifier}%\n")
    input("Change recorded successfully. Press Enter to continue...")

def view_changes():
    clear_screen()
    print("=== Change Log ===\n")
    try:
        with open(CHANGE_LOG, "r") as f:
            print(f.read() or "No changes recorded.")
    except FileNotFoundError:
        print("No change log found.")
    input("\nPress Enter to continue...")
