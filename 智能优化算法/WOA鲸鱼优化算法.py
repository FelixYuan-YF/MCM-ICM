import numpy as np
import matplotlib.pyplot as plt

# 定义目标函数
def objective_function(x):
    return np.sum(x**2)

# 初始化鲸鱼种群
def initialize_population(pop_size, dim, bounds):
    return np.random.uniform(bounds[0], bounds[1], (pop_size, dim))

# 更新鲸鱼位置
def update_position(whale, best_whale, a, bounds):
    r1 = np.random.rand()
    r2 = np.random.rand()
    A = 2 * a * r1 - a
    C = 2 * r2
    b = 1
    l = np.random.uniform(-1, 1)
    p = np.random.rand()
    D = abs(C * best_whale - whale)
    if p < 0.5:
        if abs(A) < 1:
            new_position = best_whale - A * D
        else:
            rand_whale = np.random.uniform(bounds[0], bounds[1], len(whale))
            D_rand = abs(C * rand_whale - whale)
            new_position = rand_whale - A * D_rand
    else:
        distance_to_best = abs(best_whale - whale)
        new_position = distance_to_best * np.exp(b * l) * np.cos(2 * np.pi * l) + best_whale
    return np.clip(new_position, bounds[0], bounds[1])

# 参数设置
pop_size = 30       # 种群规模
dim = 2             # 维度
bounds = [-10, 10]  # 搜索空间边界
max_iter = 100      # 最大迭代次数

# 初始化种群
population = initialize_population(pop_size, dim, bounds)
best_whale = population[0]
best_fitness = objective_function(best_whale)

# 迭代优化
fitness_history = []
for t in range(max_iter):
    a = 2 - t * (2 / max_iter)  # 线性衰减参数
    for i in range(pop_size):
        fitness = objective_function(population[i])
        if fitness < best_fitness:
            best_fitness = fitness
            best_whale = population[i]
        population[i] = update_position(population[i], best_whale, a, bounds)
    fitness_history.append(best_fitness)
    print(f"Iteration {t+1}: Best Fitness = {best_fitness}")

print(f"Optimal Solution: {best_whale}")
print(f"Optimal Fitness: {best_fitness}")

# 绘制适应度值变化曲线
plt.plot(fitness_history)
plt.title('Fitness over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Best Fitness')
plt.show()
