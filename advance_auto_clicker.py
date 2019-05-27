
import os
import pyautogui
import time
import msvcrt
z = "\n      x             x\n       x           x\n           xxxxx\n         xxxxxxxxx\n        xx  xxx  xx\n        xxxxxxxxxxx\n    ********GHOST*******\n"



def rec(_action):
    #recording mrosses
    x = pyautogui.position()#touple
    color = pyautogui.pixel(x[0],x[1])#touple
    pos = pyautogui.position()#touple
    st = list()
    st.append(_action)
    st.append(pos)
    st.append(color)
    while True:
        if msvcrt.kbhit():
            key = str(msvcrt.getch())
            if key[2:-1] == 'f':
                break
        else:
            pass
    st.append(pyautogui.position())
    return st

def writefile(x):
    #writing to the external file
        text = str()
        for item in x:
            for it in item:
                text += str(it) + ","
        temp = text[0:-1:1]
        myfile = open("Moves.txt", mode='a')
        myfile.write(temp + '\n')
        myfile.close()
        





def startRec():
    #recording option
    print('\n** Start recording **\n')
    print("m - for rec movment \nc - for rec cutting \nf - for confrim movment\nn - reset records\ne - exit")
    while True:
        if msvcrt.kbhit():
            key = str(msvcrt.getch())
            if key[2:-1] == 'm':
                print("rec move")
                writefile(rec('m'))
                print("...done")
            if key[2:-1] == 'c':
                print("rec cut")
                writefile(rec('c')) 
                print('...done')
            if key[2:-1] == 'n':
                clearCord()
            if key[2:-1] == 'e':
                print('** exit from rec mode! **\n')
                break
        else:
            pass



def txtToCordsList():
    #reads the external file and make a list of it
    myfile = open("moves.txt", mode="r")
    fromTxtFile = myfile.readlines()
    myfile.close()
    
    cordList = list()
    temp = str()
    for cord in fromTxtFile:
        temp = cord[0:-1:]
        temp = temp.split(',')
        cordList.append(temp)
    return cordList




def cordsList(cordList):
    # running the list of cords and sending them to the currect function
    for step in cordList:
        if step[0] == "m":
            move(step)
        elif step[0] == 'c':
            treeCut(step)



def testColor(x,y,regColor):
    #checking the color of exact position
    pyautogui.moveTo((x,y))
    im = pyautogui.screenshot()
    ls = (int(x),int(y))
    color = im.getpixel(ls)
    print('check ls = '+str(color) + 'color = '+str(regColor))
    if color == regColor:
        print('**match!**')
        return True

def move(cord):
    #clicking the exact position after color matches
    print('\n\tmove to cord - ' +str(cord)+'\n')
    x = cord[1]
    y = cord[2]
    col = (int(cord[3]),int(cord[4]),int(cord[5]))
    
    #checking the color
    while True:
        if testColor(x,y,col):
            pyautogui.moveTo((cord[6],cord[7]))
            time.sleep(1)
            pyautogui.click((cord[6],cord[7]))
            time.sleep(1)
            print("moving...\n\n")
            break
        else:
            time.sleep(1)
            print('wait for next move')
        




def treeCut(cord):
    #checking if there is a tree and the inventory capacity
    x = cord[1]
    y = cord[2]
    col = (int(cord[3]),int(cord[4]),int(cord[5]))
    
    #checking the color
    while True:
        if testColor(x,y,col):
            print('\n\tcutting the cord - ' +str(cord)+'\n')
            pyautogui.moveTo((cord[6],cord[7]))
            time.sleep(1)
            pyautogui.click((cord[6],cord[7]))
            print("cutting")
            time.sleep(8)
            #stop the cutting if the inventory is full
            if(invIsFull(1307,664,(110, 79, 39))):
                break
        else:
            time.sleep(2)
            if(invIsFull(1307,664,(110, 79, 39))):
                break
            print('wait for tree to grow')
        





def invIsFull(x,y,z):
    #checking if the inventory is full
    if testColor(x,y,z):
        return True
    return False

def clearCord():
    if os.path.exists("Moves.txt"):
        os.remove("Moves.txt")
        print("Reset file!")
    else:
        print("The file does not exist")


while True:
    print(z)
    print("r - for recording \na - for action")
    while True:
        if msvcrt.kbhit():
            key = str(msvcrt.getch())
            if key[2:-1] == 'r':
                startRec()
                break
            elif key[2:-1] == 'a':
                while True:
                    cordsList(txtToCordsList())

