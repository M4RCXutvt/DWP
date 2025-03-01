import pandas as pd
nba_players_name = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()
nba_players_age = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['AGE']).squeeze()

print('Nombre de los jugadores: \n{nba_players_name}')
print(f'\nEdad de los jugadores: \n{nba_players_age}')
print(f'Función LEN: {len(nba_players_name)}')
print(f'Función TYPE: {type(nba_players_name)}')
print (f'Función SORTED: {sorted(nba_players_age)}')
print (f'Función MAX: {max(nba_players_age)}')
print(f'Función MIN: {min(nba_players_age)}')
