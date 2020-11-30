import pickle
import os
import tqdm
from bert_serving.client import BertClient
import re
from sklearn.metrics.pairwise import cosine_similarity

events_dict = pickle.load(open("causal_dict.p", "rb"))
findings_info = dict()
event_findings_dict_file = open("event_findings_dict.pkl", "wb")
# bc = BertClient(check_length=False)
all_unique_accident_id = set()
accident_id_file = open("all_unique_accident_ids.txt", "w")
all_unique_objects = set()
all_unique_terrain = set()
all_unique_weather_encounter = set()
all_unique_weather_encounter_on_ground = set()
all_unique_objects_on_ground_collisions = set()

weather_conditions_NTSB = open("weather_conditions_NTSB.txt", "w")
weather_conditions_on_ground_NTSB = open("weather_conditions_on_ground_NTSB.txt", "w")
in_flight_collision_objects_NTSB = open("in_flight_collision_objects_NTSB.txt", "w")
on_ground_collision_objects_NTSB = open("on_ground_collision_objects_NTSB.txt", "w")
terrain_ADREP_mappings = open("terrain_ADREP_mappings.txt", "w")

open_list = ["[","{","("]
close_list = ["]","}",")"]

def clean_finding_seq(s):
    if "(C)" in s:
        s = s.strip("(C)")
    elif "(F)" in s:
        s = s.strip("(F)")
    s = s.strip()
    if s.endswith("(S"):
        s = s.replace("(S", "(S)")
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    if count != 0:
        s = s + ')'
    return s

for key in tqdm.tqdm(events_dict):
    accident_id_file.write(key + '\n')
    findings_info[key] = set()
    all_occ = events_dict[key]
    _, all_occ = all_occ
    if all_occ is not None:
        occ_seq = all_occ.sequence_of_occs()
        findings_seq = all_occ.sequence_of_findings()

        for i in range(len(occ_seq)):
##EVENT: IN FLIGHT COLLISION WITH OBJECT
            if occ_seq[i].strip() == "IN FLIGHT COLLISION WITH OBJECT":
                for j in range(len(findings_seq[i])):
                    if "OBJECT - " in findings_seq[i][j]:
                        findings_seq[i][j] = clean_finding_seq(findings_seq[i][j])
                        all_unique_objects.add(findings_seq[i][j])
                        findings_info[key].add((i, "IN FLIGHT COLLISION WITH OBJECT - " + findings_seq[i][j][9:].strip()))
                        break
                    elif j == len(findings_seq[i])-1:
                        findings_info[key].add((i, "IN FLIGHT COLLISION WITH OBJECT - __UNKOWN__OBJECT"))
                        all_unique_objects.add(f"IN FLIGHT COLLISION WITH OBJECT - __UNKOWN__OBJECT")

##EVENT: ON GROUND/WATER COLLISION WITH OBJECT
            if occ_seq[i].strip() == "ON GROUND/WATER COLLISION WITH OBJECT":
                for j in range(len(findings_seq[i])):
                    if "OBJECT - " in findings_seq[i][j]:
                        findings_seq[i][j] = clean_finding_seq(findings_seq[i][j])
                        all_unique_objects_on_ground_collisions.add(findings_seq[i][j])
                        findings_info[key].add((i, "ON GROUND/WATER COLLISION WITH OBJECT - " + findings_seq[i][j][9:].strip()))
                        break
                    elif j == len(findings_seq[i])-1:
                        findings_info[key].add((i, "ON GROUND/WATER COLLISION WITH OBJECT - __UNKOWN__OBJECT"))
                        all_unique_objects_on_ground_collisions.add("ON GROUND/WATER COLLISION WITH OBJECT - __UNKOWN__OBJECT")
