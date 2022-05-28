import tkinter as tk
from tkinter import ttk
from random import randint

class SortApp(tk.Tk):

    lines = []

    def __init__(self):
        super().__init__()
        self.maxsize(600, 600)
        self.title('Sort App')

        self.alg = tk.StringVar()

        # defining sort algorythms and functions
        self.options = {
            "Bubble sorting":self.bubble_sort, 
            "Selection sorting":self.selection_sort,
            "Insertion sorting":self.insertion_sort,
            "Heap sorting":self.heap_sort
        }

        self.canvas = tk.Canvas(self, width=600, height=400, bg="white")
        self.canvas.pack()

        # menu elements
        frame = tk.Frame(self, width=600, height=100, bg="white")
        frame.pack(side='bottom')
        tk.Label(frame, text="Choose algorythm:", bg='white').pack(side='left', pady=10)
        self.menu = ttk.Combobox(frame, textvariable=self.alg, values=[_ for _ in self.options.keys()])
        self.menu.pack(pady=10, padx=5, side='left')    
        tk.Button(frame, text="Start", bg="green", command=self.start).pack(side='right', pady=10, padx=10, ipadx=10)

    def generate_lines(self):
        """Genetanes and redraws random-sized lines on the canvas"""
        self.lines = []
        for _ in range(120):
            self.lines.append(randint(1, 400))
        self.redraw(self.lines, ['black' for x in range(len(self.lines))])


    def redraw(self, lines, colors):
        """Redrawing lines on the canvas"""

        self.canvas.delete("all")
        can_height = 400
        line_width = 5

        for i, line_height in enumerate(lines):
            x0 = i*line_width
            y0 = can_height
            x1 = ((i+1)*line_width)
            y1 = can_height - line_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i], outline=colors[i])
        self.update_idletasks()


    def bubble_sort(self, lines):
        n = len(lines)
        
        for i in range(n-1):
            for j in range(i+1, n):
                if lines[j] < lines[i]:
                    lines[j], lines[i] = lines[i], lines[j]
                    colors = ['green' if x == i else 'black' for x in range(len(lines))]
                    colors[j] = 'red'
                    self.redraw(lines, colors)
            
        self.redraw(lines, ['black' for x in range(len(lines))])

    def selection_sort(self, lines):
        n = len(lines)

        for i in range(n):
            lowest_value_index = i
            for j in range(i + 1, n):
                if lines[j] < lines[lowest_value_index]:
                    lowest_value_index = j
            lines[i], lines[lowest_value_index] = lines[lowest_value_index], lines[i]
            colors = ['green' if x == i else 'black' for x in range(len(lines))]
            colors[lowest_value_index] = 'red'
            self.redraw(lines, colors)
        
        self.redraw(lines, ['black' for x in range(len(lines))])

    def insertion_sort(self, lines):

        for i in range(1, len(lines)):
            item_to_insert = lines[i]
            j = i - 1
            while j >= 0 and lines[j] > item_to_insert:
                lines[j + 1] = lines[j]
                j -= 1
                colors = ['green' if x == j else 'black' for x in range(len(lines))]
                colors[i] = 'red'
                self.redraw(lines, colors)
            lines[j + 1] = item_to_insert
        
        self.redraw(lines, ['black' for x in range(len(lines))])

    def heapify(self, lines, heap_size, root_index):

        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and lines[left_child] > lines[largest]:
            largest = left_child
        if right_child < heap_size and lines[right_child] > lines[largest]:
            largest = right_child
        if largest != root_index:
            lines[root_index], lines[largest] = lines[largest], lines[root_index]
            colors = ['green' if x == root_index else 'black' for x in range(len(lines))]
            colors[largest] = 'red'
            self.redraw(lines, colors)
            self.heapify(lines, heap_size, largest)


    def heap_sort(self, lines):

        n = len(lines)
        
        for i in range(n, -1, -1):
            self.heapify(lines, n, i)

        for i in range(n - 1, 0, -1):
            lines[i], lines[0] = lines[0], lines[i]
            self.redraw(lines, ['yellow' if x == i else 'black' for x in range(len(lines))])
            self.heapify(lines, i, 0)
        self.redraw(lines, ['black' for x in range(len(lines))])


    def start(self):
        self.generate_lines()
        self.options[self.menu.get()](self.lines)


# class Line():
#     def __init__(self, color) -> None:
#         self.color = color
#         self.size = randint(50, 350)


if __name__ == '__main__':
    app = SortApp()
    app.mainloop()