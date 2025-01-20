from keras.models import Sequential
from keras.layers import SimpleRNN, Dense

model = Sequential()

# 添加RNN层，输入形状为（时间步长，特征维度）
model.add(SimpleRNN(units=50, input_shape=(timesteps, features)))

# 添加全连接层
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

# model.fit(x_train, y_train, epochs=100, batch_size=32)

# y_pred = model.predict(x_test)

# 评估模型

# score = model.evaluate(x_test, y_test, batch_size=32)

# print(score)