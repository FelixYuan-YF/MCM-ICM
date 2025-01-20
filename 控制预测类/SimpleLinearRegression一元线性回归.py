import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 生成示例数据
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([2, 3, 5, 7, 11])

# 创建线性回归模型并拟合数据
model = LinearRegression()
model.fit(X, Y)

# 输出模型参数
print(f'截距（β0）：{model.intercept_}')
print(f'斜率（β1）：{model.coef_[0]}')

# 预测
Y_pred = model.predict(X)

# 可视化
plt.scatter(X, Y, color='blue', label='实际数据')
plt.plot(X, Y_pred, color='red', label='拟合直线')
plt.xlabel('自变量 X')
plt.ylabel('因变量 Y')
plt.legend()
plt.show()
