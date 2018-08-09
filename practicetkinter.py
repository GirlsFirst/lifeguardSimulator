# mode-demo.py

from tkinter import *
from PIL import ImageTk, Image
import random
####################################
# init
####################################

def init(data):
    data.img = PhotoImage(file = 'pixelpool4.gif')
    image = data.img
    data.guard= PhotoImage(file = 'guard5.gif')
    image2 = data.guard
    data.swim1 = PhotoImage(file = 'swimmer4.gif')
    # swimmer4 is 122 x 122 pixels
    image3 = data.swim1
    data.swim2 = PhotoImage(file = 'swimmerB4.gif')
    image4 = data.swim2
    data.numSwimmers = random.randint(3, 6)
    data.listSwimmers = populateList(data)
    data.bottle = PhotoImage(file = 'bottle.gif')
    image5 = data.bottle
    data.redcross = PhotoImage(file = 'lifeguard.gif')
    image6 = data.redcross
    data.puddle = PhotoImage(file = 'puddle.gif')
    data.sign = PhotoImage(file = 'sign2.gif')
    # There is only one init, not one-per-mode
    data.mode = "splashScreen"
    data.score = 0
    data.highscore = 0
    data.imageX = 100
    data.imageY = 100
    data.millisecond = 0
    data.bottle1 = True
    data.bottle2 = True
    data.bottle3 = True
    data.countdown = 30
    data.puddle1 = True
    data.puddle2 = True
    data.puddle3 = True
    data.drowntimer = 0
    data.drowning = False
    data.deathtimer = 120


    data.swimRight = True
    data.pixelwidth1 = 700
    data.pixelwidth0 = 200
###########################
# Swimmer Values
###########################
    data.img2X = 200
    data.img2Y = 200
    data.img3X = 200
    data.img3Y = 300
    data.img4X = 250
    data.img4Y = 350
    data.img5X = 250
    data.img5Y = 400
    data.img6X = 320
    data.img6Y = 440
    data.img7X = 400
    data.img7Y = 500

###################################
#  add on functions
####################################

def extra(data, x, y):
    data.x = x
    data.y = y
    data.r = random.randit(200,480)


def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def populateList(data):
    listSwimmers = []
    xcoordinatesList = []
    for i in range(random.randint(3, 6)):
        listSwimmers.append([random.randint(190,650), random.randint(200,450), True, random.randint(80, 400), False])
    for item in listSwimmers:
        xcoordinatesList.append(item[0])
    print("listSwimmers", listSwimmers)
    return listSwimmers



####################################
# mode dispatcher
####################################




def mousePressed(event, data):
    if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
    elif (data.mode == "playGame"):   playGameMousePressed(event, data)
    elif (data.mode == "help"):       helpMousePressed(event, data)
    elif (data.mode == "gameOver"):   gameOverMousePressed(event,data)

def keyPressed(event, data):
    if (data.mode == "splashScreen"): splashScreenKeyPressed(event, data)
    elif (data.mode == "playGame"):   playGameKeyPressed(event, data)
    elif (data.mode == "help"):       helpKeyPressed(event, data)
    elif (data.mode == "gameOver"):   gameOverKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)
    elif (data.mode == "gameOver"):       gameOverTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)
    elif (data.mode == "gameOver"):       gameOverRedrawAll(canvas,data)

####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    if event.x > data.width/2-200 and event.y < data.height/2+50 and event.x < data.width/2+200 and event.y > data.height/2-50:
        data.mode = "playGame"
    if event.x > data.width/2-200 and event.y > data.height/2+150 and event.x < data.width/2+200 and event.y < data.height/2+250:
        data.mode = "help"
def splashScreenKeyPressed(event, data):
    pass

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-200,
                       text="Welcome to the Lifeguard Simulator!", font="Arial 45 bold italic")
    canvas.create_rectangle(data.width/2-200, data.height/2-50,data.width/2+200, data.height/2+50 ,fill="red")
    canvas.create_text(data.width/2, data.height/2,
                   text="Start game", font="Arial 30")
    canvas.create_rectangle(data.width/2-200, data.height/2+150, data.width/2+200, data.height/2+250,fill="blue")
    canvas.create_text(data.width/2, data.height/2+200,
                    text="Instructions", font="Arial 30")
####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass
    # if event.x > data.width

def helpKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.mode = "playGame"
def retryPressed(event, data):
    data.mode = "playGame"
    # createSwimmer(canvas, data)
