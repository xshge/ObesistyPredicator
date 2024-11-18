import streamlit as st
import pickle as pl
import numpy as np

with open('model2.pkl','rb') as f:
    model= pl.load(f)

sex_op = ['Female','Male']
exercise = ["None",'Sometimes','Moderate','Frequent']
tech = ["Barely","Moderate","Frequent"]
trans = ['Car','Bike','MotorBike','Public Transportation','Walking']
weights = ['Under Weight','Normal Weight','Obesity_Type_I','Obesity_Type_II','Obesity_Type_III','OverWeight_Level_I','OverWeight_Level_II']

st.header("Predict your obesity level")

with st.form("my_form"):
    Age = st.number_input("Age: ", min_value= 1,step= 1)
    Height = st.number_input("Height(m): ",  min_value= 0.1, step= 0.01)
    Weight = st.number_input("Weight(kg): ", min_value= 10, step= 1)
    Gender = st.radio("Gender: ", options= range(len(sex_op)), format_func= sex_op.__getitem__)
    History = st.checkbox("Family with a history of obesity?")
    Smoke = st.checkbox("Do you smoke?")
    CH = st.number_input("How much water do you drink per day? (liter): ", min_value = 1.0, max_value= 3.0, step= 0.01)
    FAF = st.selectbox("How often do you exercise?", options= range(len(exercise)), format_func= exercise.__getitem__, index = 0)
    TUE = st.selectbox("How often do you use your digital devices during your day?", options= range(len(tech)), format_func= tech.__getitem__, index = 0)
    Trans = st.selectbox("What is your main form of transportation?",options = range(len(trans)), format_func= trans.__getitem__,index= 0 )
    submit = st.form_submit_button('predict')   


if submit:
    result = np.array([[Gender,Age,Height,Weight,History,Smoke,CH,FAF,TUE,Trans]])
    pred = model.predict(result)
    
    st.subheader(weights[pred[0]])