##EVENT: IN FLIGHT COLLISION WITH TERRAIN/WATER
            # elif occ_seq[i].strip() == "IN FLIGHT COLLISION WITH TERRAIN/WATER":
            #     terrain_ADREP_1_encoding = bc.encode(["high terrain, a hill or a mountain"])
            #     terrain_ADREP_2_encoding = bc.encode(["level terrain or water"])
            #     for j in range(len(findings_seq[i])):
            #         if "TERRAIN CONDITION" in findings_seq[i][j]:
            #             findings_seq[i][j] = clean_finding_seq(findings_seq[i][j])
            #             if findings_seq[i][j] not in all_unique_terrain:
            #                 finding_vec = bc.encode([re.sub("\/", "\s", findings_seq[i][j][19:].strip())])
            #                 c1 = cosine_similarity(terrain_ADREP_1_encoding, finding_vec)
            #                 c2 = cosine_similarity(terrain_ADREP_2_encoding, finding_vec)
            #                 if c1 > c2:
            #                     terrain_ADREP_mappings.write("high terrain, a hill or a mountain --> " + \
            #                     "IN FLIGHT COLLISION WITH TERRAIN/WATER" + " - " + findings_seq[i][j][19:].strip() + '\n')
            #                 else:
            #                     terrain_ADREP_mappings.write("level terrain or water --> " + \
            #                     "IN FLIGHT COLLISION WITH TERRAIN/WATER" + " - " + findings_seq[i][j][19:].strip() + '\n')
            #             all_unique_terrain.add(findings_seq[i][j])
            #             findings_info[key].add((i, "IN FLIGHT COLLISION WITH TERRAIN/WATER - " + findings_seq[i][j][19:].strip()))
            #             break
            #         elif j == len(findings_seq[i])-1:
            #             findings_info[key].add((i, "IN FLIGHT COLLISION WITH TERRAIN/WATER - __UNKOWN__TERRAIN_CONDITION"))

#EVENT: IN FLIGHT ENCOUNTER WITH WEATHER
            elif occ_seq[i].strip() == "IN FLIGHT ENCOUNTER WITH WEATHER":
                for j in range(len(findings_seq[i])):
                    if "WEATHER CONDITION" in findings_seq[i][j]:
                        findings_seq[i][j] = clean_finding_seq(findings_seq[i][j])
                        all_unique_weather_encounter.add(findings_seq[i][j])
                        findings_info[key].add((i, "IN FLIGHT ENCOUNTER WITH WEATHER - " + findings_seq[i][j][20:].strip()))
                        break
                    elif j == len(findings_seq[i])-1:
                        findings_info[key].add((i, "IN FLIGHT ENCOUNTER WITH WEATHER - __UNKOWN__WEATHER_CONDITION"))
                        all_unique_weather_encounter.add("IN FLIGHT ENCOUNTER WITH WEATHER - __UNKOWN__WEATHER_CONDITION")

#EVENT: ON GROUND/WATER ENCOUNTER WITH WEATHER
            elif occ_seq[i].strip() == "ON GROUND/WATER ENCOUNTER WITH WEATHER":
                for j in range(len(findings_seq[i])):
                    if "WEATHER CONDITION" in findings_seq[i][j]:
                        findings_seq[i][j] = clean_finding_seq(findings_seq[i][j])
                        all_unique_weather_encounter_on_ground.add(findings_seq[i][j])
                        findings_info[key].add((i, "ON GROUND/WATER ENCOUNTER WITH WEATHER - " + findings_seq[i][j][20:].strip()))
                        break
                    elif j == len(findings_seq[i])-1:
                        findings_info[key].add((i, "ON GROUND/WATER ENCOUNTER WITH WEATHER - __UNKOWN__WEATHER_CONDITION"))
                        all_unique_weather_encounter_on_ground.add("ON GROUND/WATER ENCOUNTER WITH WEATHER - __UNKOWN__WEATHER_CONDITION")


pickle.dump(findings_info, event_findings_dict_file)
for c in all_unique_weather_encounter:
    weather_conditions_NTSB.write("IN FLIGHT ENCOUNTER WITH WEATHER - " + c[20:] + '\n')
for c in all_unique_weather_encounter_on_ground:
    weather_conditions_on_ground_NTSB.write("ON GROUND/WATER ENCOUNTER WITH WEATHER - " + c[20:] + '\n')
for c in all_unique_objects:
    in_flight_collision_objects_NTSB.write("IN FLIGHT COLLISION WITH OBJECT - " + c[9:] + '\n')
for c in all_unique_objects_on_ground_collisions:
    on_ground_collision_objects_NTSB.write("ON GROUND/WATER COLLISION WITH OBJECT - " + c[9:] + '\n')
