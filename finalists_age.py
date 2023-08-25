# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:10:35 2021

@author: RR
"""

import matplotlib.pyplot as plt
import pandas as pd
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team

def get_team_slugs(team,year):
    team_slugs=[]
    player_totals=client.players_season_totals(season_end_year=year)
    for p in player_totals:
        if p.get('team')==team:
            team_slugs.append([p.get('slug'),p.get('age')])
    return team_slugs


def get_playoff_total_time(team,year):
    playoff_total_time=[]
    team_slugs=get_team_slugs(team,year)
#    print('1')
    m=0
    for m in range(len(team_slugs)):
#        print(team_slugs[m][0])
        player_boxscore=client.playoff_player_box_scores(player_identifier=team_slugs[m][0],season_end_year=year)
        if player_boxscore!=False and player_boxscore!=[]:
            if player_boxscore[0].get('team')==team:
#                print('3')
                player_time=0
                j=0
                for j in range(len(player_boxscore)):
#                    print('4')
                    player_time+=player_boxscore[j].get('seconds_played')
                playoff_total_time.append(team_slugs[m]+[player_time/60])
    return playoff_total_time

finalists=[]
excel=pd.read_excel('C:/Users/HP/Desktop/New folder/NBA/OC/Finals_Teams_Age/finalist_list.xlsx')
for it in range(len(excel['team'].values)):
    team=excel['team'].values[it].upper()
    team=team.replace(' ','_')
    finalists.append([Team[team],excel['year'].values[it]])

i=0
finalists_list=[]
for i in range(len(finalists)):
    playoff_total_time=get_playoff_total_time(finalists[i][0],finalists[i][1])
    mins_total=sum([row[2] for row in playoff_total_time])
    temp_prod_total=0
    k=0
    for k in range(len(playoff_total_time)):
        temp_prod=playoff_total_time[k][1]*playoff_total_time[k][2]
        temp_prod_total+=temp_prod
    mins_avg_age=temp_prod_total/mins_total
    print(finalists[i][0].name,finalists[i][1],': Minutes Averaged Age = ',mins_avg_age)
    finalists_list.append(finalists[i][0].name,finalists[i][1],mins_avg_age)

excel_plot=pd.read_excel('C:/Users/HP/Desktop/New folder/NBA/OC/Finals_Teams_Age/finalists_age_since_1980.xlsx')
x=list(excel_plot['Year'].values)
y=list(excel_plot['Mins avg Age'].values)
team_names=list(excel_plot['Team'].values)
for tn in range(len(team_names)):
    tn3=team_names[tn]
    team_names[tn]=tn3[0:3]
winner_list=pd.read_excel('C:/Users/HP/Desktop/New folder/NBA/OC/Finals_Teams_Age/finalist_list.xlsx')
winner=[list(winner_list['year'][33:]),list(winner_list['winner'][33:])]    


for i in range(len(winner[1])):
    a=winner[1][i].upper()
    b=a[0:3]
    winner[1][i]=b
    
plt.style.use('dark_background')
fig, ax = plt.subplots(dpi=1000)
plt.rc('font',size=7.5)
ax.grid(True,lw=0.3,color='grey')
ax.set_ylim([25,32.75])
ax.set_xlabel('Year',size=10)
ax.set_ylabel('Age',size=10)
ax.set_title('NBA finalists age (mins averaged)',fontsize=10)

for i in range(len(x)):
    if y[i]<26:
        ax.scatter(x[i], y[i],s=6,color='lightyellow')
        ax.annotate(team_names[i]+','+str(x[i]),(x[i]+0.5,y[i]+0.1),fontsize=7.2)
    elif y[i]<27:
        ax.scatter(x[i], y[i],s=6,color='cornsilk')
    elif y[i]<28:
        ax.scatter(x[i], y[i],s=6,color='palegoldenrod')
    elif y[i]<29:
        ax.scatter(x[i], y[i],s=6,color='khaki')
    elif y[i]<30:
        ax.scatter(x[i], y[i],s=6,color='gold')
    elif y[i]<31:
        ax.scatter(x[i], y[i],s=6,color='goldenrod')
    else:
        ax.scatter(x[i], y[i],s=6,color='darkgoldenrod')
        ax.annotate(team_names[i]+','+str(x[i]),(x[i]+0.5,y[i]+0.1),fontsize=7.2)

# for i in range(len(x)):
#     if i%2==0:
#         if team_names[i]==winner[1][int(i/2)]:
#             print(team_names[i],x[i])
#             ax.scatter(x[i], y[i],s=5,color='yellow')
#             ax.scatter(x[i+1], y[i+1],s=5,color='red')
#         else:
#             ax.scatter(x[i+1], y[i+1],s=5,color='yellow')
#             ax.scatter(x[i], y[i],s=5,color='red')
#             # else:
#             #     ax.scatter(x[i+1], y[i+1],s=10,color='gold')
#             #     ax.scatter(x[i], y[i],s=10,color='red',label='OLDER')
#     if y[i]<26:
#         ax.annotate(team_names[i]+','+str(x[i]),(x[i]+0.5,y[i]+0.1),fontsize=7.2)
#     elif y[i]>31:
#         ax.annotate(team_names[i]+','+str(x[i]),(x[i]+0.5,y[i]+0.1),fontsize=7.2)
# ax.legend(['WINNER','RUNNER-UP'],loc='upper left')