def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-210,
                       text="You are a Lifeguard!", font="Arial 40 bold italic")
    canvas.create_text(data.width/2, data.height/2-150,
                       text="How to play:", font="Arial 24")
    canvas.create_text(data.width/2, data.height/2-90,
                       text="Save the drowning patrons by pressing the 'Space Bar' to enter the pool!", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2-20,
                       text="Press the 'F' on them to save them!", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+50,
                   text="Use W,A,S,D keys to move!", font= "Helvetica 30 bold italic")
    canvas.create_text(data.width/2, data.height/2+120,
                       text="Don't step on glass or the chlorine puddles! Pick up bottles by 'P'", font= "Arial 20")
    canvas.create_text(data.width/2, data.height/2+160,
                        text="Press H to play", font= "Helvetica 20 italic")

####################################
# playGame mode
####################################
#
# def createSwimmer(canvas,data):
#     aRandomNumber = randint(3,6)
#     if aRandomNumber == 3:
#         canvas.create_image(data.img2X, data.img2Y, image=data.swim1)
#         canvas.create_image(data.img3X, data.img3Y, image=data.swim1)
#         canvas.create_image(data.img4X, data.img4Y, image=data.swim2)
#     if aRandomNumber == 4:
#         canvas.create_image(data.img2X, data.img2Y, image=data.swim1)
#         canvas.create_image(data.img3X, data.img3Y, image=data.swim1)
#         canvas.create_image(data.img4X, data.img4Y, image=data.swim2)
#         canvas.create_image(data.img5X, data.img5Y, image=data.swim2)
#     if aRandomNumber == 5:
#         canvas.create_image(data.img2X, data.img2Y, image=data.swim1)
#         canvas.create_image(data.img3X, data.img3Y, image=data.swim1)
#         canvas.create_image(data.img4X, data.img4Y, image=data.swim2)
#         canvas.create_image(data.img5X, data.img5Y, image=data.swim2)
#         canvas.create_image(data.img6X, data.img6Y, image=data.swim1)
#     if aRandomNumber == 6:
#         canvas.create_image(data.img2X, data.img2Y, image=data.swim1)
#         canvas.create_image(data.img3X, data.img3Y, image=data.swim1)
#         canvas.create_image(data.img4X, data.img4Y, image=data.swim2)
#         canvas.create_image(data.img5X, data.img5Y, image=data.swim2)
#         canvas.create_image(data.img6X, data.img6Y, image=data.swim1)
#         canvas.create_image(data.img7X, data.img7Y, image=data.swim2)

def playGameMousePressed(event, data):
    data.score = 0
    print(event.x, event.y)

def playGameKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.mode = "help"
    if (event.keysym == 't'):
        data.mode = "splashScreen"

    ################
    #drowning instance
    for i in range(len(data.listSwimmers)):
        if data.listSwimmers[i][4]== True:
            data.deathtimer = data.deathtimer -1
            if data.deathtimer == 0:
                data.mode = "gameOver"
            if (event.keysym == 'f'):
                print("My coords")
                print(data.imageX, data.imageY)
                print(data.listSwimmers[i][0], data.listSwimmers[i][1])
                if data.listSwimmers[i][0] <= data.imageX +40 and data.listSwimmers[i][0] >= data.imageX -40 and data.listSwimmers[i][1] <= data.imageY +40 and data.listSwimmers[i][1] >= data.imageY -40:
                    data.listSwimmers[i][4] = False
                    data.score += 2000
                    data.deathtimer = 120
                    data.countdown += 1




    ###############
    #chlorine death

    if data.imageX >= 265 and data.imageX <= 305 and data.imageY >= 50 and data.imageY <= 100:
        print(data.imageX,data.imageY)
        data.score -=1000
        data.mode = "gameOver"
    if data.imageX >= 30 and data.imageX <= 75 and data.imageY >= 250 and data.imageY <= 325:
        print(data.imageX, data.imageY)
        data.score -=1000
        data.mode = "gameOver"
    if data.imageX >= 278 and data.imageX <= 325 and data.imageY >= 480 and data.imageY <=547:
        data.score -=1000
        print(data.imageX, data.imageY)
        data.mode = "gameOver"

    ################
# moving protagonist
    if (event.keysym == 'w'):
        if data.imageY <= 0:
            data.imageY=599
            data.imageX = data.imageX
        else:
            data.imageY -=10
    if (event.keysym == 'a'):
        if data.imageX <=0:
            data.imageX = 799
            data.imageY = data.imageY
        else:
            data.imageX -=10
    if (event.keysym == 's'):
        if data.imageY >=600:
            data.imageY = 1
            data.imageX = data.imageX
        else:
            data.imageY +=10
    if (event.keysym == 'd'):
        if data.imageX >=800:
            data.imageX = 1
            data.imageY = data.imageY
        else:
            data.imageX +=10

