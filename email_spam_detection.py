import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
data=pd.read_csv(r"D:\Machine Learning\spam mail.csv")
print(data.head())
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(data['Masseges'])
data['category']=data['Category'].map({'spam':1,'ham':0})
print(data.head())
data.drop(['Category'],axis=1)
y=data[['category']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=SVC()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(model.score(x_test,y_test))

import streamlit as st
st.title("Email Spam Detector")
st.markdown("Please enter the email below to check if it is spam or ham:")
email=st.text_input("Enter your email")
if st.button("check"):
    if email:
        new_mail=vectorizer.transform([email])
        prediction=model.predict(new_mail)
        label_map={'spam':1,'ham':0}
        label=label_map[prediction[0]]
        st.write("The Email is",label)
    else:
        st.error("Please enter an email")
    
    

