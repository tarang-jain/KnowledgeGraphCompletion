#THIS FILE IS USED TO EXTRACT ALL THE UNSTRUCTURED TEXT AND EXCLUDE ALL THE REMAINING INFORMATION FROM REPORTS

import os
import fileinput

"""Remove the processed_texts directory if it already exists"""
os.system("rm -rf processed_texts")
os.system("for i in `seq 1981 2018`; do for j in `seq 1 12`; do mkdir -p processed_texts/$i/$j; done; done")
#for year in range(1983, 2019):
#    for month in range(1, 13):
#        for file in os.listdir(os.path.join(str(year), str(month))):
#            Lines = open(os.path.join(str(year), str(month), file), "r").readlines()
#            with open(os.path.join("processed_texts", str(year), str(month), file), "a+") as write_file:
#                for line in Lines:
#                    if "The National Transportation Safety Board (NTSB), established in 1967" in line or "Administrative Information" == line.strip() :
#                        break
#                    if "INFORMATION" not in line.strip() and "National Transportation Safety Board" not in line.strip() and line.strip() != "Analysis":
#                        write_file.write(line)

# write = False
# for year in range(1983, 2019):
#     for month in range(1, 13):
#         for file in os.listdir(os.path.join(str(year), str(month))):
#             Lines = open(os.path.join(str(year), str(month), file), "r").readlines()
#             with open(os.path.join("processed_texts", str(year), str(month), file), "a+") as write_file:
#                 for i in range(len(Lines)):
#                     line=Lines[i]
#                     if "The National Transportation Safety Board (NTSB), established in 1967" in line or "Administrative Information" == line.strip() :
#                         break
#                     if line.strip() == "Analysis" or line.strip() == "Probable Cause and Findings" or line.strip() == "Factual Information":
#                         write = True
#                         continue
#                     if write and "INFORMATION" not in line.strip() and "National Transportation Safety Board" not in line.strip():
#                         if len(line.split()) <= 3 and Lines[i-1][-1] == '.' or line.strip() == "Findings":
#                             write = False
#                             continue
#                         write_file.write(line)

years = list(range(1982, 2019))

