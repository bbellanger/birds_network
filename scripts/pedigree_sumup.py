# IMPORT THE NECESSARY PACKAGES
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt

# Import datetime
from datetime import datetime

# For kinship and pedigree
import PyAGH
import graphviz

# Import API
import urllib.request, json, csv

# NECESSARY FUNCTIONS
# Remove birds with no Dam or no Sire
# Define a function that drops rows
def filter_rows_by_values(df, col, values):
    return df[~df[col].isin(values)]

# Use the function:
# data = filter_rows_by_values(data, "sire", [None])

# Definition of the function kinship_score
def k_score(row):
    median = row['p_group_median']
    upper = row['p_group_upper']
    if row['p_kinship'] == 0:
        return 10
    elif 0 < row['p_kinship'] < median :
        return 7
    elif median <= row['p_kinship'] <= upper :
        return 4
    elif row['p_kinship'] > upper :
        return 0
    else:
        return "NA"

# Use the function:
# selected_rows['k_score'] = selected_rows.apply(k_score, axis=1)

# IMPORT THE BIRDS DATASET
with urllib.request.urlopen("https://gracula.psyc.virginia.edu/birds/api/pedigree/?species=zebf") as url:
    data = pd.read_json(url)

# Clean up
data["uuid"] = data["uuid"].str[:6]
data["name"] = data["name"].str[5:]
data["sire"] = data["sire"].str[5:]
data["dam"] = data["dam"].str[5:]

# replace 'None' by 'origin' in sire/dam
data["sire"] = data["sire"].replace({None: "Origin"})
data["dam"] = data["dam"].replace({None: "Origin"})

# CALCULATE THE AGE OF THE BIRDS
# Calculate the age for all the birds
today = datetime.today()

# Convert acquisition into a timestamp
birth = pd.to_datetime(data['acquired_on'])

# Calculate
data["age"] = (today - birth).dt.days

# Convert in 0 & 1
data = data*1

for index, row in data.iterrows():
    if row['alive'] == 0:
        data.at[index, 'age'] = "NA"

# GENERATE A PEDEGREE TABLE TO USE
ped = pd.DataFrame()

ped["id"] = data["name"]
ped["sire"] = data["sire"]
ped["dam"] = data["dam"]

ped = filter_rows_by_values(ped, "sire", ["Origin"]) # Filter out the birds brought from the store

# ADD THE COEFF OF INBREEDING TO THE DATA
sort_ped = PyAGH.sortPed(ped) # Select all the birds for analysis instead of a given bird
A = PyAGH.makeA(sort_ped)

coef_inbreeding = PyAGH.coefInbreeding(A)
coef_kinship = PyAGH.coefKinship(A)

# Making it shinny
coef_inbreeding["name"] = coef_inbreeding["ID"]
coef_inbreeding["coef_inbreeding"] = coef_inbreeding["F"]
coef_inbreeding = coef_inbreeding[["name", "coef_inbreeding"]]

parent_kinship = pd.DataFrame()

parent_kinship['sire'] = coef_kinship['ID1']
parent_kinship['dam'] = coef_kinship['ID2']
parent_kinship['p_kinship'] = coef_kinship['r']

# MERGE IT TO THE DATA
data = pd.merge(
    data, coef_inbreeding, on=["name"]
)

# EXTRACT THE PARENTS KINSHIP
master = pd.merge(data, parent_kinship, how="left", on=['sire', 'dam'])
# AND THE KINSHIP SCORE
# Calculate the median and the respective quartiles
p_k_mean = master['p_kinship'].mean()
p_k_median = master['p_kinship'].median()

master['p_k_mean'] = p_k_mean

# EXTRACT DATA FROM A GIVING LIST OF BIRDS
input_table = pd.read_csv("../input/list_input.csv")

# Filter the birds from the input list out of the mastersheet
selected_rows = master[master['name'].isin(input_table['name'])]

# Selected group mean and median
selected_rows['p_group_median'] = selected_rows['p_kinship'].median()
selected_rows['p_group_mean'] = selected_rows['p_kinship'].mean()
selected_rows['p_group_upper'] = selected_rows['p_kinship'].quantile(0.75)
selected_rows['p_group_lower'] = selected_rows['p_kinship'].quantile(0.25)

selected_rows['k_score'] = selected_rows.apply(k_score, axis=1)

# EXPORT TABLE AS CSV
master.to_csv("../output/master.csv")
selected_rows.to_csv("../output/selected_birds.csv")

# GENERATES HEATMAP AND CLUSTER FOR SELECTED BIRDS
list_of_birds = []

for index, row in selected_rows.iterrows():
    bird = row['name']
    list_of_birds.append(bird)

ped_selected = PyAGH.selectPed(data=ped, id=list_of_birds, generation=2) # Print X generations of the chosen bird
ped_selected = PyAGH.sortPed(ped_selected)

sort_ped = PyAGH.sortPed(ped_selected) # Sort the pedigree first
A = PyAGH.makeA(sort_ped)

cluster_example = PyAGH.cluster(A)
plt.xticks(rotation=90)
plt.savefig('../output/cluster_selected_birds.png', facecolor='w', dpi=300)

heatmap_example = PyAGH.heat(A)
plt.xticks(rotation=90)
plt.savefig('../output/heatmap_selected_birds.png', facecolor='w',dpi=500)