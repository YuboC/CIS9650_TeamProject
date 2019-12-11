# CIS 9650 FINAL PROJECT
# PROJECT WHERE TO LIVE
# Christopher Chong, Chin Chia Leong, Ka Ren Liu, Aruna Visweswara, Wei Chi Yeh, Yubo Zhang



# import tkinter GUI library and pandas data analysis library
import tkinter as tk
import pandas as pd



# adding labels to the tkinter GUI: inputs is what the text will be
def labelmaker(inputs):
    return tk.Label(master, text = inputs).pack() 



# accesses the medical data file and creates a dataframe from it
def medical():
    healthDf = pd.read_csv('healthFacilityData.csv') #read the cvs header file 
    healthDf = healthDf[["Facility Name", "Description", "Facility City", "Facility Zip Code","Ownership Type"]]
    healthDf.columns = ["hospitalName", "hospitalType", "hospCity","zipcode","hospitalOwnershipType"]
    healthDf = healthDf.dropna() # drop null values
    healthDf = healthDf[healthDf["zipcode"].map(len) == 5]
    
    healthDf = healthDf[healthDf["hospCity"] == "New York"]
    healthDf["hospitalName"] = healthDf["hospitalName"].astype(str) 
    healthDf["hospitalType"] = healthDf["hospitalType"].astype(str) 
    healthDf["hospCity"] = healthDf["hospCity"].astype(str)
    healthDf["hospitalOwnershipType"] = healthDf["hospitalOwnershipType"].astype(str) 
    
    healthDf = healthDf[healthDf["zipcode"] != "0"]
    
    medbyziplist = []
    mdf = pd.DataFrame(columns = ["zipcode", "count_of_medical_facility"])
    
    for z in healthDf["zipcode"]:
        if z not in medbyziplist:
            medbyziplist.append(z)
            
    for z in medbyziplist:
        temp = healthDf[healthDf["zipcode"] == z]
        count = temp.count()["zipcode"]
        mdf = mdf.append({"zipcode": z, "count_of_medical_facility": count}, ignore_index = True)
    
    # sort the values, drop and get new index    
    mdf = mdf.sort_values(by = "count_of_medical_facility", ascending = False)
    mdf = mdf.reset_index(drop = True)
    
    return mdf
 
    
    
# accesses the crime data file and creates a dataframe from it
def crime():
    crime = pd.read_csv("crime_for_final_project.csv") # cleaned version, see clean_crime_data for original file
    
    crimesbyziplist = []
    cdf = pd.DataFrame(columns = ["zipcode", "count_of_crimes"])
    
    for z in crime["zipcode"]:
        if z not in crimesbyziplist:
            crimesbyziplist.append(z)
            
    for z in crimesbyziplist:
        temp = crime[crime["zipcode"] == z]
        count = temp.count()["zipcode"]
        cdf = cdf.append({"zipcode": z, "count_of_crimes": count}, ignore_index = True)
    
    # altering the type of the columns to match analysis needs
    cdf["count_of_crimes"] = cdf["count_of_crimes"].astype(int)
    cdf["zipcode"] = cdf["zipcode"].astype(str)
    
    # sort the values, drop and get new index
    cdf = cdf.sort_values(by = "count_of_crimes")
    cdf = cdf.reset_index(drop = True)
    
    return cdf



# accesses the housing data file and creates a dataframe from it    
def housing():
    # reads file and take relevant columns and giving them appropriate names
    df = pd.read_csv("rollingsales_manhattan.csv")
    df = df[["NEIGHBORHOOD", "ZIP CODE", " SALE PRICE "]]
    df.columns = ["neighborhood", "zipcode", "sale_price"]
    df = df.dropna() # drop null values
    
    # altering the type of the columns to match analysis needs
    df["neighborhood"] = df["neighborhood"].astype(str)
    df["zipcode"] = df["zipcode"].astype(int)
    df["zipcode"] = df["zipcode"].astype(str)
    df["sale_price"] = df["sale_price"].str.replace(",", "")
    df["sale_price"] = df["sale_price"].astype(int)
    df = df[df["zipcode"] != "0"]
    
    # creating dataframe hdf for zipcode and median housing price
    pricebyziplist = []
    hdf = pd.DataFrame(columns = ["zipcode", "median_housing_price"])
    
    for z in df["zipcode"]:
        if z not in pricebyziplist:
            pricebyziplist.append(z)
            
    for z in pricebyziplist:
        zdf = df[df["zipcode"] == z]
        median = zdf.median()["sale_price"]
        hdf = hdf.append({"zipcode": z, "median_housing_price": median}, ignore_index = True)
    
    # sort the values, drop and get new index    
    hdf = hdf.sort_values(by = "median_housing_price")
    hdf = hdf.reset_index(drop = True)
    
    return hdf



