import numpy
import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

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

df_drivers.head(n=10)


