import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

tree = [
    "      *      ",
    "     ***     ",
    "    *****    ",
    "   *******   ",
    "  *********  ",
    " *********** ",
    "*************",
    "     |||     "
]

lyrics = [
    "A face-on lover",
    "With a fire in his heart",
    "A man undercover",
    "But you tore me apart",
    "",
    "oh-ooh",
    "",
    "Now I've found a real love,",
    "you'll never fool me again"
]

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

lyric_pen = turtle.Turtle()
lyric_pen.hideturtle()
lyric_pen.penup()

def draw_tree():
    pen.clear()
    start_x = -300
    start_y = 200
    
    for i, line in enumerate(tree):
        current_x = start_x
        current_y = start_y - (i * 25)
        
        for char in line:
            pen.goto(current_x, current_y)
            if char == "*":
                pen.color(random.choice(colors))
            else:
                pen.color('white')
            pen.write(char, font=('Courier', 20, 'bold'))
            current_x += 15
            
    screen.update()
    screen.ontimer(draw_tree, 130)

line_index = 0
char_index = 0

def type_lyrics():
    global line_index, char_index
    
    if line_index < len(lyrics):
        line = lyrics[line_index]
        
        if char_index < len(line):
            char = line[char_index]
            x = -50 + (char_index * 12)
            y = 180 - (line_index * 30)
            
            lyric_pen.goto(x, y)
            lyric_pen.color(random.choice(colors))
            lyric_pen.write(char, font=('Courier', 14, 'bold'))
            
            char_index += 1
            screen.ontimer(type_lyrics, 120)
        else:
            line_index += 1
            char_index = 0
            screen.ontimer(type_lyrics, 120)

draw_tree()
type_lyrics()

screen.mainloop()
