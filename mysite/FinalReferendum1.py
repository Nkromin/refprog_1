
import pandas as pd


from plotly.offline import iplot

import re
import plotly
plotly.tools.set_credentials_file(username='AlmightyHeathcliff', api_key='m9tmWBi9h3qzn3UMn9Gq')
plotly.offline.init_notebook_mode()
import plotly.plotly as py
import plotly.graph_objs as go
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import nltk
#import seaborn as sns
#get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
nltk.download('stopwords')

modiWinner=0
rahulWinner=0


# In[337]:


df = pd.read_csv('ModiStream.csv')
cf = pd.read_csv('RahulStream.csv')

# In[338]:


df.columns = ['User','Time','Tweet']
cf.columns = ['User','Time','Tweet']




# In[340]:


#df.loc[0,'T'][2:]


# In[341]:


def removeNoise(s):
     s = re.sub(r"http.?://[^\s]+[\s]?", " ", s)
     #s = re.sub(r"[^\s]+[\s]?", " ", s)
     s = re.sub(r"\s?[0-9]+\.?[0-9]*", " ", s)
     s = re.sub("[^a-zA-Z'.,!?#]+", ' ', s)   #Remove all punctuation except one punct
     return s
df['T'] = df['Tweet'].apply(removeNoise)
cf['T'] = cf['Tweet'].apply(removeNoise)


# In[ ]:





# In[342]:


def removeHindi(x):
    counter=0
    x=x.split()
    for i in x:
        if(i=='u'):
            counter+=1
    if(counter>10):
        return "nil"
    else:
        return ' '.join(x)


df['T']=df['T'].apply(removeHindi)
cf['T']=cf['T'].apply(removeHindi)


# In[343]:


def stitch(y):
    try:
        x=y.split()
        xx=x[1:]
        temp=' '.join(xx)
        return temp
    except:
        return "Eskerra"
df['T'] = df['T'].apply(stitch)
cf['T'] = cf['T'].apply(stitch)


# In[345]:


sid = SentimentIntensityAnalyzer()


# In[346]:


posList=[]
for sentence in df['T']:
    try:
      #print(sentence)
      ss = sid.polarity_scores(sentence)
      posList.append(ss['pos'])
    except:
        pass


RposList=[]
for sentence in cf['T']:
    try:
      #print(sentence)
      ss = sid.polarity_scores(sentence)
      RposList.append(ss['pos'])
    except:
        pass


# In[347]:


negList=[]
for sentence in df['T']:
    try:
      ss = sid.polarity_scores(sentence)
      negList.append(ss['neg'])
    except:
        pass



RnegList=[]
for sentence in cf['T']:
    try:
      ss = sid.polarity_scores(sentence)
      RnegList.append(ss['neg'])
    except:
        pass
# In[348]:


AverageList=[]
for sentence in df['T']:
    try:
      ss = sid.polarity_scores(sentence)
      AverageList.append(ss['neu'])
    except:
        pass

RAverageList=[]
for sentence in cf['T']:
    try:
      ss = sid.polarity_scores(sentence)
      RAverageList.append(ss['neu'])
    except:
        pass


# In[349]:


df['neg']=pd.Series(negList)
cf['neg']=pd.Series(RnegList)


# In[350]:


df['pos']=pd.Series(posList)
cf['pos']=pd.Series(RposList)

# In[351]:


df['neu']=pd.Series(AverageList)
cf['neu']=pd.Series(RAverageList)

# In[352]:


df.drop(df[(df['neu']==0.000) ].index,inplace=True)
cf.drop(cf[(cf['neu']==0.000) ].index,inplace=True)

# ## Most Frequent TWEETER

# In[353]:





# In[355]:


d=df['User'].value_counts()
ndf=pd.DataFrame(d)
#ndf.set_index('Name')


ndf['Sno']=np.arange(0,len(ndf.index))
ndf['Name'] = ndf.index


# In[356]:


ndf.index=ndf['Sno']



# In[357]:


ndf.head()
ndf.drop('Sno',axis=1,inplace=True)


# In[358]:


ndf=ndf.loc[np.arange(0,5),['User','Name']]


# In[549]:






trace = go.Bar(
    x=ndf['Name'],
    y=ndf['User'],
    marker={'color': 'orange'}

)

