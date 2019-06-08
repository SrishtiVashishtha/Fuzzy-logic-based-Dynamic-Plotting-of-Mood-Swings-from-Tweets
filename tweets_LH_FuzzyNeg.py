import nltk
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import PlaintextCorpusReader
import copy
import matplotlib.pyplot as plt
import pickle

corpus_root = 'C:\\MyData\\PythonPractice\\tweetscorpus'
wordlists = PlaintextCorpusReader(corpus_root, 'twittertweets.txt')
doc=wordlists.raw("twittertweets.txt")

sentences =doc.split(".")
senlen=len(sentences)-1
stokens = [nltk.word_tokenize(sent) for sent in sentences]  # Tokenization

taggedlist=[]
for stoken in stokens:        
     taggedlist.append(nltk.pos_tag(stoken)) #Part of Speech Tagging (POS) using NLTK POS Tagger
wnl = nltk.WordNetLemmatizer()      # Lemmatization

score_list_pos=[]
score_list_neg=[]
global_lpn_sum=[]
global_timestamp_sum=[]
global_union=[]
global_intersection=[]
global_union_timestamp_sum=[]
global_intersection_timestamp_sum=[]
selected_tagwords=[]

#POS
#Selection of word tokens which are either noun, adjective, verb or adverb

for idx,taggedsent in enumerate(taggedlist):
    score_list_pos.append([])
    score_list_neg.append([])
    selected_tagwords.append([])
    for idx2,t in enumerate(taggedsent):
        newtag=''
        lemmatized=wnl.lemmatize(t[0])
        if t[1].startswith('NN'):
            newtag='n'
        elif t[1].startswith('JJ'):
            newtag='a'
        elif t[1].startswith('V'):
            newtag='v'
        elif t[1].startswith('R'):
            newtag='r'
        else:
            newtag=''       
        if(newtag!=''):    
            synsets = list(swn.senti_synsets(lemmatized, newtag))
            #print(synsets)
            temp=t[0]
            selected_tagwords[idx].append(temp) # stores the selected words
            
            scorepos=scoreneg=0
            if(len(synsets)>0):
                for syn in synsets:
                    #print(syn)
                    scorepos=syn.pos_score() # Positive score of word  using SentiWordNet lexicon
                    scoreneg=syn.neg_score() # Negative score of word  using SentiWordNet lexicon
                    p=round((scorepos/len(synsets)),4)  
                    n=round((scoreneg/len(synsets)),4)

                score_list_pos[idx].append(p)
                score_list_neg[idx].append(n)          
                
for j in range(senlen):
    
    print("\n" + str(j+1)+ ": "+ sentences[j])
    words = nltk.word_tokenize(sentences[j])
    tagged = nltk.pos_tag(words)    
    #print("\n "+str(tagged))   # Words and their POS tags
    
    b=[]
    b.append(selected_tagwords[j])
    stagwords=[]        
    stagwords=copy.copy(b[0])
    print("\n Selected Tagged tokens are : ")
    print(stagwords)
    
    list_pos=[]
    list_pos.append(score_list_pos[j])
    lp=[]        
    lp=copy.copy(list_pos[0])
    
    list_neg=[]
    list_neg.append(score_list_neg[j])
    ln=[]        
    ln=copy.copy(list_neg[0])

    mlneg=[]
    notverypos=[]
    print("\n Sentence "+ str(j+1) +" Positive Score for each word in sentence :")
    #print(score_list_pos[j])
    print(lp) 
    
    print("\n Sentence "+ str(j+1) +" Negative Score for each word in sentence :")
    #print(score_list_neg[j])
    print(ln)
    
    #VERY POSITIVE , NOT VERY POSITIVE
    
    for i in range(len(lp)):
        t=pow(lp[i],2)  #very positive
        s=1-t
        notverypos.append(round(s,4))
#    print("\n Not Very Positive")
#    print(notverypos)
    
    #NOT VERY NEGATIVE , MORE OR LESS NEGATIVE
    
    for i in range(len(lp)):
        p=pow(ln[i],0.5)
        mlneg.append(round(p,4))
#    print("\n More or less Negative")
#    print(mlneg)
    
# INTERSECTION OPEARATION  MORE OR LESS NEG AND NOT VERY POSITIVE
    
    inter=[]
    print("\n Sentence "+ str(j+1) +" More or less Negative and not Very Positive Score for each word in sentence :")    
    for word in range(len(lp)):
        if mlneg[word]<notverypos[word]:
            inter.append(mlneg[word])
        else:
            inter.append(notverypos[word])
    print(inter)
    inte=round(sum([word_score for word_score in inter]),4)
    print(inte)
    global_intersection.append(inte)
    
print("\n Mood Swing Fuzzy Negative Values of Tweets for all timestamps (30) is : \n")
print(global_intersection)
plt.plot(global_intersection)
plt.title("Mood Swings Fuzzy Negative Values while watching IndVsPak ICC World Cup (2017) Final Match")
plt.xlabel("Time Stamp")
plt.ylabel("Card_FuzzyNeg_Value")
plt.show()

# FIXED WINDOW TIMESTAMP PLOTS

window=senlen/3
#print(int(window))  # convert float to integer because range() function requires integer type argument

for i in range(int(window)):
    t1=[]
    sumt1=[]
    t1.append(global_intersection[3*i:3*i+3])
    tlist=[]        
    tlist=copy.copy(t1[0])
    z=round(sum([w for w in tlist]),4)
    sumt1.append(z)
    global_intersection_timestamp_sum.append(z)
print("\n Mood Swing Fuzzy Negative Values of Tweets when there is fixed timestamp (3) :")
print(global_intersection_timestamp_sum)
plt.plot(global_intersection_timestamp_sum)
plt.title("Mood Swings Fuzzy Negative Values while watching IndVsPak ICC World Cup (2017) Final Match")
plt.xlabel("Time Window")
plt.ylabel("FuzzyNeg_Value")
plt.show()

filename = 'FuzzyNeg.pickle'
outfile = open(filename,'wb')
pickle.dump(global_intersection_timestamp_sum,outfile)
outfile.close()