# accesses the food retail options data file and creates a dataframe from it
def retail():
    # reads file and take relevant columns and giving them appropriate names
    df = pd.read_csv("Retail_Food_Stores_NYC.csv")
    df = df[["County","Zip Code"]]
    df = df.dropna()
    rdf = df[(df["County"] == "New York")]
    rdf = rdf.groupby(["Zip Code"])["County"].count().reset_index(name = "count")
    rdf = rdf.rename(columns = {"Zip Code": "zipcode"})
    
    # altering the type of the columns to match analysis needs
    rdf["zipcode"] = rdf["zipcode"].astype(int)
    rdf["zipcode"] = rdf["zipcode"].astype(str)
    
    # sort the values, drop and get new index
    rdf = rdf.sort_values(by = "count", ascending = False)
    rdf = rdf.reset_index(drop = True)
    
    return rdf
  
    

# accesses the dine in restaurant data file and creates a dataframe from it
def restaurant():
    # reads file and take relevant columns and giving them appropriate names
    data = pd.read_csv("restaurant.csv")
    data = data.dropna()
    data = data.rename(columns = {"ZIPCODE": "zipcode"})
    
    # altering the type of the columns to match analysis needs
    data["zipcode"] = data["zipcode"].astype(int)
    data["zipcode"] = data["zipcode"].astype(str)
    data = data.drop(columns = ["BORO"])    
    
    # creating new dataframe ndf for analysis with the counts of restaurants per zipcode
    restaurantsbyziplist = []
    ndf = pd.DataFrame(columns = ["zipcode", "count_of_restaurants"])
    
    for z in data["zipcode"]:
        if z not in restaurantsbyziplist:
            restaurantsbyziplist.append(z)
            
    for z in restaurantsbyziplist:
        temp = data[data["zipcode"] == z]
        count = temp.count()["zipcode"]
        ndf = ndf.append({"zipcode": z, "count_of_restaurants": count}, ignore_index = True)
    
    # altering the type of the columns to match analysis needs
    ndf["count_of_restaurants"] = ndf["count_of_restaurants"].astype(int)
    
    # sort the values, drop and get new index
    ndf = ndf.sort_values(by = "count_of_restaurants", ascending = False)
    ndf = ndf.reset_index(drop = True)
    
    return ndf



