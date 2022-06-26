# Data Pipeline

This is the web scraper project that employs the scraper on the Amazon website and collects data for the specified product. iPhone 13 data has been scraped from the Amazon website.

The project uses Python, Selenium, Chromedrive, AWS S3, AWS RDS to perform the above.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)



## General Information
- The Amazon website is one of very well known and the most used website in the world.
- There are many manufacturers, influencers, entrepreneurs etc. who would like to sell their products around world. 
- The sellers would use the informtion they gained from the website to grow their business.


## Technologies Used
- Python 3.10.4
- Chromedriver 101.0.4951.41 
- Chrome 101.0.4951.67
- AWS S3 (in progress)
- AWS RDS (in progress)
- Docker (in progress)
- Postgresql (in progress)



## Features
List the ready features here:
- ability to accept cookies
- selection of required options
- data file as json and excel file will be created, uploaded to AWS S3 bucket and to Postgres RDS


## Screenshots
section _in progress_


## Setup
The required libraries are:
- selenium / webdriver
- time
- os
- uuid
- psycopg2
- pandas
- unittest
- boto3
- sqlalchemy


Required additional modules:
- import config: xpath constants, input RDS credentials
- test_Amazon.py script which carries out the unittest.


## Usage
1. The code gives an option for the user to enter required item on the search box.

2. The code scrapes first image of each item on the website.

3. Selenium drive is used to control the link(s).


## Project Status
Project is: _in progress_ 


## Room for Improvement
Room for improvement:
- More product information can be scraped depending on user's preference.
- The scraped data can be emailed to user immediately after completion of the operation.

To do:
- Creating GUI for user to use the webscraper easily.
- Implementing the webscraper interface to a website.


## Acknowledgements
- This project was given by AiCore program as a data collection pipeline project.


## Contact
Created by [@mansurcan](mansurcan@gmail.com) - feel free to contact me!

