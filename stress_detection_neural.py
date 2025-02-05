# -*- coding: utf-8 -*-
"""stress_detection_neural.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jKuM7xUGYpiaFw9u68Se_v5Vn3N0Q590
"""



from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_curve, roc_auc_score, precision_recall_curve, auc, f1_score, precision_score, recall_score, ConfusionMatrixDisplay

df = pd.read_csv('/content/drive/MyDrive/stress_detection.csv')

X = df.drop(['participant_id'], axis=1)

X['PSS_score'] = pd.to_numeric(X['PSS_score'], errors='coerce')

# Create a new column to store the stress categories
X['stress_category'] = ''

for row in range(0, len(X['PSS_score'])):
    if X['PSS_score'].iloc[row] < 13:
        X['stress_category'].iloc[row] = 'low_stress'
    elif X['PSS_score'].iloc[row] >= 14 and X['PSS_score'].iloc[row] < 26:
        X['stress_category'].iloc[row] = 'medium_stress'
    else:
        X['stress_category'].iloc[row] = 'high_stress'

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from tensorflow.keras.utils import to_categorical

y= X['stress_category']
X = X.drop(['PSS_score','stress_category'],axis=1)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

y = to_categorical(y, 3)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 919, stratify=y)

nn_model = Sequential()
nn_model.add(Dense(256, activation='relu', input_dim=X_train.shape[1]))
nn_model.add(Dense(180, activation='relu'))
nn_model.add(Dense(128, activation='relu'))
nn_model.add(Dense(64, activation='relu'))
nn_model.add(Dense(32, activation='relu'))
nn_model.add(Dense(3, activation='softmax'))
nn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
nn_model.summary()

nn_model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

y_pred=nn_model.predict(X_test)

y_pred_cm = np.argmax(y_pred, axis=1)

cm = confusion_matrix(np.argmax(y_test, axis=1), y_pred_cm)


print(cm)

auc = roc_auc_score(y_test, y_pred)
print(auc)