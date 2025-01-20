import numpy as np

# 定义评价指标集
factors = ['价格', '质量', '服务']

# 定义评价等级集
grades = ['差', '一般', '好', '很好', '优秀']

# 定义各指标的权重（假设已确定）
weights = np.array([0.3, 0.5, 0.2])

# 构建隶属度矩阵（根据专家打分或调查问卷结果）
# 行对应指标，列对应评价等级
# 例如，价格指标对各评价等级的隶属度为 [0.1, 0.2, 0.4, 0.2, 0.1]
membership_matrix = np.array([
    [0.1, 0.2, 0.4, 0.2, 0.1],  # 价格
    [0.0, 0.1, 0.3, 0.4, 0.2],  # 质量
    [0.2, 0.3, 0.3, 0.1, 0.1]   # 服务
])

# 进行模糊综合评价
# 计算加权隶属度矩阵
weighted_matrix = weights[:, np.newaxis] * membership_matrix

# 求各评价等级的综合隶属度
result = weighted_matrix.sum(axis=0)

# 输出结果
print("各评价等级的综合隶属度：")
for grade, value in zip(grades, result):
    print(f"{grade}: {value:.2f}")

# 确定最终评价结果（选择隶属度最大的评价等级）
final_grade = grades[np.argmax(result)]
print(f"\n最终评价结果：{final_grade}")