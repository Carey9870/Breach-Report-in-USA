import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# load and read the dataset
b_report = pd.read_csv('breach_report.csv', encoding='latin5')

# load preprocessor.py
b_report = preprocessor.preprocess(b_report)

# sidebar ui
st.sidebar.title('Cyber Breaches in the USA')

# sidebar components
user_menu = st.sidebar.radio(
    'Select an Option', (
        'Count of Cyber Breaches per State', 'Type of Breach', 'Covered Entity Type', 'Location of Breached Information',
        'Business Associate Present', 'Name of Covered Entity per State per Business Associate Present',
        'Location of Breached Information Breach Submission Date Type of Breach', 'Name of Covered Entity Covered Entity Type State'
))

if user_menu == 'Count of Cyber Breaches per State':
    st.subheader('Count of Cyber Breaches per State')
    Count_of_Cyber_Breaches_per_State = helper.CountofCyberBreachesperState(b_report)
    st.table(Count_of_Cyber_Breaches_per_State)

if user_menu == 'Type of Breach':
    st.subheader('Types of Breaches that have Occurred')
    Type_of_Breach = helper.TypeofBreach(b_report)
    st.table(Type_of_Breach)

if user_menu == 'Covered Entity Type':
    st.subheader('Covered Entity Type')
    Count_of_Types_of_Breaches_per_Entity_Type = helper.CoveredEntityType(b_report)
    st.table(Count_of_Types_of_Breaches_per_Entity_Type)

if user_menu == 'Location of Breached Information':
    st.subheader('Location of Breached Information')
    Location_of_Breached_Information = helper.LocationofBreachedInformation(b_report)
    st.table(Location_of_Breached_Information)

if user_menu == 'Business Associate Present':
    st.subheader('Business Associate Present')
    Business_Associate_Present = helper.BusinessAssociatePresent(b_report)
    st.table(Business_Associate_Present)

if user_menu == 'Name of Covered Entity per State per Business Associate Present':
    st.subheader('Name of Covered Entity per State per Business Associate Present')
    Name_of_Covered_Entity_per_State_per_Business_Associate_Present = helper.NameofCoveredEntityperStateperBusinessAssociatePresent(b_report)
    st.table(Name_of_Covered_Entity_per_State_per_Business_Associate_Present)

if user_menu == 'Location of Breached Information Breach Submission Date Type of Breach':
    st.subheader('Location of Breached Information per Breach Submission Date per Type of Breach')
    Location_of_Breached_Information_Breach_Submission_Date_Type_of_Breach = helper.LocationofBreachedInformationBreachSubmissionDateTypeofBreach(b_report)
    st.table(Location_of_Breached_Information_Breach_Submission_Date_Type_of_Breach)

if user_menu == 'Name of Covered Entity Covered Entity Type State':
    st.subheader('Name of Covered Entity Covered Entity Type State')
    Name_of_Covered_Entity_Covered_Entity_Type_State = helper. NameofCoveredEntityCoveredEntityTypeState(b_report)
    st.table(Name_of_Covered_Entity_Covered_Entity_Type_State)