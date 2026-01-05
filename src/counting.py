# src/counting.py
class LineCounter:
    def __init__(self, line_x=0.0):
        self.line_x = line_x
        self.last_positions = {}   # id -> last_x
        self.count_lr = 0          # left -> right
        self.count_rl = 0          # right -> left

    def update(self, tracked_objects):
        """
        tracked_objects: list of (id, x, y)
        """
        for tid, x, y in tracked_objects:
            if tid in self.last_positions:
                prev_x = self.last_positions[tid]
                # crossing left -> right
                if prev_x < self.line_x and x >= self.line_x:
                    self.count_lr += 1
                # crossing right -> left
                elif prev_x > self.line_x and x <= self.line_x:
                    self.count_rl += 1
            self.last_positions[tid] = x

        return self.count_lr, self.count_rl
