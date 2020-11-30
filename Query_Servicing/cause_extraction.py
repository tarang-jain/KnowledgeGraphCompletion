import glob
import os
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer


i=1980
count=0
count1=0
sentences=''
files_in_dir = []
cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
cluster5 = []
cluster6 = []

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

#vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


while(i<2020):
    x=str(i+1)
    i=i+1
    y=1
    while(y<=12):
        os.chdir(r'C:/Users/Qumar/Desktop/4000 reports in text format/'+x+'/'+str(y))
        y=y+1
        myFiles = glob.glob('*')
        #print(myFiles)



        for q in myFiles:
            #print('hello'+str(q))
            if(str(q)!=''):
                files_in_dir=r'C:/Users/Qumar/Desktop/4000 reports in text format/'+x+'/'+str(y)+'/'+str(q)
                #files_in_dir.append(os.path.join(str(y), x))
                #with open( os.path.join( dir, file ) ,"r") as fd:
                #file_content.append( fd.read )

                #for c in files_in_dir:
                #for k in c:
                #open(k)

                with open(q, "r", encoding="utf8") as f:
                    c=0
                    p=0
                    s=0
                    An=0
                    file1 = open(r"C:/Users/Qumar/Desktop/file1.txt","a", encoding="utf8")
                    file2 = open(r"C:/Users/Qumar/Desktop/file2.txt","a", encoding="utf8")
                    #file3 = open(r"C:/Users/Qumar/Desktop/file3.txt","a")
                    file1.write("\n\n\n"+q+"\n")

                    lines = f.read().splitlines()
                    sentences =' '.join(map(str, f.read().split('\n')))


                    #print(lines)
                    #lines2 = [i[len("Occurrence")] for i in lines]
                    for v in lines:
                        #print(str(v))
                        z = v.split()

                        #print(z)
                        if(s==1):
                            file1.write("\n"+v)
                            print(v.encode("utf-8"))
                            s=0
                        if(p==1):
                            file1.write("\n"+v)
                            print(v.encode("utf-8"))
                        if(An==1 and c==0):
                            file1.write("\n"+v)
                            print(v.encode("utf-8"))
                            #An=0

                        for w in z:
                            if(w=="Number:"):
                                s=1


                            elif(w=="Occurrence" and p==0):
                                file1.write("\n"+v)
                                print(v.encode("utf-8"))
                                c=1
                                count=count+1
                            elif(w=="cause(s)" and c==0 ):

                                p=1
                                count=count+1
                                c=1
                            elif(w=="Findings"):
                                p=0
                            elif(w=="Analysis"):
                                An=An+1

                    if(c==0):
                        file2.write("\n"+q)
                        count1=count1+1

                stemmer = nltk.stem.porter.PorterStemmer()
                remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
                vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
                #print(cosine_sim( 'Pilot Error ',sentences))
                #print(cosine_sim('IN FLIGHT COLLISION WITH OBJECT', sentences))
                #print(cosine_sim('IN FLIGHT ENCOUNTER WITH WEATHER',sentences))
                #print(cosine_sim('LOSS OF CONTROL - ON GROUND/WATER Phase of Operation: LANDING - ROLL', sentences))
                #print(cosine_sim('NOSE OVER  Phase of Operation: LANDING - ROLL', sentences))
                #print(cosine_sim('IN FLIGHT COLLISION WITH TERRAIN/WATER', sentences))

                a=cosine_sim( 'Pilot Error ',sentences)
                b=cosine_sim('IN FLIGHT COLLISION WITH OBJECT', sentences)
                c=cosine_sim('IN FLIGHT ENCOUNTER WITH WEATHER',sentences)
                d=cosine_sim('LOSS OF CONTROL - ON GROUND/WATER Phase of Operation: LANDING - ROLL', sentences)
                e=cosine_sim('NOSE OVER  Phase of Operation: LANDING - ROLL', sentences)
                g=cosine_sim('IN FLIGHT COLLISION WITH TERRAIN/WATER', sentences)

                #number = [a,b,c,d,e,g]
                #
                #if(max(number)==a):
                    #print("cluster1",a)#
                #elif(max(number)==b):
                    #cluster2[i]==f
                    #i=i+1
                    #print("cluster2",b)
                #elif(max(number)==c):
                    #cluster3[i]==f
                    #i=i+1
                    #print("cluster3",c)
                #elif(max(number)==d):
                    #cluster4[i]==f
                    #i=i+1
                    #print("cluster4",d)
                #elif(max(number)==e):
                    #cluster5[i]==f
                    #i=i+1
                    #print("cluster5",e)
                #elif(max(number)==g):
                    #cluster6[i]==f
                    #i=i+1
                    #print("cluster6",g)


print(count)
print(count1)
