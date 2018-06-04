
# coding: utf-8

# In[1]:


class10_Score= [["Ram", 76, "Meena", 87, "Deepak", 81, "Sahil", 36, "Aarti", 47]]


# In[2]:


import numpy as np
class10_Score1= np.array(class10_Score)


# In[3]:


class10_Score


# In[27]:


type(class10_Score)


# In[4]:


class10_Score1


# In[26]:


type(class10_Score1)


# In[6]:


class10_Score.append("Surender")


# In[7]:


class10_Score.append(70)


# In[8]:


class10_Score


# In[9]:


class10_Score1


# In[10]:


np.delete(class10_Score1,-1)


# In[12]:


class10_Score=[10,20,40]


# In[13]:


class10_Score + class10_Score


# In[14]:


class10_score1= np.array([10,20,40])


# In[15]:


class10_score1 + class10_score1


# In[16]:


class10_Score2= np.array([10,50,60,80,90,95,72])


# In[17]:


class10_Score2 > 60


# In[18]:


class10_Score2[class10_Score2 > 60]


# In[19]:


np_2d= np.array([[5,7,5,5,6],
                [6,8,9,8,4]])


# In[20]:


np_2d


# In[21]:


np_2d.shape


# In[22]:


np_2d[1,3]


# In[23]:


np_2d[1][3]


# In[24]:


np_2d[:,1:3]


# In[25]:


np_2d[1,:]

