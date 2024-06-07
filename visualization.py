import pygame

class Visualization:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def draw(self, targets, tracks, interceptors):
        self.screen.fill((0, 0, 0))
        for target in targets:
            color = (255, 0, 0) if target['type'] == 'rudal' else (0, 255, 0)
            pygame.draw.circle(self.screen, color, (int(target['x']), int(target['y'])), 5)
        for track in tracks:
            pygame.draw.circle(self.screen, (0, 0, 255), (int(track['x']), int(track['y'])), 5, 1)
        for interceptor in interceptors:
            pygame.draw.circle(self.screen, (255, 255, 255), (int(interceptor['x']), int(interceptor['y'])), 3)
        pygame.display.flip()
        self.clock.tick(30)
