==========================================

# Bike Sharing Dataset Analysis Setup

==========================================

## Set Up Environment - Shell/Terminal

mkdir proyek_analisis_data

cd proyek_analisis_data

pipenv install

pipenv shell

pip install -r requirements.txt

## Run Streamlit app

streamlit run final_dashboard/dashboard.py

==========================================

# Bike Sharing Dataset

==========================================

Hadi Fanaee-T  
Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto  
INESC Porto, Campus da FEUP  
Rua Dr. Roberto Frias, 378  
4200 - 465 Porto, Portugal  

=========================================
## Background 
=========================================

Bike sharing systems are a new generation of traditional bike rentals where the whole process from membership, rental, and return has become automatic. Through these systems, users can easily rent a bike from a particular position and return it at another position. Currently, there are over 500 bike-sharing programs around the world, which include over 500 thousand bicycles. Today, there exists great interest in these systems due to their important role in traffic, environmental, and health issues.

Apart from interesting real-world applications of bike sharing systems, the characteristics of data being generated by these systems make them attractive for research. Unlike other transport services such as buses or subways, the duration of travel, departure, and arrival positions are explicitly recorded in these systems. This feature turns bike sharing systems into a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most important events in the city could be detected via monitoring these data.

=========================================
## Data Set
=========================================

The bike-sharing rental process is highly correlated to environmental and seasonal settings. For instance, weather conditions, precipitation, day of the week, season, and hour of the day can affect rental behaviors. The core dataset is related to a two-year historical log corresponding to years 2011 and 2012 from the Capital Bikeshare system in Washington D.C., USA, which is publicly available at [Capital Bikeshare System Data](http://capitalbikeshare.com/system-data). We aggregated the data on an hourly and daily basis and then extracted and added the corresponding weather and seasonal information. Weather information is extracted from [Free Meteo](http://www.freemeteo.com).

=========================================
## Associated Tasks
=========================================

- **Regression:** Prediction of bike rental counts hourly or daily based on environmental and seasonal settings.
  
- **Event and Anomaly Detection:** Count of rented bikes is correlated to events in the town, which can be traced via search engines. For instance, querying "2012-10-30 Washington D.C." in Google returns related results to Hurricane Sandy. Some of the important events are identified in [1]. Therefore, the data can also be used for validating anomaly or event detection algorithms.

=========================================
## Files
=========================================

- **Readme.txt**
- **hour.csv:** bike sharing counts aggregated on an hourly basis. Records: 17,379 hours
- **day.csv:** bike sharing counts aggregated on a daily basis. Records: 731 days

=========================================
## Dataset Characteristics
=========================================

Both hour.csv and day.csv have the following fields, except `hr` which is not available in `day.csv`:

- **instant:** record index
- **dteday:** date
- **season:** season (1:spring, 2:summer, 3:fall, 4:winter)
- **yr:** year (0: 2011, 1: 2012)
- **mnth:** month (1 to 12)
- **hr:** hour (0 to 23)
- **holiday:** weather day is a holiday or not (extracted from [DCHR Holiday Schedule](http://dchr.dc.gov/page/holiday-schedule))
- **weekday:** day of the week
- **workingday:** if the day is neither weekend nor holiday, it is 1; otherwise, it is 0.
- **weathersit:** 
    - 1: Clear, Few clouds, Partly cloudy
    - 2: Mist + Cloudy, Mist + Broken clouds
    - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds
    - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist
- **temp:** Normalized temperature in Celsius. The values are divided by 41 (max)
- **atemp:** Normalized feeling temperature in Celsius. The values are divided by 50 (max)
- **hum:** Normalized humidity. The values are divided by 100 (max)
- **windspeed:** Normalized wind speed. The values are divided by 67 (max)
- **casual:** count of casual users
- **registered:** count of registered users
- **cnt:** count of total rental bikes including both casual and registered

=========================================
## License
=========================================

Use of this dataset in publications must be cited in the following publication:

[1] Fanaee-T, Hadi, and Gama, Joao, "Event labeling combining ensemble detectors and background knowledge", Progress in Artificial Intelligence (2013): pp. 1-15, Springer Berlin Heidelberg, doi:10.1007/s13748-013-0040-3.

=========================================
## Contact
=========================================

For further information about this dataset and the project, please contact:

**Hadi Fanaee-T**  
Email: [hadi.fanaee@fe.up.pt](mailto:hadi.fanaee@fe.up.pt)  
Laboratory of Artificial Intelligence and Decision Support (LIAAD)  
University of Porto  
INESC Porto, Campus da FEUP  
Rua Dr. Roberto Frias, 378  
4200 - 465 Porto, Portugal  
