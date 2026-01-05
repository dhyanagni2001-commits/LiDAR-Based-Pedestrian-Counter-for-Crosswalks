# src/tracking.py
import numpy as np

class SimpleTracker:
    def __init__(self, max_distance=0.7):
        self.max_distance = max_distance
        self.next_id = 0
        self.tracks = {}  # id -> {"pos": (x,y)}

    def update(self, detections):
        """
        detections: Nx2 array of (x, y)
        returns: list of (id, x, y)
        """
        detections = np.array(detections)
        assigned = set()
        updated_tracks = {}

        # Step 1: assign existing tracks
        for track_id, track in self.tracks.items():
            if len(detections) == 0:
                continue
            dists = np.linalg.norm(detections - track["pos"], axis=1)
            idx = np.argmin(dists)
            if dists[idx] < self.max_distance and idx not in assigned:
                new_pos = detections[idx]
                assigned.add(idx)
                updated_tracks[track_id] = {"pos": new_pos}
            # else: track disappears

        # Step 2: create new tracks for unassigned detections
        for i, det in enumerate(detections):
            if i in assigned:
                continue
            updated_tracks[self.next_id] = {"pos": det}
            self.next_id += 1

        self.tracks = updated_tracks
        return [(tid, t["pos"][0], t["pos"][1]) for tid, t in self.tracks.items()]
