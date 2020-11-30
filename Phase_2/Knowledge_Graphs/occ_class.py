import numpy as np

class occ:
    def __init__(self,occurrence, phase_of_op, all_findings):
        self.occurrence = occurrence
        self.phase_of_op = phase_of_op
        self.all_findings = all_findings

    def get_occ(self):
        return self.occurrence

    def get_phase_op(self):
        return self.phase_of_op

    def get_all_findings(self):
        return self.all_findings


class all_occ:
    def __init__(self,list_of_occs):
        self.list_of_occs = list_of_occs

    ## all occurrences in sorted order. It means that the first element of the list is occurrence 1
    def sequence_of_occs(self):
        only_occurrences = [occur.get_occ() for occur in self.list_of_occs]
        return only_occurrences

    def sequence_of_findings(self):
        only_occurrences = [occur.get_all_findings() for occur in self.list_of_occs]
        return only_occurrences

    def get_occs_str_seq(self):
        only_occurrences = [occur.get_occ() for occur in self.list_of_occs]
        joiner = " --> "
        seq=joiner.join(only_occurrences)
        return seq
