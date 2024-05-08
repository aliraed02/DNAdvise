import json
from gene import generation_chain
import streamlit as st



def main():


    st.set_page_config(page_title="DNAdvise", page_icon= "🧬", layout="wide")
    st.title("DNAdvise - Personalized Health Advice")
    over_view ="""
    Welcome to DNAdvise! DNAdvise is a revolutionary concept merging genetic data and AI to offer personalized health advice.
    By analyzing saliva samples, it provides insights into disease risks and generates customized lifestyle
    recommendations for proactive well-being.
    """
    st.write(f"<div style='font-family: Times New Roman; font-size: 20px;'>{over_view}</div>", unsafe_allow_html=True)





    with open(r'D:\Python\Gen AI\DNAdvise\response.json', 'r') as file:
        RESPONSE_JSON = json.load(file)
    st.sidebar.title("Menu")
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=30)
    gender = st.sidebar.radio("Gender", ["Male", "Female"], key="gender_radio")
    height = st.sidebar.number_input("Height (cm)", min_value=0, value=170)
    weight = st.sidebar.number_input("Weight (kg)", min_value=0, value=70)
    exercise_routine = st.sidebar.selectbox("Exercise Routine", ["Sedentary", "Light", "Moderate", "Active", "Very Active"], key="exercise_select")
    sleep_hours = st.sidebar.number_input("Sleep Hours", min_value=0, max_value=24, value=8)
    stress_level = st.sidebar.radio("Stress Level", ["Low", "Medium", "High"], key="stress_radio")
    smoking_status = st.sidebar.radio("Smoking Status", ["Yes", "No"], key="smoking_radio")
    alcohol_consumption = st.sidebar.radio("Alcohol Consumption", ["Yes", "No"], key="alcohol_radio")
    type_2_diabetes = st.sidebar.text_input("Type 2 Diabetes", "")
    coronary_heart_disease = st.sidebar.text_input("Coronary Heart Disease", "")
    obesity = st.sidebar.text_input("Obesity", "")
    hypertension = st.sidebar.text_input("Hypertension", "")
    colorectal_cancer = st.sidebar.text_input("Colorectal Cancer", "")
    alzhimers = st.sidebar.text_input("Alzheimer's", "")

    if(st.sidebar.button("Generate")):
        with st.spinner("Processing"):
            response = generation_chain({
                "age": age,
                "gender": gender,
                "height": height,
                "weight": weight,
                "exercise_routine": exercise_routine,
                "sleep_hours": sleep_hours,
                "stress_level": stress_level,
                "smoking_status": smoking_status,
                "alcohol_consumption": alcohol_consumption,
                "type_2_diabetes": type_2_diabetes,
                "coronary_heart_disease": coronary_heart_disease,
                "obesity": obesity,
                "hypertension": hypertension,
                "colorectal_cancer": colorectal_cancer,
                "alzhimers": alzhimers,
                "response_json": json.dumps(RESPONSE_JSON)
            })
            output = json.loads(json.dumps(response['response']))
            st.write(f"<div style='font-family: Times New Roman; font-size: 20px;'>{output}</div>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    st.sidebar.text("© 2024 DNAdvise")





if __name__ == '__main__':
    main()
