import pandas as pd
nba_players = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()
# Funcion describe
print(f'Función describe con una serie: {nba_players.describe()}')
#Funcion head
print(f'Primeros 5 elementos de una serie: \n {nba_players.head()}')
print(f'\n\nPrimeros 10 elementos de una serie: \n {nba_players.head(10)}')
#uncion tail
print(f'\n\n\núltimos 5 elementos de una serie:\n {nba_players.tail()}')
print(f'\n\nUtimos 10 elementos de una serie:\n {nba_players.tail(10)}')