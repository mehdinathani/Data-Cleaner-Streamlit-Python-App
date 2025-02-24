# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up the app
st.set_page_config(page_title="Data Analysis", page_icon=":bar_chart:", layout="wide")
st.title("Data Analysis")
st.write("Transform your files from CSV and Excel format with built-in data cleaning and visualization.")

# File Upload
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", accept_multiple_files=True, type=['csv', 'xlsx', 'xls'])

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        file_key = f"df_{file.name}"

        # Read File
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext in [".xlsx", ".xls"]:
                df = pd.read_excel(file, engine="openpyxl")
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error loading {file.name}: {e}")
            continue
        
        # Store in session state
        if file_key not in st.session_state:
            st.session_state[file_key] = df
        df = st.session_state[file_key]

        # File Information
        st.subheader(f"File Information: {file.name}")
        st.write(f"- **File Type:** {file_ext}")
        st.write(f"- **Number of Rows:** {df.shape[0]}")
        st.write(f"- **Number of Columns:** {df.shape[1]}")
        st.write(f"- **Data Types:**")
        st.write(df.dtypes)
        st.write(f"- **Missing Values:**")
        st.write(df.isnull().sum())
        st.write(f"- **Duplicate Rows:** {df.duplicated().sum()}")
        st.write(f"- **Unique Values per Column:**")
        st.write(df.nunique())
        st.write(f"- **Summary Statistics:**")
        st.write(df.describe())
        st.write(f"- **File Size:** {file.getbuffer().nbytes / 1024:.2f} KB")

        # Preview Data
        st.subheader("Preview Data")
        st.write(df.head())

        # Data Cleaning Options
        # Options for Data Cleaning
    st.subheader("Data Cleaning Options")
    if st.checkbox(f"Clean Data for {file.name}"):
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Remove Duplicates from {file.name}"):
                df = st.session_state[file_key]  # Get the stored dataframe
                df = df.drop_duplicates()  # Remove duplicates
                st.session_state[file_key] = df  # Update the session state
                st.write("✅ Duplicates Removed!")
                st.write(df.head())  # Display updated DataFrame

        with col2:
            if st.button(f"Fill Missing Values from {file.name}"):
                df = st.session_state[file_key]  # Get stored dataframe
                numeric_cols = df.select_dtypes(include=['number']).columns  # Select numeric columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())  # Fill missing values
                st.session_state[file_key] = df  # Update session state
                st.write("✅ Missing values have been filled!")
                st.write(df.head())  # Display updated DataFrame

        # Column Selection
        st.subheader("Select Columns")
        try:
            columns = st.multiselect(f"Choose columns from {file.name}", df.columns, default=df.columns)
            if columns:
                st.session_state[file_key] = df[columns]
                df = st.session_state[file_key]
            else:
                st.warning("Please select at least one column.")
        except Exception as e:
            st.error(f"Error selecting columns: {e}")

        # Data Visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            numeric_df = df.select_dtypes(include="number")
            if not numeric_df.empty:
                st.bar_chart(numeric_df.iloc[:, :2])  # Display first two numeric columns
            else:
                st.warning("No numeric columns available for visualization.")

        # File Conversion
        st.subheader("File Conversion")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            df = st.session_state[file_key]

            try:
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                else:
                    df.to_excel(buffer, index=False, engine="openpyxl")
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)
                st.download_button(
                    label=f"Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type,
                )
                st.success(f"{file.name} converted successfully!")

            except Exception as e:
                st.error(f"Error converting {file.name}: {e}")

st.success("Thank you for using the Data Analysis App! 🚀")
