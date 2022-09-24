from turtle import Turtle


class Score:
    def __init__(self):
        self.score = 0
        self.segment = []
        self.max_score = 0

    def appear(self):
        segment = Turtle(visible=False)
        segment.goto(-280, 280)
        segment.color('white')
        text = 'Score: {0}, max score {1}'.format(self.score, self.max_score)
        segment.write(text)
        self.segment.append(segment)

    def change(self):
        self.score += 1

    def update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score

    def clearing(self):
        self.segment[0].clear()
        self.segment.clear()
