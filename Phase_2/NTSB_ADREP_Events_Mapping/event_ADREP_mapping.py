import pickle
from bert_serving.client import BertClient
import tqdm
import ngtpy
import re

def clean_finding_seq(s):
    if "(C)" in s:
        s = s.strip("(C)")
    elif "(F)" in s:
        s = s.strip("(F)")
    s = s.strip()
    return s

bc = BertClient(check_length = False)
all_embeddings = []
paths_to_leaves = pickle.load(open("../ADREP_Data_Extraction/paths_to_leaves.pkl", "rb"))
for path in tqdm.tqdm(paths_to_leaves):
    for i in range(1, len(path)):
        path[i] = path[i].strip()
        path[i] = re.sub(r'\([^)]*\)', '', path[i])
        path[i] = re.sub("\(", "", path[i])
        path[i] = re.sub("\)", "", path[i])
        path[i] = re.sub('[0-9]', '', path[i])
        path[i] = re.sub(':', '', path[i])
        path[i] = path[i].lower()
    path = " ||| ".join(path[1:])
    embedding = bc.encode([path])

    all_embeddings.append(embedding.tolist())

with open("full_path_embeddings.pkl", "wb") as write_file:
    pickle.dump(all_embeddings, write_file)


all_embeddings = pickle.load(open("full_path_embeddings.pkl", "rb"))
print(len(all_embeddings[0][0]))
ngtpy.create(b"event_index", len(all_embeddings[0][0]))
index = ngtpy.Index(b"event_index")
for i in range(len(all_embeddings)):
    all_embeddings[i] = all_embeddings[i][0]
index.batch_insert(all_embeddings)
index.save()

all_event_mappings = open("all_event_mappings_bert_base_uncased.txt", "w")
all_events_ntsb = open("all_events.txt").readlines()
for event in all_events_ntsb:
    event_embedding = bc.encode([event.lower()])
    result = index.search(event_embedding, 1)
    for i, o in enumerate(result):
        event_mapping = " --> ".join(paths_to_leaves[int(str(o[0]))])
        all_event_mappings.write(event + "===" + event_mapping + '\n')

event_path_mappings_non_leaf = dict()
event_path_mappings_leaves = dict()
event_path_mappings_leaves_non_exact = dict()

for event in tqdm.tqdm(all_events_ntsb):
    exact_leaf_match = False
    event = event.strip("\n")
    event = event.strip()
    event_lower = event.lower()
    for path in paths_to_leaves:
        for i in range(len(path)):
            node = re.sub(r'\([^)]*\)', '', path[i])
            node = re.sub("\(", "", path[i])
            node = re.sub("\)", "", path[i])
            node = re.sub('[0-9]', '', path[i])
            node = re.sub(':', '', path[i])
            node = re.sub('-', ' ', path[i])
            node = path[i].strip()
            if event_lower == node.lower() and i== len(path)-1:
                event_path_mappings_leaves[event] = path[1:]
                exact_leaf_match = True
            elif event_lower in node.lower() and not exact_leaf_match and i != len(path)-1:
                if event not in event_path_mappings_non_leaf:
                    event_path_mappings_non_leaf[event] = []
                event_path_mappings_non_leaf[event].append(path[i])
                event_path_mappings_non_leaf[event] = list(set(event_path_mappings_non_leaf[event]))
            elif event_lower in node.lower() and not exact_leaf_match and i == len(path)-1:
                if event not in event_path_mappings_leaves_non_exact:
                    event_path_mappings_leaves_non_exact[event] = []
                event_path_mappings_leaves_non_exact[event].append(path[1:])

pickle.dump(event_path_mappings_leaves, open("event_path_mappings_leaves_regex.pkl", "wb"))
pickle.dump(event_path_mappings_non_leaf, open("event_path_mappings_non_leaf_regex.pkl", "wb"))
pickle.dump(event_path_mappings_leaves_non_exact, open("event_path_mappings_leaves_non_exact_regex.pkl", "wb"))
