# src/main_offline_demo.py
from lidar_io import generate_simulation_sequence
from clustering import cluster_pedestrians
from tracking import SimpleTracker
from counting import LineCounter

def main():
    frames = generate_simulation_sequence(num_frames=200)
    tracker = SimpleTracker(max_distance=0.6)
    counter = LineCounter(line_x=0.0)

    for t, frame_points in enumerate(frames):
        centers, _ = cluster_pedestrians(frame_points, eps=0.5, min_samples=1)
        tracked = tracker.update(centers)
        lr, rl = counter.update(tracked)

        print(f"Frame {t:03d} | Active tracks: {len(tracked)} | L->R: {lr} | R->L: {rl}")

if __name__ == "__main__":
    main()
