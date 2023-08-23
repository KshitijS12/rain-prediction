
# Harnessing Meteorological Indicators for Rain Prediction

- This project focusses on the analysis of various weather variables taken daily from different locations in Australia over a period of time.
- This meteorogical data is then used to train models to be able to predict chances of Rain for today and tomorrow.
- The best model is then deployed using the Flask server.


## Data
The data in use is stored in a `csv` file and is names **weatherAUS.csv**. It is taken directly from [Kaggle](https://www.kaggle.com/datasets/trisha2094/weatheraus).

- The data contains 145460 rows where each row has the weather information for a day and location.
- The total number of columns are 23. Their description is as follows.

| **Column Name** | **Definition** | **Units** |
| --------------- | -------------- | --------- |
| `Date` | Date of the Observation taken| N/A |
| `Location` | Location of the Weather Station | N/A |
| `MinTemp` | Minimum temperature in the 24 hours to 9am. Sometimes only known to the nearest whole degree | Degrees Celsius |
| `MaxTemp` | Maximum temperature in the 24 hours to 9am. Sometimes only known to the nearest whole degree | Degrees Celsius |
| `Rainfall` | Precipitation (rainfall) in the 24 hours to 9am. Sometimes only known to the nearest whole millimeter | Millimeters |
| `Evaporation` | "Class A" pan evaporation in the 24 hours to 9am | Millimeters |
| `Sunshine` | Bright sunshine in the 24 hours to midnight | Hours |
| `WindGustDir` | Direction of the strongest wind gust in the 24 hours to midnight | 16 compass points |
| `WindGustSpeed` | Speed of the strongest wind gust in the 24 hours to midnight | Kilometers per hour |
| `WindDir9am` | Direction of the wind at 9am | 16 compass points |
| `WindDir3pm` | Direction of the wind at 3pm | 16 compass points |
| `WindSpeed9am` | Speed of the wind at 9am | Kilometers per hour |
| `WindSpeed3pm` | Speed of the wind at 3pm | Kilometers per hour |
| `Humidity9am` | Relative humidity at 9am | Percent |
| `Humidity3pm` | Relative humidity at 3pm | Percent |
| `Pressure9am` | Atmospheric pressure reduced to mean sea level at 9am | Hectopascals |
| `Pressure3pm` | Atmospheric pressure reduced to mean sea level at 3pm | Hectopascals |
| `Cloud9am` | Fraction of sky obscured by cloud at 9am | Eighths(oktas) |
| `Cloud3pm` | Fraction of sky obscured by cloud at 3pm | Eighths(oktas) |
| `Temp9am` | Temparature at 9am | Degrees Celsius |
| `Temp3pm` | Temparature at 3am | Degrees Celsius |
| `RainToday` | Did the current day receive precipitation exceeding 1mm in the 24 hours to 9am | Binary (0 = No, 1 = Yes) |
| `RainTomorrow` | Did the next day receive precipitation exceeding 1mm in the 24 hours to 9am | Binary (0 = No, 1 = Yes) |

## Code
- **Editor**: Jupyter Notebook
- **Python Version**: 3.9.7
- **Libraries Used**: calender, numpy, pandas, matplotlib, seaborn, sklearn, pickle, json, flask
## Authors

- [@KshitijS12](https://www.github.com/KshitijS12)

