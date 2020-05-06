from PIL import Image
import random
import numpy as np

def to2D():
    for i in range(1, 841):
        stringTailer = " (" + str(i) + ")"

        # previous location
        imgLocationPaper = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps/rps/paper/" + "paper" + stringTailer + ".png"
        imgLocationRock = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps/rps/rock/" + "rock" + stringTailer + ".png"
        imgLocationScissors = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps/rps/scissors/" + "scissors" + stringTailer + ".png"

        # 2D location
        TDLocationPaper = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps2D/paper/" + "paper" + stringTailer + ".png"
        TDLocationRock = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps2D/rock/" + "rock" + stringTailer + ".png"
        TDLocationScissors = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps2D/scissors/" + "scissors" + stringTailer + ".png"

        # convert
        imgPaper = Image.open(imgLocationPaper).convert('L')
        imgRock = Image.open(imgLocationRock).convert('L')
        imgScissors = Image.open(imgLocationScissors).convert('L')

        #save to 2D
        imgPaper.save(TDLocationPaper)
        imgRock.save(TDLocationRock)
        imgScissors.save(TDLocationScissors)


def addNoise():
    for i in range(1, 841):
        stringTailer = " (" + str(i) + ")"

        # 2D location
        TDLocationPaper = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps2D/paper/" + "paper" + stringTailer + ".png"
        TDLocationRock = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps2D/rock/" + "rock" + stringTailer + ".png"
        TDLocationScissors = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps2D/scissors/" + "scissors" + stringTailer + ".png"

        # noise location
        noiseLocationPaper = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsNoise/paper/" + "paper" + stringTailer + ".png"
        noiseLocationRock = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsNoise/rock/" + "rock" + stringTailer + ".png"
        noiseLocationScissors = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsNoise/scissors/" + "scissors" + stringTailer + ".png"

        # convert to array
        imgPaperArr = np.array(Image.open(TDLocationPaper))
        imgRockrArr = np.array(Image.open(TDLocationRock))
        imgScissorsArr = np.array(Image.open(TDLocationScissors))

        # add noise
        for k in range(0, 300):
            for j in range(0, 300):
                if imgRockrArr[k, j] > 245:
                    imgRockrArr[k, j] = random.randint(150, 255)
                if imgPaperArr[k, j] > 245:
                    imgPaperArr[k, j] = random.randint(150, 255)
                if imgScissorsArr[k, j] > 245:
                    imgScissorsArr[k, j] = random.randint(150, 255)

        imR = Image.fromarray(imgRockrArr)
        imP = Image.fromarray(imgPaperArr)
        imS = Image.fromarray(imgScissorsArr)

        imP.save(noiseLocationPaper)
        imR.save(noiseLocationRock)
        imS.save(noiseLocationScissors)


def rotate():
    for i in range(1, 841):
        stringTailer = " (" + str(i) + ")"

        # noise location
        noiseLocationPaper = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsNoise/paper/" + "paper" + stringTailer + ".png"
        noiseLocationRock = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsNoise/rock/" + "rock" + stringTailer + ".png"
        noiseLocationScissors = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsNoise/scissors/" + "scissors" + stringTailer + ".png"

        #rotate location
        rotateLocationPaper = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsRotate/paper/" + "paper" + stringTailer + ".png"
        rotateLocationRock = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsRotate/rock/" + "rock" + stringTailer + ".png"
        rotateLocationScissors = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsRotate/scissors/" + "scissors" + stringTailer + ".png"

        # final array location
        arrLocationPaper = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsArr/paper/" + "paper" + stringTailer
        arrLocationRock = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsArr/rock/" + "rock" + stringTailer
        arrLocationScissors = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsArr/scissors/" + "scissors" + stringTailer

        imgPaper = Image.open(noiseLocationPaper)
        imgRock = Image.open(noiseLocationRock)
        imgScissors = Image.open(noiseLocationScissors)

        angle = 90
        randPaper = random.randint(0, 4)
        imgPaper = imgPaper.rotate(randPaper * angle)
        imgPaperArr = np.array(imgPaper)


        randRock = random.randint(0, 4)
        imgRock = imgRock.rotate(randRock * angle)
        imgRockArr = np.array(imgRock)

        randScissors = random.randint(0, 4)
        imgScissors = imgScissors.rotate(randScissors * angle)
        imgScissorsArr = np.array(imgScissors)

        imgRock.save(rotateLocationRock)
        imgPaper.save(rotateLocationPaper)
        imgScissors.save(rotateLocationScissors)

        np.save(arrLocationPaper, imgPaperArr)
        np.save(arrLocationRock, imgRockArr)
        np.save(arrLocationScissors, imgScissorsArr)


#to2D()
#addNoise()
#rotate()


