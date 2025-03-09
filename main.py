import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import time
import ssl

def load_data():
    """Load the Titanic dataset from Google Sheets with SSL workaround."""
    sheet_url = "https://docs.google.com/spreadsheets/d/1HWrxkS1vnwFc0tdD93sPUyYYVz2Oakfy10dAZv1m-5s/export?format=csv"
    ssl._create_default_https_context = ssl._create_unverified_context  # Disable SSL verification
    df = pd.read_csv(sheet_url)
    return df

def plot_bar_chart(df):
    """Create a bar chart of survival rate by class."""
    survival_rate = df.groupby("class")["survived"].mean()
    fig, ax = plt.subplots()
    survival_rate.plot(kind='bar', ax=ax, color=['blue', 'orange', 'green'])
    ax.set_title("Survival Rate by Passenger Class")
    ax.set_ylabel("Survival Rate")
    ax.set_xlabel("Class")
    return fig

def plot_pie_chart(df):
    """Create a pie chart of survival rate by class."""
    survival_rate = df.groupby("class")["survived"].mean()
    fig, ax = plt.subplots()
    ax.pie(survival_rate, labels=survival_rate.index, autopct='%1.1f%%', colors=['blue', 'orange', 'green'])
    ax.set_title("Survival Rate by Passenger Class")
    return fig

# Load dataset
df = load_data()

# Streamlit UI
st.title("A/B Testing: Titanic Survival Rates")
st.write("### Business Question: Which class of passengers had the highest survival rate?")

# Randomly select a chart to display
chart_choice = random.choice(["bar", "pie"])

if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "chart_displayed" not in st.session_state:
    st.session_state.chart_displayed = False

if st.button("Show Chart"):
    st.session_state.start_time = time.time()
    st.session_state.chart_displayed = True
    
    if chart_choice == "bar":
        st.pyplot(plot_bar_chart(df))
    else:
        st.pyplot(plot_pie_chart(df))

if st.session_state.chart_displayed:
    if st.button("I answered your question"):
        response_time = time.time() - st.session_state.start_time
        st.write(f"You took **{response_time:.2f} seconds** to answer the question!")
#streamlit run /Users/juriweber/PycharmProjects/numpy/main.py

