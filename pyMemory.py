import libtcodpy as libtcod
from random import randint
import time
import sys

SCREEN_WIDTH = 60
SCREEN_HEIGHT = 60

libtcod.console_set_custom_font("cp437_12x12.png", libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'pyMemory', False, libtcod.RENDERER_OPENGL)
libtcod.mouse_show_cursor (True)

mouse = libtcod.Mouse()
key = libtcod.Key()

def DrawSquare(x,y,size,color): #x and y are upper left coordinates, size is side of square, color is color of square

    for a in range(size):
        for b in range(size):
            libtcod.console_put_char_ex(None,x+a,y+b,219,color,libtcod.white)

    return

def MouseSquare(mouse,x,y,size): #mouse is mouse,x and y are upper left coordinates, size is side of square

    if mouse.cx >= x and mouse.cx <= x + size and mouse.cy >= y and mouse.cy <= y + size:
        return True
    return False

while not libtcod.console_is_window_closed():    

    for level in range(10):

        #Draw Board

        Round = "Level "+str(level+1)+" ("+str(level+3)+" Colors)"
        libtcod.console_print(None,22,2,Round)

        libtcod.console_print(None,27,6,"FOCUS!")
        
        DrawSquare(10,35,15,libtcod.darker_red)
        DrawSquare(10,10,15,libtcod.darker_yellow)
        DrawSquare(35,10,15,libtcod.darker_blue)
        DrawSquare(35,35,15,libtcod.darker_green)
        libtcod.console_flush()

        #Generate Pathern
        
        Pathern = []
        del Pathern[:]
        for option in range(level+3):           
            
            rand = randint(1,4)
            
            Pathern.append(rand)
            
            if rand == 1:
                DrawSquare(10,35,15,libtcod.red)
                libtcod.console_flush()
                time.sleep(1)
                DrawSquare(10,35,15,libtcod.darker_red)
                libtcod.console_flush()
                time.sleep(1)
            elif rand == 2:
                DrawSquare(10,10,15,libtcod.yellow)
                libtcod.console_flush()
                time.sleep(1)
                DrawSquare(10,10,15,libtcod.darker_yellow)
                libtcod.console_flush()
                time.sleep(1)
            elif rand == 3:
                DrawSquare(35,10,15,libtcod.blue)
                libtcod.console_flush()
                time.sleep(1)
                DrawSquare(35,10,15,libtcod.darker_blue)
                libtcod.console_flush()
                time.sleep(1)
            elif rand == 4:
                DrawSquare(35,35,15,libtcod.green)
                libtcod.console_flush()
                time.sleep(1)
                DrawSquare(35,35,15,libtcod.darker_green)
                libtcod.console_flush()
                time.sleep(1)

        #Player

        libtcod.console_print(None,27,6,"PLAY! ")
        libtcod.console_flush()

        options = []
        del options[:]
        N = 0
        while len(options) < level+3:
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS|libtcod.EVENT_MOUSE,key,mouse)
            if mouse.lbutton_pressed and MouseSquare(mouse,10,35,15):
                options.append(1)
                N += 1
            elif mouse.lbutton_pressed and MouseSquare(mouse,10,10,15):
                options.append(2)
                N += 1
            elif mouse.lbutton_pressed and MouseSquare(mouse,35,10,15):
                options.append(3)
                N += 1
            elif mouse.lbutton_pressed and MouseSquare(mouse,35,35,15):
                options.append(4)
                N += 1

        #Check

        print options
        print Pathern

        for a in range(level+3):
            if Pathern[a] != options[a]:
                sys.exit()

        libtcod.console_print(None,27,6,"FOCUS!")
        libtcod.console_flush()

        time.sleep(1)

    

    



















                
