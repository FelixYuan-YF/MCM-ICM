from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential()

# 卷积层1
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
# 池化层1
model.add(MaxPooling2D(pool_size=(2, 2)))

# 卷积层2
model.add(Conv2D(64, (3, 3), activation='relu'))
# 池化层2
model.add(MaxPooling2D(pool_size=(2, 2)))

# 展平层
model.add(Flatten())

# 全连接层
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))  # 假设有10个类别

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

# 训练模型

# model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_test, y_test))

# 评估模型

# loss, accuracy = model.evaluate(x_test, y_test)

# 预测

# y_predict = model.predict(x_test)