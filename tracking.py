import numpy as np
import logging
import pickle
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter

class Tracker:
    def __init__(self):
        self.tracks = []
        self.filter = KalmanFilter(dim_x=4, dim_z=2)
        self.filter.F = np.array([[1, 1, 0, 0],  # state transition matrix
                                  [0, 1, 0, 0],
                                  [0, 0, 1, 1],
                                  [0, 0, 0, 1]])
        self.filter.H = np.array([[1, 0, 0, 0],  # measurement function
                                  [0, 0, 1, 0]])
        self.filter.P *= 1000.  # covariance matrix
        self.filter.R = 5  # state uncertainty
        self.filter.Q = np.eye(4)  # process uncertainty

        # Setup logging
        logging.basicConfig(filename='tracker.log', level=logging.INFO)

    def predict(self):
        self.filter.predict()

    def update_tracks(self, targets):
        self.tracks = []
        for target in targets:
            self.filter.update([target['x'], target['y']])
            prediction = self.filter.x
            track = {
                'x': prediction[0],
                'y': prediction[2],
                'vx': prediction[1],
                'vy': prediction[3],
                'type': target['type']
            }
            self.tracks.append(track)
            logging.info(f"Updated track: {track}")
        return self.tracks

    def save_state(self, filename='tracker_state.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.tracks, f)

    def load_state(self, filename='tracker_state.pkl'):
        with open(filename, 'rb') as f:
            self.tracks = pickle.load(f)

    def visualize_tracks(self):
        plt.figure()
        for track in self.tracks:
            plt.scatter(track['x'], track['y'], label=f"Type: {track['type']}")
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.title('Tracks Visualization')
        plt.legend()
        plt.show()

# Contoh penggunaan
tracker = Tracker()
targets = [{'x': 10, 'y': 20, 'vx': 1, 'vy': 1, 'type': 'A'}, {'x': 15, 'y': 25, 'vx': -1, 'vy': -1, 'type': 'B'}]
tracker.update_tracks(targets)
tracker.visualize_tracks()
tracker.save_state()
