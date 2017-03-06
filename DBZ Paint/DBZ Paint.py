#DBZ Paint.py
#Adam Youssef

from pygame import*
from random import*
from math import*
from tkinter import*

root = Tk()                                 
root.withdraw()

screen = display.set_mode ((1100, 950))
running = True
down = False #tracks if mouse button is down

mx, my = 0, 0 #gets mouse position
c = ((0, 0, 0)) #colour for pencils, shapes and fills
size = 5 #size for lines, brush and eraser
startx = 0
starty = 0
pixels = [] #list to hold pixels for fill bucket
current = (0, 0) #current pixels being checked for replacement colour
undo = [] #list that holds undo pictures
redo = [] #list that holds redo pictures

bpic = image.load("wallpaper.png") #loads image
pic1 = transform.smoothscale (bpic, (1100, 950))#changes the images size
screen.blit(pic1, (0, 0)) #blits image on screen

penpic = image.load("pencil.jpg")
pic2 = transform.scale (penpic, (50, 50))
screen.blit (pic2, (130, 230))

eraserpic = image.load("Eraser.png")
pic3 = transform.scale (eraserpic, (50, 50))
screen.blit (pic3, (225, 230))

brushpic = image.load("paintbrush.png")
pic4 = transform.scale (brushpic, (50, 50))
screen.blit (pic4, (130, 330))

bucketpic = image.load("bucket.jpg")
pic5 = transform.scale (bucketpic, (50, 50))
screen.blit (pic5, (225, 330))

trashpic = image.load("trash can.jpg")
pic6 = transform.scale (trashpic, (50, 50))
screen.blit (pic6, (225, 630))

savepic = image.load("save.png")
pic7 = transform.scale (savepic, (50, 50))
screen.blit (pic7, (110, 875))

loadpic = image.load("load.png")
pic8 = transform.scale (loadpic, (50, 50))
screen.blit (pic8, (165, 875))

linepic = image.load("line.png")
pic9 = transform.scale (linepic, (50, 50))
screen.blit (pic9, (130, 630))

colourpic = image.load("colors.png")
pic10 = transform.scale (colourpic, (250, 190))
screen.blit (pic10, (830, 690))

undopic = image.load("undo.png")
pic11 = transform.smoothscale (undopic, (50, 50))
screen.blit (pic11, (5, 875))

redopic = image.load("redo.png")
pic12 = transform.smoothscale (redopic, (50, 50))
screen.blit (pic12, (60, 875))

cellgpic = image.load("cell games arena.jpg")
pic13 = transform.smoothscale (cellgpic, (250, 115))
screen.blit (pic13, (535, 690))

kamipic = image.load("kami's lookout.jpg")
pic14 = transform.smoothscale (kamipic, (250, 115))
screen.blit (pic14, (535, 810))

tournypic = image.load("world tournament.jpg")
pic15 = transform.smoothscale (tournypic, (250, 115))
screen.blit (pic15, (280, 690))

namekpic = image.load("namek.png")
pic16 = transform.smoothscale (namekpic, (250, 115))
screen.blit (pic16, (280, 810))

gokuipic = image.load("goku icon.jpg")
pic17 = transform.smoothscale (gokuipic, (60, 60))
screen.blit (pic17, (325, 15))

vegetaipic = image.load("vegeta icon.jpg")
pic18 = transform.smoothscale (vegetaipic, (60, 60))
screen.blit (pic18, (455, 15))

gohanipic = image.load("gohan icon.jpg")
pic19 = transform.smoothscale (gohanipic, (60, 60))
screen.blit (pic19, (585 ,15))

friezaipic = image.load("frieza icon.jpg")
pic20 = transform.smoothscale (friezaipic, (60, 60))
screen.blit (pic20, (715 ,15))

cellipic = image.load("cell icon.jpg")
pic21 = transform.smoothscale (cellipic, (60, 60))
screen.blit (pic21, (845 ,15))

buuipic = image.load("buu icon.jpg")
pic22 = transform.smoothscale (buuipic, (60, 60))
screen.blit (pic22, (975 ,15))

gokupic = image.load("goku.png")
pic23 = transform.smoothscale (gokupic, (65, 100))

vegetapic = image.load("vegeta.png")
pic24 = transform.smoothscale (vegetapic, (75, 105))

gohanpic = image.load("gohan.png")
pic25 = transform.smoothscale (gohanpic, (100, 105))

friezapic = image.load("frieza.png")
pic26 = transform.smoothscale (friezapic, (75, 100))

cellpic = image.load("cell.png")
pic27 = transform.smoothscale (cellpic, (55, 100))

buupic = image.load("buu.png")
pic28 = transform.smoothscale (buupic, (75, 100))

tool = "pencil"

