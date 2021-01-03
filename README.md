# Formula-1-driver-consistency


Formula 1 (F1) is an open-wheel racing series considered by many to be the pinacle of motorsport. Although largely seen as a Eurpoean sport, F1 races (Grand Prix) are held anually all over the world.


In formula 1, consistency is the key to winning championships for the top drivers/teams and to earning one-off podiums for midfield teams when the top runners make mistakes (case in point: the 2020 Italian grand prix). 

So who is the most consistent driver? I would like to propose that the best way to answer this is to look at the distribution of lap times throughout a race. A smaller spread of lap times should equate to a more consistent driver. To get the most accurate picture, we should look at this spread over the course of an entire season. We'll then analyze the variances of the variances and perform the appropriate hypothesis testing to see how confidently we can identify the most consistent driver. 

This project is divided into 2 notebooks: 

### 1) Database Initialization
I decided to use this project as an excuse to practice SQL queries, so this is where we convert the CSV files into the postgresql database that will be queried. 

### 2) Formula 1 Driver Consistency 
This is the "main" notebook of the project. This one features the lap time distributions for each race in the 2019 season and distribution of the coefficients of variation for each driver during the whole season. In a future update, I will include a section on hypothesis testing.


Sources:
original dataset from kaggle: https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020

team color hex codes: https://www.reddit.com/r/formula1/comments/609hcd/f1_2017_team_color_hex_codes/
