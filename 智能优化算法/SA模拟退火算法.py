import numpy as np
import matplotlib.pyplot as plt

# 定义目标函数
def objective_function(x):
    return x**2 + 4 * np.sin(5 * x) + 7 * np.cos(3 * x)

# 模拟退火算法参数
T_initial = 1000      # 初始温度
T_min = 1e-3          # 最小温度
cooling_rate = 0.99   # 降温系数
max_iter = 1000       # 每个温度的最大迭代次数

# 搜索空间范围
x_min, x_max = -10, 10

# 模拟退火算法
def simulated_annealing():
    # 初始化
    current_x = np.random.uniform(x_min, x_max)  # 随机初始解
    current_f = objective_function(current_x)   # 当前解的目标函数值
    T = T_initial  # 当前温度

    best_x, best_f = current_x, current_f  # 记录历史最优解
    
    while T > T_min:
        for _ in range(max_iter):
            # 在当前解附近生成新解
            new_x = current_x + np.random.uniform(-1, 1)
            # 确保新解在搜索空间范围内
            new_x = np.clip(new_x, x_min, x_max)
            new_f = objective_function(new_x)

            # 判断是否接受新解
            delta_f = new_f - current_f
            if delta_f < 0 or np.random.rand() < np.exp(-delta_f / T):
                current_x, current_f = new_x, new_f

            # 更新历史最优解
            if current_f < best_f:
                best_x, best_f = current_x, current_f

        # 降温
        T *= cooling_rate

    return best_x, best_f

# 执行模拟退火算法
best_x, best_f = simulated_annealing()
print(f"最优解: x = {best_x}")
print(f"目标函数值: f(x) = {best_f}")

# 可视化目标函数
x = np.linspace(x_min, x_max, 500)
y = objective_function(x)
plt.plot(x, y, label="Objective Function")
plt.scatter(best_x, best_f, color='red', label="Best Solution")
plt.title("Simulated Annealing Optimization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
