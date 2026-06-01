import turtle

class bloky:
    def __init__(self, x, y):
        self.shape = turtle.Turtle()
        self.shape.shape("square")
        self.shape.color("red")
        self.shape.penup()
        self.shape.shapesize(stretch_wid=2, stretch_len=3)
        self.shape.goto(x, y)
        
        self.block_width = 60
        self.block_height = 40

class MovingBlock(bloky):
    def __init__(self, x, y, speed):
        super().__init__(x, y)
        self.speed = speed 
        self.direction = 1
        
    def pohybzestranynastranu(self, sirka_obrazovky):
        new_x = self.shape.xcor() + (self.speed * self.direction)
        
        right_edge = (sirka_obrazovky / 2) - (self.block_width / 2)
        left_edge = -(sirka_obrazovky / 2) + (self.block_width / 2)
        
        if new_x > right_edge:
            self.direction = -1
        elif new_x < left_edge:
            self.direction = 1
            
        self.shape.setx(new_x)