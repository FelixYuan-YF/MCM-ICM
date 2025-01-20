from keras.models import Sequential
from keras.layers import LSTM, Dense

model = Sequential()

# 添加LSTM层，输入形状为（时间步长，特征维度）
model.add(LSTM(units=50, input_shape=(timesteps, features)))

# 添加全连接层
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
# model.fit(x_train, y_train, epochs=100, batch_size=32)

# 预测
# y_pred = model.predict(x_test)

# 评估
# loss = model.evaluate(x_test, y_test)