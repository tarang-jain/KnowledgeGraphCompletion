import os
import tqdm
# from bert_serving.client import BertClient
import pickle

all_entities = set()
for file in os.listdir("Triplets"):
    Lines = open("Triplets/" + file,"r").readlines()
    for line in Lines:
        triplet = line.split('\t')
        all_entities.add(triplet[1])
        all_entities.add(triplet[-1])

with open("all_entities", "w") as write_file:
    for entity in list(all_entities):
        write_file.write(entity)
