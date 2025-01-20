import numpy as np
from scipy.optimize import minimize

# 定义目标函数
def objective(x):
    # 目标1：最小化生产成本
    cost = x[0]**2 + x[1]**2
    # 目标2：最小化生产时间
    time = (x[0] - 1)**2 + (x[1] - 1)**2
    # 目标3：最大化产品质量
    quality = -(x[0] - 2)**2 - (x[1] - 2)**2
    return [cost, time, quality]

# 定义约束条件
def constraint(x):
    return x[0] + x[1] - 3

# 初始猜测
x0 = np.array([1, 1])

# 求解多目标优化问题
result = minimize(lambda x: np.sum(objective(x)), x0, constraints={'type': 'eq', 'fun': constraint})
print(f"最优解：{result.x}")