import pandas as pd
nba_players = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', usecols= ['DRtg']).squeeze()

some_values= nba_players.iloc[:5]
addition_1 = some_values + 10
addition_2 = some_values.add(10)
print('Realización de una suma')
print(some_values)
print(addition_1)
print(addition_2)
print('Realización de una resta')
subtract_1 = some_values - 10
subtract_2 = some_values.sub(10)
print(subtract_1)
print(subtract_2)