import networkx as nx
import matplotlib.pyplot as plt

# 创建一个有向图
DG = nx.DiGraph()

# 添加节点和边
DG.add_edges_from([(1, 2, {'weight': 1}),
                  (1, 3, {'weight': 4}),
                  (2, 3, {'weight': 2}),
                  (2, 4, {'weight': 5}),
                  (3, 4, {'weight': 1})])

# 计算从节点1到节点4的最短路径
shortest_path = nx.shortest_path(DG, source=1, target=4, weight='weight')
print(f"从节点1到节点4的最短路径是：{shortest_path}")

# 创建一个无向图
G = nx.Graph()

# 添加节点和边
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# 检查图是否是连通的
is_connected = nx.is_connected(G)
print(f"图是否连通：{is_connected}")

# 绘制图
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
plt.show()