# accesses the demographics data file and creates a dataframe from it    
def demographics():
    demoMetaDf = pd.read_csv('DemoMeta.csv') #read the cvs header file 
    demoDf = pd.read_csv('Demo.csv') #read the csv data file 

    demoIDLis = ['NAME'] #column ID
    demoColNames = ['Zipcode'] #column names
    
    for x in demoMetaDf['GEO_ID']:
        demoIDLis.append(x)
    
    for x in demoMetaDf['Names of Columns']:
        demoColNames.append(x)
    
    demoDf = demoDf[demoIDLis]    
    demoDf = demoDf.drop(index = 0) #dropping the first index 
    
    #demoDf = demoDf.dropna() #drop any columns with No values 
    demoDf.columns = demoColNames    
    demoDf = demoDf[(demoDf.Male!='0') ] #drop any columns with No values  
    
    # rename column for analysis
    demoDf = demoDf.rename(columns = {"Zipcode": "zipcode"})
    
    # convert all 30 columns to the appropriate data type for analysis
    demoDf["zipcode"] = demoDf["zipcode"].astype(int)
    demoDf["zipcode"] = demoDf["zipcode"].astype(str)
    demoDf["Male"] = demoDf["Male"].astype(int)
    demoDf["Female"] = demoDf["Female"].astype(int)
    demoDf["Under 5 years"] = demoDf["Under 5 years"].astype(int)
    demoDf["5 to 9 years"] = demoDf["5 to 9 years"].astype(int)
    demoDf["10 to 14 years"] = demoDf["10 to 14 years"].astype(int)
    demoDf["15 to 19 years"] = demoDf["15 to 19 years"].astype(int)
    demoDf["20 to 24 years"] = demoDf["20 to 24 years"].astype(int)
    demoDf["25 to 34 years"] = demoDf["25 to 34 years"].astype(int)
    demoDf["35 to 44 years"] = demoDf["35 to 44 years"].astype(int)
    demoDf["45 to 54 years"] = demoDf["45 to 54 years"].astype(int)
    demoDf["55 to 59 years"] = demoDf["55 to 59 years"].astype(int)
    demoDf["60 to 64 years"] = demoDf["60 to 64 years"].astype(int)
    demoDf["65 to 74 years"] = demoDf["65 to 74 years"].astype(int)
    demoDf["75 to 84 years"] = demoDf["75 to 84 years"].astype(int)
    demoDf["85 years and over"] = demoDf["85 years and over"].astype(int)
    demoDf["White"] = demoDf["White"].astype(int)
    demoDf["Black or African American"] = demoDf["Black or African American"].astype(int)
    demoDf["American Indian and Alaska Native"] = demoDf["American Indian and Alaska Native"].astype(int)
    demoDf["Asian Indian"] = demoDf["Asian Indian"].astype(int)
    demoDf["Chinese"] = demoDf["Chinese"].astype(int)
    demoDf["Filipino"] = demoDf["Filipino"].astype(int)
    demoDf["Japanese"] = demoDf["Japanese"].astype(int)
    demoDf["Korean"] = demoDf["Korean"].astype(int)
    demoDf["Vietnamese"] = demoDf["Vietnamese"].astype(int)
    demoDf["Other Asian"] = demoDf["Other Asian"].astype(int)
    demoDf["Other Pacific Islander "] = demoDf["Other Pacific Islander "].astype(int)
    demoDf["Other race"] = demoDf["Other race"].astype(int)
    demoDf["Mix Race"] = demoDf["Mix Race"].astype(int)
    demoDf["Hispanic or Latino (of any race)"] = demoDf["Hispanic or Latino (of any race)"].astype(int)
    
    return demoDf
    


# function to calculate what place each zipcode is in the other categories/parameters
def getRank(df, zipc, parameter):
    index = df[df["zipcode"] == zipc].index[0]
    return labelmaker(zipc + " ranks #" + str(index + 1) + " in " + parameter + ".")



# intermediate function that calls getRank() for each parameter; see above function for details
def getSelection2(selection2, selection1):
    if selection1 !=  "Medical" and selection1 != "Crime" and selection1 != "Housing" and selection1 != "Retail" and selection1 != "Restaurant":
        ddf = demographics()
        ddf["percentage_of_interest"] = ddf.apply(lambda row:(row[selection1] / (row["Male"] + row["Female"])), axis = 1)
        ddf = ddf.sort_values(by = "percentage_of_interest", ascending = False)
        ddf = ddf.reset_index(drop = True)
        getRank(ddf, selection2, selection1)
    getRank(medical(), selection2, "medical")
    getRank(crime(), selection2, "crime")
    getRank(housing(),selection2, "housing")
    getRank(retail(), selection2, "retail")
    getRank(restaurant(), selection2, "restaurants")



# gets the top 3 values for each dataframe
def topThree (df):
    zip1 = df.iloc[0]
    zip2 = df.iloc[1]
    zip3 = df.iloc[2]
    
    return zip1, zip2, zip3



