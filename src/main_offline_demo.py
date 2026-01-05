import matplotlib.pyplot as plt

from lidar_io import generate_simulation_sequence
from clustering import cluster_pedestrians
from tracking import SimpleTracker
from counting import LineCounter
from visualization import plot_frame


def main():
    # generate simulated LiDAR frames
    frames = generate_simulation_sequence(num_frames=200)

    # tracker for object IDs
    tracker = SimpleTracker(max_distance=0.6)

    # virtual line x = 0 for crossing
    counter = LineCounter(line_x=0.0)

    # enable interactive plotting
    plt.ion()

    for t, frame_points in enumerate(frames):

        # 1) cluster lidar points into persons
        centers, _ = cluster_pedestrians(
            frame_points,
            eps=0.5,
            min_samples=1
        )

        # 2) track objects with persistent IDs
        tracked = tracker.update(centers)

        # 3) update counters for crossings
        lr, rl = counter.update(tracked)

        # 4) print log output
        print(
            f"Frame {t:03d} | Active tracks: {len(tracked)} | "
            f"L->R: {lr} | R->L: {rl}"
        )

        # 5) visualize
        plot_frame(frame_points, tracked, line_x=0.0)

    # keep window open at end
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
