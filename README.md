# Code Institute PP3

# Oxford Weather Data
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
This application has been designed to allow users to compare weather data by month in Oxford, for the years 1950 and 2022. This includes the monthly sun hours, rainfall in millimetres and the minimum and maximum temperatures. 
This weather data was extracted from the Met Office UK database. 
The site is for users who are interested in comparing weather data, such as students and researchers who want insights from weather data for these years and who want to add to the data for 2024.

**Site Owner:**
The application provides data for 1950 and 2022 and allows the user to compare data. The application also allows users to input and delete new data for 2024.

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

### Functions
The application includes a number of functions outlined below:
1. Display menu
2. Get month input
3. Fetch data
4. Compare data
5. Input or delete data

6. Input weather data
I added in a line of code to the top of mu run.py file: 
from datetime import datetime 
This allowed me to set the date to allow for the user to only be able to inut data up to the current month.

7. Delete weather data

![Image]()


### Main script

Testing:
I put my main script to execute under the function and not below all the functions so compare_sun_hours threw an error of not defined.  see screenshots.

### Refactoring

![Image]() 
Type error:
During refactoring the code bug: Modify compare_data Function

modify the compare_data function so that it doesn't expect the month as a parameter since it's getting the month inside the function already. 

Modify Calls in main() Function

Adjust the calls in the main() function to remove the unnecessary month argument, as it's now handled within compare_data

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

## Website Validators:
https://pep8ci.herokuapp.com/

## Tutorials & Advice:
https://www.w3schools.com/

Code Institute - Love Sandwiches project.
Replit 100 days of python tutorials
Google Sheet

## Credits
My mentor Spencer Bariball for his continued support and expertise.

The Met Office Oxford Weather Station data: [Link](https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/oxforddata.txt)



