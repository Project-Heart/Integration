import streamlit as st
import base64
import sklearn
import numpy as np
import pickle as pkl
from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler()
#Load the saved model
model=pkl.load(open("final_model.p","rb"))

st.set_page_config(page_title="Healthy Heart App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")

def preprocess(age,ejection,serum,time ):   
 
    
    # Pre-processing user input   
    a=float(age)
    e=float(ejection)
    s=float(serum)
    t=float(time)
    a1=(a-mean[0])/std[0]
    e1=(e-mean[4])/std[4]
    s1=(s-mean[7])/std[7]
    t1=(t-mean[11])/std[11]
    user_input=[a1,e1,s1,t1]
    user_input=np.array(user_input)
    user_input=[user_input]
    prediction=model.predict(user_input)
    return prediction
    
    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Healthy Heart App</h1> 
    </div> 
    """
      
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by Team-5 ')
      
# following lines create boxes in which user can enter data required to make prediction
age=st.selectbox ("Enter Age",range(1,96,40))
ejection = st.radio("Enter Ejection Fraction: ", range(1,81,14))
serum = st.number_input('Enter serum_creatinine')
time=st.selectbox('Enter follow up time ',range(1,286,4))




#user_input=preprocess(sex,cp,exang, fbs, slope, thal )
pred=preprocess(age,ejection,serum,time)




if st.button("Predict"):    
  if pred[0] == 0:
    st.error('Warning! You have high risk of getting a heart attack!')
    
  else:
    st.success('You have lower risk of getting a heart disease!')
    
   



st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether you are at a risk of developing a heart disease.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have a healthy heart")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)

if feedback:
  st.header("Thank you for rating the app!")
  st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 
