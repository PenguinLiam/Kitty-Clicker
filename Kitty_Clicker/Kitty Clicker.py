import pygame as py
#import UpgradesTab

#the font of everything in the game
gamefont = "Calibri"

#Value of clicks
ClickValue = 1

#Cost of Upgrades
CFCost = 5000
MCost = 20000
BCost = 55000
RCCost = 127000

#Cost of Shops
CLCost = 100
PSCost = 500
CBCost = 1500
CTCost = 5000
ECost = 60000
FCost = 1000000
CFCost = 100000000
QECost = 100000000000

#Increase in cost of shops after purchase
CostIncrease = 1.15

#Increase in cost of upgrade after purchase
UCostIncrease = 5.5

#Screen Dimentions
ScreenX = 640
ScreenY = 480

py.init()
screen = py.display.set_mode((ScreenX, ScreenY))
white = (255, 255, 255)
black = (0, 0, 0)

#Counter
def counter():
    font = py.font.SysFont(gamefont, 24)
    posx = ScreenX / 2.4
    posy = (ScreenY / 11) * 10
    size = font.size("Kitty Counter: " + str(round(kittens)))
    pos = (posx - size[0] / 2, posy - size[1] / 2)
    label = font.render("Kitty Counter: " + str(round(kittens)), 1, black)
    screen.blit(label, pos)

def cpscounter():
    global cps
    font = py.font.SysFont(gamefont, 20)
    posx = ScreenX / 2.4
    posy = ((ScreenY / 11) * 10) + ScreenY / 25 * 1
    size = font.size("Kittens/Sec: " + str(round(cps)))
    pos = (posx - size[0] / 2, posy - size[1] / 5)
    label = font.render("Kittens/Sec: " + str(round(cps)), 1, black)
    screen.blit(label, pos)
                
#Centre Kitten
class Kitty():
    def __init__(self, posx, posy):
        self.posx = ScreenX / 2.37 #start point
        self.posy = ScreenY / 2 #start point
        self.image = py.image.load("kitten.png")
    def Update(self):
        global kittens
        global clicks
        global ClickValue
        self.rect = py.Rect(0, 0, 242, 209)
        self.rect.center = (self.posx, self.posy)
        if self.rect.collidepoint(py.mouse.get_pos()):
            for event in events:
                if event.type == py.MOUSEBUTTONDOWN:
                    kittens += ClickValue
                    clicks += 1
    def Draw(self):
        image = py.transform.scale(self.image, (242, 209))
        screen.blit(image, self.rect)

#Upgrades on the left of the screen
class UpgradeButton(py.sprite.Sprite):
    def __init__(self, ButtonNumber, text, ID, colour):
        super().__init__()
        self.colour = colour
        self.posx = 0 #start position
        self.posy = ScreenY / 9
        self.ButtonNumber = ButtonNumber
        self.text = text
        self.ID = ID
    def update(self):
        global ClickValue
        global kittens
        global cps
        global UCostIncrease
        global CatFood
        global Milk
        global Bed
        global RescueCentre
        global CFCost
        self.rect = py.Rect(self.posx, self.posy * self.ButtonNumber, ScreenX / 8, ScreenY / 9)
        font = py.font.SysFont(gamefont, 22)
        label = font.render(self.text, 1, black)
        py.draw.rect(screen, self.colour, self.rect)
        py.draw.rect(screen, black, self.rect, 1)
        screen.blit(label, self.rect)
        if self.rect.collidepoint(py.mouse.get_pos()):
            for event in events:
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.ID == "CF":
                        if kittens < CFCost:
                            ClickValue = ClickValue
                        elif kittens >= CFCost:
                            kittens -= CFCost
                            CFCost *= UCostIncrease
                            CatFood += 1
                    if self.ID == "M":
                        if kittens < MCost:
                            print("Too low")
                        elif kittens >= MCost:
                            print("Yeah")
                    
