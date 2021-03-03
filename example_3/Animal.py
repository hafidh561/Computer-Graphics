import pygame


class Animal:
    def __init__(self):
        self.window = (600, 600)
        self.caption = "Animal"
        self.display = pygame.display.set_mode(self.window)
        self.running = True

    def run(self):
        # Intiliazie PyGame
        pygame.init()
        display = self.display
        pygame.display.set_caption(self.caption)

        # Run PyGame
        while self.running:
            display.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            # Create Animal
            self.draw_animal()

            # Update Animal
            pygame.display.update()

    def draw_animal(self):
        # Body
        pygame.draw.circle(
            self.display,
            (3, 107, 183, 255),
            (int(self.window[0] / 2), int(self.window[1] / 2)),
            100,
        )

        # Leg Left
        pygame.draw.rect(
            self.display, (3, 107, 183, 255), pygame.Rect(240, 370, 20, 100)
        )

        # Leg Right
        pygame.draw.rect(
            self.display, (3, 107, 183, 255), pygame.Rect(340, 370, 20, 100)
        )

        # Head
        pygame.draw.ellipse(
            self.display,
            (3, 107, 183, 255),
            pygame.Rect(256, 160, 90, 170),
        )
        pygame.draw.ellipse(
            self.display, (255, 255, 255, 255), pygame.Rect(256, 160, 90, 170), 2
        )

        # Eye Left
        pygame.draw.ellipse(
            self.display,
            (255, 255, 255, 255),
            pygame.Rect(274, 220, 20, 30),
        )
        surface = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (82, 14, 15, 255),
            pygame.Rect(0, 0, 10, 15),
        )
        surface = pygame.transform.rotate(surface, -20)
        self.display.blit(surface, (277, 234))

        # Eye Right
        pygame.draw.ellipse(
            self.display,
            (255, 255, 255, 255),
            pygame.Rect(309, 220, 20, 30),
        )
        surface = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (82, 14, 15, 255),
            pygame.Rect(0, 0, 10, 15),
        )
        surface = pygame.transform.rotate(surface, 20)
        self.display.blit(surface, (310, 230))

        # Mouth
        pygame.draw.ellipse(
            self.display,
            (255, 0, 0, 255),
            pygame.Rect(290, 290, 24, 20),
        )
        pygame.draw.ellipse(
            self.display, (0, 0, 0, 255), pygame.Rect(290, 290, 24, 20), 2
        )

        # Nose
        pygame.draw.circle(
            self.display,
            (255, 0, 0, 255),
            (298, 270),
            2,
        )
        pygame.draw.circle(
            self.display,
            (255, 0, 0, 255),
            (305, 270),
            2,
        )

        # Ear Left
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (3, 107, 183, 255),
            pygame.Rect(0, 0, 50, 15),
        )
        surface = pygame.transform.rotate(surface, 42)
        self.display.blit(surface, (225, 144))

        # Ear Right
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (3, 107, 183, 255),
            pygame.Rect(0, 0, 50, 15),
        )
        surface = pygame.transform.rotate(surface, -42)
        self.display.blit(surface, (274, 179))

        # Horn Left
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (0, 0, 0, 255),
            pygame.Rect(0, 0, 12, 6),
        )
        surface = pygame.transform.rotate(surface, -50)
        self.display.blit(surface, (210, 152))

        # Horn Right
        surface = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        surface = surface.convert_alpha()
        pygame.draw.ellipse(
            surface,
            (0, 0, 0, 255),
            pygame.Rect(0, 0, 12, 6),
        )
        surface = pygame.transform.rotate(surface, 50)
        self.display.blit(surface, (310, 85))