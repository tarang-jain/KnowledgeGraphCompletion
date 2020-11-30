import spacy
from owlready2 import *
from spacy.tokenizer import Tokenizer
from .search_accident import *
from .search_all import *
import re
#from django.http import HttpResponse
#extends /home.html
#print(request.POST.get('fname', None))
#from rdflib import URIRef, Namespace
class SparqlQueries:
    def __init__(self):
        my_world = World()
        onto_path.append(r"/home/tarangjain")
        #onto_path.append(r"/home/qumar_1921cs27/")
        my_world.get_ontology("/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II-20200816T091910Z-001/KG IMPRINT II/AircraftAccident.owl").load() #path to the owl file is given here
        #sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()
        #in_path = '/home/qumar_1921cs27/new_data.txt'

    def search(self,new_doc):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(new_doc)
        print(doc)
        x1=''
        x2=''
        y1=''
        z1=''
        p1=''
        p2=''
        c=0
        n=0
        a=0
        r=''
        flag=0
        x=''
        xx=''
        count=0
        cp=0
        y=''
        xx1=''

        #count=0,nlp=''
        print("\ntext\t lemma\t pos\t tag\t dep_\t shape\t is_alpha\t is_stop")
        for token in doc:
            if((token.tag_=='NNS' or token.tag_=='NN' or token.tag_=='NNP' ) and (token.dep_=='compound' or token.dep_=='nsubj' or token.dep_=='nsubjpass' or token.dep_=='poss' or token.dep_=='ROOT' or token.dep_=='dobj' or token.dep_=='pobj') and n==0 ):
                x1=token.lemma_.capitalize()
                n+=1
                a+=1
                print(x1)
            #if((token.tag_=='NNS' or token.tag_=='NN' or token.pos_=='PROPN' ) and (token.dep_=='nsubj' or token.dep_=='nsubjpass' or token.dep_=='poss' or token.dep_=='compound' or token.dep_=='pobj') and flag==0 and n==0):
                #x=token.lemma_.capitalize()
                #flag+=1
            elif((token.tag_=='NNS' or token.tag_=='NN' or token.pos_=='PROPN' ) and (token.dep_=='dobj' or token.dep_=='compound' or token.dep_=='ROOT' or token.dep_=='nsubj' or token.dep_=='ROOT' or token.dep_=='attr')  ):
                xx=token.lemma_.capitalize()
                xx1=xx1+xx
                flag+=1


            elif(token.tag_=='NN' and token.dep_=='conj'):
                x2=token.lemma_.capitalize()
            #elif(( token.tag_=='NNP' ) and (token.dep_=='dobj' or token.dep_=='pobj' or token.dep_=='compound' or token.dep_=='acomp' or token.dep_=='ROOT') and c==0):
                #y1=token.lemma_.capitalize()
                #c+=1
            elif(token.tag_=='NN' and token.dep_=='conj'):
                y2=token.lemma_.capitalize()
            elif(token.tag_=='NNP' and (token.dep_=='nmod' or token.dep_=='dep' or token.dep_=='attr')):
                z1=token.lemma_.capitalize()
            elif(token.tag_=='NNP' and token.dep_=='conj'):
                z2=token.lemma_.capitalize()
            print(token.lemma+1)
            print(token.text,'\t', token.lemma_,'\t', token.pos_,'\t', token.tag_,'\t', token.dep_,'\t', token.shape_,'\t', token.is_alpha,'\t', token.is_stop)
        #        self.graph = my_world.as_rdflib_graph()
        #sparql1='SELECT DISTINCT ?'+x1+' ? where{ ?x a rdf:'+x1+'. ?'+x1+' ?p rdf:'+y1+' }'
        sparql1='SELECT DISTINCT ?'+x1+' where{ ?'+x1+' ?p1 rdf:'+y1+' }'
        sparql2='SELECT ?'+x1+' ?'+y1+' where{ ?'+x1+' ?'+p1+' ?'+y1+' }'
        sparql3='SELECT ?'+x1+' ?'+y1+' where{ ?'+x1+' ?'+p1+' ?'+y1+'. ?'+y1+' ?'+p2+' ?'+z1+' }'
        sparql4='SELECT ?'+x1+' ?'+x2+' where{ ?'+x1+' ?'+p1+' ?'+y1+'. ?'+y1+' ?'+p2+' ?'+z1+' }'
        sparql5='SELECT DISTINCT ?sub ?obj where{ ?sub ?'+p1+' ?obj }'
        z=x1
        #print(sparql1)








        for token in doc:
            #y=str(token)
            y=token.lemma_.capitalize()
            print('typte of token is:',type(y))
            #v=get_class(self,y,x1)
            pr=get_predicate(self,y,x1)
            r=' '.join(str(item) for item in pr)
            #print('hiiii',r1)
            #r2=r1.replace("{'type'}",'')
            #r1=r2.replace("{'domain'}",'')
            print('hellooo',r)
            if(r!='' and r!="{'type'} {'domain'}" and r!="{'first'} {'type'} {'domain'} {'range'}" and r!="{'type'} {'range'}" and r!="{'type'} {'domain'} {'range'}"):
                cp+=1
                y1=y
                print(y)
                break

        if(cp>0):
            z='s'
            v=get_class(self,y,x1)
            print(v)
            g=0
            pr=get_predicate(self,y1,x1)
            print(pr)
            print(pr[0])
            r=' '.join(str(item) for item in pr[0])
            print(r)
            #v=get_objectclass(self,r)
            r1=' '.join(str(item) for item in v)
            r2=r1.replace("{'",'')
            r3=r2.replace("'}",'')
            r1=r3.split()
            #r1=r3.replace("NamedIndividual",'')
            print('q',x1)
            for item in r1:
                print(item)
                #if((str(item)!=x1 or str(item)!=x1+xx1) and str(item)!="NamedIndividual"):
                if((str(item)!=x1 ) and str(item)!="NamedIndividual"):
                    print('hi',item)
                    g+=1
            if(g>0):
                sparql1="SELECT ?"+z+" WHERE {?"+z+" ?p ?object . ?object rdf:"+r+" rdf:"+y1+" }"
            else:
                sparql1="SELECT ?"+z+" WHERE {?"+z+" rdf:"+r+" rdf:"+y1+" }"


        else:
            reln=''
            i=0
            v=[]

            re1='has'+x1+xx1

            rel=get_relations(self,re1)
            rel1=' '.join(str(item) for item in rel)
            g1=rel1.replace("[",'')
            rel=g1.replace("]",'')
            if(rel!=''):
                print('hiiii')
                #reln+=' '.join(str(item) for item in rel)
                #reln.translate({ord('{'):None, ord('}'):None})
                reln1=rel.replace("{'",'')
                reln2=reln1.replace("'}",'')
                reln3=reln2.split()
                #reln1=re.sub(r'{^}','',reln)

                print(reln3)
                for r in reln3:
                    print(str(r))
                    v1=''
                    v.append(get_objectclass(self,r))
                    v1+=' '.join(str(item) for item in v)
                    #reln.translate({ord('{'):None, ord('}'):None})
                    r1=v1.replace("{'",'')
                    r2=r1.replace("'}",'')
                    r1=r2.replace("['",'')
                    r2=r1.replace("']",'')
                    r3=r2.split()
                    #v[i]=get_objectclass(self,r)
                    print(r3)
                    #print(v[i])
                    i+=1
                    if(count>0):
                        break
                    for ob in r3:    #object class (Range) of the predicate
                        ob1=ob.replace("[",'')
                        ob2=ob1.replace("]",'')
                        ob=ob2.replace(",",'')
                        print('Hellooo   '+ob)
                        print(x1+xx1)
                        if(ob==x1+xx1):
                            sparql1="SELECT DISTINCT ?o WHERE {?s rdf:"+r+" ?o}"
                            #response1=searchq(self,sparql1,'o')
                            #print(response1)
                            z='o'
                            count+=1
                            break
                        else:
                            print('next')
            else:
                print('hello')
                sparql1="SELECT DISTINCT ?subject WHERE { ?subject a rdf:"+x1+xx1+" }"
                z='subject'
                #response1=searchq(self,sparql1,z)
                #print(response1)



        response1=searchq(self,sparql1,z)
        return response1



def search1(q1):
    runQuery = SparqlQueries()
    result1=runQuery.search(q1)
    return result1
