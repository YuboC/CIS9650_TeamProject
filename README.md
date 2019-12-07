# CIS9650_TeamProject
## Finding The Best Neighborhood To Live
## In New York City, For You!

- CIS 9650
- Professor Ali Koc

By:
- Christopher Chong
- Chin-Chia Leong
- Ka Ren Liu
- Aruna Visweswara
- Wei-Chi Yeh
- Yubo Zhang

## PROBLEM STATEMENT

Our project seeks to find which zip codes around New York City are the “best” neighborhoods to live in for a user. Being the best is subjective, and recognizing this, our group has identified six different characteristics that a user can input when prompted to find the best neighborhoods for them. The characteristics are crimes, medical facilities, pricing of real estate, demographics, access to dining, and access to supermarkets and grocery stores. Most application that are involved in identifying a good neighborhood do so through very limited filters and criteria. However, there are a lot more factors to consider in making decisions about the best neighborhood to live in.  This project, when implemented, will give home buyers and renters a wider range of data points to visualize their lifestyle and needs in a certain neighborhood, thus helping them decide as to where to purchase homes or to rent by prioritizing these six characteristics.

## APPROACH

Each team member collects data based on one of the six features. We ensure that each data set has zip code or can be converted to zip codes. After the data has been filtered and free from any nulls or irregular values, we plan to build a code that can access each comma-separated values (csv) file and run analysis based on the different characteristics. The code will be written in Python, utilizing pandas for dataframes and data handling. In addition, we are adding a user interface using the tkinter GUI library and several plots using the seaborn statistical data visualization library. The users will be prompted for an input of which characteristic matters to them the most. Based on this input, the code will call the proper function and run analysis from the files relevant to that characteristic and return the top three zip codes to the user. The user can then decide if they want to see how their zip code of interest will rank in the other characteristics, giving them insight as to whether they have found the zip code that they want to live in. For example, if the three options for best housing by median housing prices are 10022, 10128, and 10006, the user can input 10022 and see how 10022 does in the other categories. They can also choose the other two, or any zip code in Manhattan.

## ANALYSIS

In addition to creating a user input interface for finding what is the best zip codes to live in, we utilized seaborn to conduct regression testing on three parameters that we were interested in. These three were crime (arrest rates), housing (rental rates derived from median housing price and taking current rental percentage rates in 2019), and medical facilities (number of hospitals and clinics in a zip code). We ran three analysis and plotted them again each other: Arrest Count vs. Facility Count, Rental Price vs. Facility Count, and Rental Price vs. Arrest Count. Of the three analysis, we wanted to see if an increase in medical facilities yielded higher crime rates, an increase in medical facilities yielded higher rental prices, or if an increase in crime yielded a decrease in rental price. From our visual, we suggest that there appears to be a possible correlation between Arrest Count vs. Rental Price in Manhattan, while the other two analysis yielded inconclusive results.

## DATASETS

The data sets we plan to use has been gathered in the following Google Drive folder and is available in this GitHub repository:
https://drive.google.com/drive/folders/1fBR1k4QuSpaptG9UMYcb7BjKspU6FSVr?usp=sharing
https://github.com/YuboC/CIS9650_TeamProject

We have also included a presentation slide of our project, which is also located in the Google Drive folder above.
