import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
airquality = 'dataset/airquality.csv'
airquality_data = pd.read_csv(airquality)
# print(data.head())

# removing pm2.5 (not enough data)
airquality_data = airquality_data.drop(columns=['pm25'])


# change dataset language
translations = {
    'tanggal': 'date',
    'stasiun': 'station',
    'pm10': 'PM10',
    'so2': 'SO2',
    'co': 'CO',
    'o3': 'O3',
    'no2': 'NO2',
    'max': 'max_value',
    'critical': 'critical_pollutant',
    'categori': 'category',
}
airquality_data.rename(columns=translations, inplace=True)

# fill out NA values
for column in ['PM10', 'SO2', 'CO', 'O3', 'NO2']:
    airquality_data[column] = airquality_data[column].fillna(airquality_data[column].mean())

# Time Series Analysis
airquality_data['date'] = pd.to_datetime(airquality_data['date'])
plt.figure(figsize=(12, 6))
plt.plot(airquality_data['date'], airquality_data['PM10'], label='PM10')
plt.plot(airquality_data['date'], airquality_data['SO2'], label='SO2')
plt.plot(airquality_data['date'], airquality_data['CO'], label='CO')
plt.plot(airquality_data['date'], airquality_data['O3'], label='O3')
plt.plot(airquality_data['date'], airquality_data['NO2'], label='NO2')
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('Pollutant Concentrations Over Time')
plt.legend()
plt.show()

# Correlation Matrix
correlation_matrix = airquality_data[['PM10', 'SO2', 'CO', 'O3', 'NO2']].corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Pollutant Correlation Heatmap')
plt.show()
