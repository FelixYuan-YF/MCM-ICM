import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 示例数据：自变量X1, X2和因变量Y
data = {
    'X1': [1, 2, 3, 4, 5],
    'X2': [2, 4, 6, 8, 10],
    'Y': [3, 5, 7, 9, 11]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 定义自变量和因变量
X = df[['X1', 'X2']]
y = df['Y']

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X, y)

# 输出模型参数
print(f'截距（β0）：{model.intercept_}')
print(f'回归系数（β1, β2）：{model.coef_}')