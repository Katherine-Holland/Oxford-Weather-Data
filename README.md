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
This site has been designed to allow users to compare weather data by month in Oxford, for the years 1950 and 2022. This includes the monthly sun hours, rainfall in millimetres and the minimum and maximum temperatures. This weather data was extracted from the Met Office UK database. The site is for users who are interested in comparing weather data, such as students.

## Design
The wireframe was created using Balsamiq. 

## Features
Below are the core functions and elements I incorporated into the site.

## Google Sheets 


### Functions

![Image]()
Add in adding data to sheet

To allow the user to input weather data onto a Google Spreadsheet, you need to create a function to capture user input and write it to the correct sheet, ensuring it's validated and limited to the current month. Here's what you need to do:

Add a Menu Option to Input Data:
Update the menu to include an option for users to input new data.
Create a Function to Get User Data:
Create a function to ask the user for the required data (month, sun hours, min temp, max temp, rainfall).
Round User Inputs:
If the input is a decimal, round it to the nearest whole number.
Validate User Input:
Ensure the month is valid (between 1 and the current month), and the values are numbers.
Add Data to Google Sheet:
Write the input data to the appropriate row and column in the Google Sheet.
User testing

### Main script

Testing:
I put my main script to execute under the function and not below all the functions so compare_sun_hours threw an error of not defined.  see screenshots.

### Refactoring

![Image]() 
Testing: 

refactoring the code - Type error:
Modify compare_data Function

You should modify the compare_data function so that it doesn't expect the month as a parameter since it's getting the month inside the function already. 

Modify Calls in main() Function

Adjust the calls in the main() function to remove the unnecessary month argument, as it's now handled within compare_data

## Deployment
I deployed the site via Heroku. These are the steps I followed, using the Code Institute 'Love Sandwiches" project to guide me.
1. Within the Heroku dashboard I created a new app and called it Oxford-Weather-Data. 
2. I selected my location and created the app.
3. 




When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.
Testing:
Removed exiting as it wasnt needed from the main memu after deployment and it didn’t have a use.

## Manual Testing
1. I tested it using two popular browsers, Chrome and Firefox, both of which worked as expected.
![Console]()
2. deleting data from the sheet
bugs - exiting if yes or no is answered with the wrong words back to main screen with invalid input. 
I added a while loop to allow two attempts before defaulting to the main menu.
I added return instrqad of break to add clear exit points for the user and reduce the chance of the programme looping incorrectly.

**Pep8ci**

The site passed through validation successfully.
![pep8ci](assets/)


## Future Features
The site could be expanded into a list of locations across the U.K and the years could also be expanded across a wider range.

## Credits
My mentor Spencer Bariball.

## Images:
**Wireframe:**
https://balsamiq.com/

## Website Validators:
https://pep8ci.herokuapp.com/

## Tutorials & Advice:
https://www.w3schools.com/

Code Institute - Love Sandwiches project.

**Google Charts:**











