import pandas as games
import quandl
import matplotlib.pyplot as pol
import seaborn as sns
import datetime

pol.subplots(figsize=(13,13))
games=games.read_csv('ign.csv')
games.drop(['Unnamed: 0','url'],axis=1,inplace=True)
games.drop(games.index[516],inplace=True)	

games.replace(['Action, Adventure','Action, RPG','Adventure','Fighting',
                 'Platformer','Racing, Action','Racing','Shooter','Simulation']
                ,['Act,adv','Act,RPG','Adv','Fight','Plat','Rac,Act','Race','Shoot','Simltn'],inplace=True)

max_genres=games.groupby('genre')['genre'].count()
max_genres=max_genres[max_genres.values>200]
max_genres.sort_values(ascending=True,inplace=True)
mean_games=games[games['genre'].isin(max_genres.index)]
abc=mean_games.groupby(['release_year','genre'])['score'].mean().reset_index()
abc=abc.pivot('release_year','genre','score')
sns.heatmap(abc,annot=True,cmap='RdYlGn',linewidths=0.4,yticklabels='auto')
pol.yticks(rotation='horizontal')
pol.xticks(rotation='vertical')
pol.title('Average Score By Genres')
pol.show()