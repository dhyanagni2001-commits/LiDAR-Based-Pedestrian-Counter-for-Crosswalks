# **🚦 LiDAR-Based Pedestrian Counter for Crosswalks**

A privacy-preserving pedestrian-counting system that uses 2D LiDAR point clouds instead of cameras.
The system detects pedestrians, tracks them over time, and counts how many cross a virtual line (a crosswalk), including direction.

Built with:

Python

NumPy / Scikit-Learn

Matplotlib

Streamlit Dashboard

# ✨ Features

✔️ Works without cameras (privacy-friendly)

✔️ 2D LiDAR simulation or real LiDAR datasets

✔️ DBSCAN clustering to form pedestrian blobs

✔️ Multi-object tracking with persistent IDs

✔️ Line-crossing counting logic (Left→Right and Right→Left)

✔️ Live matplotlib visualization

✔️ Streamlit web dashboard UI

✔️ Modular and easy to extend

# 🧭 Use-cases

Smart crosswalks

Traffic engineering studies

Smart-city infrastructure

Pedestrian flow analysis

Safety monitoring without video recording

# 🛠️ Installation
1️⃣ Clone the repository

2️⃣ Create virtual environment

3️⃣ Install dependencies

# ▶️ Run the offline demo (terminal visualization)

This version:

simulates LiDAR points

tracks pedestrians

counts crossings

shows a live matplotlib animation

run: python -m src.main_offline_demo
You will see:

moving points

IDs on tracked pedestrians

red vertical virtual line

live counter in terminal

# 🖥️ Run the Streamlit Web Dashboard

This UI shows:

live pedestrian counts

left→right & right→left totals

LiDAR scatter plot animation

Run:

streamlit run dashboard.py

# 🧠 How It Works (Pipeline)

Generate or load 2D LiDAR points

Cluster points into pedestrians (DBSCAN)

Track cluster centroids frame-to-frame

Assign each one a persistent ID

Detect when a track crosses virtual line

Count direction:

Left ➜ Right

Right ➜ Left