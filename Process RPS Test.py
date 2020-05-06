from PIL import Image
import random
import numpy as np

rootFolder = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps-test-set/"
rootFolder2 = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rps2DTest/"
rootFolder3 = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsNoiseTest/"
rootFolder4 = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsRotateTest/"
rootFolder5 = "C:/Users/Administrator/Desktop/Course/COMP 562 Res/Final Project/rpsArrTest/"
paperFolder = "paper/"
rockFolder = "rock/"
scissorsFolder = "scissors/"
paperFile = "testpaper"
rockFile = "testrock"
scissorsFile = "testscissors"
pngTailer = ".png"

def to2D():
    for i in range(1, 125):
        stringTailer = " (" + str(i) + ")"
        # previous location
        imgLocationPaper = rootFolder + paperFolder + paperFile + stringTailer + pngTailer
        imgLocationRock = rootFolder + rockFolder + rockFile + stringTailer + pngTailer
        imgLocationScissors = rootFolder + scissorsFolder + scissorsFile + stringTailer + pngTailer

        # 2D location
        TDLocationPaper = rootFolder2 + paperFolder + paperFile + stringTailer + pngTailer
        TDLocationRock = rootFolder2 + rockFolder + rockFile + stringTailer + pngTailer
        TDLocationScissors = rootFolder2 + scissorsFolder + scissorsFile + stringTailer + pngTailer

        # convert
        imgPaper = Image.open(imgLocationPaper).convert('L')
        imgRock = Image.open(imgLocationRock).convert('L')
        imgScissors = Image.open(imgLocationScissors).convert('L')

        #save to 2D
        imgPaper.save(TDLocationPaper)
        imgRock.save(TDLocationRock)
        imgScissors.save(TDLocationScissors)


def addNoise():
    for i in range(1, 125):
        stringTailer = " (" + str(i) + ")"

        # 2D location
        TDLocationPaper = rootFolder2 + paperFolder + paperFile + stringTailer + pngTailer
        TDLocationRock = rootFolder2 + rockFolder + rockFile + stringTailer + pngTailer
        TDLocationScissors = rootFolder2 + scissorsFolder + scissorsFile + stringTailer + pngTailer

        # noise location
        noiseLocationPaper = rootFolder3 + paperFolder + paperFile + stringTailer + pngTailer
        noiseLocationRock = rootFolder3 + rockFolder + rockFile + stringTailer + pngTailer
        noiseLocationScissors = rootFolder3 + scissorsFolder + scissorsFile + stringTailer + pngTailer

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
    for i in range(1, 125):
        stringTailer = " (" + str(i) + ")"

        # noise location
        noiseLocationPaper = rootFolder3 + paperFolder + paperFile + stringTailer + pngTailer
        noiseLocationRock = rootFolder3 + rockFolder + rockFile + stringTailer + pngTailer
        noiseLocationScissors = rootFolder3 + scissorsFolder + scissorsFile + stringTailer + pngTailer

        #rotate location
        rotateLocationPaper = rootFolder4 + paperFolder + paperFile + stringTailer + pngTailer
        rotateLocationRock = rootFolder4 + rockFolder + rockFile + stringTailer + pngTailer
        rotateLocationScissors = rootFolder4 + scissorsFolder + scissorsFile + stringTailer + pngTailer

        # final array location
        arrLocationPaper = rootFolder5 + paperFolder + paperFile + stringTailer
        arrLocationRock = rootFolder5 + rockFolder + rockFile + stringTailer
        arrLocationScissors = rootFolder5 + scissorsFolder + scissorsFile + stringTailer

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

        imgPaper.save(rotateLocationPaper)
        imgRock.save(rotateLocationRock)
        imgScissors.save(rotateLocationScissors)

        np.save(arrLocationPaper, imgPaperArr)
        np.save(arrLocationRock, imgRockArr)
        np.save(arrLocationScissors, imgScissorsArr)


#to2D()
#addNoise()
#rotate()