#Shops on the right of screen
class ShopButton(py.sprite.Sprite):
    def __init__(self, ButtonNumber, text, ID, colour, description):
        super().__init__()
        self.colour = colour
        self.posx = 450
        self.posy = ScreenY / 9 #start point
        self.ButtonNumber = ButtonNumber
        self.text = text
        self.ID = ID
        self.description = description
        self.ttext = []
    def update(self):
        global clicks
        global kittens
        global CatLady
        global PetStore
        global CatBreeder
        global CatTrap
        global Ebay
        global Factory
        global CloningFacility
        global QMarkEMark
        global CLCost
        global PSCost
        global CBCost
        global CTCost
        global ECost
        global FCost
        global CFCost
        global QECost
        global CostIncrease
        global hovering
        if self.ID == "CL":
            self.ttext = [" Cost: " + str(round(CLCost))]
        elif self.ID == "PS":
            self.ttext = [" Cost: " + str(round(PSCost))]
        elif self.ID == "CB":
            self.ttext = [" Cost: " + str(round(CBCost))]
        elif self.ID == "CT":
            self.ttext = [" Cost: " + str(round(CTCost))]
        elif self.ID == "E":
            self.ttext = [" Cost: " + str(round(ECost))]
        elif self.ID == "F":
            self.ttext = [" Cost: " + str(round(FCost))]
        elif self.ID == "CF":
            self.ttext = [" Cost: " + str(round(CFCost))]
        elif self.ID == "?!":
            self.ttext = [" Cost: " + str(round(QECost))]
        self.ttext.extend(self.description.split("|"))
        self.rect = py.Rect((ScreenX / 14) * 10.5, (ScreenY / 9) * self.ButtonNumber, ScreenX, (ScreenY / 9))
        font = py.font.SysFont(gamefont, 22)
        label = font.render(self.text, 1, black)
        py.draw.rect(screen, self.colour, self.rect)
        py.draw.rect(screen, black, self.rect, 1)
        screen.blit(label, self.rect)
        if self.rect.collidepoint(py.mouse.get_pos()):
            for event in events:
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.ID == "CL":
                        if kittens < CLCost:
                            CatLady = CatLady
                        elif kittens >= CLCost:
                            kittens -= CLCost
                            CLCost *= CostIncrease
                            print(CLCost)
                            CatLady += 1
                    if self.ID == "PS":
                        if kittens < PSCost:
                            PetStore = PetStore
                        elif kittens >= PSCost:
                            kittens -= PSCost
                            PSCost *= CostIncrease
                            PetStore += 1
                    if self.ID == "CB":
                        if kittens < CBCost:
                            CatBreeder += CatBreeder
                        elif kittens >= CBCost:
                            kittens -= CBCost
                            CBCost *= CostIncrease
                            CatBreeder += 1
                    if self.ID == "CT":
                        if kittens < CTCost:
                            CatTrap += CatTrap
                        elif kittens >= CTCost:
                            kittens -= CTCost
                            CTCost *= CostIncrease
                            CatTrap += 1
                    if self.ID == "E":
                        if kittens < ECost:
                            Ebay += Ebay
                        elif kittens >= ECost:
                            kittens -= ECost
                            ECost *= CostIncrease
                            Ebay += 1
                    if self.ID == "F":
                        if kittens < FCost:
                            Factory += Factory
                        elif kittens >= FCost:
                            kittens -= FCost
                            FCost *= CostIncrease
                            Factory += 1
                    if self.ID == "CF":
                        if kittens < CFCost:
                            CloningFacility += CloningFacility
                        elif kittens >= CFCost:
                            kittens -= CFCost
                            CFCost *= CostIncrease
                            CloningFacility += 1
                    if self.ID == "?!":
                        if kittens < QECost:
                            QMarkEMark += QMarkEMark
                        elif kittens >= QECost:
                            kittens -= QECost
                            QECost *= CostIncrease
                            QMarkEMark += 1
        if self.rect.collidepoint(py.mouse.get_pos()):
            hovering = self.ttext


def hover():
    if hovering != None:
        trect = py.Rect((py.mouse.get_pos()[0] - 300, py.mouse.get_pos()[1]), (300, 53))
        if py.mouse.get_pos()[1] > ScreenY * 0.8:
            trect.centery -= 50
        py.draw.rect(screen, (191, 191, 191), trect)
        py.draw.rect(screen, black, trect, 1)
        ymod = 0
        textsize = 24
        for t in hovering:
            font = py.font.SysFont(gamefont, textsize)
            tlabel = font.render(t, 1, black)
            trect.centery += ymod
            screen.blit(tlabel, (trect[0], trect[1] + ymod))
            if ymod == 0:
                ymod += 10
            else:
                ymod += 2
            if textsize == 24:
                textsize = 15

#Tabs at the top of the screen
class Tabs(py.sprite.Sprite):
    def __init__(self, ButtonNumber, text, ID, colour):
        super().__init__()
        self.ButtonNumber = ButtonNumber
        self.text = text
        self.ID = ID
        self.colour = colour
        self.posx = ScreenX / 3
        self.posy = 0
    def update(self):
        global page
        self.rect = py.Rect(0, 0, ScreenX / 9, ScreenY / 3)
        self.rect = py.Rect((self.posx * self.ButtonNumber) - self.posx, self.posy, (ScreenX / 3), (ScreenY / 9))
        font = py.font.SysFont(gamefont, 28)
        label = font.render(self.text, 1, black)
        py.draw.rect(screen, self.colour, self.rect)
        py.draw.rect(screen, black, self.rect, 1)
        screen.blit(label, self.rect)
        if self.rect.collidepoint(py.mouse.get_pos()):
            for event in events:
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.ID == "UP":
                        page = 2
                    if self.ID == "ST":
                        page = 3
                    if self.ID == "AC":
                        page = 4

class BackButton(py.sprite.Sprite):
    def __init__(self, text, ID, colour):
        super().__init__()
        self.text = text
        self.ID = ID
        self.colour = colour
        self.posx = 0
        self.posy = 0
    def update(self):
        global page
        self.rect = py.Rect(0, 0 + ((ScreenY / 9) * 8), 100, 100)
        font = py.font.SysFont(gamefont, 26)
        label = font.render(self.text, 1, black)
        py.draw.rect(screen, self.colour, self.rect)
        py.draw.rect(screen, black, self.rect, 1)
        screen.blit(label, self.rect)
        if self.rect.collidepoint(py.mouse.get_pos()):
            for event in events:
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.ID == "BACK":
                        page = 1


