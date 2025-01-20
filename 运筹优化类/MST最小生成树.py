import networkx as nx

# 创建一个加权无向图
G = nx.Graph()
edges = [
    ('A', 'B', 4),
    ('A', 'H', 8),
    ('B', 'H', 11),
    ('B', 'C', 8),
    ('H', 'I', 7),
    ('H', 'G', 1),
    ('I', 'G', 6),
    ('I', 'C', 2),
    ('C', 'F', 4),
    ('C', 'D', 7),
    ('G', 'F', 2),
    ('F', 'D', 14),
    ('F', 'E', 10),
    ('D', 'E', 9)
]
G.add_weighted_edges_from(edges)

# 使用Kruskal算法计算最小生成树
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# 输出最小生成树的边
print("最小生成树的边：")
for edge in mst.edges(data=True):
    print(edge)
