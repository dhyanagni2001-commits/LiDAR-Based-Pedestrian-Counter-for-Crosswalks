import streamlit as st
import numpy as np
import time
import pandas as pd


from src.lidar_io import generate_simulation_sequence
from src.clustering import cluster_pedestrians
from src.tracking import SimpleTracker
from src.counting import LineCounter



st.set_page_config(
    page_title="LiDAR Pedestrian Counter",
    layout="wide"
)

st.title("🚦 LiDAR-Based Pedestrian Counter Dashboard")


placeholder_counts = st.empty()
placeholder_plot = st.empty()

frames = generate_simulation_sequence(num_frames=400)

tracker = SimpleTracker(max_distance=0.6)
counter = LineCounter(line_x=0.0)

for frame in frames:

    centers, _ = cluster_pedestrians(frame, eps=0.5, min_samples=1)

    tracked = tracker.update(centers)

    lr, rl = counter.update(tracked)

    with placeholder_counts.container():
        st.subheader("Live Counts")
        st.metric("Left ➜ Right", lr)
        st.metric("Right ➜ Left", rl)

    with placeholder_plot.container():
        st.subheader("LiDAR Scan Visualization")
        points = np.array(frame)

        df = pd.DataFrame(points, columns=["x", "y"])

        st.scatter_chart(
            df,
            x="x",
            y="y"
        )

    time.sleep(0.05)
