# Formula-1-Statistics


Formula 1 (F1) is an open-wheel racing series considered by many to be the pinacle of motorsport. Although largely seen as a Eurpoean sport, F1 races (Grand Prix) are held annually all over the world.

Teams are required to develop and build their own cars to fit within the regulations. The consequence of this is that the teams with the most money are usually the ones that win. This makes it difficult to determine whether a driver's performance is due to innate talent or car performance. That question has been the subject of endless debate among the fans, pundits, [blogs](https://f1metrics.wordpress.com/), and even some [research papers](https://www.degruyter.com/view/journals/jqas/12/2/article-p99.xml?language=en). 

In this project, I query a postgreSQL database built from the F1 dataset on [kaggle](https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020) to get the race results and lap times for the 2019 F1 season. I use this data to evaluate some key performance metrics that evaluate driver and team performance, such as retirements, positions gained / lost during a race, and the overall consistency of lap times. 

This project is divided into 2 notebooks: 

### 1) Database Initialization
Download the csv files from kaggle and import into the postgresql database. 


### 2) Formula 1 2019 visualizations and performance metrics
Analysis of 4 metrics: race traces, start / finish positions, retirements, and lap time consistency. 


This project is being periodically updated. See TODO.md for a list of planned updates. 
