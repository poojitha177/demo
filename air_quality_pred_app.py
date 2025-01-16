import streamlit as st
import joblib
import numpy as np

#load the model
model = joblib.load(r"C:\Users\338561\Desktop\streamlit\model1.pkl")


# st.markdown(
#     """<style>
#     body {
#         background-color: #f5f5f5;        
#     }
#     .main {
#         background: white;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0px 0px 10px rgba(0, 0, 0, 0, 1);
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

#title of the app
st.title("Air Quality Prediction App")
st.markdown(
    """
    This application predicts the **Air Quality** based on the input environmental features like **temperature, NO2,
    SO2, CO** and **proximity to industrial areas**. Enter the values in the  sidebar and click **Predict** to see 
    the results.
    """
)

#create the input fields for user data
with st.form("Input Form"):
    st.header("Enter the Input features")
    temperature = st.number_input("Temperature", min_value=-50.0, max_value=50.0, step=0.1)
    no2 = st.number_input("NO2", min_value=0.0, max_value=500.0, step=0.1)
    so2 = st.number_input("SO2", min_value=0.0, max_value=500.0, step=0.1)
    co = st.number_input("CO", min_value=0.0, max_value=50.0, step=0.1)
    proximity = st.number_input("Proximity to Industrial Areas", min_value=0.0, max_value=100.0, step=0.1)
    
    submitted = st.form_submit_button("Predict")

#make predictions when user clicks a button
if submitted:
    input_data = np.array([[temperature, no2, so2, co, proximity]])
    prediction = model.predict(input_data)[0]
    
    # st.markdown(f"Predicted Air Quality Index: **{prediction}**")
    # if prediction[0] == 1:
    #     st.success("The air quality is **Good**.")
    # else:
    #     st.warning("The air quality is **Bad**.")

    output = "Poor" if prediction == 1 else "Good"

    st.subheader("Prediction Result")
    st.write(f"The Air Qaulity Prediction is: **{output}**")
    
    