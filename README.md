# CIS9650_TeamProject
## Finding The Best Neighborhood To Live
## In New York City, For You!

- CIS 9650
- Professor Ali Koc

By:
- Christopher Chong
- Chin Chia Leong
- Ka Ren Liu
- Aruna Visweswara
- Wei Chi Yeh
- Yubo Zhang

## PROBLEM STATEMENT

Our project seeks to find which zip codes around New York City are the “best” neighborhoods to live in for a user. Being the best is subjective, and recognizing this, our group has identified six different characteristics that a user can input when prompted to find the best neighborhoods for them. The characteristics are crimes, transportation, pricing of real estate, demographics, access to dining, and access to supermarkets and grocery stores. Most apps that are involved in identifying a good neighborhood do so through very limited filters and criteria. However, there are a lot more factors to consider in making decisions about the best neighborhood to live in.  This project, when implemented, will give home buyers and renters a wider range of data points to visualize their lifestyle and needs in a certain neighborhood, thus helping them decide as to where to purchase homes or to rent by prioritizing these six characteristics.

## APPROACH

Each team member collects data based on one of the six features. We ensure that each data set has zip code and borough data. After the data has been filtered and free from any nulls or irregular values, we plan to build a code that can access each comma-separated values (csv) file and run analysis based on the different characteristics. The code will be written in Python, utilizing pandas and numpy for logical analysis and matplotlib for any charts and graphs for data visualization. We will be using dictionaries and lists depending on the type of data structure that will make the search efficient. The users will be prompted for an input of which characteristic matters to them the most. Based on this input, the code will call the proper function and run analysis from the files relevant to that characteristic and return the top three zip codes by boroughs to the user. The user can then decide if they want to see how their zip code of interest will rank in the other five characteristics, giving them insight as to whether they have found the zip code that they want to live in. This process can be repeated for different zip codes and different characteristics. The program will allow the user to enter inputs as many times as they want until they key in an exit option which will exit the program.

## DATASETS

The data sets we plan to use has been gathered in the following Google Drive folder:
<https://drive.google.com/open?id=1JdOEgqaEE7fHdHQH503GTXXK25SettqL>

## ANALYSIS

The data sets will be analysed using the user inputs as criteria to find out the top-ranked zip codes for each criteria. For example, if the user selects “access to dining” as their priority, the data regarding dining options in each zip code will be analyzed and ordered, with respect to the borough. The user will be given the top three options by borough. Let’s say it is 10022, 10128, and 10006 for Manhattan, then the user can prioritize how 10022 does in the other five categories. Repeating this process, the user can decide the best neighborhood for them to live in!
