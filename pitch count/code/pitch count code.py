import pandas as pd
import copy
import matplotlib.pyplot as plt
import numpy as np
import random
csv_file = r'pitches.csv'
#csv_file = r'fakepitches.csv'
df = pd.read_csv(csv_file)


all_pitchers = []
for pitcher in df['Pitcher']:
    if pitcher not in all_pitchers:
        all_pitchers.append(pitcher)
#        print(pitcher)

#print(all_pitchers)

pitchess = {}

pitchtypes = []

everyone = {}

for pitcher in all_pitchers:
    pitchess[pitcher] = {}

#print(pitchess)
print('Got list of all pitchers')

#for pitcher in df['Pitcher']:
    #pitchess[pitcher].update( {df['Total Pitches Before'] : df['Is Fastball']} )
    #print(pitchess[pitcher])

for index, row in df.iterrows():
    pitcher = row['Pitcher']
    #print(row["Total Pitches Before"], row["Is Fastball"])
    if row['Total Pitches Before'] in everyone:
        everyone[row['Total Pitches Before']].append(str(row['Is Fastball']))
    else:
        everyone.update( {row['Total Pitches Before'] : [str(row['Is Fastball'])]})
    if row['Total Pitches Before'] in pitchess[pitcher]:
        pitchess[pitcher][row['Total Pitches Before']].append(str(row['Is Fastball']))
    else:
        pitchess[pitcher].update( {row['Total Pitches Before'] : [str(row['Is Fastball'])]})
    #print(pitchess[pitcher])

print('Done.')

print(everyone)

#pitchcopy = pitchess.copy()
pitchcopy = copy.deepcopy(pitchess)
everyonecopy = copy.deepcopy(everyone)

for pitcher in pitchcopy:
    yescount = 0
    nocount = 0
    for i in range(len(pitchess[pitcher])):
        yescount += pitchess[pitcher][i].count('True')
        nocount += pitchess[pitcher][i].count('False')
    try:
        fastballpercent = yescount / (yescount + nocount)
    except:
        print(yescount)
        print(nocount)
        print(pitcher)
        print(i)
        print(pitchess[pitcher][i])
        fastballpercent = 0
    for i in range(len(pitchess[pitcher])):
        yescounthere = pitchess[pitcher][i].count('True')
        nocounthere = pitchess[pitcher][i].count('False')
        try:
            fastballpercenthere = yescounthere / (yescounthere + nocounthere)
        except:
            print(yescounthere)
            print(nocounthere)
            print(pitcher)
            print(i)
            print(pitchess[pitcher][i])
            fastballpercenthere = 0
        diff = fastballpercenthere - fastballpercent
        pitchcopy[pitcher][i] = diff

everyoneyescount = 0
everyonenocount = 0
for i in range(len(everyone)):
    everyoneyescount += everyone[i].count('True')
    everyonenocount += everyone[i].count('False')
    everyonefastballpercent = everyoneyescount / (everyoneyescount + everyonenocount)
for i in range(len(everyone)):
    everyoneyescounthere = everyone[i].count('True')
    everyonenocounthere = everyone[i].count('False')
    everyonefastballpercenthere = everyoneyescounthere / (everyoneyescounthere + everyonenocounthere)
    everyonediff = everyonefastballpercenthere - everyonefastballpercent
    everyonecopy[i] = everyonediff

print(everyonecopy)

print('This is done.')
	
    
collective = {}

for pitcher in pitchcopy:
    for i in range(len(pitchcopy[pitcher])):
        if i in collective:
            collective[i].append(pitchcopy[pitcher][i])
        else:
            collective.update({i:[pitchcopy[pitcher][i]]})

for i in collective:
    avg = sum(collective[i]) / len(collective[i])
    collective[i] = avg

