import occ_class
import pickle

all_occs = list(pickle.load(open("occ_dict.p", "rb")).values())

all_causes = set()
all_factors = set()
all_agents = set()

for obj in all_occs:
    _, occ_class_object = obj
    if occ_class_object is not None:
        findings_list = occ_class_object.sequence_of_findings()
        for finding in findings_list:
            for each_finding in finding:
                if "(C)" in each_finding or "Cause" in each_finding:
                    all_causes.add(each_finding)
                elif "(F)" in "Factor" in each_finding:
                    all_factors.add(each_finding)

with open("all_causes.txt", "w") as causes_file, open("all_factors.txt", "w") as factors_file:
    for cause in list(all_causes):
        causes_file.write(cause + "\n")

    for factor in list(all_factors):
        factors_file.write(factor + "\n")

for cause in all_causes:
    cause1 = cause.strip().split(" - ")
    if len(cause1)>2:
        all_agents.add(cause1[-1])

agents_file = open("all_agents.txt", "w")
for agent in list(all_agents):
    agents_file.write(agent + '\n')

for obj in all_occs:
    _, occ_class_object = obj
    if occ_class_object is not None:
        occ_list = occ_class_object.sequence_of_occs()
        for event in occ_list:
            all_events.add(event)

with open("all_events.txt", "w") as events_file:
    for event in list(all_events):
        events_file.write(event + "\n")
