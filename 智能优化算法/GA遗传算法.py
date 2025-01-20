import numpy as np
import matplotlib.pyplot as plt

# 定义目标函数
def objective_function(x):
    return 10 * np.sin(5 * x) + 7 * np.cos(4 * x)

# 遗传算法参数
POP_SIZE = 100      # 种群大小
DNA_SIZE = 16       # DNA长度
CROSS_RATE = 0.8    # 交叉概率
MUTATION_RATE = 0.003  # 变异概率
GENERATIONS = 200   # 迭代次数
X_BOUND = [0, 10]   # x的范围

# 将DNA（二进制）转换为十进制数值
def translate_DNA(pop):
    # 将二进制DNA转换为十进制，并映射到X_BOUND范围内
    return pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2**DNA_SIZE - 1) * (X_BOUND[1] - X_BOUND[0]) + X_BOUND[0]

# 计算适应度
def get_fitness(pred):
    return pred + 1e-3 - np.min(pred)

# 选择
def select(pop, fitness):
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True, p=fitness/fitness.sum())
    return pop[idx]

# 交叉
def crossover(parent, pop):
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0, POP_SIZE, size=1)
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool_)
        parent[cross_points] = pop[i_, cross_points]
    return parent

# 变异
def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child

# 初始化种群
pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE))

# 记录每一代的最优值
best_values = []

# 开始进化
for _ in range(GENERATIONS):
    F_values = objective_function(translate_DNA(pop))
    fitness = get_fitness(F_values)
    best_values.append(np.max(F_values))
    pop = select(pop, fitness)
    pop_copy = pop.copy()
    for parent in pop:
        child = crossover(parent, pop_copy)
        child = mutate(child)
        parent[:] = child

# 输出结果
best_DNA = pop[np.argmax(fitness)]
best_x = translate_DNA(best_DNA)
print(f"最优的x值: {best_x}")
print(f"对应的最大函数值: {objective_function(best_x)}")

# 绘制结果
plt.plot(best_values)
plt.xlabel('Generation')
plt.ylabel('Max Fitness')
plt.title('Genetic Algorithm Optimization')
plt.show()
