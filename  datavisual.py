import numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
import sklearn

df_drivers= pd.read_csv('/home/beloslava/Projects/random/formula-1/data/drivers.csv', na_values='\\N')
df_circuits= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/circuits.csv", na_values='\\N')
df_constructorresults = pd.read_csv("/home/beloslava/Projects/random/formula-1/data/constructor_results.csv", na_values='\\N')
df_constructorstandings = pd.read_csv("/home/beloslava/Projects/random/formula-1/data/constructor_standings.csv", na_values='\\N')
df_constructors = pd.read_csv("/home/beloslava/Projects/random/formula-1/data/constructors.csv", na_values='\\N')
df_driverstangings= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/driver_standings.csv", na_values='\\N')
df_laptimes= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/lap_times.csv", na_values='\\N')
df_pitstops= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/pit_stops.csv", na_values='\\N')
df_qualifying= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/qualifying.csv", na_values='\\N')
df_races= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/races.csv", na_values='\\N')
df_results= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/results.csv", na_values='\\N')
df_seasons= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/seasons.csv", na_values='\\N')
df_status= pd.read_csv("/home/beloslava/Projects/random/formula-1/data/status.csv", na_values='\\N')

display(df_drivers.head(n=10))
display(df_results.head(n=20))

col_list_drivers = ['driverId','forename','surname','code']
df_drivers_cl = df_drivers.filter(col_list_drivers, axis=1)

col_list_teams = ['constructorId','name']
df_teams_cl = df_constructors.filter(col_list_teams, axis=1)

col_list_races = ['raceId','year','round']
df_races_cl = df_races.filter(col_list_races, axis=1) 

col_list_results = ['raceId','driverId','constructorId','position',]
df_results_cl = df_results[df_results['position'] < 11].filter(col_list_results, axis=1)

print('Drivers')
print(df_drivers_cl.head(n=10))
print('')
print('Teams')
print(df_teams_cl.head(n=10))
print('')
print('Races')
print(df_races_cl.head(n=10))
print('')
print('Results')
print(df_results_cl.head(n=20))

sns.set_theme(style='whitegrid')
fig, axis = plt.subplots(1,1, figsize=(20, 5), sharex=True)

df_races_plot = df_races_cl['year'].value_counts().reset_index()
df_races_plot.columns = ['Year', 'Races']
df_races_plot.rename(columns={'Year' : 'Races'})
df_races_plot.sort_values(by=['Year'], inplace=True)
df_races_plot.sort_values(by=['Year'])

graph = sns.barplot(x=df_races_plot['Year'], y=df_races_plot['Races'], palette="crest")
graph.set(title='Qty races per Year', xlabel='Years', ylabel='Races')
graph.set_xticklabels(labels=graph.get_xticklabels(), rotation=90)

max = df_races_plot.describe() * 1.1
max_y = 0

_, max_y_f = graph.get_ylim()
max_y = max_y_f if max_y_f > max_y else max_y
graph.set(ylim=(0, max_y))

display(fig.show())
display(df_races_plot.transpose())

df_drivers_years_points = df_results_cl.filter(['driverId','constructorId','points','year'], axis=1)
points_drivers_array = []
points_teams_array=[]

years = []

for year in years:
    
    points_year = df_drivers_years_points[df_drivers_years_points['year'] == year]
    for index, driver in df_drivers_cl.iterrows():
        
        array = []
        driver_name = f'''{driver['forename']} {driver['surname']}'''
        array.extend([driver_name, driver['code']])
        array.append(year)
        array.append(points_year[points_year['driverId'] == driver['driverId']].sum()['points'])
        points_drivers_array.append(array)
    
    for index, team in df_teams_cl.iterrows():
        
        array = []
        array.extend([team['name'], year])
        array.append(points_year[points_year['constructorId'] == team['constructorId']].sum()['points'])
        points_teams_array.append(array)

df_drivers_points = pd.DataFrame(points_drivers_array, columns=('name','code','year','points'))
df_teams_points = pd.DataFrame(points_teams_array, columns=('name','year','points'))

view_drivers = df_drivers_points[df_drivers_points['year'] == 2021]
view_drivers = view_drivers[view_drivers['points'] > 0]
display(view_drivers[view_drivers['year'] == 2021].sort_values(by=['points'], ascending=False))