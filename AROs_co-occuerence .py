#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
a=pd.read_table("AROs_file.csv", sep=",", index_col=0, nrows=100)


# In[10]:


a[0:5]


# In[11]:


a['AROs'] = a['AROs'].str.split(',').apply(set)
AROs = set.union(*a['AROs'].tolist())
len(AROs)


# In[12]:


# AROs co-occurrence matrix.
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
adj_m = pd.DataFrame(index=AROs, columns=AROs)
for aros_i in tqdm(AROs):
    for aros_j in AROs:
        # print(genome_bin_i)
        # print(set([type(aro) for aro in aros_i]))
        # print(genome_bin_j)
        # print(set([type(aro) for aro in aros_j]))
        value = a[a.AROs.apply(lambda x: aros_i in x and aros_j in x)].shape[0]
        G.add_edge(aros_i, aros_j, weight=value)
        adj_m.loc[aros_i, aros_j] = value
        adj_m.loc[aros_j, aros_i] = value
print(adj_m.iloc[0:10, 0:10])
density = nx.density(G)
print("Network density:", density)
nx.draw_networkx(G, with_labels=True)
plt.savefig("p00p.png", dpi=300, bbox_inches='tight')
plt.show()


# In[18]:


adj_m.iloc[0:10, 0:10]


# In[6]:


adj_m


# In[8]:


adj_m.to_csv("AROs_co-occuerence.csv")


# In[ ]:




