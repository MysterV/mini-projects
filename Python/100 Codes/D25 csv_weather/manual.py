f = open('weather_data.csv').readlines()
temperatures = []
column = 2
for i in range(len(f)):
    f[i] = f[i].strip().split(',')

for i in range(1, len(f)):
    temperatures.append(f[i][column])
print(temperatures)


