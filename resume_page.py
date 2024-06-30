import streamlit as st

def show_resume_page():
    st.title('Resume Page')
    st.image('Resume_Picture.jpg', width = 300)

    st.header('SUMMARY')
    st.write("""
    Dynamic data professional with a robust background spanning the biotech industry, including gene therapy, pharmaceuticals, and medical devices, as well as experience in solar EPC (Engineering, Procurement, and Construction). Expert in leveraging advanced programming, data manipulation, statistical analysis, visualization, and modeling skills to drive actionable insights and deliver impactful results. Adept at translating complex data into strategic decisions and solutions, poised to excel in data roles that bridge expertise with cutting-edge analytics.
    """)

    st.header('EDUCATION')
    st.write("""
    **Eastern University – St. Davids, PA (online)**  
    Master of Science – Data Science, Expected Graduation: June 2024

    **University of California, San Diego – San Diego, CA**  
    Bachelor of Science – Human Biology, June 2020
    """)

    st.header('PROFESSIONAL EXPERIENCE')
    
    st.subheader('SOLV Energy – San Diego, CA')
    st.write("""
    **Business Intelligence Analyst**  
    *October 2024 - Present*
    - Develop and maintain interactive dashboards, reports, and visualizations using business intelligence tools (Power BI).
    - Collaborate with stakeholders across the organization to build strong relationships and support data accessibility and improvement.
    - Document technical requirements for reports and dashboards to facilitate further development by the Software Development group.
    - Provide training and technical support for self-service reporting and promote a culture of data-driven decision-making.
    - Conduct ad hoc data analysis, identify trends and insights, and present findings to stakeholders at all levels.
    - Support business planning and contribute to the digital solutions roadmap, including automating data workflows and optimizing analytical models.
    - Maintain a centralized knowledge base for business data access and usage, ensuring compliance with data governance best practices.       
    """)

    st.subheader('Eastern University – St. Davids, PA (remote)')
    st.write("""
    **Graduate Assistant, DTSC 520: Data Science Fundamentals**  
    *January 2023 - Present*  
    - Work collaboratively with professors and other assistants to provide help to students on a variety of topics ranging from Python programming (NumPy and Pandas), data visualization (Matplotlib, Seaborn, and Plotly), and version control (GitHub).
    - Arrange weekly discussion sections to present topics covered in lectures and create assignments that facilitate learning and recall.
    """)

    st.subheader('Rejuvenate Bio – San Diego, CA')
    st.write("""
    **Senior Research Associate, Process Analytics**  
    *May 2023 – June 2023*  
    - Developed automated data analysis tools and spreadsheets for laboratory testing to generate instantaneous reportable results and significantly reduced turnaround time of report delivery by 90%.
    - Presented project and report updates on a weekly basis as well as company-wide updates for the Process and Analytical Development departments to showcase results of data and trends.
    - Led DOEs (Design of Experiments) and bridging projects for comparability studies among different analytical laboratory equipment to develop machine-learning predictive models and statistical analysis presented to stakeholders.
    """)

    st.write("""
    **Quality Control Associate**  
    *February 2023 – May 2023*  
    - Utilized statistical analysis using JMP software for hypothesis testing, ad-hoc and post-hoc analysis, graphing, and data trending.
    - Designed a database system with PostgreSQL used by QC and AD departments to implement and streamline an ETL process that gathered data from multiple sources of raw laboratory equipment data and refined experimental results.
    """)

    st.subheader('Fate Therapeutics – San Diego, CA')
    st.write("""
    **Quality Control Associate**  
    *November 2021 – January 2023*  
    - Conducted molecular testing for lot release and stability studies of clinical drug products.
    - Produced and revised Standard Operating Procedures (SOPs), equipment methods, and data analysis spreadsheets using Microsoft Word, Excel, and Smartsheet.
    - Facilitated training for molecular methods to new and current Quality Control associates.
    """)

    st.subheader('Lumira DX – San Diego, CA')
    st.write("""
    **Quality Control Specialist**  
    *May 2021 – November 2021*  
    - Performed testing for lot release and stability studies.
    - Provided IQ/OQ/PQ equipment validation as needed for laboratory equipment.
    - Created interactive dashboards using Tableau to visualize testing metrics and trending.
    """)

    st.subheader('Helix – San Diego, CA')
    st.write("""
    **Clinical Laboratory Technician**  
    *November 2020 – May 2021*  
    - Performed automated RNA extraction and RT-qPCR-based genetic testing.
    - Reviewed, revised, and updated SOPs.
    """)

    st.header('SKILLS')
    st.write("""
    - Python, R, SQL, and Power BI for data retrieval, manipulation, visualization, and machine learning.
    - Statistical Analysis: Hypothesis Testing, ad/post-hoc analysis, trending, and graphing (JMP).
    - Microsoft Office for tabular data wrangling and presentations.
    - Data analytics and diagnostic testing for generating insight and providing solutions.
    """)

    st.header('CERTIFICATIONS')
    st.write("""
    **Google Data Analytics**  
    *November 2022*  
    - Data cleaning and organization for analysis using Google Spreadsheets, SQL, and R.
    - Data visualization to communicate findings with dashboards using Tableau.

    **Machine Learning Specialization**  
    *July 2023*  
    - Learned about and built machine learning models (supervised and unsupervised methods) from scratch as well as with ML and Deep Learning frameworks (TensorFlow and Sci-Kit Learn) to create and train models for predictive and classification tasks.
    """)

    st.markdown(
        """
        <hr style="border: 1px solid #ccc;">
        """,
        unsafe_allow_html=True
    )
