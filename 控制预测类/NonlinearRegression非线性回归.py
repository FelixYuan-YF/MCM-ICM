import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义非线性函数，例如指数衰减函数
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# 生成示例数据
x_data = np.linspace(0, 4, 50)
y_data = func(x_data, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=len(x_data))

# 使用curve_fit进行非线性回归
popt, pcov = curve_fit(func, x_data, y_data)

# 输出拟合参数
print(f'拟合参数：a={popt[0]}, b={popt[1]}, c={popt[2]}')

# 绘制数据和拟合曲线
plt.scatter(x_data, y_data, label='数据点')
plt.plot(x_data, func(x_data, *popt), 'r-', label='拟合曲线')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
