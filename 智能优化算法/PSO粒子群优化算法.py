import random

# 定义目标函数
def objective_function(x):
    return x**2 + 5

# 粒子类
class Particle:
    def __init__(self, x_min, x_max):
        self.position = random.uniform(x_min, x_max)  # 粒子的位置
        self.velocity = random.uniform(-1, 1)        # 粒子的速度
        self.best_position = self.position           # 粒子个体的最佳位置
        self.best_value = objective_function(self.position)  # 粒子个体的最佳适应值

    def update_velocity(self, global_best_position, inertia_weight, cognitive_coefficient, social_coefficient):
        r1 = random.random()
        r2 = random.random()
        cognitive_velocity = cognitive_coefficient * r1 * (self.best_position - self.position)
        social_velocity = social_coefficient * r2 * (global_best_position - self.position)
        self.velocity = inertia_weight * self.velocity + cognitive_velocity + social_velocity

    def update_position(self, x_min, x_max):
        self.position += self.velocity
        # 边界检查
        if self.position < x_min:
            self.position = x_min
        elif self.position > x_max:
            self.position = x_max

# 粒子群优化算法
def particle_swarm_optimization(objective_function, x_min, x_max, num_particles, num_iterations):
    # 初始化粒子群
    particles = [Particle(x_min, x_max) for _ in range(num_particles)]
    # 初始化全局最佳位置
    global_best_position = min(particles, key=lambda p: p.best_value).position
    global_best_value = objective_function(global_best_position)

    # PSO参数
    inertia_weight = 0.5
    cognitive_coefficient = 1.5
    social_coefficient = 1.5

    # 迭代优化
    for _ in range(num_iterations):
        for particle in particles:
            # 更新速度和位置
            particle.update_velocity(global_best_position, inertia_weight, cognitive_coefficient, social_coefficient)
            particle.update_position(x_min, x_max)

            # 计算适应值
            current_value = objective_function(particle.position)

            # 更新个体最佳位置
            if current_value < particle.best_value:
                particle.best_value = current_value
                particle.best_position = particle.position

            # 更新全局最佳位置
            if current_value < global_best_value:
                global_best_value = current_value
                global_best_position = particle.position

    return global_best_position, global_best_value

# 参数设置
x_min = -10
x_max = 10
num_particles = 30
num_iterations = 100

# 运行粒子群优化算法
best_position, best_value = particle_swarm_optimization(objective_function, x_min, x_max, num_particles, num_iterations)

# 输出结果
print(f"最优解：x = {best_position}")
print(f"最优解对应的目标函数值：f(x) = {best_value}")
