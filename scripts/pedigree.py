# Import the necessary python packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import API
import urllib.request, json, csv

# Make a network and plot it
import networkx as nx
from pyvis import network as net
from pyvis.network import Network

# Import the birds dataset
with urllib.request.urlopen("https://gracula.psyc.virginia.edu/birds/api/pedigree/?species=zebf") as url:
    data = pd.read_json(url)

data["uuid"] = data["uuid"].str[:6] # Shorten the uuid string to 6 characters

# Remove birds with no Dam or no Sire
# Define a function that drops rows
def filter_rows_by_values(df, col, values):
    return df[~df[col].isin(values)]

data = filter_rows_by_values(data, "sire", [None])

# Save as a csv
data.to_csv('../build/pedigree.csv', encoding='utf-8', index=False)

# Use NetworkX to build the network out of the csv
# Define the variables to extract:
name = data["name"]
sire = data["sire"]
dam = data["dam"]
alive = data["alive"]
sex = data["sex"]

# Make a network for the birds now!
G = nx.Graph()

data = data.reset_index() # Make sure indexes pair with number of rows
for index, row in data.iterrows():
    G.add_nodes_from([(row['name'], {"alive": row['alive']})])
    G.add_edge(row['dam'], row['name'])
    G.add_edge(row['sire'], row['name'])

# Use Pyvis to generate a dynamical network representation
g = net.Network(height="750px", width="100%", bgcolor="#222222", font_color="white", select_menu=True, notebook=False)
g.barnes_hut()

nxg = G
g.from_nx(nxg)
# g.toggle_physics(True) # Toggle the physic in-between nodes
g.generate_html(name="example.html", local=True, notebook=False)
g.show('example.html', notebook=False)