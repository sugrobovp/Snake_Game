from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.last = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.speed(1)
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.segments[0].forward(20)

    def turn_north(self):
        self.segments[0].setheading(90)

    def turn_south(self):
        self.segments[0].setheading(270)

    def turn_east(self):
        self.segments[0].setheading(0)

    def turn_west(self):
        self.segments[0].setheading(180)

    def grow(self):
        new_segment = Turtle('square')
        new_segment.speed(1)
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.last.pos() + (0.01, 0.01))
        self.segments.append(new_segment)

    def get_positions(self):
        positions = []
        for seg in self.segments:
            positions.append(seg.pos())
        return positions

    def no_intersections(self):
        positions = self.get_positions()
        for pos in positions:
            if positions.count(pos) > 1:
                return False
        return True






