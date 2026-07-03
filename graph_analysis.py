import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("social_network.csv")

# Create graph
G = nx.from_pandas_edgelist(df, "Person1", "Person2")

# Display graph information
print("Number of Nodes:", G.number_of_nodes())
print("Number of Edges:", G.number_of_edges())

# Draw graph
nx.draw(G, with_labels=True)
plt.title("Social Network Graph")
plt.show()