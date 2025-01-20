import numpy as np
import pandas as pd

def grey_relational_analysis(reference, comparatives, rho=0.5):
    """
    进行灰色关联分析
    :param reference: 参考序列（1D numpy array）
    :param comparatives: 比较序列（2D numpy array，每行对应一个比较序列）
    :param rho: 分辨系数，取值范围 [0,1]，一般取 0.5
    :return: 各比较序列与参考序列的关联度（1D numpy array）
    """
    # 数据无量纲化处理（极差法）
    def normalize(data):
        return (data - np.min(data)) / (np.max(data) - np.min(data))

    # 对参考序列和比较序列进行无量纲化处理
    reference_normalized = normalize(reference)
    comparatives_normalized = np.array([normalize(comp) for comp in comparatives])

    # 计算关联系数
    diff_matrix = np.abs(reference_normalized - comparatives_normalized)
    min_diff = np.min(diff_matrix)
    max_diff = np.max(diff_matrix)
    xi = (min_diff + rho * max_diff) / (diff_matrix + rho * max_diff)

    # 计算关联度
    correlation_degree = np.mean(xi, axis=1)
    return correlation_degree

# 示例数据：参考序列和比较序列
reference = np.array([1, 2, 3, 4, 5])
comparatives = np.array([
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6]
])

# 进行灰色关联分析
correlation_degrees = grey_relational_analysis(reference, comparatives)
print("各比较序列与参考序列的关联度：", correlation_degrees)