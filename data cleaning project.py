import pandas as pd
import csv

df = pd.read_csv('star_final.csv')

# (97, 11)
print(df.shape)
print(list(df))

del df['Unnamed: 0']
del df['Luminosity']
del df['Unnamed: 6']

df = df.rename({
    'Star_name.1': 'dwarf_star_name',
    'Distance.1': 'dwarf_star_distance',
    'Mass.1': 'dwarf_star_mass',
    'Radius.1': 'dwarf_star_radius'
}, axis = 'columns')

#(97, 10)
print(df.shape)
print(list(df))

df.to_csv('star_finalest_final.csv')