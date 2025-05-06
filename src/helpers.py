class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point at ({self.x},{self.y})"

class Line():
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self,canvas,fill_color):
        canvas.create_line(self.point1.x,self.point1.y,self.point2.x,self.point2.y,fill=fill_color,width=2)

class Cell():
    def __init__(self,x1,y1,x2,y2,window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._top_left_point, self._top_right_point, self._bottom_left_point,self._bottom_right_point = Point(x1,y1), Point(x2,y1), Point(x1,y2), Point(x2,y2)
        self._win = window

    def draw(self):
        # If no window is provided, nothing to draw return.
        if not self._win:
            return
        # Colors for showing and hiding lines.
        show_line_color = 'black'
        hide_line_color = 'white'
        
        # Left Wall Portion
        correct_color = show_line_color if self.has_left_wall else hide_line_color
        self._win.draw_line(Line(self._top_left_point,self._bottom_left_point),correct_color)
        # Right Wall Portion
        correct_color = show_line_color if self.has_right_wall else hide_line_color
        self._win.draw_line(Line(self._top_right_point,self._bottom_right_point),correct_color)
        # Top Wall Portion
        correct_color = show_line_color if self.has_top_wall else hide_line_color
        self._win.draw_line(Line(self._top_left_point,self._top_right_point),correct_color)
        # Bottom Wall Portion
        correct_color = show_line_color if self.has_bottom_wall else hide_line_color
        self._win.draw_line(Line(self._bottom_left_point,self._bottom_right_point),correct_color)

    def draw_move(self,to_cell,undo=False):
        if undo:
            line_color = 'red'
        else:
            line_color = 'gray'
        #line_color = 'red' if undo else line_color = 'gray'
        self_center = Point((self._x1 + self._x2) / 2,(self._y1 + self._y2) / 2)
        to_center = Point((to_cell._x1 + to_cell._x2) / 2,(to_cell._y1 + to_cell._y2) / 2)
        self._win.draw_line(Line(self_center,to_center),line_color)