import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime  # To get the current month

# Set up the connection to Google Sheets
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
               "4. Compare minimum temperature", "5. Input new weather data for 2024", "6. Exit"]
    for option in options:
        print(option)
    return input("Enter your choice (1-6):\n ")

def get_month_input():
    """Get and validate month input from the user."""
    try:
        month = int(input("Please input a month number (1-12):\n "))
        current_month = datetime.now().month  # Get the current month
        if 1 <= month <= current_month:
            return month
        else:
            print(f"Invalid month. Please enter a number between 1 and {current_month}.")
            return None
    except ValueError:
        print("Please enter a valid number for month.")
        return None

def fetch_data(month, column):
    """Fetch the data from the spreadsheet for a given month and column."""
    try:
        sheet_1950 = SHEET.worksheet("1950")
        sheet_2022 = SHEET.worksheet("2022")
        row_index = month + 1  # Adjusted for header row
        data_1950 = int(sheet_1950.cell(row_index, column).value)
        data_2022 = int(sheet_2022.cell(row_index, column).value)
        return data_1950, data_2022
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return None, None

def compare_data(data_type, column):
    """General function comparing weather data."""
    month = get_month_input()
    if month is None:
        return
    month_name = MONTH_NAMES[month - 1]

    data_1950, data_2022 = fetch_data(month, column)
    if data_1950 is None:  # If fetching data has failed
        return

    print(f"\n{data_type.capitalize()} in {month_name} 1950: {data_1950}")
    print(f"{data_type.capitalize()} in {month_name} 2022: {data_2022}")
    
    if data_1950 < data_2022:
        print(f"More {data_type} in 2022.")
    elif data_1950 > data_2022:
        print(f"More {data_type} in 1950.")
    else:
        print(f"The {data_type} is the same in both years.")

def input_weather_data():
    """Function to input new weather data for 2024."""
    month = get_month_input()
    if month is None:
        return

    # Ask for input and round to the nearest whole number
    try:
        sun_hours = round(float(input("Enter sun hours: ")))
        min_temp = round(float(input("Enter minimum temperature: ")))
        max_temp = round(float(input("Enter maximum temperature: ")))
        rain_mm = round(float(input("Enter rainfall in mm: ")))

        # Access the 2024 sheet
        sheet_2024 = SHEET.worksheet("2024")
        row_index = month + 1  # Adjusting for the header row

        # Write the data to the appropriate row
        sheet_2024.update_cell(row_index, 2, max_temp)  # Maximum temperature in column B
        sheet_2024.update_cell(row_index, 3, min_temp)  # Minimum temperature in column C
        sheet_2024.update_cell(row_index, 4, rain_mm)  # Rainfall in mm in column D
        sheet_2024.update_cell(row_index, 5, sun_hours)  # Sun hours in column E

        print("Data successfully added to the 2024 sheet.")
    except ValueError:
        print("Please enter valid numerical values.")
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
            input_weather_data()  # New option to input weather data
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
