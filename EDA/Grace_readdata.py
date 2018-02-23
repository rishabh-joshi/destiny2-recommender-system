#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:55:53 2018

@author: yuecui
"""

import json
import pandas as pd
import pprint

with open("/Users/yuecui/Desktop/Destiny/Data/PGCR_graph_dataset0.json") as json_file: #"Data/Destiny2_allPvP_matches/PGCR_graph_dataset0.json
    match_data = json.load(json_file)
    


from itertools import chain
match_data = list(chain.from_iterable(match_data))

match_data[5]


for i in range(len(match_data)-1):
   if len(match_data[i].keys()) != 6:
       del match_data[i]
       
       

ids = dict()
fireteamids = dict()
i = 0
for mtch in match_data:
    ids[i] = []
    fireteamids[i] = []
    for player in mtch["Response"]["entries"]:
        #print(i)
        fireteamids[i].append(player["values"]["fireteamId"]["basic"]["value"])
        ids[i].append(player["characterId"])
    i = i+1
    
###Check length of fireteam id
#for x,y in fireteamids.items():
    #print(len(y))        
     


v = list(fireteamids.values())
final = list() ###create an empty list for new subset of match_data
for j in range(len(v)):
    if len(v[j]) == 8:
        final.append(match_data[j])
        
ids = dict()
fireteamids = dict()
i = 0
for mtch in final:
    ids[i] = []
    fireteamids[i] = []
    for player in mtch["Response"]["entries"]:
        #print(i)
        fireteamids[i].append(player["values"]["fireteamId"]["basic"]["value"])
        ids[i].append(player["characterId"])
    i = i+1
###Check length of fireteam id
for x,y in fireteamids.items():
    print(len(y))        
           


full_list = [teamids for j in fireteamids for teamids in fireteamids[j]]
   
teamsets = list()
for j in fireteamids: #matches
    teamsets.append([])
    team1set = set()
    team2set = set()
    for k in range(4):
        team1set.add(ids[j][k])
    for k in range(4,8):
        team2set.add(ids[j][k])
    
    teamsets[j].append(team1set)
    teamsets[j].append(team2set)
 

print(teamsets[0:10])


allsets = [frozenset(tmset) for mtchsets in teamsets for tmset in mtchsets]
print(allsets[0:10])

setofsets = set(allsets)
print(str(len(setofsets)))


#The above indicates that the fireteamID may not be directly representative of the 
#team composition, since there are 15991 different teams in terms of the characterIDs 
#they are composed of, but 8830 different fireteamIDs. 
#However since we are only looking at full teams it would be better to check only among those.


fullteam1matches = []
fullteam2matches = []
fullteam1fireteamid = []
fullteam2fireteamid = []
for mtch in fireteamids:
    team1set = set()
    team2set = set()
    chk = 0
    for k in range(4):
        team1set.add(fireteamids[mtch][k])
    for k in range(4,8):
        team2set.add(fireteamids[mtch][k])
    if len(team1set) ==1:
        fullteam1matches.append(mtch)
        fullteam1fireteamid.append(fireteamids[mtch][0])
        #chk = 1
    if len(team2set) ==1 :
        fullteam2matches.append(mtch)
        fullteam2fireteamid.append(fireteamids[mtch][5])



fullteam1fireteamid[1:10]
fullteam2fireteamid[1:10]











