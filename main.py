# Import statements
import turtle
import random
import math

# Set screen and backround
screen = turtle.Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("lightblue")

# Set multiple turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for color in colors:
  t = turtle.Turtle()
  t.shape("turtle")
  t.color(color)
  t.pendown()
  t.speed(0)
  t.goto(random.randint(-300, 300), random.randint(-300, 300))
  turtles.append(t)

# Set collition detection
def collision(t1, t2):
  distance = math.sqrt((t1.xcor() - t2.xcor())** 2 + (t1.ycor() - t2.ycor())**2)
  return distance < 30

# Set turtle movement at random speeds
def move(t):
  speed = random.randint(1, 5)
  t.forward(speed)

  # Setting boundary limits
  try:
      x, y = t.position()
      if x < -300 or x > 300 or y < -300 or y > 300:
        t.setheading(random.randint(0, 360))

  except turtle.Terminator:
    print("\nProgram terminated by user.")
    quit()

# Main loop
try:
    while True:
      for i in range(len(turtles)):
        move(turtles[i])
    
        for j in range(i + 1, len(turtles)):
          if collision(turtles[i], turtles[j]):
            turtles[i].setheading(random.randint(0, 360))
            turtles[j].setheading(random.randint(0, 360))
    
except turtle.Terminator:
  print("\nProgram Terminated")



