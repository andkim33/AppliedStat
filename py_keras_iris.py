"""
Before Python, you should run the following scripts in R .
(file : r_iris_save.txt)

data(iris)
names(iris) = c("SL","SW","PL","PW","SP")
levels(iris$SP) = c("st","vc","vg")
write.csv(iris, file=’c:/data/pydata/n_iris.csv’)

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# pip install tensorflow, 
# pip install keras

import tensorflow as tf
import keras
import pandas as pd
iris=pd.read_csv('c:/data/pydata/n_iris.csv')
iris["SP"] = iris["SP"].astype("category").cat.codes
X=iris.iloc[:,1:-1]
y=iris["SP"]
Y = tf.keras.utils.to_categorical(y, num_classes=3)

# train test split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)
X_train.shape

# Scale data to have mean 0 and variance 1 in X_train
# Modified Standardization  
zX_train = ZScaler(X_train)

from keras.models import Sequential
from keras.layers import Dense
model_1 = Sequential()
model_1.add(Dense(8, input_dim=4, activation='relu'))
model_1.add(Dense(3, activation='softmax'))
model_1.compile(loss='categorical_crossentropy', 
                      optimizer='adam', 
                      metrics=['accuracy'])
model_1.summary()
model_1.fit(zX_train, Y_train, batch_size=5, epochs=50)
_, accuracy = model_1.evaluate(zX_train, Y_train)
print('Accuracy: %.2f' % (accuracy*100))
Accuracy: 96.19

zX_test = ZScaler_test(X_train, X_test)
_, accuracy = model_1.evaluate(zX_test, Y_test)
2/2 [==============================] - 0s 3ms/step - loss: 0.2056 - accuracy: 0.9333
print('Accuracy: %.2f' % (accuracy*100))
Accuracy: 93.33

prediction = model_1.predict(zX_test)
prediction_ = np.argmax(prediction, axis = 1)
Y_test_target = np.argmax(Y_test, axis=1)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(Y_test_target, prediction_))
[[13  0  0]
 [ 0 13  0]
 [ 0  3 16]]
print(classification_report(Y_test_target, prediction_))
              precision    recall  f1-score   support
           0       1.00      1.00      1.00        13
           1       0.81      1.00      0.90        13
           2       1.00      0.84      0.91        19
    accuracy                           0.93        45
   macro avg       0.94      0.95      0.94        45
weighted avg       0.95      0.93      0.93        45