# function that takes the first entry value and controls the output based on the criteria specified by the first parameter of interest
def getSelection1(selection1):
    # intermediary function that gets the value from the second entry and calls getSelection2 (); see above function
    def task2():
        selection2 = entry2.get()
        labelmaker("You selected " + selection2)
        getSelection2(selection2, selection1)
    
    # if statements for control, depending on what the first entry is
    if selection1 == "Medical":
        mdf = medical()
        zip1, zip2, zip3 = topThree(mdf)
        labelmaker("The top 3 zipcodes with the highest number of medical facilities are:")
        labelmaker(zip1["zipcode"] + ": " + str(zip1["count_of_medical_facility"]))
        labelmaker(zip2["zipcode"] + ": " + str(zip2["count_of_medical_facility"]))
        labelmaker(zip3["zipcode"] + ": " + str(zip3["count_of_medical_facility"]))
    elif selection1 == "Crime":
        cdf = crime()
        zip1, zip2, zip3 = topThree(cdf)
        labelmaker("The top 3 zipcodes with the lowest crimes are:")
        labelmaker(zip1["zipcode"] + ": " + str(zip1["count_of_crimes"]))
        labelmaker(zip2["zipcode"] + ": " + str(zip2["count_of_crimes"]))
        labelmaker(zip3["zipcode"] + ": " + str(zip3["count_of_crimes"]))
    elif selection1 == "Housing":
        hdf = housing()
        zip1, zip2, zip3 = topThree(hdf)
        labelmaker("The top 3 zipcodes with the lowest median housing price are:")
        labelmaker(zip1["zipcode"] + ": $" + str(zip1["median_housing_price"]))
        labelmaker(zip2["zipcode"] + ": $" + str(zip2["median_housing_price"]))
        labelmaker(zip3["zipcode"] + ": $" + str(zip3["median_housing_price"]))
    elif selection1 == "Retail":
        rdf = retail()
        zip1, zip2, zip3 = topThree(rdf)
        labelmaker("The top 3 zipcodes with the highest retail food store options are:")
        labelmaker(zip1["zipcode"] + ": " + str(zip1["count"]) + " stores")
        labelmaker(zip2["zipcode"] + ": " + str(zip2["count"]) + " stores")
        labelmaker(zip3["zipcode"] + ": " + str(zip3["count"]) + " stores")
    elif selection1 == "Restaurant":
        ndf = restaurant()
        zip1, zip2, zip3 = topThree(ndf)
        labelmaker("The top 3 zipcodes with the highest dine-in restaurant options are:")
        labelmaker(zip1["zipcode"] + ": " + str(zip1["count_of_restaurants"]) + " stores")
        labelmaker(zip2["zipcode"] + ": " + str(zip2["count_of_restaurants"]) + " stores")
        labelmaker(zip3["zipcode"] + ": " + str(zip3["count_of_restaurants"]) + " stores")
    else:
        ddf = demographics()
        ddf["percentage_of_interest"] = ddf.apply(lambda row:(row[selection1] / (row["Male"] + row["Female"])), axis = 1)
        ddf = ddf.sort_values(by = "percentage_of_interest", ascending = False)
        ddf = ddf.reset_index(drop = True)
        zip1, zip2, zip3 = topThree(ddf)
        labelmaker("The top 3 zipcodes with the highest percentage of " + selection1 + " populations are: ")
        labelmaker(zip1["zipcode"] + ": " + str(zip1["percentage_of_interest"] * 100) + "%.")
        labelmaker(zip2["zipcode"] + ": " + str(zip2["percentage_of_interest"] * 100) + "%.")
        labelmaker(zip3["zipcode"] + ": " + str(zip3["percentage_of_interest"] * 100) + "%.")
    

    # statements executed after running the analysis of the first parameter. By now three zipcodes of interest should be outputed.
    labelmaker("See how any zipcode ranks in other parameters. You can select from any zipcode, or if interested, from the 3 listed above :)")
    
    entry2 = tk.Entry(master)
    entry2.pack()
    
    button2 = tk.Button(text = 'Enter', command = task2)
    button2.pack()
        


# intermediary function that gets the value from the first entry
def task1():
    selection1 = entry1.get()
    labelmaker("You selected " + selection1)
    getSelection1(selection1)
 


# main code starts here
# setting the main tkinter window and the initial labels
master = tk.Tk()
labelmaker("=======================================================================================================================================")
labelmaker("Welcome to 'Project Where To Live'. This program will help you find the best zipcodes to live in Manhattan.")
labelmaker("Please enter which parameter matters to you the most.")
labelmaker("Your options are: Medical, Crime, Housing, Retail, Restaurant, or Enter a Demographic of Interest")
labelmaker("(i.e. For highest number of retail food options, enter 'Retail'.")
labelmaker("For highest percentage of Chinese population, enter 'Chinese' {See Column F of DemoMeta.csv for choice of 30 different demographic options})")


# createst the first entry textbox and button with "enter" for selection
entry1 = tk.Entry(master)
entry1.pack()

button1 = tk.Button(text = 'Enter', command = task1)
button1.pack()

master.mainloop()
