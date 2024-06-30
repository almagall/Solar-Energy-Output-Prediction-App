import streamlit as st

def show_bio_page():
    st.title('Bio Page')
    st.subheader('About Me:')
    st.write("""
    I graduated from UCSD in 2020 with a bachelor’s in Human Biology. Ever since then, I journeyed into the biotech industry at the start of my career, and from there transitioned over to the renewable energy sector as a Business Intelligence Analyst. I’ve had the opportunity to work at great companies and expand my skills with each job. I’ve specifically worked in clinical lab technician, quality control, research associate roles, and now as an analyst. Throughout all these roles, I’ve realized the tremendous value of data and its role in shaping all industry sectors.

    What I can say is my favorite part of the jobs I’ve worked at is leveraging data to tell compelling stories that lead to informed decisions and action. I believe that data, when properly analyzed and interpreted, can unlock invaluable insights that drive innovation and positively impact human lives.

    In October 2022 I decided to take the leap and pursue a master’s in data science at Eastern University and have thoroughly enjoyed all the courses I have taken so far. I continue to refine my skills through the program as well by being a GA (previously for DTSC 520: Fundamentals of Data Science and now DTSC 560: Data Science for Business).

    As my time in the data science program comes to a close, I look forward to delving more into machine learning in applicable business practice in order to utilize my skills throughout the program to leverage machine learning to enhance business solutions and outcomes.
    """)
    st.markdown(
        """
        <hr style="border: 1px solid #ccc;">
        """,
        unsafe_allow_html=True
    )