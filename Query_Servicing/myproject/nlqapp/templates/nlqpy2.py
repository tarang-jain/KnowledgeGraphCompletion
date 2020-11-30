#from .nlqpy import *
from owlready2 import *
import types
onto_path.append(r"/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II-20200816T091910Z-001/KG IMPRINT II")
onto = get_ontology("https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl").load()
onto.AircraftAccident
namespace=onto.get_namespace("http://www.cse.iitb.ac.in/~amitpatil/aircraft_sbase.owl#")
def search2(qu):
    Aircraft ="AircraftAccident."+ qu
    qp=' '
    qp1=''
    qp2=''

    with onto:
        l1=(list(onto.classes()))
        #for i in l1:
            #print(list(i.ancestors()))
        for i in l1:
            #qp=' '.join([str(elem) for elem in i])
            qp=(str(i).strip('[]').__add__(" "))
            if(qp.__contains__(Aircraft)):
                qp2=str(list(i.instances()))
                break
            print(qp2)
            #qp1+=qp
            #qp=' '
       # print(qp1)
            #for ele in i:
                #if(ele==Aircraft):
                    #qp=qp.list(i.instances()))
                    #qp=+qp
                    #print(list(ele.instances()))
                   # exit
    return qp2
        #print(list(namespace.PropulsionGroup.ancestors() if namespace.PropulsionGroup else []))
        #print(namespace.Aircraft.is_a)
        #print(list(onto.AircraftCategory.get_properties("Helicopter")))
        #print(Aircraft.iri)
        #print(onto.Aircraft.instances() if onto.Aircraft else [])
        #class qu(Thing)=qu
            #pass
            #print(qu.iri())

            #pass
        #for i in qu.individuals():
            #print(i)
            #return i
        #return qu.instances()
    #with onto:
        #class NewClass():
            #print(NewClass.__getattribute__)
    #return list(NewClass.__class__)
