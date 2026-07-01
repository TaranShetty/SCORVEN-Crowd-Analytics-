import streamlit as st
import cv2
import pandas as pd
import numpy as np
import time
import tempfile
from ultralytics import YOLO
import plotly.express as px
import plotly.graph_objects as go
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Advanced Crowd Analytics", layout="wide")
st.title("🚀 AI Crowd Intelligence Dashboard")

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    model_path = os.path.join("model", "best.pt")
    model = YOLO(model_path)
    model.to("cpu")
    return model

model = load_model()

# ---------------- SIDEBAR ----------------
st.sidebar.header("🕹 Control Panel")
source_radio = st.sidebar.radio("Select Source:", ("Webcam", "Upload Video"))
conf_level = st.sidebar.slider("Detection Sensitivity", 0.0, 1.0, 0.4)
line_thickness = st.sidebar.slider("Box Thickness", 1, 5, 2)

uploaded_file = None
if source_radio == "Upload Video":
    uploaded_file = st.sidebar.file_uploader("Upload Footage", type=["mp4", "avi", "mov"])

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["time", "count"])

if "density_stats" not in st.session_state:
    st.session_state.density_stats = {"Low":0, "Moderate":0, "High":0}

# ---------------- DASHBOARD LAYOUT ----------------
col1, col2 = st.columns([2,1])

video_placeholder = col1.empty()

with col2:
    st.subheader("📊 Live Metrics")
    curr_metric = st.empty()
    peak_metric = st.empty()
    avg_metric = st.empty()
    min_metric = st.empty()
    status_metric = st.empty()

st.markdown("---")
trend_placeholder = st.empty()
dist_placeholder = st.empty()

# ---------------- PROCESSING FUNCTION ----------------
def process_video(source):
    cap = cv2.VideoCapture(source)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Inference
        results = model.predict(source=frame, conf=conf_level, verbose=False)
        annotated_frame = results[0].plot(labels=False, conf=False, line_width=line_thickness)

        count = len(results[0].boxes)

        # Update History
        current_time = time.strftime("%H:%M:%S")
        new_data = pd.DataFrame({"time":[current_time], "count":[count]})
        st.session_state.history = pd.concat(
            [st.session_state.history, new_data]
        ).tail(60)

        # Determine Density
        if count < 5:
            status = "Low"
            color = "green"
            st.session_state.density_stats["Low"] += 1
        elif count < 15:
            status = "Moderate"
            color = "orange"
            st.session_state.density_stats["Moderate"] += 1
        else:
            status = "High"
            color = "red"
            st.session_state.density_stats["High"] += 1

        # ---------------- UI UPDATE ----------------
        video_placeholder.image(annotated_frame, channels="BGR", use_container_width=True)

        curr_metric.metric("👥 Current Count", count)
        peak_metric.metric("📈 Peak Count", st.session_state.history["count"].max())
        avg_metric.metric("📊 Average Count", round(st.session_state.history["count"].mean(),2))
        min_metric.metric("📉 Minimum Count", st.session_state.history["count"].min())
        status_metric.markdown(f"**Crowd Density:** :{color}[{status}]")

        # ---------------- TREND GRAPH ----------------
        fig_trend = px.area(
            st.session_state.history,
            x="time",
            y="count",
            template="plotly_dark"
        )
        fig_trend.update_layout(
            height=400,
            xaxis_title="Time (Last 60 seconds)",
            yaxis_title="People Count",
            margin=dict(l=10,r=10,t=10,b=10)
        )
        trend_placeholder.plotly_chart(fig_trend, use_container_width=True)

        # ---------------- DENSITY DISTRIBUTION ----------------
        fig_pie = go.Figure(data=[go.Pie(
            labels=list(st.session_state.density_stats.keys()),
            values=list(st.session_state.density_stats.values()),
            hole=0.4
        )])
        fig_pie.update_layout(
            template="plotly_dark",
            height=400,
            title="Density Distribution (Session)"
        )
        dist_placeholder.plotly_chart(fig_pie, use_container_width=True)

    cap.release()

# ---------------- EXECUTION ----------------
if source_radio == "Webcam":
    process_video(0)
elif source_radio == "Upload Video" and uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    process_video(tfile.name)
else:
    st.info("Select a source from the sidebar to begin.")
