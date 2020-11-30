from owlready2 import *
import types
onto_path.append(r"/home/tarangjain/KG_IMPRINT_II/KG IMPRINT II-20200816T091910Z-001/KG IMPRINT II")
onto = get_ontology("https://www.cse.iitb.ac.in/~amitpatil/AircraftAccident.owl").load()
onto.AircraftAccident
namespace=onto.get_namespace("http://www.cse.iitb.ac.in/~amitpatil/aircraft_sbase.owl#")
def search5(qu):
    Aircraft ="AircraftAccident."+ qu
    qp=' '
    qp1=''
    qp2=''

    with onto:
        l1=(list(onto.classes()))
        #qp2=list(onto.qu.get_relations())
        print(l1)
        #for i in l1:
            #print(list(i.ancestors()))
        for i in l1:
            #qp=' '.join([str(elem) for elem in i])
            qp=(str(i).strip('[]').__add__(" "))
            if(qp.__contains__(Aircraft)):
                qp2=list(i.ancestors())

                break
            print(qp2)


    return qp2
