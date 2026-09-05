import streamlit as st
import json
import pandas as pd

# Set up the title of your app
st.title("📂 JSON File Uploader & Viewer")

# 1. Create the file uploader component restricted to JSON files
uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])

# 2. Check if a file has been uploaded
if uploaded_file is not None:
    try:
        # 3. Load the JSON data
        json_data = json.load(uploaded_file)
        
        st.success("File uploaded successfully!")
        
        # --- Do something with the data ---
        
        # Option A: Display raw interactive JSON structure
        st.subheader("Raw JSON Viewer")
        st.json(json_data)
        
        # Option B: Convert to DataFrame if it's flat/tabular data
        st.subheader("Tabular View (If applicable)")
        df = pd.DataFrame(json_data)
        st.dataframe(df)
        
    except Exception as e:
        st.error(f"Error parsing JSON file: {e}")
