from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
# tim = Turtle()
# tim.write((0,0), True)
# tim.write(arg="hello")
# screen = Screen()
# screen.exitonclick()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.readfile()
        # self.pensize(50)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        # self.write(arg=f"Score = {self.score}", move=False, align="center")
        self.display()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.writefile()
        self.score = 0
        self.display()

    def writefile(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def readfile(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def inc_score(self):
        self.score += 1

    def display(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}", move=False, align=ALIGNMENT,font=FONT)
