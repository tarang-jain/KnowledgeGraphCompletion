from owlready2 import *
import os
import tqdm
import pickle

default_world.get_ontology("/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II/aircraft_base.owl").load()
onto = default_world.get_ontology("/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II/AircraftAccident.owl").load()
#default_world.set_backend(filename = "/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II/AircraftAccident_new.sqlite3")
#default_world.set_backend(filename = "/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II/aircraft_base_new.sqlite3")

default_world.save()

graph = default_world.as_rdflib_graph()

all_queries = open("cleaned_sparql_queries2.txt", "r").readlines()

current_query = ""
query_count = 0

for line in all_queries:
    if "PREFIX" in line:
        query_count += 1
        current_query = str(query_count)
    if len(current_query) != 0:
        with open(current_query + ".txt", "a+") as write_file:
            if not ("1-" in line or "2-" in line or "3-" in line):
                write_file.write(line)

query_count = 119
all_query_response_pairs = dict()
all_query_response_pairs_unanswered = dict()
all_query_response_pairs_answered = dict()

for query_number in tqdm.tqdm(range(1,query_count+1)):
    with open(str(query_number) + ".txt", 'r') as current_query_file:
        data = (current_query_file.read().replace('\n', ' ')).strip('\ufeff')
        if "->" in data:
            data = data.replace("->", "")
        r = list(graph.query(data))
        all_query_response_pairs[query_number] = str(r)
        if len(r) == 0:
            all_query_response_pairs_unanswered[query_number] = str(r)
        else:
            all_query_response_pairs_answered[query_number] = str(r)

with open("all_query_response_pairs.pkl", "wb") as write_file:
    pickle.dump(all_query_response_pairs, write_file)
#
with open("all_query_response_pairs_unaswered.pkl", "wb") as write_file:
    pickle.dump(all_query_response_pairs_unanswered, write_file)
#
with open("all_query_response_pairs_answered.pkl", "wb") as write_file:
    pickle.dump(all_query_response_pairs_answered, write_file)
