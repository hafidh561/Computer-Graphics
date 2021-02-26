import pygame
from pygame import gfxdraw


class Polygon:
    def __init__(self, vertices):
        self.height, self.width = 800, 600
        self.caption = "Polygon"
        self.vertices = [(i[0] * 30 + 200, i[1] * 30 + 100) for i in vertices]
        self.display = pygame.display.set_mode((self.height, self.width))
        self.running = True

    def run_boundary_fill(self):
        # Intiliazie PyGame
        print(self.vertices)
        pygame.init()
        display = self.display
        pygame.display.set_caption(self.caption)

        # Run PyGame
        while self.running:
            display.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            # Create Polygon
            self.draw_polygon()

            # Boundary Fill
            self.boundary_fill(
                400,
                200,
                (255, 0, 0, 255),
                (255, 255, 255, 255),
            )

            # Update Polygon
            pygame.display.update()

    def run_scan_line(self):
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

            # Create Polygon
            self.draw_polygon()

            # Boundary Fill
            self.scan_line(
                (255, 0, 0, 255),
                (255, 255, 255, 255),
            )

            # Update Polygon
            pygame.display.update()

    def draw_polygon(self):
        pygame.draw.polygon(self.display, (255, 255, 255, 255), self.vertices, 1)

    def scan_line(self, fillcol, boundcol):
        get = list()
        y_max = 0
        y_min = 0
        y_always_max = 0
        y_always_min = 0
        xy_min = 0

        # Search GET
        for i, x in enumerate(self.vertices):
            if i == len(self.vertices) - 1:
                break
            else:
                if x[1] > self.vertices[i + 1][1]:
                    y_max = x[1]
                else:
                    y_max = self.vertices[i + 1][1]

                if x[1] < self.vertices[i + 1][1]:
                    y_min = x[1]
                    xy_min = x[0]
                else:
                    y_min = self.vertices[i + 1][1]
                    xy_min = self.vertices[i + 1][0]

                slope = (self.vertices[i + 1][0] - x[0]) / (
                    self.vertices[i + 1][1] - x[1]
                )

                if y_always_max < y_max:
                    y_always_max = y_max

                if i == 0:
                    y_always_min = y_min
                else:
                    if y_always_max > y_min:
                        y_always_min = y_min

                get.append((y_max, xy_min, slope))

        # Sort GET
        get_new = [[None]] * (y_always_max + 1)
        for i, x in enumerate(self.vertices):
            if i == len(self.vertices) - 1:
                break
            if x[1] < self.vertices[i + 1][1]:
                if get_new[x[1]][0] is None:
                    get_new[x[1]] = [list(get[i])]
                else:
                    get_new[x[1]].append(list(get[i]))
            elif x[1] > self.vertices[i + 1][1]:
                if get_new[x[1]][0] is None:
                    get_new[self.vertices[i + 1][1]] = [list(get[i])]
                else:
                    get_new[self.vertices[i + 1][1]].append(list(get[i]))

        # Choose AET and Change Value Variable
        y_min = y_always_min
        y_max = y_always_max
        aet = None
        get = get_new.copy()
        if get[y_min][0][1] >= get[y_min][1][1]:
            aet = [get[y_min][1], get[y_min][0]]
        else:
            aet = [get[y_min][0], get[y_min][1]]
        left = aet[0][1]
        right = aet[1][1]

        # Draw First Pixel in y_min
        self.draw_pixel(left, right, y_min, fillcol)

        # Draw Untill y == y_max
        for y in range(y_min + 1, y_max + 1):

            # Change AET With New GET and Draw Pixel
            if y == aet[0][0] and y == aet[1][0]:
                try:
                    aet[0] = get[y][0]
                    aet[1] = get[y][0]
                    left = aet[0][0]
                    right = aet[0][0]
                except:
                    break
                self.draw_pixel(left, right, y)
                continue
            elif y == aet[0][0]:
                aet[0] = get[y][0]
                if round(aet[0][1]) >= round(right + aet[1][2]):
                    left = right + aet[1][2]
                    right = aet[0][1]
                else:
                    left = aet[0][1]
                    right = right + aet[1][2]
                self.draw_pixel(left, right, y, fillcol)
                continue
            elif y == aet[1][0]:
                aet[1] = get[y][0]
                if round(left + aet[0][2]) >= round(aet[1][1]):
                    left = aet[1][1]
                    right = left + aet[0][2]
                else:
                    left = left + aet[0][2]
                    right = aet[1][1]
                self.draw_pixel(left, right, y, fillcol)
                continue

            # Choose left side and right side of x
            if round(left + (aet[0][2])) >= round(right + (aet[1][2])):
                left = right + (aet[1][2])
                right = left + (aet[0][2])
            else:
                left = left + (aet[0][2])
                right = right + (aet[1][2])

            # Draw Pixel
            self.draw_pixel(left, right, y, fillcol)

    def draw_pixel(self, left, right, y, fillcol):
        for x in range(round(left), round(right) + 1):
            gfxdraw.pixel(
                self.display,
                x,
                y,
                fillcol,
            )

    def boundary_fill(self, x, y, fillcol, boundcol):
        currcol = self.display.get_at((x, y))
        if currcol != boundcol and currcol != fillcol:
            gfxdraw.pixel(self.display, x, y, fillcol)
            self.fill_circle(x + 1, y, fillcol, boundcol)
            self.fill_circle(x, y + 1, fillcol, boundcol)
            self.fill_circle(x - 1, y, fillcol, boundcol)
            self.fill_circle(x, y - 1, fillcol, boundcol)
