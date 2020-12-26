Planned updates (not in order)

- clean data to exclude drivers that crashed on the first lap of the race. This is most likely what's causing the coefficient of variation plots to show a very low coefficient of variation (See the coefficeints of variation plot for the 2015 season).

- construct line plots showing the lap times of each driver over the course of a race. 

- Update driver names / codes and team names to handle historical data with the aim of eventually finding the most consistent driver of all time. Most likely I will either use the full name of a driver when no code is available or use the last 3 letters of their last name. 

- add properly formatted docstrings to all functions

- filter data to only feature drivers that drove in 2 or more races in any given season. 

- include a key that gives the full driver name for each code 

- Move query functions to a .py file to avoid repeating code

- Convert these visualizations into interactive dashboards using excel and / or tableau


Other ideas: 

- Which team had the best pit stops? 

- Compare which drivers / teams did better in which parts of the season (example: red bull is known for strong performances in the second half of a season because Mercedes stops development halfway through the season to focus on the next year's car)

- how are DNFs distributed by drivers / teams? Is there a particular team / driver that crashes more? What about reliability? If one team (i.e. Red Bull in 2018) has fewer mechanical DNFs could they have done better in the standings? 