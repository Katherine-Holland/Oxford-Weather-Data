import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime  # To get the current month

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('oxford_weather_data')

# List of month names for conversion
MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

def display_menu():
    """Display the menu options for the user to choose."""
    print("\nWelcome to the Oxford Weather comparison tool. Please select an option:")
    options = ["1. Compare sun hours", "2. Compare rainfall", "3. Compare maximum temperature",
               "4. Compare minimum temperature", "5. Input or delete weather data for 2024"]
    for option in options:
        print(option)
    return input("Enter your choice (1-5):\n ")

def get_month_input():
    """Get and validate month input from the user."""
    try:
        month = int(input("Please input a month number (1-12):\n "))
        current_month = datetime.now().month  # Get the current month
        if 1 <= month <= current_month:
            return month
        else:
            print(f"That month is in the future! Please enter a number between 1 and {current_month}.")
            return None
    except ValueError:
        print("Please enter a valid number for month.")
        return None

def input_or_delete_data():
    """Choose whether to input or delete data for a month."""
    print("\n1. Input new data\n2. Delete existing data")
    choice = input("Choose an option (1-2):\n ")
    month = get_month_input()
    if month is None:
        return
    if choice == '1':
        input_weather_data(month)
    elif choice == '2':
        delete_weather_data(month)
    else:
        print("Invalid choice. Please enter 1 or 2.")

def input_weather_data(month):
    """Function to input new weather data for 2024, for a specified month."""
    try:
        sun_hours = round(float(input("Enter sun hours: ")))
        min_temp = round(float(input("Enter minimum temperature: ")))
        max_temp = round(float(input("Enter maximum temperature: ")))
        rain_mm = round(float(input("Enter rainfall in mm: ")))

        sheet_2024 = SHEET.worksheet("2024")
        row_index = month + 1

        sheet_2024.update_cell(row_index, 2, max_temp)
        sheet_2024.update_cell(row_index, 3, min_temp)
        sheet_2024.update_cell(row_index, 4, rain_mm)
        sheet_2024.update_cell(row_index, 5, sun_hours)

        print("Data successfully added for {} 2024.".format(MONTH_NAMES[month-1]))
    except ValueError:
        print("Please enter valid numerical values.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_weather_data(month):
    """Function to delete existing weather data for 2024, for a specified month."""
    try:
        sheet_2024 = SHEET.worksheet("2024")
        row_index = month + 1

        # Clearing data from the row
        sheet_2024.update_cell(row_index, 2, "")
        sheet_2024.update_cell(row_index, 3, "")
        sheet_2024.update_cell(row_index, 4, "")
        sheet_2024.update_cell(row_index, 5, "")

        print("Data successfully deleted for {} 2024.".format(MONTH_NAMES[month-1]))
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            compare_data("sun hours", 5)
        elif choice == '2':
            compare_data("rainfall", 4)
        elif choice == '3':
            compare_data("maximum temperature", 2)
        elif choice == '4':
            compare_data("minimum temperature", 3)
        elif choice == '5':
            input_or_delete_data()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

