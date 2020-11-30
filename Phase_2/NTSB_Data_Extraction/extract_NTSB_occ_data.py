import os
import re
import numpy as np
import csv
import pickle
from occ_class import *

def get_all_occs(report,accident_id, lines, l_iter):
    l_iter+=1
    list_of_occs=[]
    occurrence = ""
    phase_of_op=""
    list_of_findings=[]
    findings_start=False
    while True:
        # print(accident_id+" "+report+" "+str(l_iter))
        if (lines[l_iter]).startswith("Occurrence #"):
            parts = (lines[l_iter]).split(":")
            occurrence = parts[1]
            occurrence=' '.join(occurrence.split())
        elif (lines[l_iter]).startswith("Phase of Operation:"):
            parts = (lines[l_iter]).split(":")
            phase_of_op = parts[1]
            phase_of_op = ' '.join(phase_of_op.split())
        elif lines[l_iter]=="Findings":
            findings_start=True 
        elif lines[l_iter]=="Factual Information":
            instance=occ(occurrence,phase_of_op,list_of_findings)
            list_of_occs.append(instance)
            occurrence = ""
            phase_of_op=""
            list_of_findings=[]
            findings_start=False 
            break
        elif findings_start and (not (lines[l_iter]).startswith("------")):
            if re.search(r"^[0-9]+\.", lines[l_iter]):
                finding = re.sub(r"^[0-9]+\.", "", lines[l_iter])
                finding = ' '.join(finding.split())
                list_of_findings.append(finding)
        elif (lines[l_iter]).startswith("------"):
            instance=occ(occurrence,phase_of_op,list_of_findings)
            list_of_occs.append(instance)
            occurrence = ""
            phase_of_op=""
            list_of_findings=[]
            findings_start=False 
        l_iter+=1
    final_answer = all_occ(list_of_occs)
    return l_iter, final_answer

        


def get_cause_chain(report,text):
    ## text is the contents of the report currently being processed
    ## returns the accident number and the all_occs class object

    # *************find accident number*********************
    accident_id = ""
    accident_id_found=False
    lines  = text.split('\n')
    l_iter=0
    all_occ_instance=None
    while l_iter < len(lines):
        if (not accident_id_found) and lines[l_iter] =="Accident Number:":
            l_iter+=1
            accident_id = lines[l_iter]
            accident_id_found=True
        elif accident_id_found and lines[l_iter]=="Findings":
            ## occurrences start from here. Start extracting
            factual_info_iter , all_occ_instance = get_all_occs(report,accident_id,lines,l_iter)
            l_iter = factual_info_iter
            break
        l_iter+=1

    return accident_id, all_occ_instance



causal_dict={}
directory = "Texts/"

for year_dirs in os.listdir(directory):
    if int(year_dirs)>2007:
        continue
    for month_dir in os.listdir(directory+year_dirs+"/"):
        for report in os.listdir(directory+year_dirs+"/"+month_dir+"/"):
            file = open(directory+year_dirs+"/"+month_dir+"/"+report,'r')
            contents = file.read()
            accident_id, all_occs_instance = get_cause_chain(report,contents)
            if accident_id=="":
                print("The report "+report+" does not list an accident. Most probably an incident report.\n")
            elif accident_id in causal_dict:
                existing_report = (causal_dict[accident_id])[0]
                print(accident_id+" has two reports : "+existing_report+" and "+directory+year_dirs+"/"+month_dir+"/"+report+"\n\n")
            else:
                causal_dict[accident_id] = (directory+year_dirs+"/"+month_dir+"/"+report,all_occs_instance)


with open('occ_dict.pkl', 'wb') as fp:
    pickle.dump(causal_dict, fp, protocol=pickle.HIGHEST_PROTOCOL)

