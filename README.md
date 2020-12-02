# Formula-1-driver-consistency

In formula 1, consistency is the key to winning championships for the top drivers/teams and to earning one-off podiums for midfield teams when the top runners make mistakes (case in point: the 2020 Italian grand prix). 

So who is the most consistent driver? I would like to propose that the best way to answer this is to look at the distribution of lap times throughout a race. A smaller spread of lap times should equate to a more consistent driver. To get the most accurate picture, we should look at this spread over the course of an entire season. We'll then analyze the variances of the variances and perform the appropriate hypothesis testing to see how confidently we can identify the most consistent driver. 

This project is broken down into 4 jupyter notebooks: 

### 1) Database Initialization
I decided to use this project as an excuse to practice SQL queries, so this is where we convert the CSV files into the postgresql database that will be queried. 

### 2) Formula 1 Driver Consistency 
This is the "main" notebook of the project. This one features the lap time distributions for each race in the 2019 season and distribution of the coefficients of variation for each driver during the whole season. In a future update, I will include a section on hypothesis testing.

### 3) Lap time distributions (2015-2020)
As the title suggests- these are the lap time distributions for the last 6 seasons of Formula 1. 

### 4) Coefficients of variation by season (2015-2019)
Driver consistency each year from 2015-2019. Several datapoints in these visualizations suggest that more data cleaning is needed before arriving at a good answer (see the TODO document for more details).  

Sources:
original dataset from kaggle: https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020

team color hex codes: https://www.reddit.com/r/formula1/comments/609hcd/f1_2017_team_color_hex_codes/