#rects for tools and canvas
pencil = Rect(130, 230, 50, 50) 
eraser = Rect(225, 230, 50, 50)
brush = Rect(130, 330, 50, 50)
bucket = Rect(225, 330, 50, 50)
trash = Rect(225, 630, 50, 50)
save = Rect(110, 875, 50, 50)
load = Rect(165, 875, 50, 50)
line = Rect(130, 630, 50, 50)
frect = Rect(130, 430, 50, 50)
hrect = Rect(225, 430, 50, 50)
fcirc = Rect(130, 530, 50, 50)
hcirc = Rect(225, 530, 50, 50)
color = Rect(830, 690, 250, 190)
fills = Rect(830, 885, 250, 40)
undorect = Rect(5, 875, 50, 50)
redorect = Rect(50, 875, 50, 50)
cellg = Rect(535, 690, 250, 115)
kami = Rect(535, 810, 250, 115)
tourny = Rect(280, 690, 250, 115)
namek = Rect(280, 810, 250, 115)
goku = Rect(325, 15, 60, 60)
vegeta = Rect(455, 15, 60, 60)
gohan = Rect(585, 15, 60, 60)
frieza = Rect(715, 15, 60, 60)
cell = Rect(845, 15, 60, 60)
buu = Rect(975, 15, 60, 60)
canvas = Rect(280, 80, 800, 600)

draw.rect(screen, (255, 255, 255), canvas)

undo.append(screen.subsurface(280, 80, 800, 600).copy())#copies canvas and adds it to undo list

undid = False  # flag to ensure undo or redo only occurs once per click
             
while running:
    for e in event.get(): #checks all events that happen
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN: #checks events while mouse is down
            if e.button == 1:
                startx, starty = e.pos #gets position when mouse is clicked
                lines = screen.subsurface(canvas).copy() #copies canvas
        if e.type == MOUSEBUTTONUP: #checks events when mouse is up
            undid = False 
            if down: #if mouse is up it makes it switch to up
                down = False
                undo.append(screen.subsurface(280, 80, 800, 600).copy())
            if e.button == 4: #makes scrolling up and down change size
               size += 1
            if e.button == 5:
               size -= 1
