# Census Tract Import Tool

This program is designed to facilitate the collation of Contract Rent by Census Tract .csv files, as well as their population mean centroids, sourced from the US Census, for use in our Statistics Practicum group project. This file contains a brief write-up on how to use this utility. This utility uses watchdog and PANDAS as strict requirements, so ensure these packages are installed for use. This utility contains heavily edited code from [jupiterbjy](https://stackoverflow.com/questions/69117297/using-watchdog-to-put-newly-created-file-names-into-variables) on stackoverflow.

## I. Errors and Console Logging

I have not tested this utility on all combinations of states and census tracts. It's likely that at some point, an error will come up, and I will have to make adjustments. Please pay close attention to console logs and error messages, and let me know as they happen. I have tried to keep the utility informative.

## II. How to Use It

First, ensure you have installed and updated Python 3, watchdog, and PANDAS. Run **census_import.py**, either using an IDE or from terminal. Just make sure you start it in the **census_import** directory. Download the csv files from census.gov with margin of error on, ensuring that you're downloading the 2023 5-year surveys for each census tract (which you can tick in the filters). Older census tracts may not be available in the lookup table. Without margin of error, the columns won't match up. I thought they might be useful to include, since we can easily take them out later.

When you're done, hit CTRL-C to end the program. It will write the working data frame to a .csv file which can be read into R, or back into Python if you want to use PANDAS. In addition, this .csv file will be read back into the program when you start it, so you don't have to do everything in one batch. Please push any 'completed' data frames to GitHub using a different branch. I'd rather join them in R once we have things downloaded, since I'm not very good with PANDAS.

## III. The Data

The data in the *census_tracts.csv* is drawn from counties which meet three criteria. First, the county must contain a college in this list: https://www.bestcollegereviews.org/50-best-college-towns-america/. Second, the city which contains this college must have a population which is 20% or more students. Third, the city must be the seat of the county. I have excluded particularly large capitals of notable states from the list as well. 

Some further judgement calls may be necessary. I recommend being selective even after the fact, and excluding counties from the body if we later determine that they have particularities which may confound the effect of proximity to college on rent price. Because the data for counties is drawn from 5-year samples, understand that we're looking at data estimated from 2018 to 2023.
