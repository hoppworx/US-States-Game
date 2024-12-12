from turtle import Turtle, Screen

class Location(Turtle):
    def __init__(self, position):
        super().__init__()


    def go_to_state(self, position):
        self.penup()
        self.speed("fastest")
        self.goto(position)