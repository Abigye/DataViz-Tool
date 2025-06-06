import streamlit as st
import plotly.express as px

def visualise(df):
    st.subheader("📈 Data Visualization with Plotly")

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    all_cols = df.columns.tolist()

    chart_type = st.selectbox("Choose a chart type", [
        "Scatter", "Line", "Bar", "Histogram", "Pie", "Box Plot"
    ])

    if chart_type == "Scatter":
        x = st.selectbox("X-axis", numeric_cols)
        y = st.selectbox("Y-axis", numeric_cols, index=1)
        color = st.selectbox("Color (optional)", all_cols, index=0)
        fig = px.scatter(df, x=x, y=y, color=color)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Line":
        x = st.selectbox("X-axis", all_cols)
        y = st.multiselect("Y-axis (can be multiple)", numeric_cols)
        fig = px.line(df, x=x, y=y)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Bar":
        x = st.selectbox("X-axis", all_cols)
        y = st.selectbox("Y-axis", numeric_cols)
        fig = px.bar(df, x=x, y=y, color=x)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Histogram":
        col = st.selectbox("Column", numeric_cols)
        fig = px.histogram(df, x=col)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Pie":
        col = st.selectbox("Category Column", all_cols)
        values = st.selectbox("Values Column", numeric_cols)
        fig = px.pie(df, names=col, values=values)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Box Plot":
        y = st.selectbox("Y-axis", numeric_cols)
        x = st.selectbox("X-axis (categorical)", all_cols)
        fig = px.box(df, x=x, y=y, points="all")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Invalid chart type")