import gspread
from google.oauth2.service_account import Credentials

# Google Sheets API setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('oxford_weather_data')

def compare_sun_hours():
    """
    Asks the user to input a month number and compares sun hours of that month for the years 1950 and 2022.
    """
    print("Please input a month number to compare sun hours for 1950 and 2022.")
    print("Example: January would be entered as 1, February as 2, etc.")
    try:
        month = int(input("Enter the month number (1-12): "))
        if not 1 <= month <= 12:
            print("Invalid month. Please enter a number between 1 and 12.")
            return

        # Access worksheets for both years
        sheet_1950 = SHEET.worksheet("1950")
        sheet_2022 = SHEET.worksheet("2022")

        # Fetch sun hours for the given month from each sheet
        # Google Sheets header text is on line 1 s0 add 1 to row index because of header row.
        # Sun hours are in column E (column 5).
        row_index = month + 1
        sun_hours_1950 = int(sheet_1950.cell(row_index, 5).value) 
        sun_hours_2022 = int(sheet_2022.cell(row_index, 5).value)  

        # Print comparison
        print(f"Sun hours in {month} 1950: {sun_hours_1950} hours")
        print(f"Sun hours in {month} 2022: {sun_hours_2022} hours")
        if sun_hours_1950 < sun_hours_2022:
            print(f"More sun hours in 2022 ({sun_hours_2022} hours) than in 1950 ({sun_hours_1950} hours).")
        elif sun_hours_1950 > sun_hours_2022:
            print(f"More sun hours in 1950 ({sun_hours_1950} hours) than in 2022 ({sun_hours_2022} hours).")
        else:
            print("Sun hours are the same in both years.")
    except ValueError:
        print("Please enter a valid integer.")
        #If there is an error with the execution (eg. Retrieving the Google spreadsheet)
    except Exception as e:
        print(f"An error occurred: {e}")

# Script is executed directly not via another script
if __name__ == "__main__":
    compare_sun_hours()
