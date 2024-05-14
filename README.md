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
This application has been designed to allow users to compare weather data by month in Oxford, for the years 1950 and 2022. This includes the monthly sun hours, rainfall in millimetres and the minimum and maximum temperatures. This weather data was extracted from the Met Office UK database. The site is for users who are interested in comparing weather data, such as students and researchers who want insights from weather data for these years and who want to add to the data for 2024.
**Site Owner:**
The application provides data for 1950 and 2022 and allows the user to compare data. The application also allows users to input and delete new data for 2024.

## Design
This project is a command-line application, deployed via Heroku, that allows users to manage and research a weather dataset. The data is retrieved from linked Google Sheets.

## Features
Below are the core functions and elements I incorporated into the site.

## Google Sheets 
I followed the Code Institute "Love Sandwiches" tutorial to ensure my Google Sheet was linked up to my project correctly. I have three sheets within the data set: 1950, 2022 and the current year 2024. The data for 1950 and 2022 cannot be modified and can only be used for research purposes. The 2024 sheet however, allows the user to add and delete data as appropriate. More information on the code functions can be found below.

### Functions
The application includes a number of functions outlined below:
1. Display menu
2. Get month input
3. Fetch data
4. Compare data
5. Input or delete data
6. Input weather data
7. Delete weather data

![Image]()


### Main script

Testing:
I put my main script to execute under the function and not below all the functions so compare_sun_hours threw an error of not defined.  see screenshots.

### Refactoring

![Image]() 


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


|Test Summary|Resolved?|Action Taken|
|---|---|---|
|EXAMPLE Issue with chart  |  Y |  Modified code |
| Improve user experience. Function: delete_weather_data. Issue: If exiting the menu and 'yes' or 'no' isn't typed exactly, the user is thrown out of the loop and back to the main menu. |  Y | Add a while loop to allow user two attempts before defaulting to the main menu.|
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
Type error:
During refactoring the code bug: Modify compare_data Function

modify the compare_data function so that it doesn't expect the month as a parameter since it's getting the month inside the function already. 

Modify Calls in main() Function

Adjust the calls in the main() function to remove the unnecessary month argument, as it's now handled within compare_data

## Future Features
The site could be expanded into a list of locations across the U.K and the years could also be expanded across a wider range.

## Website Validators:
https://pep8ci.herokuapp.com/

## Tutorials & Advice:
https://www.w3schools.com/

Code Institute - Love Sandwiches project.

Google Charts

## Credits
My mentor Spencer Bariball.




