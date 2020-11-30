from treelib import Node, Tree
import numpy as np
import argparse
import re
import pickle

class hierarchy_tree:

    def __init__(self, rows, split_str):
        self.rows = rows
        self.split_str = split_str

    ## GLOBALLY ACCESSIBLE STARTS

    parent_stack = [] ## This is a stack consisting of triples of event_names, event ids and their checking index
    last_event_id = ""
    last_event_name = ""
    last_event_id_check_index=0

    ## GLOBALLY ACCESSIBLE ENDS

    def is_parent(self,parent, parent_check_index, child):## parent is a event id and and child is the supposedly child event id.
        pc = parent[:parent_check_index+1]
        cc = child[:parent_check_index+1]
        if pc==cc:
            return True
        else:
            return False


    def find_parent(self,event_id):
        check_last_event = self.is_parent(self.last_event_id, self.last_event_id_check_index, event_id)
        if check_last_event:
            (self.parent_stack).append((self.last_event_name,self.last_event_id,self.last_event_id_check_index))
            return self.parent_stack[-1]
        else:
            while len(self.parent_stack)!=0:
                cur_parent_id = (self.parent_stack)[-1][1]
                cur_parent_check_index = (self.parent_stack)[-1][2]
                is_par = self.is_parent(cur_parent_id, cur_parent_check_index, event_id)
                if is_par:
                    return (self.parent_stack)[-1]
                else:
                    self.parent_stack = (self.parent_stack)[:-1]

            return None

    def find_check_index(self,event_id,parent_event_id): ## This function is to be used only after ensuring that parent_event_id is actually the parent of event_id
        ## event_id and parent_event_id are of same length
        for i in range(len(event_id)):
            if event_id[i]!=parent_event_id[i]:
                return i
        return None ## Should never reach here because ids can't be same



    def build_my_tree(self): ## rows is a list of strings of the format "<event_name>split_str<event_id>" see ok_events.csv for more details. split_str="@#@" by default
        final_tree = Tree()
        root="@#@#root@#@#"
        final_tree.create_node("Root", root)
        for row in self.rows:
            temp = row.split(self.split_str)
            if len(temp)==2:
                [event_name, event_id] = temp
            else:
                print("Following row does not have proper number of columns (maybe an empty string)"+row+'\n')
                continue
            parent_triple = self.find_parent(event_id)
            if parent_triple==None:
                final_tree.create_node(event_name,event_name +"###"+ event_id,parent=root)
            else:
                final_tree.create_node(event_name,event_name + "###" + event_id,parent=parent_triple[0] + "###" + parent_triple[1])
            self.last_event_name = event_name
            self.last_event_id = event_id
            if parent_triple==None:
                self.last_event_id_check_index= 0
            else:
                self.last_event_id_check_index = self.find_check_index(event_id,parent_triple[1])

        return final_tree


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Give CSV filename')
    parser.add_argument('--filename', type=str, default="ok_events.csv", help='CSV filename. File should be in the same folder')
    args = parser.parse_args()

    filename = args.filename

    hierarchy_file = open(filename,'r')
    contents = hierarchy_file.read()
    rows = contents.split('\n')
    hierarchy_file.close()

    htree = hierarchy_tree(rows,"@#@")

    hierarchy = htree.build_my_tree()
    hierarchy.save2file(filename+'_hierarchy.txt')
    
    #Obitain all paths from root to leaves
    paths_to_leaves = hierarchy.paths_to_leaves()
    for path_id in range(len(paths_to_leaves)):
        for event_id in range(len(paths_to_leaves[path_id])):
            if "###" in paths_to_leaves[path_id][event_id]:
                paths_to_leaves[path_id][event_id] = paths_to_leaves[path_id][event_id].split("###")[0]
    print(paths_to_leaves)
    with open("paths_to_leaves.pkl", 'wb') as write_file:
        pickle.dump(paths_to_leaves, write_file)
