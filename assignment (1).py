import networkx as nx

def random_vaccine(G):
    degrees = dict(G.degree())
    return sum(degrees.values()) / len(degrees)

def indirect_random_vaccine(G):
    degrees = dict(G.degree())
    sum_k_squared = sum(d**2 for d in degrees.values())
    sum_k = sum(degrees.values())
    return sum_k_squared / sum_k