import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/bengaluru-population.csv')

city = input('enter city:')
yearly_pop = df.groupby(['City', 'Year'])['Count'].sum().reset_index()

city_pop = yearly_pop[yearly_pop['City'] == city]

plt.plot(city_pop['Year'], city_pop['Count'])
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Bengaluru Population Over Time')
plt.show()
