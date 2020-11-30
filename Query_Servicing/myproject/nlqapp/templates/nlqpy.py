import spacy
from owlready2 import *
from spacy.tokenizer import Tokenizer
from .search_accident import *
#from django.http import HttpResponse
#extends /home.html
#print(request.POST.get('fname', None))
#from rdflib import URIRef, Namespace
class SparqlQueries:
    def __init__(self):
        my_world = World()
        onto_path.append(r"/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II-20200816T091910Z-001/KG IMPRINT II")
        #onto_path.append(r"/home/qumar_1921cs27/")
        my_world.get_ontology("https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl").load() #path to the owl file is given here
        #sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()
        #in_path = '/home/qumar_1921cs27/new_data.txt'
        #nlp = spacy.load("en_core_web_sm")
        #with open(in_path) as f:
        #    sentences = f.read().split('\n')
        #for i, sentence in enumerate(sentences):
        #    if sentence is not '':
        #        doc = nlp(sentence)
        #        doc = search(self,doc)


    def search(self,doc):
        print('\n\n')
        #doc='Which Aircraft have Honeywell Engine Manufacturer?'
        #doc=input('Enter your query:\n')
        #doc=request.POST.get('fname', None)
        nlp = spacy.load("en_core_web_sm")
        nlp.tokenizer = Tokenizer(nlp.vocab)
        new_doc=nlp(doc)
        query_line='select ?'
        noun1=''
        noun2=''
        q_noun=''
        q_propn=''
        c_pnoun=0
        c_noun=0
        pre_pos='qumar'
        #print(new_doc)
        #print(new_doc[0])
        #print("\ntext\t lemma\t pos\t tag\t dep_\t shape\t is_alpha\t is_stop\n")
        wh=0
        lh=0
        for token in new_doc:
            if(token.text=='Which'):
                wh=wh+1
            elif(token.dep_=='ROOT'):
                lh=lh+1
            exit
        if(wh>=1):
            query_line='select ?'
            noun1=''
            noun2=''
            q_noun=''
            q_propn=''
            c_pnoun=0
            c_noun=0
            pre_pos='qumar'
            #print("\ntext\t lemma\t pos\t tag\t dep_\t shape\t is_alpha\t is_stop\n")
            for token in new_doc:
                #print(token.text,"\t", token.lemma_,"\t", token.pos_,"\t", token.tag_,"\t", token.dep_,"\t",token.shape_,"\t", token.is_alpha,"\t", token.is_stop)
                if(new_doc[4].pos_=='VERB'):
                    if(token.pos_=='NOUN' and c_noun==0):
                        noun1=token.lemma_.capitalize()
                        query_line=query_line+noun1
                        c_noun=c_noun+1
                    elif(token.pos_=='AUX'):
                        query_line=query_line+' where {?'+noun1+' rdf:has'
                    elif(pre_pos=='AUX'):
                        noun2=token.lemma_.capitalize()
                        query_line=query_line+noun2+'\n?'+noun2+'. ?'+noun2+' rdf:has'
                    elif(pre_pos=='VERB' and c_pnoun==0):
                        q_propn='rdf:'+token.text.capitalize()
                        c_pnoun=c_pnoun+1
                    elif(token.pos_=='PROPN' or token.pos_=='NOUN' and c_pnoun>0):
                        query_line=query_line+token.lemma_.capitalize()
                    pre_pos=token.pos_
                else:
                    #print(token.text,"\t", token.lemma_,"\t", token.pos_,"\t", token.tag_,"\t", token.dep_,"\t",token.shape_,"\t", token.is_alpha,"\t", token.is_stop)
                    if(token.pos_=='NOUN' and c_noun==0):
                        q_noun=token.lemma_.capitalize()
                        query_line=query_line+q_noun
                        c_noun=c_noun+1
                    if(token.pos_=='AUX'):
                        query_line=query_line+' where {?'+q_noun+' rdf:has'
                    if(pre_pos=='AUX'):
                        q_propn='rdf:'+token.lemma_.capitalize()
                        c_pnoun=c_pnoun+1
                    elif(token.pos_=='PROPN' or token.pos_=='NOUN' and c_pnoun!=0):
                        query_line=query_line+token.lemma_.capitalize()
                    pre_pos=token.pos_
            query_line=query_line+' '+q_propn+'}'
            #print("\nSparql:",query_line,"\n\n")
        else:
            hvg=[]
            lis=[]
            noun_sub=[]
            d_obj=[]
            comp=[]
            no=[]
            mor=[]
            less=[]
            num=[]
            ns=0
            ls=0
            mr=0
            n=0
            hv=0
            for token in new_doc:
                if(token.pos_=='NOUN' or token.pos_=='PROPN'):
                    noun_sub.append(token.text.capitalize())
                    ns=ns+1
                if(token.dep_=='dobj'):
                    d_obj.append(token.text.capitalize())
                if(token.dep_=='compound'):
                    comp.append(token.text.capitalize())
                if(token.text=='not'):
                    no.append(token.text.capitalize())
                    n=n+1
                if(token.text=='list'):
                    lis.append(token.text.capitalize())
                if(token.lemma_=='more'):
                    mor.append(token.text.capitalize())
                    mr=mr+1
                if(token.lemma_=='less'):
                    less.append(token.text.capitalize())
                    ls=ls+1
                if(token.pos_=='NUM'):
                    num.append(token.text.capitalize())
                if(token.tag_=='VBG'):
                    hvg.append(token.text.capitalize())
                    hv=hv+1
            if(mr>0):
                if(ns>1):
                    print("\tSELECT ?",noun_sub[1]," ?",noun_sub[2],'\n')
                    print("\tWHERE{?"+noun_sub[1]+' rdf:has'+noun_sub[2],'?'+noun_sub[2])
                    print("\n\tFILTER (?"+noun_sub[2]+'>'+num[0]+')')
            elif(ls>0):
                    print("\tSELECT ?"+noun_sub[1]+" ?"+noun_sub[2]+'\n')
                    print("\tWHERE{?"+noun_sub[1]+' rdf:has'+noun_sub[2]+' ?'+noun_sub[2])
                    print("\n\tFILTER (?"+noun_sub[2]+ '<'+num[0]+')')
            else:
                print("\tSELECT DISTINCT ?"+noun_sub[0]+'\n')
                print("\tWHERE{?"+noun_sub[1]+' rdf:has'+noun_sub[1]+noun_sub[0]+' ?'+noun_sub[0]+'.\n\t')
                if(hv>0):
                    print("?"+d_obj[0]+' rdf:has'+comp[0]+comp[1],'?'+d_obj[0]+'.\n')
                if(n>0):
                    print("MINUS{\n")
                    print(" ?"+noun_sub[1]+' rdf:has'+d_obj[0],' ?'+d_obj[0]+'.\n')
                    print(" ?"+d_obj[0]+' rdf:has'+comp[0]+comp[1]+' rdf:'+d_obj[1]+'.')
                else:
                    print('\n')
            print('\n }\n')
            query_line=query_line+' '+q_propn+'}'

        print("\nSparql:",query_line,"\n\n")
        response1=searchq(self,query_line)
        return response1


def search1(q1):
    runQuery = SparqlQueries()
    result1=runQuery.search(q1)
    return result1
