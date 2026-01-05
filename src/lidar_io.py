# src/lidar_io.py
import numpy as np

def simulate_lidar_frame(pedestrians, noise_points=20):
    """
    pedestrians: list of (x, y) positions for this frame
    returns: Nx2 array of (x, y) points
    """
    pts = np.array(pedestrians)
    # Add random noise points around the scene
    noise = np.random.uniform(low=[-5, -5], high=[5, 5], size=(noise_points, 2))
    all_pts = np.vstack([pts, noise])
    return all_pts

def generate_simulation_sequence(num_frames=200):
    """
    Generate a simple sequence where pedestrians cross from left to right.
    """
    trajectories = [
        # each pedestrian: start_y, speed_x
        {"y": -1.0, "x0": -4.0, "vx": 0.05},
        {"y":  0.5, "x0": -5.0, "vx": 0.06},
        {"y":  1.5, "x0": -6.0, "vx": 0.04},
    ]

    frames = []
    for t in range(num_frames):
        ped_positions = []
        for traj in trajectories:
            x = traj["x0"] + traj["vx"] * t
            y = traj["y"]
            ped_positions.append((x, y))
        frame_points = simulate_lidar_frame(ped_positions)
        frames.append(frame_points)
    return frames
