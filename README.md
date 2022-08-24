# Surfs Up

## Project Overview

The purpose of this project is to understand temperature trends in Oahu during the months of June and December to determine if a surf and ice cream shop is sustainable year-round. The data provided includes 2010 through 2017 for June and 2010 through 2016 for December.

## Resources
* Languages/Tools: Python with multiple libraries, SQLAlchemy
* Platforms: Jupyter Notebook, via Anaconda and SQLite
* Data Sources: .sqlite and .ipynb files

## Summary of Results

Overall, the outcomes of this project hold few, if any, surprises. While there were no significant challenges with focusing on the months of June and December, it became quite evident that there is a lot of data to parse, and, simultaneously, additional data that is absent from the decision-making process (outside of weather). Below are the three key differences I observed between June and December, as required within the scope of the project.

1.	Temperatures were overall warmer in June in Oahu than in December. While the island appears to experience mild temperatures year-round, the average temperature for June (all years) was 74.9°F, with December coming in slightly lower at 71.0°F. 

<sub>Summary Statistics for Temperature in June and December – All Years</sub>

![Summary_stats_Temps](https://github.com/Kelfang/surfs_up/blob/main/Visualizations/Summary_stats_Temps.png)

2.	Precipitation averages across all stations and all years show that the average December precipitation is approximately 0.08 inches more than June. However, it is worth noting that there are more records for June since the data includes June 2017, whereas the most recent data for December is 2016. Overall, rainfall events are minor within these two months.

<sub> Summary Statistics for Precipitation in June and December – all years</sub>

![Summary_stats_Precip](https://github.com/Kelfang/surfs_up/blob/main/Visualizations/Summary_stats_Precip.png)

3.	There does seem to be a possible correlation between temperature and precipitation. The month of December has lower temperatures and more rain, specifically more days where higher rainfall amounts are recorded at a station, while June has less variablity among the data. 

## Additional Queries 

As I was working through this project, it became apparent to me that a little rain never hurt anyone and, often, rain can be followed by sun. Therefore, I decided to learn more about rainfall amounts and get a better understanding of how much rain might ruin a surfing or ice cream outing. In my search I have discovered that weather forecasting is subjective and heavily nuanced, so for the purpose of keeping my analysis simple and tied to numbers, I used a Q & A blog from a Chicago Meteorologist, Tom Skilling, to guide my additional queries below. He stated that, “Rain is classified as light, meaning rain falling at a rate between a trace and 0.10 inch per hour; moderate, 0.11 to 0.30 inch per hour; heavy, more than 0.30 inch per hour.” [^1] Many of the daily averages of precipitation recorded came in less than 0.30 inches for an entire day.

There are 1,700 precipitation records for all June dates and 927 of those records show precipitation greater than zero. Filtering further it shows that there are only 412 records that show rainfall greater than 0.10 inch. That is approximately 24% of all the records. For December there are 1,517 precipitation records for all years and 895 show precipitation greater than zero. Additionally, 423 records show the rainfall great than 0.10 inch. This equates to approximately 28% of all records. This supports my key finding (above) that December typically has more rainfall than June. Below is a link to my code that shows this analysis.

[Expanded Queries](https://github.com/Kelfang/surfs_up/blob/main/Surfs_Up_Expanded_Queries.ipynb)

While having multiple stations around Oahu gathering data is helpful and paints a more complete picture, I found it challenging to visualize the records provided. Therefore, I took the average of all the stations’ temperature and precipitation records and grouped them by date. This provided me with a daily temperature average and a daily precipitation average that is easier to evaluate while still taking all stations into consideration without selecting just one location.

Below you can see that this scatterplot easily outlines that rain on Oahu falls in small increments with very few days of significant rainfall. Often, it may be falling in one area of the island and not the other. 


![DSA_Precip_Temps_All_Years](https://github.com/Kelfang/surfs_up/blob/main/Visualizations/DSA_Precip_Temps_All_Years.png)

Even when evaluating the most recent months of December and June, you can see that the daily average doesn’t exceed 0.6 inches in either month. Almost half of June 2017 and December 2016 are recording less than 0.1 inches of rain. 


![DSA_Precip_Temps_2016_2017](https://github.com/Kelfang/surfs_up/blob/main/Visualizations/DSA_Precip_Temps_2016_2017.png)

## Final Thoughts

Based on the data I’ve reviewed and shared, I feel confident recommending that a surf and ice cream store be opened on Oahu. The temperatures are moderate to warm, even in December and appear to be fairly consistent – a traveler’s dream! Even the rainfall, when it does occur, is nominal and even fewer days show any significant rain event. In fact, December is often a popular time to travel – especially to warm islands – and Oahu is no exception.

As climate changes occur, I believe it’s important to continue to analyze this data and the queries that have been built are easily replicated. In addition, if more data points were layered in, such as percentage of sun/clouds or percentage of humidity, that would only further enhance any future decisions should additional locations be considered.  

[^1]: *WGN-TV Weather Blog, Posted Sept. 28, 2018.* [Question and Answer Link](https://wgntv.com/weather/weather-blog/do-meteorologists-have-specific-definitions-for-drizzle-light-rain-steady-rain-heavy-rain-downpour/)
