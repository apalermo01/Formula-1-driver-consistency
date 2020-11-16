# Formula-1-driver-consistency

In formula 1, consistency is the key to winning championships for the top drivers/teams and to earning one-off podiums for midfield teams when the top runners make mistakes (case in point: the 2020 Italian grand prix). To characterize the relative consistency between drivers, we'll generate a series of box plots of aggregated lap times for each driver over each race. The most consistent drivers should have the smaller relative spread over the course of a race. 

The dataset was pulled from kaggle (https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020) in csv format. I decided to use this notebook as a platform to practice SQL queries, so I converted the csv files into a postgresql database and wrote a series of queries to generate the dataframes used to make the plots. 
