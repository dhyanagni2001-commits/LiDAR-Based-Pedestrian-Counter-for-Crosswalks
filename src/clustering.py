# src/clustering.py
import numpy as np
from sklearn.cluster import DBSCAN

def cluster_pedestrians(points, eps=0.3, min_samples=3):
    """
    points: Nx2 array of (x, y)
    return: cluster_centers, labels
    """
    if len(points) == 0:
        return np.empty((0, 2)), np.array([])

    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(points)
    labels = clustering.labels_
    unique_labels = [l for l in set(labels) if l != -1]

    centers = []
    for lbl in unique_labels:
        cluster_points = points[labels == lbl]
        centers.append(cluster_points.mean(axis=0))
    centers = np.array(centers)
    return centers, labels
