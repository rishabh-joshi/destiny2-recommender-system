
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:38:11 2018

@author: Yve
"""


import json
import pandas as pd
import pprint
from itertools import chain



with open('/Users/Yve/Desktop/Destiny2/Data/0_2/PGCR_graph_dataset0.json') as json_file: #"Data/Destiny2_allPvP_matches/PGCR_graph_dataset0.json
    match_data0 = json.load(json_file)


match_data = list(chain.from_iterable(match_data0))

len(match_data[0].keys())
print(match_data[0])
len(match_data)

#drop the empty matches
for i in range(len(match_data)-1):
    if len(match_data[i].keys()) != 6:
        del match_data[i]
len(match_data)
        
        
        
        

ids = dict()
fireteamids = dict()
i = 0
for mtch in match_data:
    ids[i] = []
    fireteamids[i] = []
    for player in mtch["Response"]["entries"]:
        fireteamids[i].append(player["values"]["fireteamId"]["basic"]["value"])
        ids[i].append(player["characterId"])
    i = i+1
    
len(ids)
len(fireteamids)



full_list = [teamids for j in fireteamids for teamids in fireteamids[j]]
print(len(set(full_list))) #Total number of fireteamids across all matches - includes repeated 0s for no fireteam


### check the inconsistency with fireteamid list and match list
j=0
for i in range(len(match_data)):
    if(len(match_data[i]['Response']['entries'])!=len(fireteamids[i])):
        j+=1
        
print(j)

v = list(fireteamids.values())
final = list() ###create an empty list for new subset of match_data
for j in range(len(v)):
    if len(v[j]) == 8:
        final.append(match_data[j])

len(final)

match_data_copy = []
### filter the match with at least one of the team with all players in same fireteam
for match in final:
    team0 = []
    team1 = []
    for player in match['Response']['entries']:
        if(player['standing']==0):
            team0.append(player['values'])
        elif(player['standing']==1):
            team1.append(player['values'])
    flag= 0
    if all(item['fireteamId']['basic']['value'] == team0[0]['fireteamId']['basic']['value'] for item in team0):
        flag = 0;
    else :
        flag += 1;
    if all(item['fireteamId']['basic']['value'] == team1[0]['fireteamId']['basic']['value'] for item in team1):
        flag = 0;
    else :
        flag += 1;
    
    if flag == 0:
        match_data_copy.append(match)
len(match_data_copy)

matchid = []
avg_score_per_life = []
score = []
kills = []
deaths = []
assists = []
kda = []
efficiency = []
players = [] 
grenade = []
melee = []
Super =[] 
ability = [] #most are 0's
lightlevel = []
chrclass = []
chrlevel = []

        

for match in match_data_copy:
    match_id = match['Response']['activityDetails'].get('instanceId')
    for i in range(8):
        matchid.append(match_id)
    



for match in match_data_copy:
    for player in match['Response']['entries']:
        players.append(player.get('characterId'))
        grenade.append(player['extended']['values'].get('weaponKillsGrenade').get('basic').get('value'))
        melee.append(player['extended']['values'].get('weaponKillsMelee').get('basic').get('value'))
        Super.append(player['extended']['values'].get('weaponKillsSuper').get('basic').get('value'))
        ability.append(player['extended']['values'].get('weaponKillsAbility').get('basic').get('value'))
        lightlevel.append(player['player'].get('lightLevel'))
        chrclass.append(player['player'].get('characterClass'))
        chrlevel.append(player['player'].get('characterLevel'))
        if 'averageScorePerLife' in player['values'].keys(): 
            avg_score_per_life.append(player['values']['averageScorePerLife']['basic']['value'])
        else:
            avg_score_per_life.append('NA')
        if 'score' in player['values'].keys():
            score.append(player['values']['score']['basic']['value'])
        else:
            score.append('NA')
        if 'kills' in player['values'].keys():
            kills.append(player['values']['kills']['basic']['value']) 
        else:
            kills.append('NA')
        if 'deaths' in player['values'].keys():
            deaths.append(player['values']['deaths']['basic']['value'])
        else:
            deaths.append('NA')
        if 'assists' in player['values'].keys():
            assists.append(player['values']['assists']['basic']['value'])
        else:
            assists.append('NA')
        if 'killsDeathAssists' in player['values'].keys():
            kda.append(player['values']['killsDeathsAssists']['basic']['value'])
        else:
            kda.append('NA')
        if 'efficiency' in player['values'].keys():
            efficiency.append(player['values']['efficiency']['basic']['value'])
        else:
            efficiency.append('NA') 

table2 = pd.DataFrame(
    {'matchID': matchid,
     'playersID': players,
     'Grenade': grenade,
     'Melee': melee,
     'Super': Super,
     'Ability': ability,
     'Lightlevel': lightlevel,
     'Character_Class': chrclass,
     'Character_Level': chrlevel,
     'avg_score_per_life' : avg_score_per_life,
     'score' : score,
     'kills' : kills,
     'deaths' : deaths,
     'assists' : assists,
     'KDA' : kda,
     'efficiency' : efficiency
    })

table2.describe()
         



















