# imports
import streamlit as st
import pandas as pd
import os
import io 
from io import BytesIO

# set up the app
st.set_page_config(page_title="Data Analysis", page_icon=":bar_chart:", layout="wide")
st.title("Data Analysis")
st.write("Transform your files from CSV and Excel format with built-in data cleaning and visualisation.")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", accept_multiple_files=True, type=['CSV', 'xlsx', 'xls'])

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
             df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue
        
        # display infor about the file
        st.write("File Information:")
        st.write(f"File Name: {file.name}")
        st.write(f"File Type: {file_ext}")
        st.write(f"Number of Rows: {df.shape[0]}")
        st.write(f"Number of Columns: {df.shape[1]}")
        st.write(f"Data Types: {df.dtypes}")
        st.write(f"Missing Values: {df.isnull().sum()}")
        st.write(f"Duplicate Rows: {df.duplicated().sum()}")
        st.write(f"Unique Values: {df.nunique()}")
        st.write(f"Summary Statistics: {df.describe()}")
        st.write(f"File Size {file.size/1024:.2f} KB")

        # 5 rows
        st.write("Preview the head of Data Frame")
        st.write(df.head())

        # Options for Data Cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed")

            with col2:
                if st.button(f"Fill Missing Values from {file.name}"):
                    numaric_cols= df.select_dtypes(include=['number']).columns
                    df[numaric_cols] = df[numaric_cols].fillna(df[numaric_cols].mean())
                    st.write("Missing values have been filled!")

        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Choose columns from {file.name}", df.columns, default=df.columns)
        df = df[columns]


        # Create some visualisation
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualisation for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])
        
        #  Convert files from or to CSV
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:",["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)


            # Download Button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,


            )
st.success("Thank you for using the Data Analysis App!")











 












        