#-----------------------------------------------------------------------------
    mb = mouse.get_pressed() #gets position when mouse is pressed
    mx,my = mouse.get_pos() #gets mouse position
    
    #draws rectangles for tools
    draw.rect(screen, (0, 0, 0), canvas, 2)
    draw.rect(screen, (0, 0, 0), pencil, 2)
    draw.rect(screen, (0, 0, 0), eraser, 2)
    draw.rect(screen, (0, 0, 0), brush, 2)
    draw.rect(screen, (0, 0, 0), bucket, 2)
    draw.rect(screen, (0, 0, 0), trash, 2)
    draw.rect(screen, (0, 0, 0), line, 2)
    draw.rect(screen, (255, 255, 255), hrect)
    draw.rect(screen, (0, 0, 0), hrect, 2)
    draw.rect(screen, (0, 0, 0), (230, 442, 40, 25), 2)
    draw.rect(screen, (255, 255, 255), frect)
    draw.rect(screen, (0, 0, 0), frect, 2)
    draw.rect(screen, (0, 0, 0), (135, 442, 40, 25))
    draw.rect(screen, (255, 255, 255), fcirc)
    draw.rect(screen, (0, 0, 0), fcirc, 2)
    draw.ellipse(screen, (0, 0, 0), (135, 535, 40, 40))
    draw.rect(screen, (255, 255, 255), hcirc)
    draw.rect(screen, (0, 0, 0), hcirc, 2)
    draw.ellipse(screen, (0, 0, 0), (230, 535, 40, 40), 1)
    draw.rect(screen, c, fills)
    draw.rect(screen, (0, 0, 0), fills, 2)

    #when tool button is hit, it changes to that tool and highlighs it when cursor goes over it
    if pencil.collidepoint(mx, my): 
        draw.rect(screen, (255, 0, 0), pencil, 2)
        if pencil.collidepoint(mx, my) and mb[0] == 1:
            tool = "pencil"
    
    if eraser.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), eraser, 2)
        if eraser.collidepoint(mx, my) and mb[0] == 1:
            tool = "eraser"

    if brush.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), brush, 2)
        if brush.collidepoint(mx, my) and mb[0] == 1:
            tool = "brush"

    if bucket.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), bucket, 2)
        if bucket.collidepoint(mx, my) and mb[0] == 1:
            tool = "bucket"

    if trash.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), trash, 2)
        if trash.collidepoint(mx, my) and mb[0] == 1:
            down = True
            draw.rect(screen, (255, 255, 255), canvas)#draws rectangle to clear canvas
            draw.rect(screen, (0, 0, 0), canvas, 2)
        
    if save.collidepoint(mx, my) and mb[0] == 1:
            fname = filedialog.asksaveasfilename(defaultextension=".png")#saves screen with extension
            if fname != "": #if the file name is not blank it saves the screen
                saver = screen.subsurface(canvas).copy()
                image.save(saver, fname)
        
    if load.collidepoint(mx, my) and mb[0] == 1:
            #checks for extension and if the file name is not blank it loads and blits the image
            fname = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.bmp;*.jpg;*.jpeg")])
            if fname != "":
                saved = image.load(fname)
                screen.blit(saved, (280, 80))

    if line.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), line, 2)
        if line.collidepoint(mx, my) and mb[0] == 1:
            tool = "line"

    if frect.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), frect, 2)
        if frect.collidepoint(mx, my) and mb[0] == 1:
            tool = "frect"

    if hrect.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), hrect, 2)
        if hrect.collidepoint(mx, my) and mb[0] == 1:
            tool = "hrect"

    if fcirc.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), fcirc, 2)
        if fcirc.collidepoint(mx, my) and mb[0] == 1:
            tool = "fcirc"
            
    if hcirc.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), hcirc, 2)
        if hcirc.collidepoint(mx, my) and mb[0] == 1:
            tool = "hcirc"
            
    if fills.collidepoint(mx, my):
        draw.rect(screen, (255, 0, 0), fills, 2)
        if fills.collidepoint(mx, my) and mb[0] == 1:
            down = True
            draw.rect(screen, c, canvas)
            draw.rect(screen, (0, 0, 0), canvas, 2)#fills screen with chosen colour

    if cellg.collidepoint(mx, my) and mb[0] == 1:
        down = True
        pic11 = transform.smoothscale (cellgpic, (800, 600))
        screen.blit (pic11, (280, 80))
        draw.rect(screen, (0, 0, 0), canvas, 2)

    if kami.collidepoint(mx, my) and mb[0] == 1:
        down = True
        pic12 = transform.smoothscale (kamipic, (800, 600))
        screen.blit (pic12, (280, 80))
        draw.rect(screen, (0, 0, 0), canvas, 2)

    if tourny.collidepoint(mx, my) and mb[0] == 1:
        down = True
        pic13 = transform.smoothscale (tournypic, (800, 600))
        screen.blit (pic13, (280, 80))
        draw.rect(screen, (0, 0, 0), canvas, 2)

    if namek.collidepoint(mx, my) and mb[0] == 1:
        down = True
        pic14 = transform.smoothscale (namekpic, (800, 600))
        screen.blit (pic14, (280, 80))
        draw.rect(screen, (0, 0, 0), canvas, 2)
        
    #if the length of the undo list is greater than 0 and if it has not undid something yet it undoes the last action
    if undorect.collidepoint(mx, my) and mb[0] == 1 and len(undo) > 0 and undid == False:
        undid = True
        if len(undo) > 1:
            holder = undo[-1] #holds last picture in undo list
            undo.remove(holder) #takes it from undo to redo
            redo.append(holder)
        screen.blit(undo[-1], (280, 80)) #blits last picture in list
        draw.rect(screen, (0, 0, 0), canvas, 2)

    if redorect.collidepoint(mx, my) and mb[0] == 1 and len(undo) > 0 and undid == False:
        undid = True
        if len(redo) > 1:
            holder = redo[-1]
            redo.remove(holder)
            undo.append(holder)
        screen.blit(redo[-1], (280, 80))
        draw.rect(screen, (0, 0, 0), canvas, 2)
    
    if goku.collidepoint(mx, my) and mb[0] == 1:
        tool = "goku"

    if vegeta.collidepoint(mx, my) and mb[0] == 1:
        tool = "vegeta"

    if gohan.collidepoint(mx, my) and mb[0] == 1:
        tool = "gohan"

    if frieza.collidepoint(mx, my) and mb[0] == 1:
        tool = "frieza"

    if cell.collidepoint(mx, my) and mb[0] == 1:
        tool = "cell"

    if buu.collidepoint(mx, my) and mb[0] == 1:
        tool = "buu"
            
    if color.collidepoint(mx, my) and mb[0] == 1:
        c = screen.get_at((mx, my)) #gets colour where mouse was pressed

    if canvas.collidepoint(mx, my) and mb[0] == 1: #if the mouse is on the canvas the tools will work
        screen.set_clip(canvas) #sets clip so it doesn't draw over canvas outsides
        if tool == "pencil":
            down = True
            draw.line(screen, c, (omx, omy), (mx , my), 2) #omx/omy used to fill every pixel and so pencil is not choopy

        elif tool == "eraser":
            down = True
            dist = hypot (mx-omx, my-omy) #gets length between circles
            dist = max (1, dist) #makes it an integer
            sx = (mx - omx) / dist #gets distance so brush is not choopy
            sy = (my - omy) / dist
            for i in range (int(dist)):
                draw.circle(screen, (255, 255, 255), (int(omx + i * sx), int(omy + i * sy )), size)            

        elif tool == "brush":
            down = True
            dist = hypot (mx-omx, my-omy)
            dist = max (1, dist)
            sx = (mx - omx) / dist
            sy = (my - omy) / dist
            for i in range (int(dist)):
                draw.circle(screen, c, (int(omx + i * sx), int(omy + i * sy )), size)

        elif tool == "bucket":
            down = True
            rep = screen.get_at((mx,my)) #gets colour you want to replace
            fill = c #colour you use to replace rep
            if rep != fill: #if the rep colour is not the same as the fill colour the spot you clicked is added to the list
                pixels = [(mx, my)]
                while pixels != []: #while pixels is not empty it keeps popping off points around the one chosen and checks its colour 
                    fx, fy = pixels.pop() #until it gets to a colour that isn't the rep or fill colour 
                    if screen.get_at((fx, fy)) == rep and canvas.collidepoint(fx, fy):
                        screen.set_at((fx, fy), fill) #changes the rep coloured points to the fill colour
                        pixels += [(fx + 1, fy), (fx - 1, fy), (fx, fy + 1), (fx, fy - 1)] #checks points around fx and fy

        elif tool == "line":
            down = True
            screen.blit(lines, canvas) #stops mulitple lines
            draw.line(screen, c, (startx, starty),(mx,my), size) #draws line
            
        elif tool == "frect":
            down = True
            screen.blit(lines, canvas) 
            draw.rect(screen, c, (startx, starty, mx  - startx, my - starty)) #allows rectangle to be drawn in any direction
           #filled rectangle automatically normalizes 
        elif tool == "hrect":
            down = True
            screen.blit(lines, canvas)
            draw.rect(screen, c, (startx, starty, mx  - startx, my - starty), 2)

        elif tool == "fcirc":
            down = True
            circle = Rect(startx, starty, mx - startx, my - starty)
            circle.normalize() #normalizes circle to be able to draw backwards
            screen.blit(lines, canvas)
            draw.ellipse(screen, c, circle)

        elif tool == "hcirc":
            down = True
            circle = Rect(startx, starty, mx - startx, my - starty)
            circle.normalize()
            screen.blit(lines, canvas)
            if circle.width < 4 or circle.height < 4: #makes it so that if the circle is really small it draws the filled one instead 
                draw.ellipse(screen, c, circle)
            else:
                draw.ellipse(screen, c, circle, 1)

        elif canvas.collidepoint(mx, my) and tool == "goku":
            cw = pic23.get_width() #gets picture width
            ch = pic23.get_height() #gets picture height
            screen.blit(lines, canvas) 
            if mb[0] == 1:
                down = True
                screen.blit(pic23, (mx-cw/2, my-ch/2))#blits picture where you click 

        elif canvas.collidepoint(mx, my) and tool == "vegeta":
            cw = pic24.get_width()
            ch = pic24.get_height()
            screen.blit(lines, canvas)
            if mb[0] == 1:
                down = True
                screen.blit(pic24, (mx-cw/2, my-ch/2))

        elif canvas.collidepoint(mx, my) and tool == "gohan":
            cw = pic25.get_width()
            ch = pic25.get_height()
            screen.blit(lines, canvas)
            screen.blit(pic25, (mx-cw/2, my-ch/2))
            if mb[0] == 1:
                down = True
                screen.blit(pic25, (mx-cw/2, my-ch/2))

        elif canvas.collidepoint(mx, my) and tool == "frieza":
            cw = pic26.get_width()
            ch = pic26.get_height()
            screen.blit(lines, canvas)
            screen.blit(pic26, (mx-cw/2, my-ch/2))
            if mb[0] == 1:
                down = True
                screen.blit(pic26, (mx-cw/2, my-ch/2))

        elif canvas.collidepoint(mx, my) and tool == "cell":
            cw = pic27.get_width()
            ch = pic27.get_height()
            screen.blit(lines, canvas)
            screen.blit(pic27, (mx-cw/2, my-ch/2))
            if mb[0] == 1:
                down = True
                screen.blit(pic27, (mx-cw/2, my-ch/2))

        elif canvas.collidepoint(mx, my) and tool == "buu":
            cw = pic28.get_width()
            ch = pic28.get_height()
            screen.blit(lines, canvas)
            screen.blit(pic28, (mx-cw/2, my-ch/2))
            if mb[0] == 1:
                down = True
                screen.blit(pic28, (mx-cw/2, my-ch/2))
            
        screen.set_clip(None) #sets clip so it doesn't go over canvas
#-----------------------------------------------------------------------------
    omx,omy = mx,my #fills in holes so drawing is crisp
    display.flip ()
quit()

    
