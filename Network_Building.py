import csv
import networkx as nx
from operator import itemgetter
from networkx.algorithms import community
from pprint import pprint

import pandas as pd
a=pd.read_table("AROs_file.csv", sep=",")

#converts the Genome Bin to nodes by storiing them into array
with open('AROs_file.csv', 'r') as nodecsv: 
    nodereader = csv.reader(nodecsv) 
    nodes = [n[1] for n in nodereader][1:]
node_names = [n[0] for n in nodes] 

#converts the AROs to edges by storing them into dictionary 
with open('AROs_file.csv', 'r') as edgecsv: 
    edgereader = csv.reader(edgecsv) 
    edges = [set(e[2].split(',')) for e in edgereader][1:]
    #edges = [e for n in edgereader][1:]

pprint(nodes[0:10])
pprint(edges[0:10])

#stores all the AROs in a list
df = pd.read_csv('AROs_file.csv', index_col=0)
df['AROs'] = df['AROs'].str.split(',')
df = df.set_index('Genome_Bin')
df

#creates a matrix which shows how many AROs do each bin have in common with one another 
adj_m = pd.DataFrame(index=df.index, columns=df.index)
for genome_bin_i, aros_i in df.iterrows():
    for genome_bin_j, aros_j in df.iterrows():
        aros_i = aros_i[0]
        aros_j = aros_j[0]
        # print(genome_bin_i)
        # print(set([type(aro) for aro in aros_i]))
        # print(genome_bin_j)
        # print(set([type(aro) for aro in aros_j]))
        adj_m.loc[genome_bin_i, genome_bin_j] = len(set(aros_i).intersection(set(aros_j)))
adj_m

#constructs the graph
G = nx.Graph()
for genome_bin_i, aros_i in df.iterrows():
    for genome_bin_j, aros_j in df.iterrows():
        aros_i = aros_i[0]
        aros_j = aros_j[0]
        # print(genome_bin_i)
        # print(set([type(aro) for aro in aros_i]))
        # print(genome_bin_j)
        # print(set([type(aro) for aro in aros_j]))
        num_overlap_aros = len(set(aros_i).intersection(set(aros_j)))
        G.add_edge(genome_bin_i, genome_bin_j, weight=num_overlap_aros)
density = nx.density(G)
print("Network density:", density)
nx.draw_networkx(G, with_labels=True)

