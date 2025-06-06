import streamlit as st

from src.load_data import load_data
from src.clean_data import clean_data
from src.visualise import visualise
# from src.insights import generate_insights


st.title("Data Viz Tool")

file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=False)

if file:
    st.subheader("Raw Data")
    data = load_data(file)
    st.write(data)

    tab = st.radio("Choose what you want to do:", ["🧹 Clean Data", "📈 Visualize Data"])

    if tab == "🧹 Clean Data":
        clean_data(data)
    elif tab == "📈 Visualize Data":
        visualise(data)

    # st.subheader("Cleaned Data")
    # cleaned_data = clean_data(data)
    # st.write(cleaned_data)

    # if st.checkbox("Show raw data"):
    #     st.write(data)

    # if st.checkbox("Show cleaned data"):
    #     st.write(cleaned_data)

    # if st.checkbox("Generate insights"):
    #     insights = generate_insights(cleaned_data)
    #     st.write(insights)

    # if st.checkbox("Visualize data"):
    #     visualize(cleaned_data)

    # if st.checkbox("Save cleaned data"):
    #     save_data(cleaned_data)§

    # if st.checkbox("Save visualization"):
    #     save_visualization(visualization)