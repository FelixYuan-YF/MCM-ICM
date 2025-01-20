import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 生成示例时间序列数据
np.random.seed(0)
dates = pd.date_range(start='2020-01-01', periods=100, freq='D')
data = np.cumsum(np.random.randn(100))  # 随机游走数据
ts = pd.Series(data, index=dates)

# 拟合ARIMA模型
model = ARIMA(ts, order=(1, 1, 1))  # ARIMA(p=1, d=1, q=1)
fitted_model = model.fit()

# 进行预测
forecast_steps = 10
forecast = fitted_model.forecast(steps=forecast_steps)

# 可视化结果
plt.figure(figsize=(10, 6))
plt.plot(ts, label='历史数据')
plt.plot(forecast.index, forecast, label='预测数据', color='red')
plt.xlabel('日期')
plt.ylabel('值')
plt.title('ARIMA模型预测')
plt.legend()
plt.show()
