#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[2]:


cast = pd.read_csv('C:/Users/parit/Downloads/cast.csv')
cast.head()


# ### How many movies are listed in the titles dataframe?

# In[14]:


total =cast.title.shape[0]


# In[15]:


print(total,"movies are listed in the titles dataframe")


# ### What are the earliest two films listed in the titles dataframe?

# In[60]:


mov=cast.sort_values("year")["title"].unique()[:2]
print(f" the earliest two films listed in the titles dataframe are {mov[0]} and {mov[1]} ")


# ### How many movies have the title "Hamlet"?

# In[142]:


cast.title[cast.title=="Hamlet"]


# In[16]:


total=cast.title[cast.title=="Hamlet"].count()


# In[20]:


print(total,"movies have the title 'Hamlet'")


# ### How many movies are titled "North by Northwest"?

# In[10]:


cast.title[cast.title=="North by Northwest"]


# In[23]:


total=cast.title[cast.title=="North by Northwest"].shape[0]


# In[25]:


print(total,"movies are titled North by Northwest")


# ### When was the first movie titled "Hamlet" made?

# In[31]:


st_movie=cast[cast.title=="Hamlet"].sort_values("year")


# In[36]:


first=st_movie.year.iloc[0]


# In[37]:


print("the first movie titled Hamlet was made in",first)


# ### List all of the "Treasure Island" movies from earliest to most recent.

# In[62]:


cast[cast.title=="Treasure Island"].sort_values("year").reset_index()


# In[ ]:





# ### How many movies were made in the year 1950?

# In[63]:


mov_cnt=cast.year[cast.year==1950].count()


# In[64]:


print(f"{mov_cnt} movies were made in the year 1950")


# ### How many movies were made in the year 1960?

# In[38]:


mov_cnt=cast.title[cast.year==1960].count()


# In[39]:


print(f"{mov_cnt} movies were made in the year 1960")


# ### How many movies were made from 1950 through 1959?

# In[40]:


mov_cnt=cast.year[cast.year>=1950][cast.year<=1959].count()


# In[41]:


print(mov_cnt,"movies were made from 1950 through 1959")


# ### In what years has a movie titled "Batman" been released?

# In[75]:


cast[cast.title=="Batman"]["year"].unique()


# In[ ]:





# ### How many roles were there in the movie "Inception"?

# In[42]:


roles=cast.name[cast.title=="Inception"].count()


# In[43]:


print(roles,"roles were there in the movie Inception")


# ### How many roles in the movie "Inception" are NOT ranked by an "n" value?

# In[44]:


roles=cast.n[cast.title=="Inception"].isnull().sum()


# In[45]:


print(roles,"roles in the movie Inception are NOT ranked by an n value")


# ### But how many roles in the movie "Inception" did receive an "n" value?

# In[46]:


roles=cast.n[cast.title=="Inception"].count()


# In[47]:


print(roles,"many roles in the movie Inception did receive an n value")


# ### Display the cast of "North by Northwest" in their correct "n"-value order, ignoring roles that did not earn a numeric "n" value.

# In[78]:


cast[cast.title=="North by Northwest"].sort_values("n").dropna()


# ### Display the entire cast, in "n"-order, of the 1972 film "Sleuth".

# In[49]:


cast[cast.title=="Sleuth"][cast.year==1972].sort_values("n",ascending=False).head(1)


# ### Now display the entire cast, in "n"-order, of the 2007 version of "Sleuth".

# In[80]:


cast[cast.title=="Sleuth"][cast.year==2007].sort_values("n",ascending=False).head(1)


# ### How many roles were credited in the silent 1921 version of Hamlet?

# In[50]:


roles=cast.n[cast.title=="Hamlet"][cast.year==1921].shape[0]


# In[51]:


print(roles,"roles were credited in the silent 1921 version of Hamlet")


# ### How many roles were credited in Branagh’s 1996 Hamlet?

# In[52]:


roles=cast.n[cast.title=="Hamlet"][cast.year==1996].shape[0]


# In[53]:


print(roles,"roles were credited in Branagh’s 1996 Hamlet")


# ### How many "Hamlet" roles have been listed in all film credits through history?

# In[54]:


roles=cast.n[cast.title=="Hamlet"].shape[0]


# In[57]:


print(roles,"Hamlet roles have been listed in all film credits through history")


# ### How many people have played an "Ophelia"?

# In[102]:


cast.name[cast.title=="Ophelia"].shape[0]


# ### How many people have played a role called "The Dude"?

# In[107]:


cast.name[cast.character=="The Dude"].shape[0]


# In[ ]:





# ### How many people have played a role called "The Stranger"?

# In[110]:


cast.name[cast.character=="The Stranger"].shape[0]


# In[ ]:





# ### How many roles has Sidney Poitier played throughout his career?

# In[62]:


cast.character[cast.name=="Sidney Poitier"].count()


# ### How many roles has Judi Dench played?

# In[112]:


cast.character[cast.name=="Judi Dench"].shape[0]


# In[ ]:





# ### List the supporting roles (having n=2) played by Cary Grant in the 1940s, in order by year.

# In[64]:


cast[cast.name=="Cary Grant"][cast.n==2][cast.year>=1940]


# In[ ]:





# ### List the leading roles that Cary Grant played in the 1940s in order by year.

# In[65]:


cast[cast.name=="Cary Grant"][cast.n==1][cast.year>=1940][cast.year<=1949].sort_values("year")


# In[ ]:





# ### How many roles were available for actors in the 1950s?

# In[113]:


cast.n[cast.type=="actor"][cast.year>=1950][cast.year<=1959].shape[0]


# In[ ]:





# ### How many roles were available for actresses in the 1950s?

# In[114]:


cast.n[cast.type=="actress"][cast.year>=1950][cast.year<=1959].shape[0]


# In[ ]:





# ### How many leading roles (n=1) were available from the beginning of film history through 1980?

# In[116]:


cast.n[cast.n==1][cast.year<1980].shape[0]


# In[ ]:





# ### How many non-leading roles were available through from the beginning of film history through 1980?

# In[118]:


cast.n[cast.n!=1][cast.year<1980].shape[0]


# ### How many roles through 1980 were minor enough that they did not warrant a numeric "n" rank?

# In[138]:


cast.n[cast.year<1980].shape[0]


# In[139]:


cast.n[cast.year<1980].dropna().shape[0]


# In[140]:


cast.n[cast.year<1980].shape[0] - cast.n[cast.year<1980].dropna().shape[0]


# In[ ]:




