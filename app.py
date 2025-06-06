import streamlit as st

from src.load_data import load_data
from src.clean_data import clean_data
from src.visualise import visualise
# from src.insights import generate_insights

st.set_page_config(page_title="Data Explorer", layout="wide")

st.title("🧪 Data Viz Tool")

file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=False)

if file:
    data_raw = load_data(file)

    if "cleaned_df" not in st.session_state:
        st.session_state.cleaned_df = data_raw.copy()

    st.subheader("Raw Data")
    st.dataframe(data_raw)

    option = st.radio("Choose what you want to do:", ["🧹 Clean Data", "📈 Visualize Data", "🔍 Generate Insights"], horizontal=True)

    if option == "🧹 Clean Data":
        cleaned_data = clean_data(data_raw.copy())
        st.session_state.cleaned_df = cleaned_data 

        csv = cleaned_data.to_csv(index=False).encode('utf-8')
        st.download_button("Download Cleaned Data as CSV", data=csv, file_name="cleaned_data.csv", mime="text/csv")

    elif option == "📈 Visualize Data":
        st.subheader("📊 Visualization")

        data_source = st.radio("Choose data source", ["Raw Data", "Cleaned Data"], horizontal=True)

        data_to_use = data_raw if data_source == "Raw Data" else st.session_state.cleaned_df

        visualise(data_to_use)

else:
    st.info("Upload a CSV or Excel file to begin.")
