import streamlit as st

st.title("Welcome to BMI Calculation")
weight=st.number_input("Enter your weight in kgs")
sts=st.radio('Enter your height format:',('cms','metres','feet'))
if(sts=='cms'):
    height=st.number_input('centimeters')
    try:
        bmi=weight/((height/100)**2)
    except:
        st.text("enter some value")
elif(sts=='meters'):
    height=st.number_input('meters')
    try:
        bmi=weight/((height)**2)
    except:
        st.text("enter some value")
else:
    height=st.number_input('feet')
    try:
        bmi=weight/((height/3.28)**2)
    except:
        st.text("enter some value")
if(st.button("Generate")):
    st.text("your bmi is {}.".format(bmi))
    if (bmi<16):
        st.error("extremely underweight")
    elif (bmi>16 and bmi<18.5):
        st.warning("under weight")
    elif (bmi>18.5 and bmi<25):
        st.success("normal")
    elif (bmi>25 and bmi<30):
        st.warning("overweight")
    elif(bmi>=30):
        st.error("extremely overweight")
        



                
