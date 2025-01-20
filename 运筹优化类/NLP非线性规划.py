import numpy as np
from scipy.optimize import minimize

# 定义目标函数：f(x) = x1^2 + x2^2
def objective(x):
    return x[0]**2 + 2*x[1]**2

# 定义约束条件：x1 + x2 = 1
def constraint(x):
    return x[0] + x[1] - 1

# 初始猜测值：设置变量 x1 和 x2 的初始值
x0 = np.array([0.5, 0.5])

# 定义约束字典
# 'type': 'eq' 表示等式约束
# 'type': 'ineq' 表示不等式约束
# 'eq'表示表达式等于0 ；'ineq'表示表达式大于等于0
cons = {'type': 'eq', 'fun': constraint}

# 调用优化函数 minimize
solution = minimize(objective, x0, constraints=cons)

# 输出结果
print(f"最优解：x1 = {solution.x[0]:.2f}, x2 = {solution.x[1]:.2f}")
print(f"最小目标函数值：{solution.fun:.2f}")
