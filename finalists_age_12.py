# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:38:55 2021

@author: RR
"""
# import scraper_data_reference.py
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
import pandas as pd
# a=scraper_data_reference.reference()

class reference:
    "reference data, abbreviations"
    abbreviations={'ATLANTA HAWKS': 'ATL',
     'ST. LOUIS HAWKS': 'SLH',
     'MILWAUKEE HAWKS': 'MIL',
     'TRI-CITIES BLACKHAWKS': 'TCB',
     'BOSTON CELTICS': 'BOS',
     'BROOKLYN NETS': 'BRK',
     'NEW JERSEY NETS': 'NJN',
     'CHICAGO BULLS': 'CHI',
     'CHARLOTTE HORNET': 'CHO',
     'CHARLOTTE BOBCATS': 'CHA',
     'CLEVELAND CAVALIERS': 'CLE',
     'DALLAS MAVERICKS': 'DAL',
     'DENVER NUGGETS': 'DEN',
     'DETROIT PISTONS': 'DET',
     'FORT WAYNE PISTONS': 'FWP',
     'GOLDEN STATE WARRIORS': 'GSW',
     'SAN FRANCISCO WARRIORS': 'SFW',
     'PHILADELPHIA WARRIORS': 'PHI',
     'HOUSTON ROCKETS': 'HOU',
     'INDIANA PACERS': 'IND',
     'LOS ANGELES CLIPPERS': 'LAC',
     'SAN DIEGO CLIPPERS': 'SDC',
     'BUFFALO BRAVES': 'BUF',
     'LOS ANGELES LAKERS': 'LAL',
     'MINNEAPOLIS LAKERS': 'MIN',
     'MEMPHIS GRIZZLIES': 'MEM',
     'VANCOUVER GRIZZLIES': 'VAN',
     'MIAMI HEAT': 'MIA',
     'MILWAUKEE BUCKS': 'MIL',
     'MINNESOTA TIMBERWOLVES': 'MIN',
     'NEW ORLEANS PELICANS': 'NOP',
     'NEW ORLEANS/OKLAHOMA CITY HORNETS': 'NOK',
     'NEW ORLEANS HORNETS': 'NOH',
     'NEW YORK KNICKS': 'NYK',
     'OKLAHOMA CITY THUNDER': 'OKC',
     'SEATTLE SUPERSONICS': 'SEA',
     'ORLANDO MAGIC': 'ORL',
     'PHILADELPHIA 76ERS': 'PHI',
     'SYRACUSE NATIONALS': 'SYR',
     'PHOENIX SUNS': 'PHO',
     'PORTLAND TRAIL BLAZERS': 'POR',
     'SACRAMENTO KINGS': 'SAC',
     'KANSAS CITY KINGS': 'KCK',
     'KANSAS CITY-OMAHA KINGS': 'KCK',
     'CINCINNATI ROYALS': 'CIN',
     'ROCHESTER ROYALS': 'ROR',
     'SAN ANTONIO SPURS': 'SAS',
     'TORONTO RAPTORS': 'TOR',
     'UTAH JAZZ': 'UTA',
     'NEW ORLEANS JAZZ': 'NOJ',
     'WASHINGTON WIZARDS': 'WAS',
     'WASHINGTON BULLETS': 'WAS',
     'CAPITAL BULLETS': 'CAP',
     'BALTIMORE BULLETS': 'BAL',
     'CHICAGO ZEPHYRS': 'CHI',
     'CHICAGO PACKERS': 'CHI',
     'ANDERSON PACKERS': 'AND',
     'CHICAGO STAGS': 'CHI',
     'INDIANAPOLIS OLYMPIANS': 'IND',
     'SHEBOYGAN RED SKINS': 'SRS',
     'ST. LOUIS BOMBERS': 'SLB',
     'WASHINGTON CAPITOLS': 'WAS',
     'WATERLOO HAWKS': 'WAT'}
    
a=reference()

def get_maa(team,year,ps):
    team_stats=get_roster_stats(team,year,data_format='TOTALS',playoffs=ps)
    total_mins=0
    total_agemins=0
    for t in range(len(team_stats)):
        total_mins+=int(team_stats['MP'][t])
        total_agemins+=int(team_stats['AGE'][t])*int(team_stats['MP'][t])
    return(round(total_agemins/total_mins,3))
    

finalists=[]
excel=pd.read_excel('C:/Users/HP/Desktop/New folder/NBA/OC/Finals_Teams_Age/finalist_list.xlsx')
for it in range(len(excel['year'].values)):
    team_name=excel['winner'][it].upper()
    finalists.append([a.abbreviations[team_name],excel['year'][it]])
    team_name=excel['runner'][it].upper()
    finalists.append([a.abbreviations[team_name],excel['year'][it]])

for i in range(len(finalists)):
    avg_age=get_maa(finalists[i][0],finalists[i][1],1)
    finalists[i].append(avg_age)
    print(finalists[i])