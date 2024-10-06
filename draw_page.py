import tkinter as tk
from tkinter import colorchooser, simpledialog

class DrawingApp: 
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.canvas = tk.Canvas(self.frame, width=400, height=400)
        self.canvas.pack()

        self.isdrawing = False
        self.start_x = 0
        self.start_y = 0

        self.line_width = 1
        self.line_color = "black"
        self.fill_color = "black"  # Default fill color
    
    def draw_menu(self):
        menubar = tk.Menu(self.root)
        
        shape_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Shape", menu=shape_menu)
        shape_menu.add_command(label="Draw freely", command=self.enable_free_draw)
        shape_menu.add_command(label="Draw line", command=self.draw_straight_line)
        shape_menu.add_command(label="Draw triangle", command=self.draw_triangle)
        shape_menu.add_command(label="Draw rectangle", command=self.draw_rectangle)
        shape_menu.add_command(label="Draw circle", command=self.draw_circle)

        options_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Choose drawing color", command=self.choose_color)
        options_menu.add_command(label="Choose drawing line width", command=self.choose_line_width)

        menubar.add_command(label="Clear canvas", command=self.clear_canvas)

        self.root.config(menu=menubar)

    # Function to draw lines
    def start_drawing(self, event):
        self.isdrawing = True
        self.start_x = event.x
        self.start_y = event.y

    def draw(self, event):
        if self.isdrawing:
            x = event.x
            y = event.y
            self.canvas.create_line(self.start_x, self.start_y, x, y, width=self.line_width, fill=self.line_color)
            self.start_x = x
            self.start_y = y

    def stop_drawing(self, event):
        self.isdrawing = False

    def enable_free_draw(self):
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    # Function to draw straight line
    def draw_straight_line(self):
        self.canvas.bind("<Button-1>", self.draw_straight_line_start)

    def draw_straight_line_start(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.canvas.bind("<Button-1>", self.draw_straight_line_end)

    def draw_straight_line_end(self, event):
        end_x = event.x
        end_y = event.y
        self.canvas.create_line(self.start_x, self.start_y, end_x, end_y, width=self.line_width, fill=self.line_color)
        # Unbind the canvas to stop drawing straight lines after one line is drawn
        self.canvas.unbind("<Button-1>")

    # Function to draw triangle
    def draw_triangle(self):
        self.canvas.bind("<Button-1>", self.draw_triangle_start)

    def draw_triangle_start(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.canvas.bind("<Button-1>", self.draw_triangle_end)

    def draw_triangle_end(self, event):
        end_x = event.x
        end_y = event.y
        self.canvas.create_polygon(self.start_x, self.start_y, end_x, end_y, self.start_x, end_y, outline=self.line_color, width=self.line_width, fill=self.fill_color)

    # Function to draw rectangle 
    def draw_rectangle(self):
        self.canvas.bind("<Button-1>", self.draw_rectangle_start)

    def draw_rectangle_start(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.canvas.bind("<Button-1>", self.draw_rectangle_end)

    def draw_rectangle_end(self, event):
        end_x = event.x
        end_y = event.y
        self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline=self.line_color, width=self.line_width)

    # Function to draw circle
    def draw_circle(self):
        self.canvas.bind("<Button-1>", self.draw_circle_center)

    def draw_circle_center(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.canvas.bind("<Button-1>", self.draw_circle_radius)

    def draw_circle_radius(self, event):
        end_x = event.x
        end_y = event.y
        radius = ((end_x - self.start_x)**2 + (end_y - self.start_y)**2)**0.5
        self.canvas.create_oval(self.start_x - radius, self.start_y - radius, self.start_x + radius, self.start_y + radius, outline=self.line_color, width=self.line_width, fill=self.fill_color)

    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.line_color)
        if color:
            self.line_color = color[1]
            self.fill_color = color[1]  # Update fill color with the chosen color

    def choose_line_width(self):
        width = simpledialog.askinteger("Choose the line", "Enter how large it is?")
        if width:
            self.line_width = width

    def clear_canvas(self):
        self.canvas.delete("all")
