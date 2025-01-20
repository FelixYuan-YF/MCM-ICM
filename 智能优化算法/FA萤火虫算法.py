import numpy as np
import matplotlib.pyplot as plt

# 定义 Rastrigin 函数
def rastrigin(X):
    A = 10
    return A * len(X) + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in X])

# 计算萤火虫的亮度（适应度值）
def calculate_brightness(population):
    return np.array([rastrigin(ind) for ind in population])

# 更新萤火虫位置
def update_positions(population, brightness, alpha, beta_min, gamma, bounds):
    pop_size = population.shape[0]
    dim = population.shape[1]
    new_population = np.copy(population)
    for i in range(pop_size):
        for j in range(pop_size):
            if brightness[i] > brightness[j]:
                r = np.linalg.norm(population[i] - population[j])
                beta = beta_min * np.exp(-gamma * r**2)
                attraction = beta * (population[j] - population[i])
                randomization = alpha * (np.random.rand(dim) - 0.5)
                new_population[i] += attraction + randomization
                new_population[i] = np.clip(new_population[i], bounds[0], bounds[1])
    return new_population

# 参数设置
pop_size = 50       # 种群规模
dim = 2             # 维度
bounds = [-5.12, 5.12]  # 搜索空间边界
alpha = 0.5         # 随机移动参数
beta_min = 0.2      # 最小吸引度
gamma = 1.0         # 吸收系数
generations = 100   # 迭代次数

# 初始化种群
population = np.random.uniform(bounds[0], bounds[1], (pop_size, dim))

# 迭代优化
best_solution = None
best_fitness = float('inf')
for gen in range(generations):
    brightness = calculate_brightness(population)
    population = update_positions(population, brightness, alpha, beta_min, gamma, bounds)
    min_brightness = np.min(brightness)
    if min_brightness < best_fitness:
        best_fitness = min_brightness
        best_solution = population[np.argmin(brightness)]
    print(f"Generation {gen+1}: Best Fitness = {best_fitness}")

print(f"Optimal Solution: {best_solution}")
print(f"Optimal Fitness: {best_fitness}")

# 可视化结果
x = np.linspace(bounds[0], bounds[1], 400)
y = np.linspace(bounds[0], bounds[1], 400)
X, Y = np.meshgrid(x, y)
Z = np.array([rastrigin([x, y]) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = Z.reshape(X.shape)

plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.scatter(population[:, 0], population[:, 1], color='red', marker='o')
plt.title('Firefly Algorithm Optimization')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()
