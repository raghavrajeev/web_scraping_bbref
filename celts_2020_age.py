# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team

celts_slugs=[]
player_totals=client.players_season_totals(season_end_year=2020)
for p in player_totals:
    if p.get('team')==Team.DENVER_NUGGETS:
        celts_slugs.append([p.get('slug'),p.get('age')])

playoff_total_time=[]
for i in range(len(celts_slugs)):
    playoff_box_scores_temp=client.playoff_player_box_scores(player_identifier=celts_slugs[i][0],season_end_year=2020)
    player_time=0
    for j in range(len(playoff_box_scores_temp)):
        player_time+=playoff_box_scores_temp[j].get('seconds_played')
    playoff_total_time.append(celts_slugs[i]+[player_time/60])

mins_total=sum([row[2] for row in playoff_total_time])
temp_prod_total=0
for i in range(len(playoff_total_time)):
    temp_prod=playoff_total_time[i][1]*playoff_total_time[i][2]
    temp_prod_total+=temp_prod
mins_avg_age=temp_prod_total/mins_total
print('Minutes Averaged Age=',mins_avg_age)

celts_names=[]
player_totals=client.players_season_totals(season_end_year=2020)
for p in player_totals:
    if p.get('team')==Team.DENVER_NUGGETS:
        celts_names.append(p.get('name'))

y=[row[2] for row in playoff_total_time]
x=[row[1] for row in playoff_total_time]

fig, ax = plt.subplots(dpi=1000)
plt.style.use('dark_background')
plt.rc('font',size=8)
ax.scatter(x, y,s=15,color='c')
ax.grid(True,lw=0.3,color='grey')
ax.set_xlim([19,33])
ax.set_ylim([-25,740])
ax.set_xlabel('Age',size=10)
ax.set_ylabel('Total Minutes',size=10)
ax.set_title('BOS 2020 playoff minutes (Minutes Avg Age=25.047)')
# for i, txt in enumerate(celts_names):
#     if y[i]>30:
#         if celts_names[i]=='Robert Williams':
#             ax.annotate(txt, (x[i]+0.2, y[i]-20),fontsize=6.3)
#         else:
#             ax.annotate(txt, (x[i]+0.2, y[i]+10),fontsize=6.3)
        
            