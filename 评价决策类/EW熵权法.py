import numpy as np
import pandas as pd

# 示例数据：行表示评价对象，列表示指标
data = {
    '指标1': [0.5, 0.7, 0.6],
    '指标2': [0.2, 0.3, 0.4],
    '指标3': [0.4, 0.1, 0.5]
}
df = pd.DataFrame(data)

# 步骤1：数据标准化（归一化处理）
df_normalized = df.apply(lambda x: (x - x.min()) / (x.max() - x.min()))

# 步骤2：计算各指标的比重
P = df_normalized.div(df_normalized.sum(axis=0), axis=1)

# 步骤3：计算信息熵
epsilon = 1e-10  # 防止log(0)的情况
E = - (P * np.log(P + epsilon)).sum(axis=0) / np.log(len(df))

# 步骤4：计算差异系数
g = 1 - E

# 步骤5：计算各指标的权重
weights = g / g.sum()

print("各指标的权重：")
print(weights)