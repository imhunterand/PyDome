class Interceptor:
    def __init__(self, interception_speed, detection_range):
        self.interception_speed = interception_speed
        self.detection_range = detection_range
        self.interceptors = []

    def launch_interceptor(self, track):
        interceptor = {
            'x': 400,
            'y': 300,
            'vx': (track['x'] - 400) / self.interception_speed,
            'vy': (track['y'] - 300) / self.interception_speed
        }
        self.interceptors.append(interceptor)

    def update_interceptors(self):
        for interceptor in self.interceptors:
            interceptor['x'] += interceptor['vx']
            interceptor['y'] += interceptor['vy']
        return self.interceptors