written_count = 0
for year in years:
    if 1982 <= year and year <= 1988:
        for month in range(1, 13):
            for file in os.listdir(os.path.join("Texts", str(year), str(month))):
                Lines = open(os.path.join("Texts", str(year), str(month), file), "r").readlines()
                write_file = open(os.path.join("processed_texts", str(year), str(month), file), "w")
                for i in range(len(Lines)):
                    if Lines[i].strip() == "Analysis":
                        for j in range(i+1, len(Lines)):
                            if Lines[j].strip() != "Probable Cause and Findings":
                                line = Lines[j].replace("FLT", "FLIGHT")
                                line = line.replace("PLT", "PILOT")
                                line = line.replace("ACFT", "AIRCRAFT")
                                line = line.replace("ATC", "AIR TRAFFIC CONTROL")
                                line = line.replace("&", "AND")
                                line = line.replace("QTS", "QUARTERS")
                                line = line.replace("RWY", "RUNWAY")
                                if "FT" in line.split(" "):
                                    line = line.replace("FT", "FEET")
                                if "RT" in line.split(" "):
                                    line = line.replace("RT", "RIGHT")
                                if "PWR" in line.split(" "):
                                    line = line.replace("PWR", "POWER")
                                if "APRX" in line.split(" "):
                                    line = line.replace("APRX", "APPROXIMATELY")
                                if "APCH" in line.split(" "):
                                    line = line.replace("APCH", "APPROACH")
                                write_file.write(line)
                                written_count +=1
                            else:
                                break
                    elif written_count >0:
                        written_count =0
                        break

    elif 1989 <= year and year <= 1994:
        for month in range(1, 13):
            for file in os.listdir(os.path.join("Texts", str(year), str(month))):
                Lines = open(os.path.join("Texts", str(year), str(month), file), "r").readlines()
                write_file = open(os.path.join("processed_texts", str(year), str(month), file), "w")
                cause_heading_found = False
                for i in range(len(Lines)):
                    if Lines[i].strip() == "Analysis":
                        for j in range(i+1, len(Lines)):
                            if Lines[j].strip() != "Probable Cause and Findings" and not cause_heading_found:
                                line = Lines[j].replace("FLT", "FLIGHT")
                                line = line.replace("PLT", "PILOT")
                                line = line.replace("ACFT", "AIRCRAFT")
                                line = line.replace("ATC", "AIR TRAFFIC CONTROL")
                                line = line.replace("&", "AND")
                                line = line.replace("QTS", "QUARTERS")
                                line = line.replace("RWY", "RUNWAY")
                                if "FT" in line.split(" "):
                                    line = line.replace("FT", "FEET")
                                if "RT" in line.split(" "):
                                    line = line.replace("RT", "RIGHT")
                                if "PWR" in line.split(" "):
                                    line = line.replace("PWR", "POWER")
                                if "APRX" in line.split(" "):
                                    line = line.replace("APRX", "APPROXIMATELY")
                                if "APCH" in line.split(" "):
                                    line = line.replace("APCH", "APPROACH")
                                write_file.write(line)
                                written_count +=1
                            elif Lines[j].strip() == "Findings":
                                break
                            elif Lines[j].strip() == "Probable Cause and Findings":
                                cause_heading_found = True
                            elif cause_heading_found \
                                and Lines[j].strip() != "The National Transportation Safety Board determines the probable cause(s) of this accident to be:" \
                                and "Page" not in Lines[j].strip():
                                line = Lines[j].replace("FLT", "FLIGHT")
                                line = line.replace("PLT", "PILOT")
                                line = line.replace("ACFT", "AIRCRAFT")
                                line = line.replace("ATC", "AIR TRAFFIC CONTROL")
                                line = line.replace("&", "AND")
                                line = line.replace("QTS", "QUARTERS")
                                line = line.replace("RWY", "RUNWAY")
                                if "FT" in line.split(" "):
                                    line = line.replace("FT", "FEET")
                                if "RT" in line.split(" "):
                                    line = line.replace("RT", "RIGHT")
                                if "PWR" in line.split(" "):
                                    line = line.replace("PWR", "POWER")
                                if "APRX" in line.split(" "):
                                    line = line.replace("APRX", "APPROXIMATELY")
                                if "APCH" in line.split(" "):
                                    line = line.replace("APCH", "APPROACH")
                                write_file.write(line)
                    elif written_count >0:
                        written_count =0
                        cause_heading_found= False
                        break

    elif 1995 <= year and year <= 2008:
        for month in range(1, 13):
            for file in os.listdir(os.path.join("Texts", str(year), str(month))):
                Lines = open(os.path.join("Texts", str(year), str(month), file), "r").readlines()
                write_file = open(os.path.join("processed_texts", str(year), str(month), file), "w")
                cause_heading_found = False
                findings_heading_found = False
                factual_information_heading_found = False
                for i in range(len(Lines)):
                    if Lines[i].strip() == "Analysis":
                        for j in range(i+1, len(Lines)):
                            if Lines[j].strip() != "Probable Cause and Findings" and not cause_heading_found:
                                write_file.write(Lines[j])
                                written_count +=1
                            elif Lines[j].strip() == "Findings":
                                findings_heading_found = True
                            elif Lines[j].strip() == "Factual Information":
                                factual_information_heading_found = True
                            elif Lines[j].strip() == "Probable Cause and Findings":
                                cause_heading_found = True
                            elif cause_heading_found and not findings_heading_found \
                                and "The National Transportation Safety Board determines" not in Lines[j].strip() \
                                and "Page" not in Lines[j].strip():
                                write_file.write(Lines[j])
                            elif factual_information_heading_found and "Page" not in Lines[j].strip():
                                if Lines[j].strip() == "Pilot Information" \
                                   or Lines[j].strip() == "Flight Instructor Information" \
                                   or Lines[j].strip() == "Student Pilot Information":
                                    break
                                else:
                                    write_file.write(Lines[j])
                    elif written_count >0:
                        written_count =0
                        cause_heading_found= False
                        break

    elif 2009 <= year and year <= 2018:
        for month in range(1, 13):
            for file in os.listdir(os.path.join("Texts", str(year), str(month))):
                Lines = open(os.path.join("Texts", str(year), str(month), file), "r").readlines()
                write_file = open(os.path.join("processed_texts", str(year), str(month), file), "w")
                cause_heading_found = False
                findings_heading_found = False
                factual_information_heading_found = False
                for i in range(len(Lines)):
                    if Lines[i].strip() == "Analysis":
                        for j in range(i+1, len(Lines)):
                            if Lines[j].strip() != "Probable Cause and Findings" and not cause_heading_found:
                                write_file.write(Lines[j])
                                written_count +=1
                            elif Lines[j].strip() == "Findings":
                                findings_heading_found = True
                            elif Lines[j].strip() == "Factual Information":
                                factual_information_heading_found = True
                            elif Lines[j].strip() == "Probable Cause and Findings":
                                cause_heading_found = True
                            elif cause_heading_found and not findings_heading_found \
                                and "The National Transportation Safety Board determines" not in Lines[j].strip() \
                                and "Page" not in Lines[j].strip():
                                write_file.write(Lines[j])
                            elif factual_information_heading_found and "Page" not in Lines[j].strip():
                                if Lines[j].strip() == "Pilot Information" \
                                   or Lines[j].strip() == "Flight Instructor Information" \
                                   or Lines[j].strip() == "Student Pilot Information" \
                                   or Lines[j].strip() == "History of Flight":
                                    break
                                else:
                                    write_file.write(Lines[j])
                    elif written_count >0:
                        written_count =0
                        cause_heading_found= False
                        break
#
# for year in list(range(1982, 1991)):
#     for month in range(1, 13):
#         for file in os.listdir(os.path.join("processed_texts", str(year), str(month))):
#             with fileinput.FileInput(os.path.join("processed_texts", str(year), str(month), file), inplace=True, backup='.bak') as file:
#                 for line in file:
#                     if "FLT" in line.split(" "):
#                         print(line.replace("FLT", "FLIGHT"), end='')
#                     if "PLT" in line.split(" "):
#                         print(line.replace("PLT", "PILOT"), end='')
#                     if "ACFT" in line.split(" "):
#                         print(line.replace("ACFT", "AIRCRAFT"), end='')
