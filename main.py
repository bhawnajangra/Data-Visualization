import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("c:\\Users\\bhawn\\Downloads\\IPL.csv")
print(df.head())
#info about data
print(df.info())

print(df.describe())        #statistical summary of the data

print(df.isnull().sum())    #checking for null values

m = df['match_winner'].value_counts()
sns.barplot(x = m.values , y = m.index , palette = 'coolwarm')
plt.title('Number of Matches Won by Each Team')
#plt.show()

df['toss_decision']
sns.countplot(x = 'toss_decision' , data = df , palette = 'coolwarm')
plt.title('Toss Decision')
#plt.show()

c = df[df['toss_decision'] == df['match_winner']]['match_id'].value_counts()
sns.barplot(x = c.values , y = c.index , palette = 'coolwarm')
plt.title('Number of Matches Won by Toss Decision')
#plt.show()

p = df[df['toss_decision'] != df['match_winner']]['match_id'].value_counts()
sns.barplot(x = p.values , y = p.index , palette = 'coolwarm')
plt.title('Number of Matches Lost by Toss Decision')
#plt.show()

sns.countplot(x=df['won_by'], palette = 'coolwarm')
plt.title('Number of Matches Won by Runs or Wickets')
#plt.show()

count = df['player_of_the_match'].value_counts().head(10)
sns.barplot(x = count.values , y = count.index , palette = 'coolwarm')
plt.title('Top 10 Players of the Match')
#plt.show()

highest_score = df['won_by'].max()
print("Highest Score in IPL is : ", highest_score)

high = df.groupby('top_scorer')['highscore'].max().sort_values(ascending = False).head(10)
sns.barplot(x = high.values , y = high.index , palette = 'coolwarm')
plt.title('Top 10 Highest Scorers in IPL')
#plt.show()

venue = df['venue'].value_counts()
sns.barplot(x = venue.values , y = venue.index , palette = 'coolwarm')
plt.title('Number of Matches Played at Each Venue')


plt.show()