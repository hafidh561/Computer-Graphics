from graphics import *
from tkinter import messagebox


class Circle:
    def __init__(self, center, radius):
        self.window = (1024, 768)
        self.x_center = center[0] + self.window[0] / 2
        self.y_center = center[1] + self.window[1] / 2
        self.radius = radius * 100

        # Create Window
        self.win = GraphWin("Circle", self.window[0], self.window[1])
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

    def circle_plot_point(self, x, y):
        pt = Point(self.x_center + x, self.y_center + y)
        pt.setFill("white")
        pt.draw(self.win)
        pt = Point(self.x_center - x, self.y_center + y)
        pt.setFill("white")
        pt.draw(self.win)
        pt = Point(self.x_center + x, self.y_center - y)
        pt.setFill("white")
        pt.draw(self.win)
        pt = Point(self.x_center - x, self.y_center - y)
        pt.setFill("white")
        pt.draw(self.win)
        pt = Point(self.x_center + y, self.y_center + x)
        pt.setFill("white")
        pt.draw(self.win)
        pt = Point(self.x_center - y, self.y_center + x)
        pt.setFill("white")
        pt.draw(self.win)
        pt = Point(self.x_center + y, self.y_center - x)
        pt.setFill("white")
        pt.draw(self.win)
        pt = Point(self.x_center - y, self.y_center - x)
        pt.setFill("white")
        pt.draw(self.win)

    def draw_circle_midpoint(self):
        x = 0
        y = self.radius
        p = 1 - self.radius
        self.circle_plot_point(x, y)
        while x < y:
            x += 1
            if p < 0:
                p += 2*x + 1
            else:
                y -= 1
                p += 2*(x-y) + 1
            self.circle_plot_point(x, y)

        self.show_message_box()

    def draw_circle_bresenham(self):
        x = 0
        y = self.radius
        d = 3 - 2*self.radius
        while y >= x:
            self.circle_plot_point(x, y)
            x += 1
            if d > 0:
                y -= 1
                d = d + 4*(x-y) + 10
            else:
                d = d + 4*x + 6
            self.circle_plot_point(x, y)

        self.show_message_box()
