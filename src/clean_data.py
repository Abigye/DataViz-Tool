import streamlit as st

def clean_data(df):
    st.subheader("🧹 Data Cleaning")
    tab1, tab2, tab3 = st.tabs(["Drop Missing Rows", "Drop Columns", "Fill Missing Values"])

    cleaned_df = df.copy()

    with tab1:
        drop_missing = st.checkbox("Drop rows with any missing values")

    with tab2:
        cols_to_drop = st.multiselect("Select columns to drop", df.columns)

    with tab3:
        fill_col = st.selectbox("Select column to fill missing values", df.columns)
        fill_value = st.text_input("Fill missing values with (e.g., 0 or 'Unknown')")

    # Apply cleaning only when button clicked
    if st.button("Apply Cleaning"):
        if drop_missing:
            cleaned_df = cleaned_df.dropna()
        if cols_to_drop:
            cleaned_df = cleaned_df.drop(columns=cols_to_drop)
        if fill_value:
            # Try to infer type (int, float) if possible
            try:
                val = float(fill_value)
                if val.is_integer():
                    val = int(val)
            except:
                val = fill_value  
            cleaned_df[fill_col] = cleaned_df[fill_col].fillna(val)

        st.success("Data cleaned successfully!")
        st.dataframe(cleaned_df)
        return cleaned_df

    else:
        st.info("Select cleaning options and click 'Apply Cleaning' to see changes.")
        st.dataframe(df)
        return df
