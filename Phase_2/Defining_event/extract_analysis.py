import pickle
import os
import tqdm

all_text = open("extracted_cause.txt", "r").readlines()
report_count = 0
all_accident_info = dict()
all_unique_defining_events = set()
Reports_root_dir = "./Reports"
for i in tqdm.tqdm(range(len(all_text))):
    all_text[i] = (all_text[i].strip("\ufeff")).strip("\n")
    if '_' in all_text[i] and len(all_text[i].split('_')) == 3:
        year, month, _ = all_text[i].split('_')
        for line in open(os.path.join(Reports_root_dir, year, month, all_text[i]), "r").readlines():
            if "Defining event" in line:
                defining_event = line[:-17].strip()
                all_unique_defining_events.add(defining_event)
                report_count += 1
                accident_id = all_text[i+2].strip('\n')
                accident_analysis = ""
                for j in range(i+3, len(all_text)):
                    all_text[j] = all_text[j].strip()
                    if all_text[j].startswith("Probable Cause and Findings") or '_' in all_text[j]:
                         accident_analysis = accident_analysis.strip('\n')
                         if len(accident_analysis.strip()) != 0:
                             all_accident_info[accident_id] = (accident_analysis.strip(), defining_event)
                             break
                    elif not all_text[j].startswith("Page") and not (len(all_text[j].split()) == 1 and any(char.isdigit() for char in all_text[j])):
                        accident_analysis = accident_analysis + ' ' + all_text[j]

pickle.dump(all_accident_info, open("all_accident_info.pkl", "wb"))
print(all_unique_defining_events)
