# Code Institute PP3

# Oxford Weather Data Comparison Tool
![mock-up]()

A Code Institute Project (PP3). Visit the live site [here](https://oxfordweatherdata-1a975addda17.herokuapp.com/).

Contents
1. [Introduction](#introduction)
2. [Design](#design)
3. [Features](#features)
4. [Manual Testing](#testing)
6. [Deployment](#deployment)
6. [Future Features](#future)
7. [Credits](#credits) 


## Introduction

**User:**
The Oxford Weather Data Comparison Tool allows users to compare monthly weather data (sun hours, rainfall, minimum and maximum temperatures) for Oxford for the years 1950 and 2022. Users can also input and delete weather data for the year 2024. 
The site is for users who are interested in comparing weather data, such as students and researchers who want insights from weather data for these years and who want to add to the data for 2024.

**Site Owner:**
The application provides data for 1950 and 2022 and allows the user to compare data. The application also allows users to input and delete new data for 2024.

This weather data was extracted from the Met Office UK database. 

## Design
This project is a command-line application, deployed via Heroku, that allows users to manage and research a weather dataset. The data is retrieved from a linked Google Sheet.

## Features
Below are the core functions and dependencies I incorporated into the site.

## Google Sheet
From my personal Google account, I created a Google Sheet and called it oxford_weather_data. I populated three worksheets. The first was a worksheet for 1950 data, the second for 2022 data and the third for the user to input or delete data for the current year (2024). I used data for this project from the Met Office station data for Oxford (link in the credits below).
The data for 1950 and 2022 cannot be modified and can only be used for research purposes. The 2024 sheet however, allows the user to add and delete data as appropriate. More information on the code functions can be found below.

**Linking the Google Sheet**
I followed the Code Institute "Love Sandwiches" tutorial to ensure my Google Sheet was linked up to my project correctly:
1) I created a new project and called it oxford_weather_data.
2) I selected API and services and then library to access the correct APIs. 
3) I first set up Googe Drive and clicked 'enable'. I generated some credentials by clicking 'create credentials'. I selected Google Drive API and the seeting 'application data'. I then created a service account name and selected 'JSON for the key type' and 'Editor' for my role. I saved the downloaded JSON file to my computer for the later stage.
3) To link up my Google Sheets API to my GitHub project I first looked for the Googlesheets API and clicked 'enable'.
4) In my Code Institute template, I dragged the JSON file into my workspace and renamed it creds.json.
5) In the JSON file I copied the client email value and went back to my Google sheet and clicked the 'share' button. I then pasted the client email into the share box and selected 'Editor' and unticked 'notify people' and then clicked share.
6) I then added the creds.JSON to the git ignore file to allow this information to be kept secure.
7) I checked the file wasn't present when I went to commit the initial project to GitHub by checking via git status before pushing to GitHub.

**Setting up the development workspace**

Within the run.py file, I used two dependencies: google-auth and the gspread library. Again, I followed the 'Love Sandwiches' tutorial to ensure I set this up correctly. 
1) I installed both of them into my workspace via the terminal using pip3 install. gspread google-auth.
2) The second stage was to add the nexessary code to the header of my .py script:

   import gspread
   from google.oauth2.service_account import Credentials
Plus I set the scope (using capitals as this is a constant variable):
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

3) I then create constant variables for the CREDS, SCOPED CREDS, then created the GSPREAD client and SHEET to allow access (making sure the sheet name matched the Google Sheet name):
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('oxford_weather_data')

4) Finally I added test data to see if the sheet was connected.

## Functions
The application includes a number of functions outlined below:

1) **display_menu()**
Purpose: Displays the menu options for the user to choose from.
Returns: The user's choice as a string, stripped of any leading or trailing whitespace.

2) **get_month_input()**
Purpose: Prompts the user to input a month number and validates the input, allowing one retry attempt.
Returns: The validated month number as an integer or None if invalid input is provided after two attempts.

3) **fetch_data(month, column)**
Purpose: Fetches weather data from the spreadsheet for a given month and column.
Parameters:
month: The month number (1-12).
column: The column number from which to fetch data.
Returns: A tuple containing the data for the specified month from 1950 and 2022 as integers, or None if the data is invalid.

4) **compare_data(data_type, column)**
Purpose: Compares weather data (e.g., sun hours, rainfall, maximum temperature, minimum temperature) between 1950 and 2022 for a specified month.
Parameters:
data_type: A string describing the type of data being compared.
column: The column number from which to fetch the data.
Behaviour: Prompts the user for a month, fetches the corresponding data, and prints a comparison between the years 1950 and 2022.

