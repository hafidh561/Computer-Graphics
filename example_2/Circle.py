import pygame
from pygame import gfxdraw


class Circle:
    def __init__(self, center, radius):
        self.height, self.width = 800, 600
        self.caption = "Circle"
        self.x_center = center[0] + int(self.height / 2)
        self.y_center = center[1] + int(self.width / 2)
        self.radius = radius * 20
        self.display = pygame.display.set_mode((self.height, self.width))
        self.running = True

    def run(self):
        # Intiliazie PyGame
        pygame.init()
        display = self.display
        pygame.display.set_caption(self.caption)

        # Run PyGame
        while self.running:
            display.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            # Create Circle
            self.draw_circle()

            # Fill Circle
            self.fill_circle(
                self.x_center, self.y_center, (255, 0, 0, 255), (255, 255, 255, 255)
            )

            # Update Circle
            pygame.display.update()

    def circle_plot_point(self, x, y):
        gfxdraw.pixel(
            self.display, self.x_center + x, self.y_center + y, (255, 255, 255)
        )
        gfxdraw.pixel(
            self.display, self.x_center - x, self.y_center + y, (255, 255, 255)
        )
        gfxdraw.pixel(
            self.display, self.x_center + x, self.y_center - y, (255, 255, 255)
        )
        gfxdraw.pixel(
            self.display, self.x_center - x, self.y_center - y, (255, 255, 255)
        )
        gfxdraw.pixel(
            self.display, self.x_center + y, self.y_center + x, (255, 255, 255)
        )
        gfxdraw.pixel(
            self.display, self.x_center - y, self.y_center + x, (255, 255, 255)
        )
        gfxdraw.pixel(
            self.display, self.x_center + y, self.y_center - x, (255, 255, 255)
        )
        gfxdraw.pixel(
            self.display, self.x_center - y, self.y_center - x, (255, 255, 255)
        )

    def draw_circle(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        self.circle_plot_point(x, y)
        while x < y:
            x += 1
            if p < 0:
                p += 2 * x + 1
            else:
                y -= 1
                p += 2 * (x - y) + 1
            self.circle_plot_point(x, y)

    def fill_circle(self, x, y, fillcol, boundcol):
        currcol = self.display.get_at((x, y))
        if currcol != boundcol and currcol != fillcol:
            gfxdraw.pixel(self.display, x, y, fillcol)
            self.fill_circle(x + 1, y, fillcol, boundcol)
            self.fill_circle(x, y + 1, fillcol, boundcol)
            self.fill_circle(x - 1, y, fillcol, boundcol)
            self.fill_circle(x, y - 1, fillcol, boundcol)
