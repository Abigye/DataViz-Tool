import streamlit as st

def clean_data(df):
    st.subheader("Data Cleaning")
    
    # Drop missing values
    if st.button("Drop Rows with Missing Values"):
        df.dropna(inplace=True)
        st.success("Missing rows removed.")
        st.dataframe(df)

    # Drop selected columns
    drop_cols = st.multiselect("Select columns to drop", df.columns)
    if st.button("Drop Selected Columns"):
        df.drop(columns=drop_cols, inplace=True)
        st.success(f"Dropped: {', '.join(drop_cols)}")
        st.dataframe(df)
    return df
