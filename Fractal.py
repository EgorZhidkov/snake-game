from tkinter import Tk, Canvas

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
COUNT_OF_SEGMENT = []


class snake_draw(object):
    length = 3
    count_of_segment = []
    colour = 'red'
    start_position_of_x = 290
    start_position_of_y = 310
    part_in_snake = 10

    def __init__(self, start_position_of_x1, start_position_of_y1, start_position_of_x2, start_position_of_y2,
                 part_in_snake):
        count = 0
        for i in range(3):
            if count == 0:
                self.instance = c.create_rectangle(start_position_of_x1, start_position_of_y1, start_position_of_x2,
                                                   start_position_of_y2, fill="red")
                count = 1
                COUNT_OF_SEGMENT.append(c)
            else:
                self.instance = c.create_rectangle(start_position_of_x1, start_position_of_y1 + part_in_snake,
                                                   start_position_of_x2,
                                                   start_position_of_y2 + part_in_snake, fill="red")
                COUNT_OF_SEGMENT.append(c)
                start_position_of_y1 += part_in_snake
                start_position_of_y2 += part_in_snake
    def move(self):


root = Tk()
root.title("PythonicWay Snake")
c = Canvas(root, width=600, height=600, bg="#003300")
c.grid()
c.focus_set()
snake = snake_draw(290, 290, 310, 310, 20)
print(COUNT_OF_SEGMENT[0])
root.mainloop()
