import numpy as np

class Tracker:
    def __init__(self):
        self.tracks = []

    def update_tracks(self, targets):
        self.tracks = []
        for target in targets:
            prediction = {
                'x': target['x'] + target['vx'] * 5,  # Memperkirakan posisi masa depan
                'y': target['y'] + target['vy'] * 5,
                'type': target['type']
            }
            self.tracks.append(prediction)
        return self.tracks
