# MS3_Umpire_Avilability

## Introduction/Description
The purpose of this app is allow teams to find available umpires in the area to attend matches
The Umpires will be able to browse a list of matches that require an umpire and see the date, time and physical location of the match.

## Project Overview
This app will allow both Netball Club representatives and Umpires to create accounts, updates password and delete accounts.
A Netball Representative will be able to create a request for an umpire for a match, the match will have a County, City, Date, Time and exact location within the rewuest. 
An Umpire will be able to view netball matches within an area or location and be able to confirm that they can attend the match.
There are assumtions made that the matches will take an hours slot and that there is a set amount that the umpire will be paid for travelling expenses

## User Experience (UX)

### Project Goals
This app that will allow clubs to create a request for an umpire for a match or matches.  There will also be an option to cancel the match if there are any issues.  This will allow umpires to view any upcoming matches that still require an umpire within the area they are currently in.

### User Stories
    1. User Story 
        * As a new club representative I need to be able to create a new login, so I can search for umpires
        * Acceptance Criteria: A new user can create a new login to be able to use the app
    2. User Story 
        * As a Club representative looking for an umpire, I need to be able to add a request for an umpire, so that the match can go ahead
        * Acceptance Criteria: A Club representative can request an umpire and receive a confirmation from an umpire to umpire the netball match
    3. User Story 
        * As an umpire I need to be able to create a new login, so I can search for matches in my area
        * Acceptance Criteria: A new user can create a new login to be able to use the app
    4. User Story 
        * As an Umpire, I need to view matches in my area, so that I can umpire the match.
        * Acceptance Criteria: A match request is visable on the app for me to confirm I am available to umpire
    5. User Story
        * As a club user, I want to be able to update my password, to ensure security of my log in to the site
        * Acceptance Criteria: Change Password option is available for me to change my password
    6. User Story
        * As an umpire, I want to be able to update my password, to ensure security of my log in to the site
        * Acceptance Criteria: Change Password option is available for me to change my password
    7. User Story
        * As a Club user, I want to be able to delete my account, if I leave the club
        * Acceptance Criteria: Ability to delete my user details
    8. User Story
        * As an umpire, I want to be able to delete my account, if I am no longer able to umpire
        * Acceptance Criteria: Ability to delete my user details

### Wire Frames
    ![Conceptial ERD] (imgs/conceptual ERD.png)
    ![logical ERD] (imgs/logical ERD.png)
    ![Physical ERD] (imgs/physical ERD.png)

## Database process
### Conceptual Design
    - 3 main databases 
        * all_users - this will hold the majority of the data, first and lastname, email address, County, City, username, password, enid which is the England Netball ID - current governing body for Netball in the UK - both players and umpires have to pay a yearly subscription to this.  The ENID will be the Primary Key and will be unique as each registered user has a unique enid.
        * umpires - this will hold details for the umpires, enid is the primary key and there will be a field for qualification of he umpire, as some matches require a specific qualification
        * matches - this will hold the details of the matches, they will have a unique auto id as the primary key.  The foreign key will be based on the user_enid and will include locations, dates and times

### Logical Design
        *all_users:
            * PK enid 
            * firstname 
            * surname 
            * email 
            * county 
            * city 
            * club 
            * umpire 
            * username 
            * password 
        * umpire :
            * PK enid 
            * firstname 
            * surname 
            * FK username 
            * county 
            * city 
            * qualification 
        * match :
            * PK id 
            * FK user_enid 
            * FK umpire_enid 
            * county 
            * city 
            * location 
            * date 
            * time 

### Physical Concept
        *all_users database fields will be:
            * PK enid numerical
            * firstname text
            * surname text
            * email text
            * county text
            * city text
            * club text
            * umpire boolean
            * username text
            * password text
        * umpire database fields will be:
            * PK enid numerical
            * firstname text
            * surname text
            * FK username text
            * county text
            * city text
            * qualification text
        * match database fields will be:
            * PK id autoincrement
            * FK user_enid text
            * FK umpire_enid text
            * county text
            * city text
            * location text
            * date date
            * time time

## Features
    - Current Features
        - Create a new user (club representative)
        - Create a new user (umpire)
        - Create a new match request
        - Confirm avilability to umpire the match
        - Delete match request (if cancelled)
    - Future Features
        - Send popup message to all umpires in an area when a new match is available

## Technologies Used
    - Visual Studio
    - GitHub
    - PostgreSQL
    - Python


## Testing
## Local Developement Set Up
    1. MS3 VS set up
        * Logged onto Visual Studio
            * created a new folder MS3_Umpire_Avilability
            * opened the folder in VS
        * logged into GitHub and created a new repository MS3_Umpire_Availability
            * copied the code to set up on vs
        * Navigated back to VS and pasted this into terminal
            * confirmed the readme file is now available in GitHub
        * Visual Studio
            * installed Python
            * Installed Django
            * Installed venv
            * Installed PostgreSQL
## Live Development
### screenshots
## Credits
ERD diagrams were created using Lucid (https://lucid.app/)
postgreSQL

