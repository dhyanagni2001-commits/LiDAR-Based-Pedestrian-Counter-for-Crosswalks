import matplotlib.pyplot as plt

def plot_frame(points, tracks, line_x=0.0):
    """
    points: Nx2 numpy array
    tracks: list of (id, x, y)
    """

    xs = points[:, 0]
    ys = points[:, 1]

    plt.clf()
    plt.scatter(xs, ys, s=10)

    # draw crossing line
    plt.axvline(x=line_x, color='r', linestyle='--')

    # draw tracked objects with labels
    for tid, x, y in tracks:
        plt.scatter(x, y, c='green')
        plt.text(x + 0.05, y + 0.05, str(tid), fontsize=8)

    plt.xlim(-7, 7)
    plt.ylim(-5, 5)
    plt.pause(0.01)
