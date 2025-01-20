import pandas

data = pandas.read_csv('weather_data.csv')
# temp = data['temp'].to_list()

# print(data[data.temp == data.temp.max()])
temp_f = data.temp[data.day == 'Monday'][0] * 1.8 + 32
print(temp_f)