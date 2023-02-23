# Machine learning with random forests for average temperature prediction.

## Overview.
The machine learning algorithm Random Forest was used to predict the average temperature in Miyazaki Prefecture. The resulting RSME was around 0.3 for both training and test data. It also approximated 1 with respect to R^2.
As a consideration, it is considered that accurate predictions were made without over-learning due to learning from sufficient explanatory variables and sufficient records. The graph below shows the results obtained in this study.

![result](result.png)

## About learning
For the purpose of predicting the average temperature in Miyazaki, data from eight regions were trained: the eight regions are Sapporo, Sendai, Tokyo, Nagoya, Osaka, Hiroshima, Fukuoka and Okinawa. The objective variable is the average temperature. The explanatory variables are mean temperature (°C), mean daily maximum temperature (°C), mean daily minimum temperature (°C), total precipitation (mm), total precipitation (mm), maximum daily precipitation (mm), sunshine hours (hours), deepest snow cover (cm), deepest snow cover (cm), total snowfall (cm), mean wind speed (m/s), mean vapour pressure (hPa), average Average humidity (%), Average cloud cover (10-minute ratio).The parameters for the random forest were n_estimators = 15,random_state = 42,n_jobs = 1,min_samples_split = 10,max_depth = 10.The evaluation methods used are RSME and R^2.

## Procedure
Download data from the JMA. Put the data to be used as training in the directory [Train_data](Train_data). Put the data to be tested in the [Test_data](Test_data) directory. As you will be referring to these directories from the programme, it is advisable to download the data with the same objective and explanatory variables.


## The data used
For data, you can download the data from [this page](https://www.data.jma.go.jp/gmd/risk/obsdl/index.php)of the [Japan Meteorological Agency](https://www.jma.go.jp/jma/index.html).On the data download screen, first select the region for the study data in the "Select a location" section. Then, in the "Select an item" section, under the temperature tab, select the monthly average temperature, the monthly average of daily maximum temperature and the monthly average of daily minimum temperature. Then, under the precipitation tab, select the monthly total of precipitation and the monthly maximum of daily precipitation. Select the monthly total of sunshine hours from the sunshine/sunshine tab. Select the monthly total for monthly deepest snowfall and monthly maximum snowfall from the snow cover/snowfall tab. Select the monthly average wind speed from the Wind tab. Select the monthly average vapour pressure and monthly average relative humidity from the humidity/barometric tab. Select the monthly average cloud cover from the cloud cover/weather tab." Under "Select a period of time", select "Display over a continuous period of time" and then select the period of time for the person." In the "Choose display options" section, leave the default display screen as it is.
Select multiple study data. At this point, select and download each of them one by one in the "Select a location" field. Then put the files in the Train_data directory. For the test data, also select one and put it in the Test_data directory.Please note that the data must be entered separately for each region, otherwise they cannot be combined.


## Rights.
- Source: the Meteorological Office (https://www.data.jma.go.jp/gmd/risk/obsdl/index.php)

- This graph was produced under my responsibility.