from graphics import *
from tkinter import messagebox


class Line:
    def __init__(self, coordinate1, coordinate2):
        self.window = (1024, 768)

        self.x1 = int((coordinate1[0] * 30) + self.window[0] / 2)
        self.y1 = int((coordinate1[1] * 30) + self.window[1] / 2)

        self.x2 = int((coordinate2[0] * 30) + self.window[0] / 2)
        self.y2 = int((coordinate2[1] * 30) + self.window[1] / 2)

        self.x = []
        self.y = []

        # Create Window
        self.win = GraphWin("Line", self.window[0], self.window[1])
        self.win.setBackground("Black")

        # Set Text
        self.message = Text(Point(512, 700), "Drawing Process")
        self.message.setSize(30)
        self.message.setTextColor("White")
        self.message.draw(self.win)

    def show_message_box(self):
        # Rename Text
        self.message.setText("Done")
        messagebox.showinfo("Info", "Drawing Done")
        self.win.getMouse()
        self.win.close()

    def draw_line_normal(self):
        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1
        y = self.y1

        try:
            y_inc = (delta_y / delta_x)
        except ZeroDivisionError:
            self.x1, self.x2 = self.y1, self.y2
            for x in range(self.x1, self.x2 + 1):
                pt = Point(round(y), round(x))
                pt.setFill("white")
                pt.draw(self.win)
            self.show_message_box()

        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1

        for x in range(self.x1, self.x2 + 1):
            pt = Point(round(x), round(y))
            pt.setFill("white")
            pt.draw(self.win)
            y += y_inc
        self.show_message_box()

    def draw_line_dda(self):
        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1
        step = abs(delta_y) if abs(delta_y) > abs(delta_x) else abs(delta_x)
        x_inc = delta_x / step
        y_inc = delta_y / step
        x = self.x1
        y = self.y1

        if self.x1 == self.x2:
            self.x1, self.x2 = self.y1, self.y2
        elif self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1

        for _ in range(self.x1, self.x2 + 1):
            pt = Point(round(x), round(y))
            pt.setFill("white")
            pt.draw(self.win)
            x += abs(x_inc)
            y += abs(y_inc)

        self.show_message_box()

    def draw_line_bresenham(self):
        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1
        p = (2*delta_y) - delta_x
        y = self.y1

        if self.x1 == self.x2:
            self.x1, self.x2 = self.y1, self.y2
        elif self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1

        for x in range(self.x1, self.x2 + 1):
            pt = Point(x, y)
            pt.setFill("white")
            pt.draw(self.win)
            if p <= 0:
                p += 2*delta_y
            else:
                p += 2*(delta_y - delta_x)
                y += 1

        self.show_message_box()
