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


### Main script


### Refactoring

![Image]() 


## Deployment
I deployed the site via Heroku. 
When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.


## Manual Testing
1. I tested it using two popular browsers, Chrome and Firefox, both of which worked as expected.
![Console]()


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
