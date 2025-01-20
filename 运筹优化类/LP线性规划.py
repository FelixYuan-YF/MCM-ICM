from scipy.optimize import linprog

# 定义目标函数的系数（注意：linprog默认求解最小化问题）
c = [-3, -5]  # 由于要最大化3x1 + 5x2，这里取相反数进行最小化

# 定义不等式约束条件的系数
A = [
    [2, 1],   # 2x1 + x2 <= 100
    [1, 2]    # x1 + 2x2 <= 80
]

# 定义不等式约束条件的右端常数
b = [100, 80]

# 定义变量的取值范围
x_bounds = (0, None)  # x1 >= 0
y_bounds = (0, None)  # x2 >= 0

# 求解线性规划问题
# 不等式约束
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
# 等式约束
# result = linprog(c, A_eq=A, b_eq=b, bounds=[x_bounds, y_bounds], method='highs')

# 输出结果
if result.success:
    print(f"最优解：x1 = {result.x[0]:.2f}, x2 = {result.x[1]:.2f}")
    print(f"最大利润：{-result.fun:.2f}")
else:
    print("线性规划问题无解")
