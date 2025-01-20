import numpy as np

def gm11(x0):
    """
    GM(1,1)模型
    :param x0: 原始数据序列（numpy数组）
    :return: 预测值序列（numpy数组）
    """
    # 累加生成序列
    x1 = np.cumsum(x0)
    
    # 构造数据矩阵B和数据向量Y
    B = np.array([[-0.5 * (x1[i] + x1[i + 1]), 1] for i in range(len(x0) - 1)])
    Y = x0[1:].reshape(-1, 1)
    
    # 计算参数向量a, b
    [[a], [b]] = np.linalg.inv(B.T @ B) @ B.T @ Y
    
    # 预测序列
    x_hat = [(x0[0] - b / a) * np.exp(-a * k) + b / a for k in range(len(x0))]
    
    return np.array(x_hat)

# 示例数据
x0 = np.array([223.3, 227.3, 230.5, 238.1, 242.9, 251.1])

# 预测
x_hat = gm11(x0)

print("原始数据：", x0)
print("预测数据：", x_hat)
