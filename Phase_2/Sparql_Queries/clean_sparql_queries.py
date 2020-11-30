import os
import fileinput

Lines = open("manual query generation.txt", "r").readlines()

with open("cleaned_sparql_queries.txt", "w") as write_file:
    for line in Lines:
        if line.strip():
            write_file.write(line)

Lines = open("cleaned_sparql_queries.txt", "r").readlines()

with open("cleaned_sparql_queries2.txt", "w") as write_file:
    for line in Lines:
        if not line[0].isdigit():
            write_file.write(line)

os.remove("cleaned_sparql_queries.txt")

with fileinput.FileInput("cleaned_sparql_queries2.txt", inplace=True, backup='.bak') as file:
    for line in file:
        if "which" in line.lower():
            print(line.replace(line, ""), end='')
        print(line.replace("-> PREFIX", "PREFIX"), end='')
