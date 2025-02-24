# Data Analysis App

## Overview
The **DataSweep** app is a web-based application built using **Streamlit** and **Python** that allows users to upload CSV and Excel files for data cleaning, transformation, and visualization. This tool is designed to streamline data handling, making it easy to explore, clean, and convert data into different formats.

## Features
- **Upload multiple files** (CSV and Excel supported)
- **View file details** (rows, columns, missing values, duplicate counts, unique values, summary statistics, etc.)
- **Preview the first five rows** of uploaded datasets
- **Data Cleaning Options**:
  - Remove duplicate rows
  - Fill missing numerical values with column means
- **Column Selection**:
  - Select specific columns for further analysis
- **Data Visualization**:
  - Generate bar charts for numerical data
- **File Conversion**:
  - Convert files between CSV and Excel formats
  - Download the processed files

## How to Use
1. **Run the App**:
   ```bash
   streamlit run app.py
   ```
   If `streamlit` is not recognized, use:
   ```bash
   python -m streamlit run app.py
   ```
2. **Upload Your Data**:
   - Click on the "Upload your files" button and select CSV or Excel files.
3. **View File Information**:
   - The app displays details like file name, size, data types, missing values, duplicates, and summary statistics.
4. **Clean Your Data**:
   - Choose to remove duplicates and fill missing values.
5. **Select Columns**:
   - Pick specific columns for analysis.
6. **Visualize Data**:
   - Check the "Show Visualization" option to generate bar charts.
7. **Convert & Download Files**:
   - Convert files to CSV or Excel and download the processed data.
8. **Completion**:
   - The app confirms successful processing with a success message.

## Technologies Used
- **Python** (Data processing & backend logic)
- **Streamlit** (Frontend & UI framework)
- **Pandas** (Data manipulation)
- **OS & IO Modules** (File handling)

## Requirements
Before running the app, install the required dependencies:
```bash
pip install streamlit pandas openpyxl
```

## Live Demo
Try out DataSweep online: [DataSweep App](https://datasweep-mehdinathani.streamlit.app/)

## License
This project is open-source and free to use.

---
Enjoy using the **DataSweep** app! 🚀

