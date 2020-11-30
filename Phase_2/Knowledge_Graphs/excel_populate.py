import pandas as pd
import os
import re
from owlready2 import *
import pickle
import numpy as np

findings_info = pickle.load(open("event_findings_dict.pkl", "rb"))
# print(findings_info.keys())
base_onto = get_ontology("aircraft_base.owl").load()
# events_onto = get_ontology("Events.owl").load()
# print(events_onto)
merged_onto = get_ontology("AircraftAccidentEvent_merged.owl").load()
instance_class_dict = dict()
all_instance_classes = set()
# for instance in events_onto.EventType.instances():
#     instance_class_dict[str(instance)[7:]] = str(instance.__class__)
# for cls in instance_class_dict.values():
#     all_instance_classes.add(cls)

# print("The range for the 'hasEvent' relation is:\n")
# for cls in all_instance_classes:
    # print(cls)

def populate_excel(accidentID, occ_list, row_count, occ):
    data_frame.at[row_count, 'Accident'] = "AccidentNumber_" + accidentID
    event = occ_list[occ-1].strip()
    event = event.strip('\n')
    accident_findings_info = []
    if accidentID in findings_info:
        if event in ["IN FLIGHT ENCOUNTER WITH WEATHER", "ON GROUND/WATER COLLISION WITH OBJECT", \
                     "ON GROUND/WATER ENCOUNTER WITH WEATHER", "IN FLIGHT COLLISION WITH OBJECT"]:
            accident_findings_info = list(findings_info[accidentID])
            for i in range(len(accident_findings_info)):
                occurrence_number, finding_info = accident_findings_info[i]
                if occurrence_number == occ - 1:
                    event = finding_info
                    break
        event = event.strip()
        event = ('_'.join(event.split()))
        data_frame.at[row_count, str(occ)] = event
    return

accident_occs_mappings = pickle.load(open("causal_dict.p", "rb"))
count = -1
data_frame = pd.DataFrame(index = np.arange(len(accident_occs_mappings)*6), columns = ['Accident', '1', '2', '3', '4', '5', '6'])
data_frame = data_frame.astype(str)
all_occs = []
print(len(list(accident_occs_mappings.keys())))
for key in list(accident_occs_mappings.keys()):
    _, occ_class_object = accident_occs_mappings[key]
    if occ_class_object is not None:
        count += 1
        occ_list = occ_class_object.sequence_of_occs()
        if len(occ_list)>=1 and len(key) != 0:
            all_occs.append((key, occ_list))

C = 0
for i in range(1, 7):
    for j in range(len(all_occs)):
        key, occ_list = all_occs[j]
        if len(occ_list)>=i:
            count += 1
            populate_excel(accidentID=key, occ_list=occ_list, row_count=count, occ=i)

data_frame = data_frame[data_frame['Accident'] != 'nan']
print(data_frame.columns)
data_frame.to_excel('./OntologyEventsData.xlsx')
