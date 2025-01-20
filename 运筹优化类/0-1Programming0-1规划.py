import pulp

# 定义问题，设置为最大化问题
problem = pulp.LpProblem("0-1_Programming_Example", pulp.LpMaximize)

# 定义决策变量，并设置为0-1变量
x1 = pulp.LpVariable('x1', cat='Binary')
x2 = pulp.LpVariable('x2', cat='Binary')

# 定义目标函数
problem += 2 * x1 + 3 * x2, "Objective_Function"

# 添加约束条件
problem += x1 + 2 * x2 <= 4, "Constraint_1"
problem += 4 * x1 + 2 * x2 <= 12, "Constraint_2"

# 求解问题
problem.solve()

# 输出结果
print(f"状态: {pulp.LpStatus[problem.status]}")
print(f"x1 的最优值: {pulp.value(x1)}")
print(f"x2 的最优值: {pulp.value(x2)}")
print(f"最大化目标函数值: {pulp.value(problem.objective)}")