time = 0
clicks = 0
kittens = 0
CatLady = 0
PetStore = 0
CatBreeder = 0
CatTrap = 0
Ebay = 0
Factory = 0
CloningFacility = 0
QMarkEMark = 0
CatFood = 0
cps = 0
hovering = None
k = Kitty(320, 240)
RButtons = py.sprite.Group()
RButtons.add(ShopButton(1, "Cat Lady", "CL", (255, 51, 0), " Spends her days collecting cats, even if they| have an owner"))
RButtons.add(ShopButton(2, "Pet Store", "PS", (255, 192, 0), " A place to go if you want affection! I spend| most of my life there"))
RButtons.add(ShopButton(3, "Cat Breeder", "CB", (255, 255, 0), " 'What happens when you mix a Tabby with a| Pursian?' - Steve 2015"))
RButtons.add(ShopButton(4, "Cat Trap", "CT", (146, 208, 80)," The Cat Lady's master contraption for| snatching their little kitty friends"))
RButtons.add(ShopButton(5, "Ebay", "E", (0, 176, 240), " Wait what? There is something very| wrong here...? "))
RButtons.add(ShopButton(6, "Factory", "F", (132, 236, 250)," Out of the steel works of Yorkshire come little| kittens in hard hats"))
RButtons.add(ShopButton(7, "Cloning Facility", "CF", (229, 117, 255), " Some say its unethical, but can you argue| with the cute meows of a army of kittens?"))
RButtons.add(ShopButton(8, "?!?!", "?!", (249, 206, 250), " A Super-Massive-Cat-Magnet of alien creation| to harness the power of the meow"))
LButtons = py.sprite.Group()
LButtons.add(UpgradeButton(1, "Cat Food", "CF", (249, 206, 250)))
LButtons.add(UpgradeButton(2, "Milk", "M", (229, 117, 255)))
LButtons.add(UpgradeButton(3, "Bed", "B", (132, 236, 250)))
LButtons.add(UpgradeButton(4, "Rescue Centre", "RC", (0, 176, 240)))
LButtons.add(UpgradeButton(5, "More Workers", "MW", (146, 208, 80)))
LButtons.add(UpgradeButton(6, "Fibre Optics", "FO", (255, 255, 0)))
LButtons.add(UpgradeButton(7, "Mad Scientists", "MS", (255, 192, 0)))
LButtons.add(UpgradeButton(8, "Bigger Magnets", "BM", (255, 51, 0)))
TopTabs = py.sprite.Group()
TopTabs.add(Tabs(1, "Upgrades", "UP", (231, 230, 230)))
TopTabs.add(Tabs(2, "Stats", "ST", (231, 230, 230)))
TopTabs.add(Tabs(3, "Achievements", "AC", (231, 230, 230)))
bbutton = py.sprite.Group()
bbutton.add(BackButton("Back", "BACK", (231, 230, 230)))
clock = py.time.Clock()
py.time.set_timer(py.USEREVENT, 1000)
page = 1

while True:
    clock.tick(60)
    hovering = None
    py.event.pump()
    events = []
    events = py.event.get()
    cps += CatLady
    cps += PetStore * 5 #5 = amount per second added
    cps += CatBreeder * 10
    cps += CatTrap * 40
    cps += Ebay * 75
    cps += Factory * 100
    cps += CloningFacility * 250
    cps += QMarkEMark * 1500
    fastcounter = cps / 60
    kittens += fastcounter
    kitens = kittens
    #print("CATLADY:", int(CatLady))
    #print("PETSTORE:", int(PetStore))
    #print("CATBREEDER:", int(CatBreeder))
    #print("CATTRAP:", int(CatTrap))
    #print("EBAY:", int(Ebay))
    #print("FACTORY:", int(Factory))        
    #print("CLONINGFACILITY:", int(CloningFacility))
    #print("?!?!:", int(QMarkEMark))
    #print(round(kittens))
    #print("CATS/SEC:", int(cps))
    if page == 1: #Main
        screen.fill((149, 211, 232))
        TopTabs.update()
        k.Update()
        k.Draw()
        RButtons.update()
        LButtons.update()
        counter()
        cpscounter()
        cps = 0
        fastcounter = 0
    if page == 2: #Upgrades tab
        screen.fill((149, 211, 232))
        TopTabs.update()
        bbutton.update()
    if page == 3: #Statistics tab
        screen.fill((149, 211, 232))
        TopTabs.update()
        bbutton.update()
    if page == 4: #Achievements tab
        screen.fill((149, 211, 232))
        TopTabs.update()
        bbutton.update()
    hover()
    py.display.flip()

#fix upgrades to make them double cps
#add tabs to access other upgrades (in progress)
#put counter into a rect
#add box around centre kitty
#add amount boxes
#work out colour scheme for drop sown boxes
#add cps counter
#add kitten silhouettes
#add a profile tab for different kittens and upgrades