############
#picking up bottles
    if (event.keysym == 'p'):
        if data.imageX >=619 and data.imageX <=642 and data.imageY >=18 and data.imageY <=72:
            data.bottle1 = False
            data.score +=1000
            data.countdown+=10
        if data.imageX >=58 and data.imageX <=92 and data.imageY >=318 and data.imageY <=403:
            data.bottle2 = False
            data.score +=1000
            data.countdown+=10
        if data.imageX >=508 and data.imageX <=563 and data.imageY >=500 and data.imageY <=587:
            data.bottle3 = False
            data.score +=1000
            data.countdown+=10
##############
def playGameGoPressed(event, data):
    if (event.keysym == 's'):
        data.mode = "playGame"
#
def playGameTimerFired(data):
    data.millisecond = data.millisecond + 1
    data.drowntimer = data.drowntimer + 1
    for i in range(len(data.listSwimmers)):
        if data.drowntimer == data.listSwimmers[i][3]:
            data.listSwimmers[i][4] == True
            data.deathtimer = data.deathtimer -1
            if data.deathtimer == 0:
                data.mode = "gameOver"
    data.score = data.score + 1
    # print(data.millisecond)
    if data.millisecond == 20:
        if data.millisecond == 5:
            data.swim1 = PhotoImage(file = 'swimmerB4.gif')
            print("Photo Changed")
        if data.millisecond == 10:
            data.swim1 = PhotoImage(file = 'swimmer4.gif')
            print("changed back")
        data.countdown -=1
        data.millisecond = 0
    # print(data.countdown)
    if data.countdown == 0:
        data.mode = "gameOver"
        data.countdown = 30
    if data.drowntimer == 400:
        data.drowntimer = 0
    # if data.millisecond == 100:
    #     for i in range(len(data.coords[0][i])):
    #         [x+5 for x in data.coords[0][i]]
    #     image3 = data.swim2
    # if data.millisecond == 200:
    #     image3 = data.swim1
    #     for i in range(len(data.coords[0][i])):
    #         [x+5 for x in data.coords]
    #         data.millisecond = 0
    #         print("Done")

    data.score += 1

    #Making Swimmers move
    for i in range(len(data.listSwimmers)):
        if data.listSwimmers[i][2] == True:
            # for i in range(len(data.listSwimmers)):
            if data.listSwimmers[i][4] == False:
                data.listSwimmers[i][0] +=5
            for i in range(len(data.listSwimmers)):
                if data.listSwimmers[i][0] +61 >= data.pixelwidth1:
                    data.listSwimmers[i][2] = False
        if data.listSwimmers[i][2] == False:
            if data.listSwimmers[i][4] == False:
            # for i in range(len(data.listSwimmers)):
                data.listSwimmers[i][0] -=5
            for i in range(len(data.listSwimmers)):
                if data.listSwimmers[i][0]+61 <= data.pixelwidth0:
                    data.listSwimmers[i][2] = True




def playGameRedrawAll(canvas, data):
    # print(type(data.listSwimmers[0][1]))
    # print(data.listSwimmers[1][0])

    image3=data.swim1
    image = PhotoImage(file = 'pixelpool4.gif')
    image2 = PhotoImage(file = 'guard5.gif')
    # canvas.create_text(data.width/2, data.height/2-40,
    #                    text="This is a fun game!", font="Arial 26 bold")
    # canvas.create_text(data.width/2, data.height/2-10,
    #                    text="Score = " + str(data.score), font="Arial 20")
    # canvas.create_text(data.width/2, data.height/2+15,
    #                    text="Click anywhere to reset score", font="Arial 20")
    # canvas.create_text(data.width/2, data.height/2+40,
    #                    text="Press 'h' for help!", font="Arial 20")
    sand_color = rgbString(222, 184, 135)
    canvas.create_rectangle(0, 0, data.width, data.height, fill=sand_color,
                             width=0)
    # canvas.create_text(data.width/2, data.height/2-40,
    #                text="This is a fun game!", font="Arial 26 bold")
    canvas.create_image(370, 260, image=data.img)
    if data.bottle1 == True:
        canvas.create_image(700,100, image=data.bottle)
    if data.bottle2 == True:
        canvas.create_image(150,400, image=data.bottle)
    if data.bottle3 == True:
        canvas.create_image(600,570, image=data.bottle)
    if data.puddle1 == True:
        canvas.create_image(330,115, image=data.puddle)
    if data.puddle2 == True:
        canvas.create_image(95,310, image=data.puddle)
    if data.puddle3 == True:
        canvas.create_image(340,540, image=data.puddle)
    canvas.create_image(829,595, image=data.sign)
    canvas.create_text(765,568, text=str(data.countdown), font="Arial 16 bold italic")
    canvas.create_text(720,568, text="Time: ", font="Arial 16 bold italic")

    canvas.create_image(data.imageX,data.imageY, image=data.guard)
