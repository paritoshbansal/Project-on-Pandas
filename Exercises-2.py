#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[19]:


titles = pd.read_csv('C:/Users/parit/Downloads/titles.csv')
titles.head()


# In[6]:


cast = pd.read_csv('C:/Users/parit/Downloads/cast.csv')
cast.head()


# ### What are the ten most common movie names of all time?

# In[20]:


titles.title.value_counts().head(10)


# In[ ]:





# ### Which three years of the 1930s saw the most films released?

# In[12]:


titles.head(1)


# In[21]:


titles.year[titles.year>=1930][titles.year<=1939].value_counts().head(3)


# ### Plot the number of films that have been released each decade over the history of cinema.

# In[28]:


(titles.year//10*10).value_counts().sort_index().plot(kind="bar")


# In[ ]:





# ### Plot the number of "Hamlet" films made each decade.

# In[34]:


(titles[titles.title=="Hamlet"].year//10*10).value_counts().sort_index().plot(kind="bar")


# In[ ]:





# ### Plot the number of "Rustler" characters in each decade of the history of film.

# In[35]:


titles.head(1)


# In[36]:


cast.head(1)


# In[37]:


(cast[cast.character=="Rustler"].year//10*10).value_counts().sort_index().plot(kind="bar")


# ### Plot the number of "Hamlet" characters each decade.

# In[38]:


(cast[cast.character=="Hamlet"].year//10*10).value_counts().sort_index().plot(kind="bar")


# In[ ]:





# ### What are the 11 most common character names in movie history?

# In[39]:


cast.head(1)


# In[41]:


cast.character.value_counts().head(11)


# ### Who are the 10 people most often credited as "Herself" in film history?

# In[43]:


cast.name[cast.character=="Herself"].value_counts().head(10)


# ### Who are the 10 people most often credited as "Himself" in film history?

# In[45]:


cast.name[cast.character=="Himself"].value_counts().head(10)


# In[ ]:





# ### Which actors or actresses appeared in the most movies in the year 1945?

# In[55]:


cast.name[cast.year==1945].value_counts().head(10)


# In[ ]:





# ### Which actors or actresses appeared in the most movies in the year 1985?

# In[56]:


cast.name[cast.year==1985].value_counts().head(10)


# In[ ]:





# ### Plot how many roles Mammootty has played in each year of his career.

# In[58]:


cast[cast.name=="Mammootty"].year.value_counts().sort_index().plot(grid=True)


# In[ ]:





# ### What are the 10 most frequent roles that start with the phrase "Patron in"?

# In[59]:


cast.head(1)


# In[69]:


cast.character[cast.character.str.startswith("Patron in")].value_counts().head(10)


# ### What are the 10 most frequent roles that start with the word "Science"?

# In[71]:


cast.character[cast.character.str.startswith("Science")].value_counts().head(10)


# In[ ]:





# ### Plot the n-values of the roles that Judi Dench has played over her career.

# In[73]:


cast.head(1)


# In[91]:


cast[cast.name=="Judi Dench"].plot(x="year",y="n",kind="scatter")


# ### Plot the n-values of Cary Grant's roles through his career.

# In[95]:


cast[cast.name=="Cary Grant"].plot(x="year",y="n",kind="scatter")


# In[ ]:





# ### Plot the n-value of the roles that Sidney Poitier has acted over the years.

# In[101]:


cast[cast.name=="Sidney Poitier"].sort_values("year").plot(x="year",y="n",kind="scatter")


# In[ ]:





# ### How many leading (n=1) roles were available to actors, and how many to actresses, in the 1950s?

# In[102]:


cast.head(1)


# In[106]:


cast.type[cast.n==1][cast.year>=1950][cast.year<=1959].value_counts()


# ### How many supporting (n=2) roles were available to actors, and how many to actresses, in the 1950s?

# In[110]:


cast.type[cast.n==2][cast.year>=1950][cast.year<=1959].value_counts()


# In[ ]:




