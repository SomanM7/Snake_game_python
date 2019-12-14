## This game is a more difficult game mode of the original snake game. It involves two peices of items which are on the canvas, one is the food for the snake to grow in size and the other, whihc i've called poison, shrinks the snake.
## What makes the game difficult is that they are both the same colour so you have to try your best and aim to eat the correct food item or you'll lose points.
## Another implementation is that after a certain score, your snake will speed up making it harder for the user.
## Good Luck!!


from tkinter import *
import random
import time



def growSnake():
    lastElement = len(snake) - 1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_rectangle(0,0,snakeSize,snakeSize,fill="#FDF3F3"))
    if (direction == "left"):
        canvas.coords(snake[lastElement+1],lastElementPos[0]+snakeSize,lastElementPos[1],lastElementPos[2]+snakeSize,lastElementPos[3])
    elif (direction == "right"):
        canvas.coords(snake[lastElement+1],lastElementPos[0]-snakeSize,lastElementPos[1],lastElementPos[2]-snakeSize,lastElementPos[3])
    elif (direction == "up"):
        canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]+snakeSize,lastElementPos[2],lastElementPos[3]+snakeSize)
    else:
        canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]-snakeSize,lastElementPos[2],lastElementPos[3]-snakeSize)

    global score
    score += 10
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)
        
def shrinkSnake():
    lastElement = len(snake) - 1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.remove(snake[lastElement])

    global score
    score -= 10
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)


    if score <0:
        gameOver = True
        score = 0
        txt = "score:" + str(score)
        canvas.itemconfigure(scoreText, text=txt)
        canvas.create_text(width/2,height/2,fill="white",font="Times 20 italic bold", text="Game Over!")
        sys.exit()
    
def moveFood():
    global food, foodX, foodY
    canvas.move(food, (foodX*(-1)), (foodY*(-1)))
    foodX = random.randint(0,width-snakeSize)
    foodY = random.randint(0,height-snakeSize)
    canvas.move(food, foodX, foodY)

def movePoison():
    global poison, poisonX, poisonY
    canvas.move(poison, (poisonX*(-1)), (poisonY*(-1)))
    poisonX = random.randint(0,width-snakeSize)
    poisonY = random.randint(0,height-snakeSize)
    canvas.move(poison, poisonX, poisonY)
    
def overlapping(a,b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False

def moveSnake():
    canvas.pack()

    positions = []
    positions.append(canvas.coords(snake[0]))
    
    if positions[0][0] < 0:
        canvas.coords(snake[0],width,positions[0][1],width-snakeSize,positions[0][3])
        canvas.pack()
    elif positions[0][2] > width:
        canvas.coords(snake[0],0-snakeSize,positions[0][1],0,positions[0][3])
    elif positions[0][3] > height:
        canvas.coords(snake[0],positions[0][0],0-snakeSize,positions[0][2],0)
    elif positions[0][1] < 0:
        canvas.coords(snake[0],positions[0][0],height,positions[0][2],height-snakeSize)
        
    positions.clear()
    positions.append(canvas.coords(snake[0]))
    print(positions[0])
    
    if direction == "left":
        canvas.move(snake[0], -snakeSize,0)
    elif direction == "right":
        canvas.move(snake[0], snakeSize,0)
    elif direction == "up":
        canvas.move(snake[0], 0,-snakeSize)
    elif direction == "down":
        canvas.move(snake[0], 0,snakeSize)
        
    sHeadPos = canvas.coords(snake[0])
    foodPos = canvas.coords(food)
    poisonPos = canvas.coords(poison)
    if overlapping(sHeadPos, foodPos):
        moveFood()
        growSnake()
        movePoison()
    elif overlapping(sHeadPos, poisonPos):
        movePoison()
        shrinkSnake()
        moveFood()

    for i in range(1,len(snake)):
        if overlapping(sHeadPos, canvas.coords(snake[i])):
            gameOver = True
            canvas.create_text(width/2,height/2,fill="white",font="Times 20 italic bold", text="Game Over!")# get other positions
    for i in range(1,len(snake)):
        positions.append(canvas.coords(snake[i]))# update positions
    for i in range(len(snake)-1):
        canvas.coords(snake[i+1],positions[i][0],positions[i][1],positions[i][2],positions[i][3])
    
    if 'gameOver' not in locals() and len(snake) < 5:
        window.after(40, moveSnake)
    elif 'gameOver' not in locals() and len(snake) >= 5 and len(snake) < 10:
        window.after(30, moveSnake)
    elif 'gameOver' not in locals() and len(snake) >= 10 and len(snake) < 15:
        window.after(20, moveSnake)
    elif 'gameOver' not in locals() and len(snake) >= 15 and len(snake) < 20:
        window.after(10, moveSnake)
    elif 'gameOver' not in locals() and len(snake) >= 20:
        window.after(5, moveSnake)

    
def placeFood():
    global food, foodX, foodY
    food = canvas.create_rectangle(0,0, snakeSize, snakeSize,fill="yellow" )
    foodX = random.randint(0,width-snakeSize)
    foodY = random.randint(0,height-snakeSize)
    canvas.move(food, foodX, foodY)

def placePoison():
    global poison, poisonX, poisonY
    poison = canvas.create_rectangle(0,0, snakeSize, snakeSize,fill="yellow" )
    poisonX = random.randint(0,width-snakeSize)
    poisonY = random.randint(0,height-snakeSize)
    canvas.move(poison, poisonX, poisonY)
    
def pause(event):
    global direction
    direction = ""
    
def leftKey(event):
    global direction
    direction = "left"
    
def rightKey(event):
    global direction
    direction = "right"
    
def upKey(event):
    global direction
    direction = "up"
    
def downKey(event):
    global direction
    direction = "down"
    
    
def setWindowDimensions(w,h):
    window = Tk() #create window
    window.title("Snake Game") #title of window
    
    ws = window.winfo_screenwidth() # computers screen size
    hs = window.winfo_screenheight()
    
    x = (ws/2) - (w/2) # calculate center
    y = (hs/2) - (h/2)
    
    window.geometry('%dx%d+%d+%d' % (w, h, x, y)) #size of window
    
    return window


width = 555 # width of snakes world
height = 555 # height of snakes world


window = setWindowDimensions(width, height)
canvas = Canvas(window, bg="black", width=width, height=height)
snake = []
snakeSize = 15
snake.append(canvas.create_rectangle(snakeSize,snakeSize,snakeSize * 2, snakeSize * 2, fill="white" ))

score=0
txt = "Score:" + str(score)
scoreText = canvas.create_text(width/2,10,fill="white",font="Times 20 italic bold", text=txt)

canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.bind("p", pause)
canvas.focus_set()

direction = "right"
placeFood()
placePoison()
moveSnake()
window.mainloop()



