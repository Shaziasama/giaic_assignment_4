import pandas as pd
import streamlit as st
import random

st.set_page_config(page_title="Student Data", page_icon="🎓", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    /* Apply a light blue background */
    body {
        background-color: #D0E8F2;
        font-family: 'Poppins', sans-serif;
    }

    /* Load Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    /* Center the entire content */
    .center-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
        margin-top: 20px;
    }

    /* Style the table container */
    .dataframe-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        width: 60%;
        margin-top: 20px;
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        border: 2px solid #4CAF50;
    }

    /* Style the header */
    h1 {
        color: #0077B6;
        font-weight: 600;
    }

    /* Style the download button */
    .download-btn {
        background-color: #0077B6;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
        margin-top: 20px;
        transition: 0.3s;
    }
    
    /* Hover Effect */
    .download-btn:hover {
        background-color: #005f87;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Center Title
st.markdown('<div class="center-container"><h1>Student CSV File Generator</h1></div>', unsafe_allow_html=True)

names = ["Ali", "Ahmed", "Sara", "Fatima", "Hassan", "Kamran", "Zain", "Nasir", "Tariq", "Noman", 
         "Ayesha", "Sana", "Zara", "Kiran", "Nida", "Nadia", "Noreen", "Zohaib"]

# Create Student Data
students = []
for i in range(1, 18):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Marks": random.randint(40, 100),
        "Grade": random.choice(["A", "B", "C", "D", "E"]),
    }
    students.append(student)

df = pd.DataFrame(students)

# Center and Style Data Table
st.markdown('<div class="center-container">', unsafe_allow_html=True)
st.subheader("Generated Students Data")
st.markdown('</div>', unsafe_allow_html=True)

# Table inside a styled container
st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
st.dataframe(df)
st.markdown('</div>', unsafe_allow_html=True)

# Center Download Button
csv = df.to_csv(index=False).encode("utf-8")

st.markdown('<div class="center-container">', unsafe_allow_html=True)
st.download_button(
    label="Download CSV File",
    data=csv,
    file_name="students.csv",
    mime="text/csv",
    key="students",
)
st.markdown('</div>', unsafe_allow_html=True)

st.success("Students Record Generated Successfully")

