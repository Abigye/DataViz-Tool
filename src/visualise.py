import streamlit as st
import plotly.express as px

def visualise(df):
    if df.empty:
        st.warning("Selected dataset is empty. Please check your data cleaning settings.")
        return

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    datetime_cols = df.select_dtypes(include='datetime').columns.tolist()
    all_cols = df.columns.tolist()

    chart_type = st.selectbox("Choose a chart type", [
        "Scatter", "Line", "Bar", "Histogram", "Pie", "Box Plot"
    ])

    if chart_type == "Scatter":
        x = st.selectbox("X-axis", numeric_cols)
        y = st.selectbox("Y-axis", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
        color = st.selectbox("Color by (optional)", [None] + categorical_cols)
        fig = px.scatter(df, x=x, y=y, color=color if color else None)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Line":
        x = st.selectbox("X-axis", datetime_cols + categorical_cols)
        y = st.multiselect("Y-axis (can be multiple)", numeric_cols)
        if y:
            fig = px.line(df, x=x, y=y)
            st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Bar":
        x = st.selectbox("X-axis (category)", categorical_cols + datetime_cols)
        y = st.selectbox("Y-axis (numeric)", numeric_cols)
        color = st.selectbox("Color by (optional)", [None] + categorical_cols)
        fig = px.bar(df, x=x, y=y, color=color if color else None)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Histogram":
        x = st.selectbox("Numeric column to plot", numeric_cols)
        group_by = st.selectbox("Group by (optional)", [None] + categorical_cols)
        fig = px.histogram(df, x=x, color=group_by if group_by else None, barmode="overlay")
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Pie":
        names = st.selectbox("Category Column", categorical_cols)
        values = st.selectbox("Values Column", numeric_cols)
        fig = px.pie(df, names=names, values=values)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Box Plot":
        y = st.selectbox("Y-axis (numeric)", numeric_cols)
        x = st.selectbox("X-axis (categorical)", categorical_cols + datetime_cols)
        fig = px.box(df, x=x, y=y, points="all")
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.error("Invalid chart type")

    format_option = st.selectbox("Select download format", ["png", "jpeg", "svg", "pdf"])

    img_bytes = fig.to_image(format=format_option)

    mime_types = {
        "png": "image/png",
        "jpeg": "image/jpeg",
        "svg": "image/svg+xml",
        "pdf": "application/pdf",
    }

    file_name = f"visualization.{format_option}"

    st.download_button(
        label=f"Download Visualization as {format_option.upper()}",
        data=img_bytes,
        file_name=file_name,
        mime=mime_types[format_option],
    )