import numpy as np

def objective_function(x):
    # 定义目标函数，这里以简单的二次函数为例
    return x[0]**2 + x[1]**2

def beetle_antennae_search(obj_func, dim, max_iter=100, step_size=0.1, sensing_length=0.01):
    # 初始化天牛的位置
    beetle_position = np.random.uniform(-10, 10, dim)
    # 初始化历史最优位置
    best_position = beetle_position.copy()
    best_value = obj_func(beetle_position)

    for _ in range(max_iter):
        # 生成随机方向向量，并进行单位化
        direction = np.random.randn(dim)
        direction /= np.linalg.norm(direction)

        # 计算左右触角的位置
        left_antenna = beetle_position + sensing_length * direction
        right_antenna = beetle_position - sensing_length * direction

        # 评估左右触角的目标函数值
        left_value = obj_func(left_antenna)
        right_value = obj_func(right_antenna)

        # 根据目标函数值调整天牛的位置
        if left_value < right_value:
            beetle_position += step_size * direction
        else:
            beetle_position -= step_size * direction

        # 更新历史最优位置
        current_value = obj_func(beetle_position)
        if current_value < best_value:
            best_value = current_value
            best_position = beetle_position.copy()

        # 动态调整步长和感知长度
        step_size *= 0.99
        sensing_length *= 0.99

    return best_position, best_value

# 参数设置
dimension = 2  # 问题的维度
iterations = 1000  # 最大迭代次数
initial_step_size = 0.1  # 初始步长
initial_sensing_length = 0.01  # 初始感知长度

# 执行天牛须搜索算法
optimal_position, optimal_value = beetle_antennae_search(
    objective_function,
    dimension,
    max_iter=iterations,
    step_size=initial_step_size,
    sensing_length=initial_sensing_length
)

print(f"最优位置: {optimal_position}")
print(f"最优值: {optimal_value}")