# Making Swimmers:
    if data.millisecond >= 5 and data.millisecond <=10:
        # for i in range(len(data.listSwimmers)):
        #     if data.listSwimmers[i][4]
        data.swim1 = PhotoImage(file = 'swimmerB4.gif')
    if data.millisecond >= 11 and data.millisecond <=16:
        data.swim1 = PhotoImage(file = 'swimmer4.gif')
    if data.millisecond >=17 and data.millisecond <=20:
        data.swim1 = PhotoImage(file = 'swimmerB4.gif')
    if data.millisecond >= 0 and data.millisecond <=4:
        data.swim1 = PhotoImage(file = 'swimmer4.gif')



    for i in range(len(data.listSwimmers)):
        canvas.create_image(int(data.listSwimmers[i][0]), int(data.listSwimmers[i][1]), image=data.swim1)

#Drowning Swimmers:

        if data.drowntimer == data.listSwimmers[i][3]:
            data.listSwimmers[i][4] = True
            if data.listSwimmers[i][4] == True:
                data.swim1 = PhotoImage(file = 'dead.gif')
            if data.listSwimmers[i][4] == False:
                return




        # print("Swimmers created!")

    # canvas.create_image(data.img2X, data.img2Y, image=data.swim1)
    # for i in range(data.numSwimmers):
    #     # canvas.create_rectangle(data.listSwimmers[i][0], data.listSwimmers[i][1], data.listSwimmers[i][0]+20, data.listSwimmers[i][1]+20,fill = "red")
    #     canvas.create_image(data.listSwimmers[i][0], data.listSwimmers[i][1], image=image3)

    # createSwimmer(canvas, data)
    #image = image.resize(300,300)
# use the run function as-is


# ############################
# GameOver Mode
##############################
def gameOverTimerFired(data):
    pass

def gameOverKeyPressed(event,data):
        if (event.keysym == 't'):
            data.mode = "splashScreen"
            data
def gameOverMousePressed(event,data):
    if event.x > data.width/2-200 and event.y < data.height/2+50 and event.x < data.width/2+200 and event.y > data.height/2-50:
        data.mode = "splashScreen"
        data.countdown = 30
        data.millisecond = 0
        data.bottle1 = True
        data.bottle2 = True
        data.bottle3 = True
        data.imageX = 100
        data.imageY = 100
        data.swimRight = True
        data.drowntimer = 0
        data.deathtimer =120
        data.score = 0
        for i in range(len(data.listSwimmers)):
            data.listSwimmers[i][4] = False
    # if event.x > data.width/2-200 and event.y > data.height/2+150 and event.x < data.width/2+200 and event.y < data.height/2+250:
    #     data.mode = "help"

def gameOverRedrawAll(canvas,data):
    canvas.create_text(data.width/2, data.height/2-200,
                       text="You lost!", font="Arial 45 bold italic")
    canvas.create_rectangle(data.width/2-200, data.height/2-50,data.width/2+200, data.height/2+50 ,fill="red")
    canvas.create_text(data.width/2, data.height/2,
                   text="Retry Game!", font="Arial 30")
    # canvas.create_rectangle(data.width/2-200, data.height/2+150, data.width/2+200, data.height/2+250,fill="blue")
    # canvas.create_text(data.width/2, data.height/2+200,
    #                 text="Instructions Again?", font="Arial 30")
    canvas.create_image(data.width/2+10,data.height/2+170, image=data.redcross)
    canvas.create_text(data.width/2-45, data.height/2-90, text="Score: ",font="Arial 25 bold")
    canvas.create_text(data.width/2+45, data.height/2-90, text=str(data.score), font="Arial 25")
    if data.score >= data.highscore:
        data.highscore = data.score
    canvas.create_text(data.width/2-45, data.height/2-140, text="High Score: ",font="Arial 25 bold")
    canvas.create_text(data.width/2+65, data.height/2-140, text=str(data.highscore), font="Arial 25")
    canvas.create_text(data.width/2+260, data.height/2+280, text="Made by Megan Friedenberg", font="Arial 14 bold italic")
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 50 # milliseconds
    root = Toplevel()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 600)
