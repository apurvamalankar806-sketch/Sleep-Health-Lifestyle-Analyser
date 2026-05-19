import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Sleep Health Analyser",
    page_icon="😴",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv", encoding='utf-8-sig')
    df.columns = df.columns.str.replace('_', ' ').str.strip().str.replace(' ', '_')
    df['BMI_Category'] = df['BMI_Category'].replace('Normal Weight', 'Normal')
    df['Sleep_Disorder'] = df['Sleep_Disorder'].fillna('None')
    df.drop(columns=['Person_ID'], inplace=True)
    return df

@st.cache_resource
def load_model():
    model = joblib.load('sleep_model.pkl')
    features = joblib.load('model_features.pkl')
    return model, features

df = load_data()
model, features = load_model()

st.title("😴 Sleep Health & Lifestyle Analyser")
st.markdown("Explore how stress, BMI, occupation and lifestyle affect sleep quality — and predict your own!")
st.divider()

# ── Sidebar ───────────────────────────────────────────────────
st.sidebar.header("🔍 Filter Data")

occupation_filter = st.sidebar.multiselect(
    "Select Occupation",
    options=df['Occupation'].unique(),
    default=df['Occupation'].unique()
)

bmi_filter = st.sidebar.multiselect(
    "Select BMI Category",
    options=df['BMI_Category'].unique(),
    default=df['BMI_Category'].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

# Apply filters
df_filtered = df[
    (df['Occupation'].isin(occupation_filter)) &
    (df['BMI_Category'].isin(bmi_filter)) &
    (df['Gender'].isin(gender_filter))
]

st.sidebar.divider()
st.sidebar.metric("Total Records", len(df_filtered))
st.sidebar.metric("Avg Sleep Quality", round(df_filtered['Quality_of_Sleep'].mean(), 2))
st.sidebar.metric("Avg Stress Level", round(df_filtered['Stress_Level'].mean(), 2))

# ── EDA Section ───────────────────────────────────────────────
st.header("📊 Exploratory Data Analysis")

# Metric cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", len(df_filtered))
col2.metric("Avg Sleep Quality", round(df_filtered['Quality_of_Sleep'].mean(), 2))
col3.metric("Avg Stress Level", round(df_filtered['Stress_Level'].mean(), 2))
col4.metric("Avg Sleep Duration", round(df_filtered['Sleep_Duration'].mean(), 2))

st.divider()

# Row 1 — two charts side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sleep Quality by Occupation")
    occ_sleep = df_filtered.groupby('Occupation')['Quality_of_Sleep'].mean().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=occ_sleep.values, y=occ_sleep.index, palette='coolwarm', ax=ax)
    ax.set_xlabel('Avg Sleep Quality')
    st.pyplot(fig)
    plt.close()

with col2:
    st.subheader("Sleep Quality by BMI Category")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='BMI_Category', y='Quality_of_Sleep', data=df_filtered,
                palette='Set2', order=['Normal', 'Overweight', 'Obese'], ax=ax)
    ax.set_xlabel('BMI Category')
    ax.set_ylabel('Sleep Quality')
    st.pyplot(fig)
    plt.close()

st.divider()

# Row 2 — two more charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Stress vs Sleep Quality")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='Stress_Level', y='Quality_of_Sleep', data=df_filtered,
                 marker='o', color='tomato', ax=ax)
    ax.set_xlabel('Stress Level')
    ax.set_ylabel('Sleep Quality')
    st.pyplot(fig)
    plt.close()

with col2:
    st.subheader("Sleep Duration Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df_filtered['Sleep_Duration'], bins=15, kde=True,
                 color='steelblue', ax=ax)
    ax.set_xlabel('Hours')
    st.pyplot(fig)
    plt.close()

    # ── Sleep Quality Quiz ────────────────────────────────────────
st.header("🧠 Predict Your Sleep Quality")
st.markdown("Answer a few simple questions and our model will predict your sleep quality score!")
st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.slider("How old are you?", 18, 65, 25)
    
    gender = st.radio("Gender", ["Male", "Female"])
    
    occupation = st.selectbox("What best describes your job?", [
        "Engineer", "Doctor", "Nurse", "Teacher",
        "Accountant", "Lawyer", "Salesperson",
        "Software Engineer", "Scientist", "Manager",
        "Sales Representative"
    ])
    
    sleep_duration = st.slider("How many hours do you sleep daily?", 4.0, 10.0, 7.0, step=0.5)
    
    daily_steps = st.slider("How many steps do you walk daily?", 1000, 20000, 7000, step=500)

with col2:
    stress_answer = st.selectbox(
        "How often do you feel overwhelmed or anxious?",
        ["Rarely", "Sometimes", "Often", "Almost Always"]
    )

    activity_answer = st.selectbox(
        "How often do you exercise per week?",
        ["Rarely (1-2x)", "Moderately (3-4x)", "Very Active (5x+)"]
    )

    bmi_answer = st.selectbox(
        "How would you describe your body weight?",
        ["Normal / Healthy", "Slightly Overweight", "Obese"]
    )

    bp_answer = st.selectbox(
        "Do you have high blood pressure?",
        ["No", "Borderline", "Yes"]
    )

    heart_rate = st.slider("What is your resting heart rate (bpm)?", 55, 100, 70)

    disorder_answer = st.selectbox(
        "Do you have any diagnosed sleep disorder?",
        ["None", "Insomnia", "Sleep Apnea"]
    )