5) **input_or_delete_data()**
Purpose: Allows the user to choose whether to input new weather data or delete existing data for a specified month, with one retry attempt.
Behaviour: Prompts the user to choose an option (input or delete), validates the choice, and then calls the corresponding function to handle the data.

6) **input_weather_data(month)**
Purpose: Inputs new weather data for the year 2024 for a specified month, with one retry attempt.
Parameters:
month: The month number (1-12) for which data is to be inputted.
Behaviour: Prompts the user for new data values (sun hours, minimum temperature, maximum temperature, rainfall), validates the input, and updates the spreadsheet.

7) **delete_weather_data(month)**
Purpose: Deletes existing weather data for the year 2024 for a specified month, with one retry attempt.
Parameters:
month: The month number (1-12) for which data is to be deleted.
Behaviour: Prompts the user to confirm data deletion, validates the input, and clears the data from the spreadsheet if confirmed.

8) **main()**
Purpose: Main menu function for the user to choose from a list of options.
Behaviour: Continuously displays the main menu, takes the user's choice, and calls the appropriate function to handle the request. Validates the user's choice and prompts for re-entry if invalid.

### Refactoring
After writing my functions, I decided I could refactor the compare data function. However, this has caused an issue with the generated responses which don't always read in the correct grammar. For example "More -maximum temperature- in 2022" which doesn't read correctly although it works for "More sun hours" and "More rainfall". See testing below.

## Deployment
I deployed the site via Heroku. These are the steps I followed, using the Code Institute 'Love Sandwiches" project to guide me.
1. Within the Heroku dashboard I created a new app and called it Oxford-Weather-Data. 
2. I selected my region and created the app.
3. I went to the settings tab and entered my environment variables (config vars). This included the CREDS.json file and the PORT with the value of 8000.
4. I then added two build pack dependencies in this order: Python and NodeJs.
5. I then went to the deploy section and selected GitHub. I searched for my GitHub repository and clicked connect to link up my code.
6. I decided to manually deploy my app via deploy branch and successfully deployed it.

## Manual Testing
1. I tested it using two popular browsers, Chrome and Firefox, both of which worked as expected.
![Console]()


|Test Summary|Resolved?|Action Taken|
|---|---|---|
|Debugging  | Y |   |
| Improve user experience. Function: delete_weather_data. Issue: If exiting the menu and 'yes' or 'no' isn't typed exactly, the user is thrown out of the loop and back to the main menu. |  Y | Add a while loop to allow user two attempts before defaulting to the main menu.|
|Retrieving data with no cell value. Function: compare  Issue: If the data returns none it specifies an error   |Y   |Added to function to allow none to be displayed|
|Issue: 2024 sheet : You can overwrite data without a warning   | Y  | Added in an option for the user to respond y or n to the arning that data was about to be overriden.|
|Issue: Input or delete data function leaves loop if invalid month number is added and returns to main screen    | Y  | Added in the number of attempts the user is given to allow a second chance before returning to the main menu.  |
|Issue: Error when whitespace was added before user input| Y  | Added .strip to inputs to avoid errors and improve user experience|
| Issue: Compare data function was refactored and uses generic message '"More {data_type} in (year) however this doesn't read well for maximum and minimum temperatures | N  | Future Fix to modify general function to allow 'Hotter' and "Cooler'.|
|  Issue: Input data for 2024 or delete existing data accepts an invalid entry which isn't 1 or 2 | Y  |Added a loop which only accepts 1 or 2 as an input|
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |


## Future Features
The site could be expanded into a list of locations across the U.K and the years could also be expanded across a wider range.
**Functionality:**
1) The user data for 2024 could become immutable after a certain time limit had passed.
2) Data could be added to historical dates if new data was discovered or more columns needed to be added.
3) The user could see the results of their input in the command line after entry.
4) The user could export data via PDF for example.

## Website Validators:
https://pep8ci.herokuapp.com/

## Tutorials & Advice:
W3 Schools (Python Date Time) [Link](https://www.w3schools.com/python/python_datetime.asp)

Code Institute - Love Sandwiches project

Replit 100 days of python tutorials: [Link](https://replit.com/learn/100-days-of-python)

## Credits:
My mentor Spencer Bariball for his continued support and expertise.

The Met Office Oxford Weather Station data: [Link](https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/oxforddata.txt)



