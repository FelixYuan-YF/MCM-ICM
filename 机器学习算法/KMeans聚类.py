from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 生成示例数据
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# 初始化K均值模型，设置簇的数量K=4
kmeans = KMeans(n_clusters=4)

# 拟合模型
kmeans.fit(X)

# 获取簇中心
centers = kmeans.cluster_centers_

# 获取每个数据点的簇标签
labels = kmeans.labels_

# 绘制结果
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], s=200, c='red', marker='X')
plt.show()
