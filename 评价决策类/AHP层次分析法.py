import numpy as np

# 定义判断矩阵
# 例如，对于三个准则：价格、质量、外观
# 数值表示两两比较的相对重要性，1 表示同等重要，>1 表示一个比另一个重要，依此类推
criteria_matrix = np.array([
    [1,   1/3, 3],
    [3,   1,   5],
    [1/3, 1/5, 1]
])

# 一致性随机指标（RI）值，用于一致性检验
RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}

def ahp(matrix):
    # 计算特征值和特征向量
    eigvals, eigvecs = np.linalg.eig(matrix)
    max_eigval = np.max(eigvals).real
    max_eigvec = eigvecs[:, np.argmax(eigvals)].real

    # 归一化特征向量，得到权重
    weights = max_eigvec / np.sum(max_eigvec)

    # 一致性检验
    n = matrix.shape[0]
    CI = (max_eigval - n) / (n - 1)
    CR = CI / RI_dict[n]

    if CR < 0.1:
        print("一致性检验通过")
    else:
        print("一致性检验未通过，请重新调整判断矩阵")

    return weights

# 计算准则的权重
criteria_weights = ahp(criteria_matrix)
print("准则的权重：", criteria_weights)

# 定义每个方案在各个准则下的评分矩阵
# 行表示方案，列表示准则
# 例如，有三个方案 A、B、C
# 对于价格准则，分数越低表示价格越高（假设 1 表示高价，3 表示低价）
# 对于质量和外观，分数越高表示越好
alternatives = np.array([
    [1, 3, 2],  # 方案 A
    [2, 2, 3],  # 方案 B
    [3, 1, 1]   # 方案 C
])

# 计算每个方案的综合得分
# 将方案矩阵的每一列与对应的准则权重相乘，然后求和
scores = alternatives @ criteria_weights
print("方案的综合得分：", scores)

# 选择得分最高的方案
best_alternative_index = np.argmax(scores)
print(f"最优方案是方案 {chr(65 + best_alternative_index)}")