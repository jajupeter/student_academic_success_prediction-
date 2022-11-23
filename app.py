import streamlit as st
import pandas as pd
from sklearn import datasets
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier



#"""House price Prediction App"""
st.write("""
    # :school: Student Success Prediction App
    *This app predicts STEM student Academic success*
    """)
    
html_temp = """
    <div style = "background - color: #f0f0f5; padding: 5px">
    <h3 style="color:#666666;text-align:left; line-height: 1.5">
    <p> <b> Choose input parameters by clicking the arrow on the Top left Corner. </b><br/ >
    This Web App will predict student academic success based on performing below or above average  
     once the following (15) parameters are inputed.<br> 
    This is based on Ensemble model - Random Forest Classifier 
    with data from UCI Machine Learning Repository http://archive.ics.uci.edu/ml/datasets/Student+Performance#.</p></h3>
    </div>
    
    """
st.markdown(html_temp, unsafe_allow_html=True)

st.sidebar.header('User Input Parameters') 

def user_input_parameters(): 
    age =  st.sidebar.slider("1. Student's age (from 15 to 22)", 15, 22, 17)        
    father_education = st.sidebar.slider("2. Father's education? (0 - none, 1= 4th grade, 2= 5th to 9th grade, 3 = secondary educatiion 4 = higher education)", 0,5,3)
    mother_education = st.sidebar.slider("3. Mother's education? (0 - none, 1= 4th grade, 2= 5th to 9th grade, 3 = secondary educatiion 4 = higher education)", 0,5,3)
    commute_time = st.sidebar.slider("4. Home to school travel time? (1 = <15 min, 2 = 15 to 30 min, 3 = 30 min to 1 hour,  4 = >1 hour)", 0, 4, 2)
    study_time = st.sidebar.slider("5. Weekly study time? (1 = <2 hours, 2 = 2 to 5 hours, 3 = 5 to 10 hours,  4 = >10 hours) ",0, 4,2 )
    failures = st.sidebar.slider("6. Number of past class failures?", 0, 4, 2)
    paid_classes= st.sidebar.selectbox('7. Extra paid classes within the course subject?',('yes', 'no'))
    family_quality = st.sidebar.slider("8. Quality of family relationships (from 1 - very bad to 5 - excellent)", 0, 5, 3)
    romantic = st.sidebar.selectbox('9. With a romantic relationship?',('yes', 'no'))
    free_time = st.sidebar.slider("10. Free time after school? (From 1 - very low to 5 - very high)", 0, 5, 3)
    go_out = st.sidebar.slider("11. Going out with friends? (From 1 - very low to 5 - very high)", 0,5,3)
    weekday_alcohol_usage = st.sidebar.slider("12. Weekday alcohol consumption? (From 1 - very low to 5 - very high)", 0, 5, 2)
    weekend_alcohol_usage = st.sidebar.slider("13. Weekend alcohol consumption? (From 1 - very low to 5 - very high)", 0, 5, 2)    
    health = st.sidebar.slider("14. current health status? (From 1 - very bad to 5 - very good) ",0, 5, 3) 
    absences = st.sidebar.slider("15. Number of school absences? ", 0, 100, 4) 
    
    
    
    features = { 'age' : age,
                'mother_education' : mother_education,
                'father_education' : father_education,
                'commute_time' : commute_time,
                'study_time' : study_time,
                'failures': failures,
                'paid_classes' : paid_classes,
                'romantic' : romantic,
                'family_quality' :family_quality,
                'free_time' : free_time,
                'go_out' : go_out,
                'weekday_alcohol_usage': weekday_alcohol_usage,
                'weekend_alcohol_usage' :  weekend_alcohol_usage, 
                'health'  : health,
                'absences' : absences,}
    
      

    
    feat = pd.DataFrame(features, index=[0])
    
    return feat
df = user_input_parameters()
df1 = np.array(df)




st.subheader('User Input parameters')
st.write(df)


# Combines user input features with entire student_input dataset
# This will be useful for the encoding phase
student = pd.read_csv('Student_input.csv')
student_drop = student.drop(columns=['grades'])
data = pd.concat([df,student_drop],axis=0)

# Encoding of ordinal features
encode = ['paid_classes','romantic']
for col in encode:
    dummy = pd.get_dummies(data[col], prefix=col)
    data = pd.concat([data,dummy], axis=1)
    del data[col]
data = data[:1] # Selects only the first row (the user input data)

# Displays the user input features
st.subheader('User Input features')
st.write(data)

# Reads in saved classification model
load_clf = pickle.load(open('Random_Forestmodel.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(data)
prediction_proba = load_clf.predict_proba(data)


st.subheader('Predict Sudent grade ')
student_grade = np.array([' Not-Successful',  ' Successful '])
st.write(student_grade[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)

