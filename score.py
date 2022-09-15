from turtle import Turtle


class Score:
    def __init__(self):
        self.score = 0
        self.segment = []

    def appear(self):
        segment = Turtle(visible=False)
        segment.goto(-280, 280)
        segment.color('white')
        text = 'Score: {0}'.format(self.score)
        segment.write(text)
        self.segment.append(segment)

    def change(self):
        self.score += 1

    def clearing(self):
        self.segment[0].clear()
        self.segment.clear()
