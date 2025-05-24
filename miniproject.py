# dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import calendar

# Load data from GCS or local
@st.cache_data
def load_data():
    # Example: Load from local CSV
    return pd.read_csv("employee_productivity.csv", parse_dates=['date'])

data = load_data()

# Title
st.title("📊 Employee Productivity Dashboard")

# Line Plot: Tasks Completed per Employee
st.subheader("Tasks Completed per Employee")
task_counts = data.groupby("employee_id")["task_completed"].sum().reset_index()
fig_line = px.line(task_counts, x='employee_id', y='task_completed', markers=True)
st.plotly_chart(fig_line)

# Box Plot: Performance Scores by Team
st.subheader("Performance Score Distribution by Team")
fig_box, ax = plt.subplots()
sns.boxplot(x='team', y='performance_score', data=data, ax=ax)
st.pyplot(fig_box)

# Heatmap: Work Hours by Day
st.subheader("Average Work Hours by Day of Week")
data['day'] = data['date'].dt.day_name()
day_order = list(calendar.day_name)
heat_data = data.groupby('day')['work_hours'].mean().reindex(day_order)
fig_heat, ax = plt.subplots()
sns.heatmap(heat_data.values.reshape(1, -1), cmap='YlGnBu', annot=True, xticklabels=day_order)
st.pyplot(fig_heat)