#d = collective
d = everyonecopy
lists = sorted(d.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.plot(x, y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data")
plt.show()
listy = []
for i in range(len(x)):
    listy.append(len(everyone[i]))
plt.plot(x,listy,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Sample Size")
plt.title("Collective Data")
plt.show()
d = everyonecopy
lists = sorted(d.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.plot(x[0:100], y[0:100],'r-')
plt.plot(np.linspace(0,100,100),np.linspace(0,0,100),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data - First 100 Pitches")
plt.show()

first_pitch_thing = {}
for pitcher in pitchcopy:
    first_pitch = pitchcopy[pitcher][0]
    first_pitch_thing[pitcher] = first_pitch

d = everyonecopy
lists = sorted(d.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.plot(x,y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red)")
plt.show()

ad = pitchcopy['Jacob deGrom']
alists = sorted(ad.items()) # sorted by key, return a list of tuples
ax, ay = zip(*alists) # unpack a list of pairs into two tuples
plt.plot(ax,ay,'b-')
plt.plot(x,y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red), Jacob deGrom (blue)")
plt.show()

aad = pitchcopy['Gerrit Cole']
aalists = sorted(aad.items()) # sorted by key, return a list of tuples
aax, aay = zip(*aalists) # unpack a list of pairs into two tuples
plt.plot(ax,ay,'b-')
plt.plot(aax,aay,'g-')
plt.plot(x,y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red), Jacob deGrom (blue), Gerrit Cole (green)")
plt.show()

aaad = pitchcopy['Clayton Kershaw']
aaalists = sorted(aaad.items()) # sorted by key, return a list of tuples
aaax, aaay = zip(*aaalists) # unpack a list of pairs into two tuples
plt.plot(ax,ay,'b-')
plt.plot(aax,aay,'g-')
plt.plot(aaax,aaay,'m-')
plt.plot(x,y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red), Jacob deGrom (blue), Gerrit Cole (green), Clayton Kershaw (magenta)")
plt.show()

ad = pitchcopy['Liam Hendriks']
alists = sorted(ad.items()) # sorted by key, return a list of tuples
ax, ay = zip(*alists) # unpack a list of pairs into two tuples
plt.plot(ax,ay,'b-')
plt.plot(x,y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red), Liam Hendriks (blue)")
plt.show()

aad = pitchcopy['Kirby Yates']
aalists = sorted(aad.items()) # sorted by key, return a list of tuples
aax, aay = zip(*aalists) # unpack a list of pairs into two tuples
plt.plot(ax,ay,'b-')
plt.plot(aax,aay,'g-')
plt.plot(x,y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red), Liam Hendriks (blue), Kirby Yates (green)")
plt.show()

aaad = pitchcopy['Josh Hader']
aaalists = sorted(aaad.items()) # sorted by key, return a list of tuples
aaax, aaay = zip(*aaalists) # unpack a list of pairs into two tuples
plt.plot(ax,ay,'b-')
plt.plot(aax,aay,'g-')
plt.plot(aaax,aaay,'m-')
plt.plot(x,y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red), Liam Hendriks (blue), Kirby Yates (green), Josh Hader (magenta)")
plt.show()


randompitch = copy.deepcopy(everyonecopy)

for j in range(len(everyonecopy)):
    fastballcount = 0
    noncount = 0
    for i in range(len(everyone[j])):
        if random.uniform(0, 1) >= everyonefastballpercent:
            noncount += 1
        else:
            fastballcount += 1
    try:
        fbpct = fastballcount / (fastballcount + noncount)
    except:
        fbpct = 1
    diffy = fbpct - everyonefastballpercent
    randompitch[j] = diffy
    
rd = randompitch
rlists = sorted(rd.items()) # sorted by key, return a list of tuples
rx, ry = zip(*rlists) # unpack a list of pairs into two tuples
plt.plot(rx,ry,'b-')
plt.plot(x,y,'r-')
plt.plot(np.linspace(0,len(d),len(d)),np.linspace(0,0,len(d)),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red) vs Random Data")
plt.show()

plt.plot(rx[0:100],ry[0:100],'b-')
plt.plot(x[0:100],y[0:100],'r-')
plt.plot(np.linspace(0,100,100),np.linspace(0,0,100),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data (red) vs Random Data - First 100")
plt.show()




fivedata = {}

i = 0
while i < 100:
    fbs_add = everyone[i].count('True') + everyone[i+1].count('True') + everyone[i+2].count('True') + everyone[i+3].count('True') + everyone[i+4].count('True')
    nonfbs_add = everyone[i].count('False') + everyone[i+1].count('False') + everyone[i+2].count('False') + everyone[i+3].count('False') + everyone[i+4].count('False')
    fbpct_add = fbs_add / (fbs_add + nonfbs_add)
    diff_add = fbpct_add - everyonefastballpercent
    fivedata[i] = diff_add
    i += 5


fd = fivedata
flists = sorted(fd.items()) # sorted by key, return a list of tuples
fx, fy = zip(*flists) # unpack a list of pairs into two tuples
plt.plot(fx,fy,'b-')
#plt.plot(x,y,'r-')
plt.plot(np.linspace(0,100,20),np.linspace(0,0,20),'k-')
plt.xlabel("Pitch Number")
plt.ylabel("Percent Fastballs Minus Collective Percent")
plt.title("Collective Data - Per 5 Pitches")
plt.show()
