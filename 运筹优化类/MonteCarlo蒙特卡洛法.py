import numpy as np

# 定义目标函数
def objective_function(x1, x2):
    return -(x1 - 2)**2 - (x2 - 3)**2 + 10

# 定义约束条件函数
def constraints(x1, x2):
    return x1 + x2 <= 10 and x1 >= 0 and x2 >= 0

# 蒙特卡罗方法求解
def monte_carlo_optimization(num_samples, objective_function, constraints):
    best_value = -np.inf
    best_solution = None

    for _ in range(num_samples):
        # 随机生成候选解
        x1 = np.random.uniform(0, 10)
        x2 = np.random.uniform(0, 10)

        # 检查是否满足约束条件
        if constraints(x1, x2):
            # 计算目标函数值
            value = objective_function(x1, x2)
            # 更新最优解
            if value > best_value:
                best_value = value
                best_solution = (x1, x2)

    return best_solution, best_value

# 运行蒙特卡罗优化
num_samples = 100000
solution, value = monte_carlo_optimization(num_samples, objective_function, constraints)

print(f"最优解：x1 = {solution[0]:.2f}, x2 = {solution[1]:.2f}")
print(f"最大目标函数值：{value:.2f}")
