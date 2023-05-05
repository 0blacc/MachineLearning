# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:54:57 2023

@author: motlatso
"""
import numpy as np
import pickle
import streamlit as st 


loaded_model = pickle.load(open('C:/Users/motlatso/Desktop/ml/trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
   
    
    #change the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance 
    #reshape the np array as we are predicting for one instance 
    input_data_reshape=(input_data_as_numpy_array.reshape(1,-1))


    #stabdardise
    prediction = loaded_model.predict(input_data_reshape)
    #print(prediction)

    if (prediction[0] == 1 ):
      return('This person is a Diabetic case')
    else:
      return('this person is a Non diabetic ')
  
def main():
    #giving a title
    st.title('Diabetes Precition Web App')
    
    #get input data
    
    
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age')
    
    #code for prediction
    diagnosis =''
    
    #create button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)
    

if __name__ == '__main__' :
    main()
    