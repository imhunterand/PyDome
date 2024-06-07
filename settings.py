class Settings:
    def __init__(self):
        self.detection_range = 500
        self.interception_speed = 50
        self.interceptor_limit = 5  # Jumlah maksimum interseptor yang dapat diluncurkan pada satu waktu
        self.target_priority = 'rudal'  # Prioritaskan 'rudal' atau 'pesawat'

    def update_settings(self, detection_range=None, interception_speed=None, interceptor_limit=None, target_priority=None):
        if detection_range:
            self.detection_range = detection_range
        if interception_speed:
            self.interception_speed = interception_speed
        if interceptor_limit:
            self.interceptor_limit = interceptor_limit
        if target_priority:
            self.target_priority = target_priority