layout = go.Layout(
    xaxis=dict(
        title='Frequent Twitterati',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Frequent NaMo Twitter Fans",
    plot_bgcolor='grey'
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = '00.html', auto_open=False)

















#############################################


Rd=cf['User'].value_counts()
Rndf=pd.DataFrame(Rd)
#ndf.set_index('Name')


Rndf['Sno']=np.arange(0,len(Rndf.index))
Rndf['Name'] = Rndf.index


# In[356]:


Rndf.index=Rndf['Sno']



# In[357]:


Rndf.drop('Sno',axis=1,inplace=True)


# In[358]:


Rndf=Rndf.loc[np.arange(0,5),['User','Name']]


# In[549]:






trace = go.Bar(
    x=Rndf['Name'],
    y=Rndf['User']
)

layout = go.Layout(
    xaxis=dict(
        title='Frequent Twitterati',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Frequent RahulGandhi Twitter Fans"
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = '01.html', auto_open=False)


#############################################


# ## Polarity of Most Frequent User

# In[362]:


def Merger(score):
    if(score==0.000):
        return 'Affirming'
    else:
        return 'Critical'

df['Polarity'] = df['neg'].apply(Merger)



# In[363]:


polar = ndf['Name']


# In[364]:


df['SNO']=np.arange(0,len(df.index))

df.set_index('SNO',inplace=True)


# ## Pie Chart Overall Representation

# In[545]:





# ## Max Tweeters Polarity

# In[550]:


PCounter=0
NCounter=0

PLIST=[]

for loop in range(len(df.index)):
    var=df.loc[loop,'User']
    if(var==polar[0]):
        if((df.loc[loop,'Polarity']=='Affirming') and (var==polar[0])):
                    PCounter+=1
        else:
                    NCounter+=1



PLIST.append([polar[0],PCounter,NCounter])



PCounter=0
NCounter=0
for loop in range(len(df.index)):
    var=df.loc[loop,'User']
    if(var==polar[1]):
        if((df.loc[loop,'Polarity']=='Affirming') and (var==polar[1])):
                    PCounter+=1
        else:
                    NCounter+=1


PLIST.append([polar[1],PCounter,NCounter])


PCounter=0
NCounter=0
for loop in range(len(df.index)):
    var=df.loc[loop,'User']
    if(var==polar[2]):
        if((df.loc[loop,'Polarity']=='Affirming') and (var==polar[2])):
                    PCounter+=1
        else:
                    NCounter+=1

PLIST.append([polar[2],PCounter,NCounter])



PCounter=0
NCounter=0
for loop in range(len(df.index)):
    var=df.loc[loop,'User']
    if(var==polar[3]):
        if((df.loc[loop,'Polarity']=='Affirming') and (var==polar[3])):
                    PCounter+=1
        else:
                    NCounter+=1

PLIST.append([polar[3],PCounter,NCounter])


PCounter=0
NCounter=0
for loop in range(len(df.index)):
    var=df.loc[loop,'User']
    if(var==polar[4]):
        if((df.loc[loop,'Polarity']=='Affirming') and (var==polar[4])):
                    PCounter+=1
        else:
                    NCounter+=1

PLIST.append([polar[4],PCounter,NCounter])

temp1 = pd.DataFrame(PLIST, columns="NAME AffirmingTweets CriticalTweets".split())
temp1.set_index('NAME',inplace=True)


# In[734]:




# In[741]:


temp1.plot(kind='bar',title='Attitude of Modi Fans towards Modi')
plt.savefig("10" + '.png', bbox_inches='tight')



######################################################################


# ## Polarity of Most Frequent User

# In[362]:



cf['Polarity'] = cf['neg'].apply(Merger)



# In[363]:


Rpolar = Rndf['Name']


# In[364]:


cf['SNO']=np.arange(0,len(cf.index))

cf.set_index('SNO',inplace=True)


# ## Pie Chart Overall Representation

# In[545]:





# ## Max Tweeters Polarity

# In[550]:


RPCounter=0
RNCounter=0

RPLIST=[]

for loop in range(len(cf.index)):
    var=cf.loc[loop,'User']
    if(var==Rpolar[0]):
        if((cf.loc[loop,'Polarity']=='Affirming') and (var==Rpolar[0])):
                    RPCounter+=1
        else:
                    RNCounter+=1



RPLIST.append([Rpolar[0],RPCounter,RNCounter])



RPCounter=0
RNCounter=0
for loop in range(len(cf.index)):
    var=cf.loc[loop,'User']
    if(var==Rpolar[1]):
        if((cf.loc[loop,'Polarity']=='Affirming') and (var==Rpolar[1])):
                    RPCounter+=1
        else:
                    RNCounter+=1


RPLIST.append([Rpolar[1],RPCounter,RNCounter])


RPCounter=0
RNCounter=0
for loop in range(len(cf.index)):
    var=cf.loc[loop,'User']
    if(var==Rpolar[2]):
        if((cf.loc[loop,'Polarity']=='Affirming') and (var==Rpolar[2])):
                    RPCounter+=1
        else:
                    RNCounter+=1

RPLIST.append([Rpolar[2],RPCounter,RNCounter])



RPCounter=0
RNCounter=0
for loop in range(len(cf.index)):
    var=cf.loc[loop,'User']
    if(var==Rpolar[3]):
        if((cf.loc[loop,'Polarity']=='Affirming') and (var==Rpolar[3])):
                    RPCounter+=1
        else:
                    RNCounter+=1

RPLIST.append([Rpolar[3],RPCounter,RNCounter])


RPCounter=0
RNCounter=0
for loop in range(len(cf.index)):
    var=cf.loc[loop,'User']
    if(var==Rpolar[4]):
        if((cf.loc[loop,'Polarity']=='Affirming') and (var==Rpolar[4])):
                    RPCounter+=1
        else:
                    RNCounter+=1

RPLIST.append([Rpolar[4],RPCounter,RNCounter])

temp11 = pd.DataFrame(RPLIST, columns="NAME AffirmingTweets CriticalTweets".split())
temp11.set_index('NAME',inplace=True)


# In[734]:




# In[741]:


temp11.plot(kind='bar',title='Attitude of Rahul fans for Rahul')
plt.savefig("11" + '.png', bbox_inches='tight')




######################################################################
# In[625]:


p=0
n=0
def OverallPolarity(x):
    global p,n
    if(x=='Affirming'):
        p+=1
    else:
        n+=1

df['Polarity'].apply(OverallPolarity)


# In[696]:


d={'Positive':p,'Critical':n}
modiWinner=n


s = pd.Series(d, name='Count')
s.index.name = 'Polarity'
ss=s.reset_index()


# ## Overall Polarity PIE

# In[706]:


labels = ss.Polarity
values = ss.Count

trace = go.Pie(labels=labels, values=values)


layout = go.Layout(
    title="Polarity Of NarendraModi Twitterati's",
)

fig = {
    'data': [trace],
    'layout': layout,
}
iplot(fig)

plotly.offline.plot(fig, filename = '20.html', auto_open=False)




#################################################

Rp=0
Rn=0
def ROverallPolarity(x):
    global Rp,Rn
    if(x=='Affirming'):
        Rp+=1
    else:
        Rn+=1

cf['Polarity'].apply(ROverallPolarity)


# In[696]:


Rd={'Positive':Rp,'Critical':Rn}
rahulWinner=Rn
Rs = pd.Series(Rd, name='Count')
Rs.index.name = 'Polarity'
Rss=Rs.reset_index()


# ## Overall Polarity PIE

# In[706]:


labels = Rss.Polarity
values = Rss.Count

trace = go.Pie(labels=labels, values=values)


layout = go.Layout(
    title="Polarity Of RahulGandhi Twitterati's",
)

fig = {
    'data': [trace],
    'layout': layout,
}
iplot(fig)

plotly.offline.plot(fig, filename = '21.html', auto_open=False)

#################################################


# ## Popular HashTag

# In[590]:


l=[]
def allHashtags(x):
    x=re.findall(r"#(\w+)", x)
    if(x==[]):
        pass
    else:
        for i in x:
            l.append("#"+i)
df['Tweet'].apply(allHashtags)


# In[370]:





# In[371]:





# In[591]:


c = Counter(l)


# In[592]:


tempDict={}
for i in range(7):
    tempDict[c.most_common(10)[i][0]] = temp=c.most_common(10)[i][1]


# In[593]:


overallFame = pd.Series(tempDict, name='Count')


# In[594]:


overallFame.index.name='FamousTags'


# In[595]:


overallFame = overallFame.reset_index()


# In[596]:





trace = go.Bar(
    x=overallFame['FamousTags'],
    y=overallFame['Count']
)

layout = go.Layout(
    xaxis=dict(
        title='Trending HashTags',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Trending HashTags for modi fans",
    plot_bgcolor='grey',
    boxgap=16,
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = '30.html', auto_open=False)

####################################################################

Rl=[]
def RallHashtags(x):
    x=re.findall(r"#(\w+)", x)
    if(x==[]):
        pass
    else:
        for i in x:
            Rl.append("#"+i)
cf['Tweet'].apply(RallHashtags)


# In[370]:





# In[371]:





# In[591]:


Rc = Counter(Rl)


# In[592]:


RtempDict={}
for i in range(7):
    RtempDict[Rc.most_common(10)[i][0]] = Rc.most_common(10)[i][1]


# In[593]:


RoverallFame = pd.Series(RtempDict, name='Count')


# In[594]:


RoverallFame.index.name='FamousTags'


# In[595]:


RoverallFame = RoverallFame.reset_index()


# In[596]:





trace = go.Bar(
    x=RoverallFame['FamousTags'],
    y=RoverallFame['Count']
)

layout = go.Layout(
    xaxis=dict(
        title='Trending HashTags',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Trending HashTags for Rahul fans",
    plot_bgcolor='grey',
    boxgap=16,
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = '31.html', auto_open=False)

####################################################################
# In[387]:


temp2 = df[df['Polarity']=='Affirming']


# In[581]:


positivel=[]
def PosHashtags(x):
    x=re.findall(r"#(\w+)", x)
    if(x==[]):
        pass
    else:
        for i in x:
            positivel.append("#"+i)
temp2['Tweet'].apply(PosHashtags)


# In[582]:


Posc = Counter(positivel)
temp2Dict={}
for i in range(7):
    temp2Dict[Posc.most_common(10)[i][0]] = Posc.most_common(10)[i][1]
PositiveFame = pd.Series(temp2Dict, name='Count')
PositiveFame.index.name='PositiveTags'
PositiveFame = PositiveFame.reset_index()


# In[604]:




trace = go.Bar(
    x=PositiveFame['PositiveTags'],
    y=PositiveFame['Count'],
     marker={'color': 'orange'}
)


layout = go.Layout(
    xaxis=dict(
        title='Trending HashTags',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Trending Hashtags When Fans Praise Modi",
    plot_bgcolor='grey',
    boxgap=16,
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = '40.html', auto_open=False)



#########################################################

Rtemp2 = cf[cf['Polarity']=='Affirming']


# In[581]:


Rpositivel=[]
def RPosHashtags(x):
    x=re.findall(r"#(\w+)", x)
    if(x==[]):
        pass
    else:
        for i in x:
            Rpositivel.append("#"+i)
Rtemp2['Tweet'].apply(RPosHashtags)


# In[582]:


RPosc = Counter(positivel)
Rtemp2Dict={}
for i in range(7):
    Rtemp2Dict[RPosc.most_common(10)[i][0]] = RPosc.most_common(10)[i][1]
RPositiveFame = pd.Series(Rtemp2Dict, name='Count')
RPositiveFame.index.name='PositiveTags'
RPositiveFame = RPositiveFame.reset_index()


# In[604]:




trace = go.Bar(
    x=RPositiveFame['PositiveTags'],
    y=RPositiveFame['Count'],
     marker={'color': 'orange'}
)


layout = go.Layout(
    xaxis=dict(
        title='Trending HashTags',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Trending Hashtags When Fans Praise Rahul",
    plot_bgcolor='grey',
    boxgap=16,
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = '41.html', auto_open=False)

#########################################################


# In[411]:


temp3 = df[df['Polarity']=='Critical']


# In[597]:


negativel=[]
def NegHashtags(x):
    x=re.findall(r"#(\w+)", x)
    if(x==[]):
        pass
    else:
        for i in x:
            negativel.append("#"+i)
temp3['Tweet'].apply(NegHashtags)


# In[598]:


Negc = Counter(negativel)
temp3Dict={}
for i in range(7):
    temp3Dict[Negc.most_common(10)[i][0]] = Negc.most_common(10)[i][1]
NegativeFame = pd.Series(temp3Dict, name='Count')
NegativeFame.index.name='InfamousTags'
NegativeFame = NegativeFame.reset_index()


# In[605]:


#NegativeFame.iplot(kind='bar',x='InfamousTags',y='Count')

trace = go.Bar(
    x=NegativeFame['InfamousTags'],
    y=NegativeFame['Count'],
     marker={'color': 'orange'}
)


layout = go.Layout(
    xaxis=dict(
        title='Trending HashTags',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Trending Hashtags When Fans Criticize Modi",
    plot_bgcolor='grey',
    boxgap=16,
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = '50.html', auto_open=False)



###################################3

Rtemp3 = cf[cf['Polarity']=='Critical']


# In[597]:


Rnegativel=[]
def RNegHashtags(x):
    x=re.findall(r"#(\w+)", x)
    if(x==[]):
        pass
    else:
        for i in x:
            Rnegativel.append("#"+i)
Rtemp3['Tweet'].apply(RNegHashtags)


# In[598]:


RNegc = Counter(Rnegativel)
Rtemp3Dict={}
for i in range(7):
    Rtemp3Dict[RNegc.most_common(10)[i][0]] = RNegc.most_common(10)[i][1]
RNegativeFame = pd.Series(Rtemp3Dict, name='Count')
RNegativeFame.index.name='InfamousTags'
RNegativeFame = RNegativeFame.reset_index()


# In[605]:


#NegativeFame.iplot(kind='bar',x='InfamousTags',y='Count')

trace = go.Bar(
    x=RNegativeFame['InfamousTags'],
    y=RNegativeFame['Count'],
     marker={'color': 'orange'}
)


layout = go.Layout(
    xaxis=dict(
        title='Trending HashTags',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Trending Hashtags When Fans Criticize Rahul",
    plot_bgcolor='grey',
    boxgap=16,
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = '51.html', auto_open=False)








fig = {
  "data": [
    {
      "values": [((modiWinner/(modiWinner+rahulWinner))*100),((rahulWinner/(modiWinner+rahulWinner))*100)],
      "labels": ['Probability of Rahul Winning','Probability of Modi Winning'],
      "domain": {"x": [0, .48]},
      "name": "Percentage of Winning",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":"Who Will Win?",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "  Win?",
                "x": 0.20,
                "y": 0.5
            }
        ]
    }
}
py.iplot(fig, filename='donut')

plotly.offline.plot(fig, filename = 'top.html', auto_open=False)




#######################################################################################################################################################





df = pd.read_csv('narendramodi')


# In[3]:


cf = pd.read_csv('rahulgandhi')


# In[4]:


df.drop('Unnamed: 0',axis=1,inplace=True)


# In[5]:


cf.drop('Unnamed: 0',axis=1,inplace=True)


# In[6]:




# In[8]:


cf.loc[df[df['Favorite']==min(df['Favorite'])]['Tweet'].index[0],'Tweet']


# In[9]:


## MOST USED WORDS


# In[10]:


famousWordList=[]
def famousWord(x):
    x=x.split()
    for i in x:
        famousWordList.append(i)
df['Tweet'].apply(famousWord)


# In[11]:


cfamousWordList=[]
def cfamousWord(x):
    x=x.split()
    for i in x:
        cfamousWordList.append(i)
cf['Tweet'].apply(cfamousWord)


# In[12]:


famousWordCounter = Counter(famousWordList)


# In[13]:


cfamousWordCounter = Counter(cfamousWordList)


# In[14]:


temp4Dict={}
for i in range(30):
    temp4Dict[famousWordCounter.most_common(30)[i][0]] = famousWordCounter.most_common(30)[i][1]
WordFame = pd.Series(temp4Dict, name='Count')
WordFame.index.name='Famous Word'
WordFame = WordFame.reset_index()


# In[15]:


ctemp4Dict={}
for i in range(30):
    ctemp4Dict[cfamousWordCounter.most_common(30)[i][0]] = cfamousWordCounter.most_common(30)[i][1]
cWordFame = pd.Series(ctemp4Dict, name='Count')
cWordFame.index.name='Famous Word'
cWordFame = cWordFame.reset_index()


# In[21]:




FilteredWords=[]
def stop(x):
    stopwords=nltk.corpus.stopwords.words("english")
    jam = ["'","Here","The","My'","RT'",'f','n']
    for j in jam:
        stopwords.append(j)
    if x not in stopwords:
        FilteredWords.append(x)
WordFame['Famous Word'].apply(stop)


# In[23]:


cFilteredWords=[]
def cstop(x):
    stopwords=nltk.corpus.stopwords.words("english")
    jam = ["'","Here","The","My'","RT'",'f','n']
    for j in jam:
        stopwords.append(j)
    if x not in stopwords:
        cFilteredWords.append(x)
cWordFame['Famous Word'].apply(cstop)


# In[34]:


# In[27]:


dicta={}

for i in FilteredWords:
    dicta[i] = WordFame.loc[WordFame[WordFame['Famous Word'] == i]['Count'].index[0], 'Count']

MSW = pd.Series(dicta, name='Count')
MSW.index.name='Common Words'
MSW = MSW.reset_index()


# In[30]:




# In[29]:


cdict={}

for i in cFilteredWords:
    cdict[i] = cWordFame.loc[cWordFame[cWordFame['Famous Word'] == i]['Count'].index[0], 'Count']

cMSW = pd.Series(cdict, name='Count')
cMSW.index.name='Common Words'
cMSW = cMSW.reset_index()


# In[31]:





trace = go.Bar(
    x=MSW['Common Words'],
    y=MSW['Count'],
     marker={'color': 'orange'}
)


layout = go.Layout(
    xaxis=dict(
        title='Most Common Words',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Frequent Words Mentioned By Modi"
)


fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = 'aa.html', auto_open=False)



# In[32]:





trace = go.Bar(
    x=cMSW['Common Words'],
    y=cMSW['Count'],
     marker={'color': 'green'}
)


layout = go.Layout(
    xaxis=dict(
        title='Frequent Twitterati',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Frequent Words Mentioned By Rahul Gandhi"
)




fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = 'ab.html', auto_open=False)



# In[33]:


## Mention of Opposition


# In[34]:


CongressCounter = 0
RahulCounter = 0
def mention(x):
    global CongressCounter,RahulCounter
    x=x.lower()
    y=x.split(" ")
    print(y)
    if "congress" in y:
        CongressCounter+=1
    if "rahul" in y or "rahulgandhi" in y or "@rahulgandhi" in y or "rahul gandhi" in y:
        RahulCounter+=1

df['Tweet'].apply(mention)


# In[35]:


bjpCounter = 0
modiCounter = 0
def cmention(x):
    global bjpCounter,modiCounter
    x=x.lower()
    y=x.split(" ")
    print(y)
    if "bjp" in y:
        bjpCounter+=1
    if "modi" in y or "narendramodi" in y or "@narendramodi" in y or "@pmoindia" in y:
        modiCounter+=1

cf['Tweet'].apply(cmention)


# In[36]:


mentionDict={"Mentioned Congress":CongressCounter,"Mentioned Rahul":RahulCounter,"General Tweets":(200-CongressCounter+RahulCounter)}


# In[37]:


cmentionDict={"Mentioned BJP":bjpCounter,"Mentioned Modi":modiCounter,"General Tweets":(200-bjpCounter+modiCounter)}


# In[38]:




fig = {
  "data": [
    {
      "values": list(mentionDict.values()),
      "labels": list(mentionDict.keys()),
      "domain": {"x": [0, .48]},
      "name": "Modi",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": list(cmentionDict.values()),
      "labels": list(cmentionDict.keys()),
      "text":"Rahul",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "Rahul",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":"The Number of times Opposition Mentioned",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Modi",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Rahul",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}
py.iplot(fig, filename='donut')

plotly.offline.plot(fig, filename = 'bb.html', auto_open=False)


# In[39]:


sid = SentimentIntensityAnalyzer()


# In[40]:


posList=[]
for sentence in df['Tweet']:
    try:
      ss = sid.polarity_scores(sentence)
      posList.append(ss['pos'])
    except:
        pass


cposList=[]
for sentence in cf['Tweet']:
    try:
      ss = sid.polarity_scores(sentence)
      cposList.append(ss['pos'])
    except:
        pass


# In[41]:


negList=[]
for sentence in df['Tweet']:
    try:
      ss = sid.polarity_scores(sentence)
      negList.append(ss['neg'])
    except:
        pass

cnegList=[]
for sentence in cf['Tweet']:
    try:
      ss = sid.polarity_scores(sentence)
      cnegList.append(ss['neg'])
    except:
        pass


# In[42]:


AverageList=[]
for sentence in df['Tweet']:
    try:
      ss = sid.polarity_scores(sentence)
      AverageList.append(ss['neu'])
    except:
        pass

cAverageList=[]
for sentence in cf['Tweet']:
    try:
      ss = sid.polarity_scores(sentence)
      cAverageList.append(ss['neu'])
    except:
        pass


# In[43]:


df['neg']=pd.Series(negList)
df['pos']=pd.Series(posList)
df['neu']=pd.Series(AverageList)
df.drop(df[(df['neu']==0.000) ].index,inplace=True)


cf['neg']=pd.Series(cnegList)
cf['pos']=pd.Series(cposList)
cf['neu']=pd.Series(cAverageList)
cf.drop(cf[(cf['neu']==0.000) ].index,inplace=True)


# In[44]:


def Merger(score):
    if(score==0.000):
        return 'Affirming'
    else:
        return 'Critical'

df['Polarity'] = df['neg'].apply(Merger)
cf['Polarity'] = cf['neg'].apply(Merger)


# In[45]:


x=df['Polarity'].value_counts()
p=x['Affirming']
n=x['Critical']
l=[p,n]



xx=cf['Polarity'].value_counts()
pp=xx['Affirming']
nn=xx['Critical']
ll=[pp,nn]


# In[46]:


fig = {
  "data": [
    {
      "labels":["Affirming Tweets","Critical Tweets"],
      "values":l,
      "domain": {"x": [0, .48]},
      "name": "Modi",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    {
     "labels":["Affirming Tweets","Critical Tweets"],
      "values":ll,
      "text":"Rahul",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "Rahul",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":"Polarity of Tweets",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Modi",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Rahul",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}
py.iplot(fig, filename='donut')

plotly.offline.plot(fig, filename = 'cc.html', auto_open=False)


# ## Comparing Tweets

# In[47]:



a = df['Favorite'].mean()
b = cf['Favorite'].mean()

likesDict={"Namo Average Favorite Count":a,"Rahul Average Favorite count":b}

FavDf = pd.Series(likesDict, name='A')
FavDf.index.name='B'
FavDf = FavDf.reset_index()



# In[48]:





trace = go.Bar(
    x=FavDf['B'],
    y=FavDf['A'],
     marker={'color': 'yellow'}
)

layout = go.Layout(
    xaxis=dict(
        title='Most Common Words',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        tickfont=dict(
            size=14,
            color='black'
        ),
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,

    ),
    title="Average Favorite Counts of Politicians"
)






fig = {
    'data': [trace],
    'layout': layout,
}


iplot(fig)

plotly.offline.plot(fig, filename = 'dd.html', auto_open=False)



# ## What side of politicians does Public Like

# '''
# # get data for politician1 where he is +
# # then -
# #find avg likes on both and off you go
# '''

# In[49]:


temp1 = df[df['Polarity']=='Affirming']


# In[50]:


p = temp1['Retweets'].mean()
q = temp1['Favorite'].mean()


# In[51]:


temp2 = df[df['Polarity']=='Critical']



# In[52]:


r = temp2['Retweets'].mean()
s = temp2['Favorite'].mean()


# In[53]:





# In[54]:


temp3 = cf[cf['Polarity']=='Affirming']



# In[55]:


a = temp3['Retweets'].mean()
b = temp3['Favorite'].mean()


# In[56]:


temp4 = cf[cf['Polarity']=='Critical']



# In[57]:


c = temp4['Retweets'].mean()
d = temp4['Favorite'].mean()


# In[58]:





# In[59]:


##plotting
'''
# make dataframe

'''


# In[60]:


PLIST = [["+ve",p,q],["-ve",r,s]]

temp1 = pd.DataFrame(PLIST, columns="Polarity Retweets Favorite".split())
temp1.set_index('Polarity',inplace=True)


# In[61]:


# In[62]:


temp1.plot(kind='bar',title="Which side of Modi does public like")
plt.savefig("namonamo" + '.png')


# In[63]:


cPLIST = [["+ve",a,b],["-ve",c,d]]

temp2 = pd.DataFrame(cPLIST, columns="Polarity Retweets Favorite".split())
temp2.set_index('Polarity',inplace=True)

temp2.plot(kind='bar',title="Which side of Rahul does public like")
plt.savefig("rahulrahul" + '.png')

