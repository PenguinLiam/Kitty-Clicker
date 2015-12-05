import pygame as py
ScrollY = 0

class item_that_scrolls(py.sprite.Sprite):
    
    def __init__(self, posx, posy):
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.image = IMAGE
    
    def update(self):
        self.rect = py.Rect(self.posx, self.posy + ScrollY, SIZEX, SIZEY) #Sets items y position to it's base y pos + the amount of scroll.



class scrollBar(py.sprite.Sprite): 
    
    def __init__(self):
        self.posx = screen * 0.9
        self.posy = ScrollY
        self.image = py.Surface((SIZEX, SIZEY))
        self.image.fill((100, 100, 100))
        self.oldPos = None
    
    def update(self):
        self.posy = ScrollY
        self.rect = (self.posx, self.posy, SIZEX, SIZEY) #creates rect based on variables
        if self.rect.collidepoint(py.mouse.get_pos()) and py.mouse.get_pressed()[0]: #If the mouse it touching the scrollbar and the left mouse button is pressed...
            if self.old != None: #If there was a previous y value
                if py.mouse.get_pos()[1] < self.oldPos: # if the mouse is higher than the old y position
                    ScrollY -= py.mouse.get_pos()[1] - self.oldPos # Adjust scrolly
                    self.posy = ScrollY # set y pos to scrolly
                if py.mouse.get_pos()[1] > self.oldPos: # if the mouse is lower than the old y position
                    ScrollY += py.mouse.get_pos()[1] - self.oldPos # Adjust scrolly
                    self.posy = ScrollY # set y pos to scrolly
            self.oldPos = self.posy #store current y pos
        else:
            self.oldPos = None # clear old y pos

#Then create a button that adjusts scrollY.
#You may have to adjust some values.
#THIS IS JUST AN EXAMPLE. I do not recommend simply copying and pasting.
