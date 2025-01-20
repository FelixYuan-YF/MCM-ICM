import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# 加载示例数据集（以鸢尾花数据集为例）
data = load_iris()
X = data.data  # 特征数据
y = data.target  # 标签

# 创建 PCA 对象，设置降维后的维度数为 2
pca = PCA(n_components=2)

# 对数据进行 PCA 降维
X_pca = pca.fit_transform(X)

# 输出主成分的方差解释比例
print("各主成分的方差解释比例：", pca.explained_variance_ratio_)

# 可视化降维后的数据
plt.figure(figsize=(8, 6))
for target in np.unique(y):
    plt.scatter(X_pca[y == target, 0], X_pca[y == target, 1], label=data.target_names[target])
plt.xlabel('主成分 1')
plt.ylabel('主成分 2')
plt.title('PCA 降维后的鸢尾花数据')
plt.legend()
plt.grid(True)
plt.show()
