
# coding: utf-8

# In[11]:


import nltk
from nltk.corpus import stopwords


# In[28]:


message = "Help me!! There are people after me."
tokenized_words = nltk.word_tokenize(sentence)
#print(tokenized_words)
stop = set(stopwords.words('english'))

sentence_word = [i for i in message.lower().split() if i not in stop]
print(sentence_word)


# In[9]:


word_class = ['help','urgent','molested','raped','following','harrasing','snatch','abusing','fight','scared','stalking','fondle',
                 'pervert','kidnapped','alarm',
'appall',
'awe',
'bully',
'coerce',
'constrain',
'daunt',
'dishearten',
'dismay',
'scare',
'subdue'
'terrify',
'terrorize',
'badger',
'bait',
'bludgeon',
'bluster',
'browbeat',
'buffalo',
'bulldoze',
'chill',
'compel',
'cow',
'dispirit',
'disquiet',
'dragoon',
'enforce',
'force',
'hound',
'oblige',
'overawe',
'ride',
'ruffle',
'spook',
'strong-arm',
'bowl over',
'lean on',
'push around',
'showboat',
"twist someone's arm",'trouble', 'sorry', 'anxiety', 'perturbation', 'uneasiness', 'disquiet', 'angst']


# In[30]:


count = 0
for ix in sentence_word:
    if ix in word_class:
        print(ix)
        count += 1
    
    
    

