import numpy as np
import pandas as pd

# 定义决策矩阵（行：方案，列：指标）
# 例如，有三个方案（A, B, C）和四个指标（成本、质量、耐用性、外观）
data = {
    '成本': [250, 200, 300],
    '质量': [7, 8, 6],
    '耐用性': [6, 7, 8],
    '外观': [8, 7, 9]
}
df = pd.DataFrame(data, index=['方案A', '方案B', '方案C'])

# 定义指标的权重（假设总和为1）
weights = np.array([0.4, 0.3, 0.2, 0.1])

# 定义每个指标的类型：1表示效益型（数值越大越好），-1表示成本型（数值越小越好）
criteria_types = np.array([-1, 1, 1, 1])

# 第一步：标准化决策矩阵
normalized_df = df / np.sqrt((df**2).sum())

# 第二步：考虑权重的标准化矩阵
weighted_normalized_df = normalized_df * weights

# 第三步：确定理想解和负理想解
ideal_solution = np.where(criteria_types == 1, weighted_normalized_df.max(), weighted_normalized_df.min())
negative_ideal_solution = np.where(criteria_types == 1, weighted_normalized_df.min(), weighted_normalized_df.max())

# 第四步：计算与理想解和负理想解的距离
distance_to_ideal = np.sqrt(((weighted_normalized_df - ideal_solution)**2).sum(axis=1))
distance_to_negative_ideal = np.sqrt(((weighted_normalized_df - negative_ideal_solution)**2).sum(axis=1))

# 第五步：计算相对接近度
relative_closeness = distance_to_negative_ideal / (distance_to_ideal + distance_to_negative_ideal)

# 输出结果
results = pd.DataFrame({
    '与理想解的距离': distance_to_ideal,
    '与负理想解的距离': distance_to_negative_ideal,
    '相对接近度': relative_closeness
}, index=df.index)

print(results)
print("\n最优方案是：", results['相对接近度'].idxmax())