#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


# In[59]:


pd.options.display.max_colwidth = 500


# In[60]:


f = pd.read_csv('202005171549_corona_tweets.csv')
df = pd.DataFrame(data = f)
df.head(3)


# In[61]:


f2 = pd.read_csv('202005171549_corona_tweets.csv', nrows=15)
print(f2)


# In[62]:


#1- How many lines are there in the dataframe? How much space does it consume in your memory? 


# In[63]:


len(df)


# In[64]:


df.memory_usage()
df.memory_usage(index=True).sum() #Overall memory consumption
df.info(memory_usage='deep')


# In[65]:


#2- What are the column names?


# In[66]:


for col in df.columns: 
    print(col) 


# In[67]:


#3- Identify the most tweeting 50 users.


# In[68]:


most_tweeting_users = df['screen_name'].value_counts() 
print(most_tweeting_users.head(50))


# In[69]:


#4- Plot a histogram of the 50 most tweeting users.


# In[70]:


most_tweeting_users.head(50).hist(bins=50) 
plt.title('Most Tweeting 50 Users')
plt.xlabel('Number of tweets')
plt.ylabel('Number of users')
plt.show()


# In[71]:


#5- Identify duplicate tweets based on the 'text' field.


# In[72]:


duplicateRowsDF = df[df['text'].duplicated()]['text']
print(duplicateRowsDF)


# In[73]:


# 6- Remove duplicate tweets based on the 'text' field. How many tweets do you have now?


# In[74]:


df.drop_duplicates(subset=['text'], inplace=False) 


# In[75]:


# 7- Replace all users names with the usrusr token. 
#You need to write a regular expression that identify user names and use the replace methodto replace it with the 'usrusr' token.


# In[76]:


#usernames = df['text'].str.findall(r'@([\w]+)')
#for item in usernames:
#    for element in item:
#        print(element)
        
df['text'] = df['text'].str.replace('@([\w]+)','usrusr', regex=True)


# In[77]:


#TESTING
usr =[]

for item in df['text'].str.lower():
        if 'usrusr' in item:
            usr.append(item)
print(url[:10])


# In[78]:


#8- Replace all URLs with 'urlurl' token in the 'text' column.


# In[79]:


#urls = df['text'].str.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
#print(urls)
#URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', thestring)
#df['text'] = df['text'].str.re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', 'urlurl')
df['text'] = df['text'].str.replace('https?://\S+','urlurl', regex=True)


# In[80]:


# TESTING
url =[]

for item in df['text'].str.lower():
        if 'urlurl' in item:
            url.append(item)
print(url[:10])


# In[81]:


#9- If a tweet starts with "RT @", it is a retweet. Remove all retweets from the dataframe.


# In[82]:


df2 = df[~df.text.str.startswith('RT @')]
df = df2


# In[83]:


# 10- If the field is_retweet contains the value True, this tweet is a retweet as well. Remove those as well.


# In[84]:


retweets = df['is_retweet'] == True
#df.drop(labels=retweets, inplace = False)
df_without_retweets = df[~df.is_retweet == True]


# In[85]:


# 11- Check how many duplicate tweets are there. Remove them. How many tweets do you have now?


# In[86]:


duplicateRowsDF = df.duplicated()
df.drop_duplicates(subset=['is_retweet'], inplace=False) 


# In[87]:


# 12- Plot a histogram of the text lengths. What is the length of the longest and the shortest tweets?


# In[88]:


length_of_tweets = df['text'].str.len()
length_of_tweets.hist(bins=50) 
plt.title('Text lengths of tweets')
plt.xlabel('Number of tweets')
plt.ylabel('Length of tweets')
plt.show()


# In[89]:


# 13- Calculate the average tweet length based on the 'text' field.


# In[90]:


length_of_tweets.mean()


# In[91]:


#14- Extract all words from the 'text' field and put them in a new column. 
#The findall method and a regular expression to recognize words will help you.


# In[92]:


words_of_tweets = df['text'].str.findall(r'\w+')
#words_of_tweets = re.findall(r'\w+', df['text'].lower())
df['Words'] = words_of_tweets
print(df['Words'])


# In[93]:


#15- Identify the words that occur the most. The Counter object from collections will help you.


# In[94]:


# empty Counter
word_counter = Counter()
#df['text'].str.findall(r'\w+')

for tokenlist in df['text'].str.lower().str.findall(r'\w+'):
    word_counter.update(tokenlist)
#print(word_counter.most_common()[:200])
print(word_counter.most_common())


# In[95]:


# 16- How many of the words occur only once? List 100 of them. Provide tweets that contain these words.


# In[96]:


occur_once_keys = []
for key, value in word_counter.items():
    if value == 1:
        occur_once_keys.append(key)
        
for item in occur_once_keys[:100]:
    print(item)


# In[97]:


#17- Find the longest 100 words. List them.


# In[98]:


new_word_counter = {}
for k in sorted(word_counter, key=len, reverse=True): # Through keys sorted by length
    new_word_counter[k] = word_counter[k]
keys = list(new_word_counter.keys())
for key in keys[0:100]:
    print(key)


# In[99]:


#18- Find tweets that are all in upper case, such as "THIS IS A TWEET ALL UPPER CASE." in their 'text' field. 


# In[100]:


#df['text'].str.isupper()
for i in df['text']:
    if i.isupper() == True:
        print(i)


# In[101]:


#19- Identify the mostly occurring 50 hashtags.


# In[102]:


word_counter2 = Counter()
for tokenlist in df['text'].str.lower().str.findall(r"#(\w+)"):
    word_counter2.update(tokenlist)
print(word_counter2.most_common()[:50])


# In[103]:


#20- Export the final dataframe to csv and Excel files.


# In[104]:


df.to_csv(r'/Volumes/Archive/final\ assignment \finalassignment.csv', index = False)
df.to_excel(r'/Volumes/Archive/final\ assignment \finalassignment.xlsx', index = False)


# In[105]:


### Find tweets about Trump (not including retweets). Print 100 of them.


# In[112]:


tweets_trump =[]

for item in df['text']:
    if 'RT' not in item:
        if 'Trump' in item:
            tweets_trump.append(item)
for item in tweets_trump[:100]:
    print(item)
    


# In[107]:


### Find tweets about Turkey (not including retweets). Print 100 of them.


# In[108]:


tweets_turkey =[]

for item in df['text'].str.lower():
    if 'RT' not in item:
        if 'turkey' in item:
            tweets_turkey.append(item)
for item in tweets_turkey[:100]:
    print(item)


# In[109]:




