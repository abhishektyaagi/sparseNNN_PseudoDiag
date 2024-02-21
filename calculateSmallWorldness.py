import numpy as np
import scipy.sparse as sp
import networkx as nx
import networkx as nx
from networkx.algorithms import bipartite
import numpy as np
import scipy.sparse as sp

'''def generate_wrapped_diagonal_matrix(dim, diagonal_starts):
    """
    Generates a matrix of given dimension where diagonals have non-zero elements,
    and diagonals wrap around if they reach the bottom.
    """
    rows, cols = dim
    matrix = np.zeros(dim)
    diagonal_length = min(rows, cols)
    
    for start_row in diagonal_starts:
        for i in range(diagonal_length):
            row = (start_row + i) % rows
            col = (i) % cols
            matrix[row, col] = 1  # Set non-zero element
    
    return sp.coo_matrix(matrix)

def create_bipartite_graph(matrix):
    rows, cols = matrix.shape
    B = nx.Graph()
    B.add_nodes_from(range(rows), bipartite=0)
    B.add_nodes_from(range(rows, rows+cols), bipartite=1)
    B.add_edges_from([(row, col+rows) for row, col in zip(*matrix.nonzero())])
    return B

def bipartite_clustering_coefficient(B):
    # Placeholder for actual bipartite clustering coefficient calculation
    return np.random.random()

def average_path_length(B):
    lengths = dict(nx.all_pairs_shortest_path_length(B))
    total_length = sum(sum(lengths[row].values()) for row in lengths) / 2
    num_paths = sum(len(lengths[row]) for row in lengths) / 2
    return total_length / num_paths'''

def bipartite_clustering_coefficient(B):
    # Automatically determine nodes for one set of the bipartite graph
    # Assuming nodes tagged with bipartite=0 form one set
    nodes_set = [n for n, d in B.nodes(data=True) if d['bipartite'] == 0]
    
    # Project the bipartite graph onto this set of nodes
    projected_G = bipartite.weighted_projected_graph(B, nodes_set)
    
    # Calculate the average clustering coefficient of the projection
    clustering_coefficient = nx.average_clustering(projected_G)
    
    return clustering_coefficient

def create_bipartite_graph(matrix):
    rows, cols = matrix.shape
    B = nx.Graph()
    B.add_nodes_from(range(rows), bipartite=0)
    B.add_nodes_from(range(rows, rows+cols), bipartite=1)
    for row, col in zip(*matrix.nonzero()):
        B.add_edge(row, col+rows)
    return B

def average_path_length(B):
    lengths = dict(nx.all_pairs_shortest_path_length(B))
    total_length = sum(sum(lengths[row].values()) for row in lengths) / 2
    num_paths = sum(len(lengths[row]) for row in lengths) / 2
    return total_length / num_paths

def generate_wrapped_diagonal_matrix(dim, diagonal_starts):
    rows, cols = dim
    matrix = np.zeros(dim)
    diagonal_length = min(rows, cols)
    
    for start_row in diagonal_starts:
        for i in range(diagonal_length):
            row = (start_row + i) % rows
            col = (i) % cols
            matrix[row, col] = 1
    
    return sp.coo_matrix(matrix)

def calculate_small_worldness(matrix):
    print("Starting calculating B, C, L")
    B = create_bipartite_graph(matrix)
    C = bipartite_clustering_coefficient(B)
    L = average_path_length(B)
    print("Finished calculating B, C, L")
    # Placeholder values for random graph comparisons
    C_rand, L_rand = 0.5, 10  # These values are placeholders
    if L == 0:
        sigma = 0
    else:
        sigma = (C / C_rand) / (L / L_rand)
        #sigma = C/L
    #return sigma
    return C, L

# Given dimensions and starting positions for diagonals
dim = (784, 300)
diagonal_starts = [0, 100, 200]  # Example starting positions

# Generate matrix and calculate small-worldness
matrix = generate_wrapped_diagonal_matrix(dim, diagonal_starts)
#sigma = calculate_small_worldness(matrix)
C,L = calculate_small_worldness(matrix)
#print(f"Small-worldness: {sigma}")
