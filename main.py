import pygame
from radar import Radar
from tracking import Tracker
from interception import Interceptor
from visualization import Visualization
from settings import Settings

def main():
    settings = Settings()
    radar = Radar(detection_range=settings.detection_range)
    tracker = Tracker()
    interceptor = Interceptor(interception_speed=settings.interception_speed, detection_range=settings.detection_range)
    visualization = Visualization()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        targets = radar.detect_targets()
        tracks = tracker.update_tracks(targets)
        if len(interceptor.interceptors) < settings.interceptor_limit:
            for track in tracks:
                if track['type'] == settings.target_priority:
                    interceptor.launch_interceptor(track)
                    break  # Hanya meluncurkan satu interseptor per siklus untuk target prioritas
        interceptors = interceptor.update_interceptors()

        visualization.draw(targets, tracks, interceptors)

    pygame.quit()

if __name__ == "__main__":
    main()
