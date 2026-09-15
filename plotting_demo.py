import streamlit as st
import numpy as np
import time

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.empty()

# Initialize with one data point
data = np.random.randn(1, 1)

chart.line_chart(data)

for i in range(1, 51):
    # Generate new rows based on the last value (random walk)
    new_rows = data[-1, :] + np.random.randn(5, 1).cumsum(axis=0)

    # Append new rows to existing data
    data = np.concatenate([data, new_rows])

    # Update the chart with full data
    chart.line_chart(data)

    progress = i * 2
    status_text.text(f"{progress}% complete")
    progress_bar.progress(progress)

    time.sleep(0.01)

progress_bar.empty()

st.button("Rerun")
