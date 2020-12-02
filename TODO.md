Planned updates (not in order)

- clean data to exclude drivers that crashed on the first lap of the race. This is most likely what's causing the coefficient of variation plots to show a minimum variation of 0 (which is impossible) (See the coefficeints of variation plot for the 2015 season).

- construct line plots showing the lap times of each driver over the course of a race. 

- Implement ANOVA hypothesis testing

- adjust cutoff parameters as needed to maximize the confidence of the hypothesis test. I originally added the cutoffs so that the coefficients of variation are not affected by safety car periods or pit stops; however, upon further reflection it may be better to remove the cutoffs since these safety car periods and pit stops affect all drivers equally, but time lost due to mistakes do not. 

- Update driver names / codes and team names to handle historical data with the aim of eventually finding the most consistent driver of all time. Most likely I will either use the full name of a driver when no code is available or use the last 3 letters of their last name. 

- add properly formatted docstrings to all functions

- filter data to only feature drivers that drove in 2 or more races in any given season. 

- include a key that gives the full driver name for each code 

- Move query functions to a .py file to avoid repeating code

- fix calc_variations() to work with the 2020 season where not all the races are finished. Alternatively, wait until the 2020 season is over in a couple weeks. 

- Convert these visualizations into interactive dashboards using excel and / or tableau