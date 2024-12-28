import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st

sonar_data = pd.read_csv('sonar_data.csv', header=None)

X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

model = LogisticRegression()
model.fit(X_train, Y_train)
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on tranining data:',training_data_accuracy)  
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on testing data :',test_data_accuracy)

st.title("* Sonar Rock VS Mine Prediction *")
input_data = st.text_input('Enter here')

if st.button('predict'):
    input_data_np_array = np.asarray(input_data.split(','), dtype=float)
    reshaped_input_data = input_data_np_array.reshape(1, -1)

    prediction_probability = model.predict_proba(reshaped_input_data)[:, 1]
    st.write(f'Predicted Probability of being a Mine: {prediction_probability[0]:.2f}')

    prediction = model.predict(reshaped_input_data)
    if prediction[0] == 'R':
        st.write('THIS IS ROCK')
    else:
        st.write('THIS IS MINE')
