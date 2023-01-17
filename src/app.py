import streamlit as st
import pandas as pd
import pickle
import numpy as np

loaded_model = pickle.load(open('modelo_diabetes.sav', 'rb'))




def diabetes_prediction(input_data):
    

    
    input_data_as_numpy_array = np.asarray(input_data)

    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'La persona es diabetica'
    else:
      return 'No es diabetica'
  
    
  
def main():
    
    
    
    st.title('Prediccion de diabetes')
    
    
    
    
    
    Pregnancies = st.text_input('embarazos')
    Glucose = st.text_input('nivel de glucosa')
    BloodPressure = st.text_input('presion sanguinea')
    SkinThickness = st.text_input('grosor de piel')
    Insulin = st.text_input('nivel de insulina')
    BMI = st.text_input('indice de masa corporal')
    DiabetesPedigreeFunction = st.text_input('nivel de diabetes')
    Age = st.text_input('Edad')
    
    
    
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()




