import random

class Radar:
    def __init__(self, detection_range):
        self.detection_range = detection_range
        self.targets = []

    def detect_targets(self):
        # Menghasilkan target secara acak untuk simulasi
        if random.random() < 0.1:  # 10% kemungkinan mendeteksi target baru setiap tick
            new_target = {
                'x': random.randint(0, 800),
                'y': random.randint(0, 600),
                'vx': random.uniform(-1, 1),
                'vy': random.uniform(-1, 1),
                'type': random.choice(['rudal', 'pesawat'])
            }
            self.targets.append(new_target)
        return self.targets
