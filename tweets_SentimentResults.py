import matplotlib.pyplot as plt
import pickle

infile = open('FuzzyPos.pickle','rb')
FuzzyPos = pickle.load(infile)
infile.close()

infile = open('FuzzyNeg.pickle','rb')
FuzzyNeg = pickle.load(infile)
infile.close()

# Moderately Pos
print("\n FuzzyPos:")
print(FuzzyPos)

# Moderately Neg
print("\n FuzzyNeg:")
print(FuzzyNeg)
    
result=[]
senti=[]

for i in range(len(FuzzyPos)):
    t=max(FuzzyPos[i],FuzzyNeg[i])
    result.append(t)
    if FuzzyPos[i]==FuzzyNeg[i]==t:
        senti.append("Neu")
    elif FuzzyPos[i]==t:
        senti.append("P")
    else:
        senti.append("N")
   
print("\n Result:")
print(result)

print("\n Final Sentiment is:")
print(senti)

plt.plot(result)
plt.title("Sentiment Reader for Mood Swings Values while watching IndVsPak ICC World Cup (2017) Final Match")
plt.xlabel("Time Stamps")
plt.show()
