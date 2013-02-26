import sys

from graphics import *
from random import *

g = GraphWin("Quarto!", 500, 500)
g.setBackground(color_rgb(125, 125, 125))

status1 = Text(Point(250, 50), "")
status1.setText("Quarto!")
status1.setSize(36)
status1.draw(g)

status2 = Text(Point(250, 150), "")
status2.setText("Click to continue")
status2.setSize(20)
status2.draw(g)

rules = Text(Point(250, 350), "")
rules.setText("To play, you and your opponent will take turns \n \n giving each other pieces to place on the board. \n \n Each unique piece has 4 different attributes: \n \n \n Square or Round, Tall or Short, Light or Dark, and Soild or Hollow \n \n \n  To win, force your opponant to place a piece that forms a Quarto: \n \n a row of 4 pieces with one of those attributes in common. \n \n \n Have fun!")
rules.setSize(14)
rules.draw(g)

p = g.getMouse()
rules.setFill(color_rgb(125, 125, 125))
#####################
#Background Elements#
#####################

bg = Circle(Point(250, 175), 156)
bg.setFill(color_rgb(125, 50, 25))
bg.draw(g)

bg = Circle(Point(250, 175), 150)
bg.setFill(color_rgb(200, 123, 50))
bg.draw(g)

#############
#Inner Rings#
#############

#       c1       #
#     a5 a1      #     
#    a6 c2 a2    #
#   b1 b2 b3 b4  #
#    a8 c3 a4    #
#     a7 a3      #
#      c4        #

# c1 = (226, 28), (274, 76)
# c2 = (226, 109), (274, 157)
# c3 = (226, 191), (274, 239)
# c4 = (226, 268), (274, 316)
#
# b1 = (104, 151), (152, 199)
# b2 = (183, 151), (231, 199)
# b3 = (271, 151), (319, 199)
# b4 = (348. 151), (248, 199)
#
# a1 = (271, 68), (319, 116)
# a2 = (309, 109), (357, 157)
# a3 = (271, 229), (319, 277)
# a4 = (309, 191), (357, 239)
# a5 = (183, 68), (231, 116)
# a6 = (141, 109), (189, 157)
# a7 = (183, 229), (231, 277)
# a8 = (141, 191), (396, 239)

#Vertical Down
c1 = Circle(Point(250, 52), 24)
c1.draw(g)
c2 = Circle(Point(250, 133), 24)
c2.draw(g)
c3 = Circle(Point(250, 215), 24)
c3.draw(g)
c4 = Circle(Point(250, 292), 24)
c4.draw(g)

#Left to Right Middle
b1 = Circle(Point(128, 175), 24)
b1.draw(g)
b2 = Circle(Point(207, 175), 24)
b2.draw(g)
b3 = Circle(Point(295, 175), 24)
b3.draw(g)
b4 = Circle(Point(372, 175), 24)
b4.draw(g)

#TopRight
a1 = Circle(Point(295, 92), 24)
a1.draw(g)
a2 = Circle(Point(333, 133), 24)
a2.draw(g)

#BottemRight
a3 = Circle(Point(295, 253), 24)
a3.draw(g)
a4 = Circle(Point(333, 215), 24)
a4.draw(g)

#TopLeft
a5 = Circle(Point(207, 92), 24)
a5.draw(g)
a6 = Circle(Point(165, 133), 24)
a6.draw(g)

#BottemLeft
a7 = Circle(Point(207, 253), 24)
a7.draw(g)
a8 = Circle(Point(165, 215), 24)
a8.draw(g)

###################
#Outer Inner Rings#
###################

#Up Down
c1 = Circle(Point(250, 52), 23)
c1.draw(g)
c2 = Circle(Point(250, 133), 23)
c2.draw(g)
c3 = Circle(Point(250, 215), 23)
c3.draw(g)
c4 = Circle(Point(250, 292), 23)
c4.draw(g)

#Sideways
b1 = Circle(Point(128, 175), 23)
b1.draw(g)
b2 = Circle(Point(207, 175), 23)
b2.draw(g)
b3 = Circle(Point(295, 175), 23)
b3.draw(g)
b4 = Circle(Point(372, 175), 23)
b4.draw(g)

#TopRight
a1 = Circle(Point(295, 92), 23)
a1.draw(g)
a2 = Circle(Point(333, 133), 23)
a2.draw(g)

#BottemRight
a3 = Circle(Point(295, 253), 23)
a3.draw(g)
a4 = Circle(Point(333, 215), 23)
a4.draw(g)

#TopLeft
a5 = Circle(Point(207, 92), 23)
a5.draw(g)
a6 = Circle(Point(165, 133), 23)
a6.draw(g)

#BottemLeft
a7 = Circle(Point(207, 253), 23)
a7.draw(g)
a8 = Circle(Point(165, 215), 23)
a8.draw(g)

#Piece Table
r = Rectangle(Point(17, 400), Point(490, 490))
r.setFill(color_rgb(130, 130, 130))
r.draw(g)

#Place next piece
r2 = Rectangle(Point(450, 357), Point(490, 397))
r2.setFill(color_rgb(125, 125, 125))
r2.draw(g)

r3 = Rectangle(Point(17, 357), Point(57, 397))
r3.setFill(color_rgb(125, 125, 125))
r3.draw(g)

play = Text(Point(84, 391), "")
play.setText("Player")
play.setSize(15)
play.draw(g)

#Place next piece text
piece = Text(Point(425, 391), "")
piece.setText("Place")
piece.setSize(15)
piece.draw(g)

player = 1

playertext = Text(Point(37, 379), "")
playertext.setText("2")
playertext.setSize(25)
playertext.draw(g)

status = Text(Point(255, 360), "")
status.setText("Welcome to Quarto! \n Player 2, please pick a piece for player 1 to play")
status.setSize(12)
status.draw(g)
# c1 = (226, 28), (274, 76)
# c2 = (226, 109), (274, 157)
# c3 = (226, 191), (274, 239)
# c4 = (226, 268), (274, 316)
#
# b1 = (104, 151), (152, 199)
# b2 = (183, 151), (231, 199)
# b3 = (271, 151), (319, 199)
# b4 = (348, 151), (396, 199)

#h = Rectangle(Point(226, 28), Point(274, 76))
#h.setFill(color_rgb(0, 0, 0))
#h.draw(g)
#h1 = Rectangle(Point(226, 109), Point(274, 157))
#h1.setFill(color_rgb(0, 0, 0))
#h1.draw(g)
#h2 = Rectangle(Point(226, 191), Point(274, 239))
#h2.setFill(color_rgb(0, 0, 0))
#h2.draw(g)
#h3 = Rectangle(Point(226, 268), Point(274, 316))
#h3.setFill(color_rgb(0, 0, 0))
#h3.draw(g)
#h4 = Rectangle(Point(104, 151), Point(152, 199))
#h4.setFill(color_rgb(0, 0, 0))
#h4.draw(g)
#h5 = Rectangle(Point(183, 151), Point(231, 199))
#h5.setFill(color_rgb(0, 0, 0))
#h5.draw(g)
#h6 = Rectangle(Point(271, 151), Point(319, 199))
#h6.setFill(color_rgb(0, 0, 0))
#h6.draw(g)
#h7 = Rectangle(Point(348, 151), Point(396, 199))
#h7.setFill(color_rgb(0, 0, 0))
#h7.draw(g)

# c1 = (226, 28), (274, 76)
# c2 = (226, 109), (274, 157)
# c3 = (226, 191), (274, 239)
# c4 = (226, 268), (274, 316)
# b1 = (104, 151), (152, 199)
# b2 = (183, 151), (231, 199)
# b3 = (271, 151), (319, 199)
# b4 = (348, 151), (396, 199)
# a1 = (271, 68), (319, 116)
# a2 = (309, 109), (357, 157)
# a3 = (271, 229), (319, 277)
# a4 = (309, 191), (357, 239)
# a5 = (183, 68), (231, 116)
# a6 = (141, 109), (189, 157)
# a7 = (183, 229), (231, 277)
# a8 = (141, 191), (189, 239)

#f = Rectangle(Point(271, 68), Point(319, 116))
#f.setFill(color_rgb(0, 0, 0))
#f.draw(g)
#f1 = Rectangle(Point(309, 109), Point(357, 157))
#f1.setFill(color_rgb(0, 0, 0))
#f1.draw(g)
#f2 = Rectangle(Point(271, 229), Point(319, 277))
#f2.setFill(color_rgb(0, 0, 0))
#f2.draw(g)
#f3 = Rectangle(Point(309, 191), Point(357, 239))
#f3.setFill(color_rgb(0, 0, 0))
#f3.draw(g)
#f4 = Rectangle(Point(183, 68), Point(231, 116))
#f4.setFill(color_rgb(0, 0, 0))
#f4.draw(g)
#f5 = Rectangle(Point(141, 109), Point(189, 157))
#f5.setFill(color_rgb(0, 0, 0))
#f5.draw(g)
#f6 = Rectangle(Point(183, 229), Point(231, 277))
#f6.setFill(color_rgb(0, 0, 0))
#f6.draw(g)
#f7 = Rectangle(Point(141, 191), Point(189, 239))
#f7.setFill(color_rgb(0, 0, 0))
#f7.draw(g)

########
#Pieces#
########

#b = block 
#r = round = Circle(Point(, ), 10/ 15)
#          .setFill(color_rgb(, , ))
#          .draw(g)

#f = fill
#h = hollow = Circle(Point(x + 10 / 15, y + 10 / 15), 5 / 10)
#          .setFill(color_rgb(, , ))
#          .draw(g)

#d = dark (0, 0, 0)
#l = light (255, 255, 255)

#s = short Rectangle(Point(x, y), Point(x + 20,y + 20))
#t = tall (x + 30, y + 30)

###############################################################################
# 1 bfdt  2 bhdt  3 bflt  4 bhlt |bt <--> rt|  5 rfdt  6 rhdt  7 rflt  8 rhlt #
# 9 bfds 10 bhds 11 bfls 12 bhls |bs <--> rs| 13 rfds 14 rhds 15 rfls 16 rhls #
###############################################################################

####
#BT#
####

#Position 1 ~ (30, 410), (60, 440)
bfdt = Rectangle(Point(30, 410), Point(60, 440))
bfdt.setFill(color_rgb(0, 0, 0))
bfdt.draw(g)

#Position 2 ~ (90, 410), (120, 440)
bhdt = Rectangle(Point(90, 410), Point(120, 440))
bhdt.setFill(color_rgb(0, 0, 0))
bhdt.draw(g)
bhdt1 = Circle(Point(105, 425), 10)
bhdt1.setFill(color_rgb(255, 255, 255))
bhdt1.draw(g)

#Position 3 ~ (150, 410), (180, 440)
bflt = Rectangle(Point(150, 410), Point(180, 440))
bflt.setFill(color_rgb(255, 255, 255))
bflt.draw(g)

#Position 4 ~ (210, 410), (240, 440)
bhlt = Rectangle(Point(210, 410), Point(240, 440))
bhlt.setFill(color_rgb(255, 255, 255))
bhlt.draw(g)
bhlt1 = Circle(Point(225, 425), 10)
bhlt1.setFill(color_rgb(0, 0, 0))
bhlt1.draw(g)

####
#RT#
####

#Position 5 ~ (265, 410), (295, 440)
rfdt = Circle(Point(280, 425), 15)
rfdt.setFill(color_rgb(0, 0, 0))
rfdt.draw(g)

#Position 6 ~ (325, 410), (355, 440)
rhdt = Circle(Point(340, 425), 15)
rhdt.setFill(color_rgb(0, 0, 0))
rhdt.draw(g)
rhdt1 = Circle(Point(340, 425), 10)
rhdt1.setFill(color_rgb(255, 255, 255))
rhdt1.draw(g)

#Position 7 ~ (385, 410), (415, 440)
rflt = Circle(Point(400, 425), 15)
rflt.setFill(color_rgb(255, 255, 255))
rflt.draw(g)

#Position 8 ~ (445, 410), (475, 440)
rhlt = Circle(Point(460, 425), 15)
rhlt.setFill(color_rgb(255, 255, 255))
rhlt.draw(g)
rhlt1 = Circle(Point(460, 425), 10)
rhlt1.setFill(color_rgb(0, 0, 0))
rhlt1.draw(g)

####
#BS#
####

#Position 9 ~ (20, 445), (70, 495)
bfds = Rectangle(Point(35, 460), Point(55, 480))
bfds.setFill(color_rgb(0, 0, 0))
bfds.draw(g)

#Position 10 ~ (80, 410), (130, 495)
bhds = Rectangle(Point(95, 460), Point(115, 480))
bhds.setFill(color_rgb(0, 0, 0))
bhds.draw(g)
bhds1 = Circle(Point(105, 470), 5)
bhds1.setFill(color_rgb(255, 255, 255))
bhds1.draw(g)

#Position 11 ~ (140, 410), (190, 495)
bfls = Rectangle(Point(155, 460), Point(175, 480))
bfls.setFill(color_rgb(255, 255, 255))
bfls.draw(g)

#Position 12 ~ (200, 410), (220, 495)
bhls = Rectangle(Point(215, 460), Point(235, 480))
bhls.setFill(color_rgb(255, 255, 255))
bhls.draw(g)
bhls1 = Circle(Point(225, 470), 5)
bhls1.setFill(color_rgb(0, 0, 0))
bhls1.draw(g)

####
#RS#
####

#Position 13 ~ (265, 455), (295, 485)
rfds = Circle(Point(280, 470), 10)
rfds.setFill(color_rgb(0, 0, 0))
rfds.draw(g)

#Position 14 ~ (325, 455), (355, 485)
rhds = Circle(Point(340, 470), 10)
rhds.setFill(color_rgb(0, 0, 0))
rhds.draw(g)
rhds1 = Circle(Point(340, 470), 5)
rhds1.setFill(color_rgb(255, 255, 255))
rhds1.draw(g)

#Position 15 ~ (385, 455), (415, 485)
rfls = Circle(Point(400, 470), 10)
rfls.setFill(color_rgb(255, 255, 255))
rfls.draw(g)

#Position 16 ~ (445, 455), (475, 485)
rhls = Circle(Point(460, 470), 10)
rhls.setFill(color_rgb(255, 255, 255))
rhls.draw(g)
rhls1 = Circle(Point(460, 470), 5)
rhls1.setFill(color_rgb(0, 0, 0))
rhls1.draw(g)


################
#Click Register#
################

#       c1       #
#     a5 a1      #     
#    a6 c2 a2    #
#   b1 b2 b3 b4  #
#    a8 c3 a4    #
#     a7 a3      #
#      c4        #



#r2 = Rectangle(Point(450, 357), Point(490, 397))
#r2.setFill(color_rgb(125, 125, 125))
#r2.draw(g)

game = True
placed = 0

p = g.getMouse()
x = p.getX()
y = p.getY()

# c1 = (226, 28), (274, 76)
# c2 = (226, 109), (274, 157)
# c3 = (226, 191), (274, 239)
# c4 = (226, 268), (274, 316)
#
# b1 = (104, 151), (152, 199)
# b2 = (183, 151), (231, 199)
# b3 = (271, 151), (319, 199)
# b4 = (348, 151), (396, 199)
#
# a1 = (271, 68), (319, 116)
# a2 = (309, 109), (357, 157)
# a3 = (271, 229), (319, 277)
# a4 = (309, 191), (357, 239)
# a5 = (183, 68), (231, 116)
# a6 = (141, 109), (189, 157)
# a7 = (183, 229), (231, 277)
# a8 = (141, 191), (396, 239)

roundWin = 0
rud1 = 0
rud2 = 0
rud3 = 0
rud4 = 0
rss1 = 0
rss2 = 0
rss3 = 0
rss4 = 0
rdi1 = 0
rdi2 = 0
#########
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#########
blockWin = 0
bud1 = 0
bud2 = 0
bud3 = 0
bud4 = 0
bss1 = 0
bss2 = 0
bss3 = 0
bss4 = 0
bdi1 = 0
bdi2 = 0
#########
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#########
fillWin = 0
fud1 = 0
fud2 = 0
fud3 = 0
fud4 = 0
fss1 = 0
fss2 = 0
fss3 = 0
fss4 = 0
fdi1 = 0
fdi2 = 0
#########
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#########
hollowWin = 0
hud1 = 0
hud2 = 0
hud3 = 0
hud4 = 0
hss1 = 0
hss2 = 0
hss3 = 0
hss4 = 0
hdi1 = 0
hdi2 = 0
#########
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#########
darkWin = 0
dud1 = 0
dud2 = 0
dud3 = 0
dud4 = 0
dss1 = 0
dss2 = 0
dss3 = 0
dss4 = 0
ddi1 = 0
ddi2 = 0
#########
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#########
lightWin = 0
lud1 = 0
lud2 = 0
lud3 = 0
lud4 = 0
lss1 = 0
lss2 = 0
lss3 = 0
lss4 = 0
ldi1 = 0
ldi2 = 0
#########
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#########
tallWin = 0
tud1 = 0
tud2 = 0
tud3 = 0
tud4 = 0
tss1 = 0
tss2 = 0
tss3 = 0
tss4 = 0
tdi1 = 0
tdi2 = 0
#########
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#########
shortWin = 0
sud1 = 0
sud2 = 0
sud3 = 0
sud4 = 0
sss1 = 0
sss2 = 0
sss3 = 0
sss4 = 0
sdi1 = 0
sdi2 = 0
#########
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#0,0,0,0#
#########



while placed != 16 and sud1 != 4 and sud2 != 4 and sud3 != 4 and sud4 != 4 and sss1 != 4 and sss2 != 4 and sss3 != 4 and sss4 != 4 and sdi1 != 4 and sdi2 != 4 and tud1 != 4 and tud2 != 4 and tud3 != 4 and tud4 != 4 and tss1 != 4 and tss2 != 4 and tss3 != 4 and tss4 != 4 and tdi1 != 4 and tdi2 != 4 and lud1 != 4 and lud2 != 4 and lud3 != 4 and lud4 != 4 and lss1 != 4 and lss2 != 4 and lss3 != 4 and lss4 != 4 and ldi1 != 4 and ldi2 != 4 and dud1 != 4 and dud2 != 4 and dud3 != 4 and dud4 != 4 and dss1 != 4 and dss2 != 4 and dss3 != 4 and dss4 != 4 and ddi1 != 4 and ddi2 != 4 and hud1 != 4 and hud2 != 4 and hud3 != 4 and hud4 != 4 and hss1 != 4 and hss2 != 4 and hss3 != 4 and hss4 != 4 and hdi1 != 4 and hdi2 != 4 and fud1 != 4 and fud2 != 4 and fud3 != 4 and fud4 != 4 and fss1 != 4 and fss2 != 4 and fss3 != 4 and fss4 != 4 and fdi1 != 4 and fdi2 != 4 and bud1 != 4 and bud2 != 4 and bud3 != 4 and bud4 != 4 and bss1 != 4 and bss2 != 4 and bss3 != 4 and bss4 != 4 and bdi1 != 4 and bdi2 != 4 and rud1 != 4 and rud2 != 4 and rud3 != 4 and rud4 != 4 and rss1 != 4 and rss2 != 4 and rss3 != 4 and rss4 != 4 and rdi1 != 4 and rdi2 != 4:
    
    player += 1
    
    if player % 2 == 0:
        playertext.setText("1")
        lastplay = 1
        s = randint(1, 2)
        if s == 1:
            status.setText("Nice choice! \n Player 1, place your piece then choose Player 2's piece.")
        if s == 2:
            status.setText("Good move! \n Remember to check all 4 attributes of a \n piece before placing it on the board.")
    if player % 2 != 0:
        playertext.setText("2")
        lastplay = 2
        s = randint(1, 2)
        if s == 1:
            status.setText("Nice thinking! \n Player 2, place your piece then choose Player 1's piece.")
        if s == 2:
            status.setText("What a play! \n Before placing a piece, try to \n anticipate how the other peices \n will help or hurt you in the future")
    
    if x >= 28 and x <= 62 and y >= 408 and y <= 442:
        o1 = Rectangle(Point(28, 408), Point(62, 442))
        o1.setFill(color_rgb(125, 125, 125))
        o1.draw(g)
        bfdt0 = Rectangle(Point(455, 362), Point(485, 392))
        bfdt0.setFill(color_rgb(0, 0, 0))
        bfdt0.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()
        
        if player % 2 == 0:
            playertext.setText("1")
            lastplay = 1
        if player % 2 != 0:
            playertext.setText("2")
            lastplay = 2
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 38), Point(266, 68))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud4 += 1
            bss4 += 1
            bdi2 += 1
            fud4 += 1
            fss4 += 1
            fdi2 += 1
            dud4 += 1
            dss4 += 1
            ddi2 += 1
            tud4 += 1
            tss4 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 119), Point(266, 149))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud3 += 1
            bss3 += 1
            bdi2 += 1
            fud3 += 1
            fss3 += 1
            fdi2 += 1
            dud3 += 1
            dss3 += 1
            ddi2 += 1
            tud3 += 1
            tss3 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 201), Point(266, 231))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud2 += 1
            bss2 += 1
            bdi2 += 1
            fud2 += 1
            fss2 += 1
            fdi2 += 1
            dud2 += 1
            dss2 += 1
            ddi2 += 1
            tud2 += 1
            tss2 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 278), Point(266, 308))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud1 += 1
            bss1 += 1
            bdi2 += 1
            fud1 += 1
            fss1 += 1
            fdi2 += 1
            dud1 += 1
            dss1 += 1
            ddi2 += 1
            tud1 += 1
            tss1 += 1
            tdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(114, 161), Point(144, 191))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud4 += 1
            bss1 += 1
            bdi1 += 1
            fud4 += 1
            fss1 += 1
            fdi1 += 1
            dud4 += 1
            dss1 += 1
            ddi1 += 1
            tud4 += 1
            tss1 += 1
            tdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 161), Point(223, 191))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud3 += 1
            bss2 += 1
            bdi1 += 1
            fud3 += 1
            fss2 += 1
            fdi1 += 1
            dud3 += 1
            dss2 += 1
            ddi1 += 1
            tud3 += 1
            tss2 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 161), Point(311, 191))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud2 += 1
            bss3 += 1
            bdi1 += 1
            fud2 += 1
            fss3 += 1
            fdi1 += 1
            dud2 += 1
            dss3 += 1
            ddi1 += 1
            tud2 += 1
            tss3 += 1
            tdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(358, 161), Point(388, 191))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud1 += 1
            bss4 += 1
            bdi1 += 1
            fud1 += 1
            fss4 += 1
            fdi1 += 1
            dud1 += 1
            dss4 += 1
            ddi1 += 1
            tud1 += 1
            tss4 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 78), Point(311, 108))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud3 += 1
            bss4 += 1
            fud3 += 1
            fss4 += 1
            dud3 += 1
            dss4 += 1
            tud3 += 1
            tss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(319, 119), Point(349, 149))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud2 += 1
            bss4 += 1
            fud2 += 1
            fss4 += 1
            dud2 += 1
            dss4 += 1
            tud2 += 1
            tss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 239), Point(311, 269))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud1 += 1
            bss2 += 1
            fud1 += 1
            fss2 += 1
            dud1 += 1
            dss2 += 1
            tud1 += 1
            tss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(319, 201), Point(349, 231))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud1 += 1
            bss3 += 1
            fud1 += 1
            fss3 += 1
            dud1 += 1
            dss3 += 1
            tud1 += 1
            tss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 78), Point(223, 108))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud4 += 1
            bss3 += 1
            fud4 += 1
            fss3 += 1
            dud4 += 1
            dss3 += 1
            tud4 += 1
            tss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(151, 119), Point(181, 149))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud4 += 1
            bss2 += 1
            fud4 += 1
            fss2 += 1
            dud4 += 1
            dss2 += 1
            tud4 += 1
            tss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 239), Point(223, 269))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud2 += 1
            bss1 += 1
            fud2 += 1
            fss1 += 1
            dud2 += 1
            dss1 += 1
            tud2 += 1
            tss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(151, 201), Point(181, 231))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud3 += 1
            bss1 += 1
            fud3 += 1
            fss1 += 1
            dud3 += 1
            dss1 += 1
            tud3 += 1
            tss1 += 1
            
# 2            
    if x >= 88 and x <= 122 and y >= 408 and y <= 442:
        o2 = Rectangle(Point(88, 408), Point(122, 442))
        o2.setFill(color_rgb(125, 125, 125))
        o2.draw(g)
        bhdt0 = Rectangle(Point(455, 362), Point(485, 392))
        bhdt0.setFill(color_rgb(0, 0, 0))
        bhdt0.draw(g)
        bhdt10 = Circle(Point(470, 377), 10)
        bhdt10.setFill(color_rgb(255, 255, 255))
        bhdt10.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 38), Point(266, 68))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 53), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)            
            bud4 += 1
            bss4 += 1
            bdi2 += 1
            hud4 += 1
            hss4 += 1
            hdi2 += 1
            dud4 += 1
            dss4 += 1
            ddi2 += 1
            tud4 += 1
            tss4 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 119), Point(266, 149))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 134), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)
            bud3 += 1
            bss3 += 1
            bdi2 += 1
            hud3 += 1
            hss3 += 1
            hdi2 += 1
            dud3 += 1
            dss3 += 1
            ddi2 += 1
            tud3 += 1
            tss3 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 201), Point(266, 231))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 216), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)
            bud2 += 1
            bss2 += 1
            bdi2 += 1
            hud2 += 1
            hss2 += 1
            hdi2 += 1
            dud2 += 1
            dss2 += 1
            ddi2 += 1
            tud2 += 1
            tss2 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 278), Point(266, 308))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 293), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)
            bud1 += 1
            bss1 += 1
            bdi2 += 1
            hud1 += 1
            hss1 += 1
            hdi2 += 1
            dud1 += 1
            dss1 += 1
            ddi2 += 1
            tud1 += 1
            tss1 += 1
            tdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(114, 161), Point(144, 191))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(129, 176), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)
            bud4 += 1
            bss1 += 1
            bdi1 += 1
            hud4 += 1
            hss1 += 1
            hdi1 += 1
            dud4 += 1
            dss1 += 1
            ddi1 += 1
            tud4 += 1
            tss1 += 1
            tdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 161), Point(223, 191))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 176), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g) 
            bud3 += 1
            bss2 += 1
            bdi1 += 1
            hud3 += 1
            hss2 += 1
            hdi1 += 1
            dud3 += 1
            dss2 += 1
            ddi1 += 1
            tud3 += 1
            tss2 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 161), Point(311, 191))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 176), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud2 += 1
            bss3 += 1
            bdi1 += 1
            hud2 += 1
            hss3 += 1
            hdi1 += 1
            dud2 += 1
            dss3 += 1
            ddi1 += 1
            tud2 += 1
            tss3 += 1
            tdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(358, 161), Point(388, 191))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(373, 176), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)
            bud1 += 1
            bss4 += 1
            bdi1 += 1
            hud1 += 1
            hss4 += 1
            hdi1 += 1
            dud1 += 1
            dss4 += 1
            ddi1 += 1
            tud1 += 1
            tss4 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 78), Point(311, 108))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 93), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud3 += 1
            bss4 += 1
            hud3 += 1
            hss4 += 1
            dud3 += 1
            dss4 += 1
            tud3 += 1
            tss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(319, 119), Point(349, 149))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(334, 134), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                       
            bud2 += 1
            bss4 += 1
            hud2 += 1
            hss4 += 1
            dud2 += 1
            dss4 += 1
            tud2 += 1
            tss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 239), Point(311, 269))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 254), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)            
            bud1 += 1
            bss2 += 1
            hud1 += 1
            hss2 += 1
            dud1 += 1
            dss2 += 1
            tud1 += 1
            tss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(319, 201), Point(349, 231))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(334, 216), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud1 += 1
            bss3 += 1
            hud1 += 1
            hss3 += 1
            dud1 += 1
            dss3 += 1
            tud1 += 1
            tss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 78), Point(223, 108))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 93), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud4 += 1
            bss3 += 1
            hud4 += 1
            hss3 += 1
            dud4 += 1
            dss3 += 1
            tud4 += 1
            tss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(151, 119), Point(181, 149))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(166, 134), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud4 += 1
            bss2 += 1
            hud4 += 1
            hss2 += 1
            dud4 += 1
            dss2 += 1
            tud4 += 1
            tss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 239), Point(223, 269))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 254), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud2 += 1
            bss1 += 1
            hud2 += 1
            hss1 += 1
            dud2 += 1
            dss1 += 1
            tud2 += 1
            tss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(151, 201), Point(181, 231))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(166, 216), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud3 += 1
            bss1 += 1
            hud3 += 1
            hss1 += 1
            dud3 += 1
            dss1 += 1
            tud3 += 1
            tss1 += 1
# 3
    if x >= 148 and x <= 182 and y >= 408 and y <= 442:
        o3 = Rectangle(Point(148, 408), Point(182, 442))
        o3.setFill(color_rgb(125, 125, 125))
        o3.draw(g)
        bflt0 = Rectangle(Point(455, 362), Point(485, 392))
        bflt0.setFill(color_rgb(255, 255, 255))
        bflt0.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 38), Point(266, 68))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bud4 += 1
            bss4 += 1
            bdi2 += 1
            fud4 += 1
            fss4 += 1
            fdi2 += 1
            lud4 += 1
            lss4 += 1
            ldi2 += 1
            tud4 += 1
            tss4 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 119), Point(266, 149))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bud3 += 1
            bss3 += 1
            bdi2 += 1
            fud3 += 1
            fss3 += 1
            fdi2 += 1
            lud3 += 1
            lss3 += 1
            ldi2 += 1
            tud3 += 1
            tss3 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 201), Point(266, 231))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bud2 += 1
            bss2 += 1
            bdi2 += 1
            fud2 += 1
            fss2 += 1
            fdi2 += 1
            lud2 += 1
            lss2 += 1
            ldi2 += 1
            tud2 += 1
            tss2 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 278), Point(266, 308))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud1 += 1
            bss1 += 1
            bdi2 += 1
            fud1 += 1
            fss1 += 1
            fdi2 += 1
            lud1 += 1
            lss1 += 1
            ldi2 += 1
            tud1 += 1
            tss1 += 1
            tdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(114, 161), Point(144, 191))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud4 += 1
            bss1 += 1
            bdi1 += 1
            fud4 += 1
            fss1 += 1
            fdi1 += 1
            lud4 += 1
            lss1 += 1
            ldi1 += 1
            tud4 += 1
            tss1 += 1
            tdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 161), Point(223, 191))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud3 += 1
            bss2 += 1
            bdi1 += 1
            fud3 += 1
            fss2 += 1
            fdi1 += 1
            lud3 += 1
            lss2 += 1
            ldi1 += 1
            tud3 += 1
            tss2 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 161), Point(311, 191))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud2 += 1
            bss3 += 1
            bdi1 += 1
            fud2 += 1
            fss3 += 1
            fdi1 += 1
            lud2 += 1
            lss3 += 1
            ldi1 += 1
            tud2 += 1
            tss3 += 1
            tdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(358, 161), Point(388, 191))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud1 += 1
            bss4 += 1
            bdi1 += 1
            fud1 += 1
            fss4 += 1
            fdi1 += 1
            lud1 += 1
            lss4 += 1
            ldi1 += 1
            tud1 += 1
            tss4 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 78), Point(311, 108))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud3 += 1
            bss4 += 1
            fud3 += 1
            fss4 += 1
            lud3 += 1
            lss4 += 1
            tud3 += 1
            tss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(319, 119), Point(349, 149))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud2 += 1
            bss4 += 1
            fud2 += 1
            fss4 += 1
            lud2 += 1
            lss4 += 1
            tud2 += 1
            tss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 239), Point(311, 269))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)            
            bud1 += 1
            bss2 += 1
            fud1 += 1
            fss2 += 1
            lud1 += 1
            lss2 += 1
            tud1 += 1
            tss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(319, 201), Point(349, 231))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud1 += 1
            bss3 += 1
            fud1 += 1
            fss3 += 1
            lud1 += 1
            lss3 += 1
            tud1 += 1
            tss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 78), Point(223, 108))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud4 += 1
            bss3 += 1
            fud4 += 1
            fss3 += 1
            lud4 += 1
            lss3 += 1
            tud4 += 1
            tss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(151, 119), Point(181, 149))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud4 += 1
            bss2 += 1
            fud4 += 1
            fss2 += 1
            lud4 += 1
            lss2 += 1
            tud4 += 1
            tss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 239), Point(223, 269))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud2 += 1
            bss1 += 1
            fud2 += 1
            fss1 += 1
            lud2 += 1
            lss1 += 1
            tud2 += 1
            tss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(151, 201), Point(181, 231))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud3 += 1
            bss1 += 1
            fud3 += 1
            fss1 += 1
            lud3 += 1
            lss1 += 1
            tud3 += 1
            tss1 += 1
#4            
    if x >= 208 and x <= 242 and y >= 408 and y <= 442:
        o4 = Rectangle(Point(208, 408), Point(242, 442))
        o4.setFill(color_rgb(125, 125, 125))
        o4.draw(g)
        bhlt0 = Rectangle(Point(455, 362), Point(485, 392))
        bhlt0.setFill(color_rgb(255, 255, 255))
        bhlt0.draw(g)
        bhlt10 = Circle(Point(470, 377), 10)
        bhlt10.setFill(color_rgb(0, 0, 0))
        bhlt10.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 38), Point(266, 68))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 53), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)            
            bud4 += 1
            bss4 += 1
            bdi2 += 1
            hud4 += 1
            hss4 += 1
            hdi2 += 1
            lud4 += 1
            lss4 += 1
            ldi2 += 1
            tud4 += 1
            tss4 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 119), Point(266, 149))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 134), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)            
            bud3 += 1
            bss3 += 1
            bdi2 += 1
            hud3 += 1
            hss3 += 1
            hdi2 += 1
            lud3 += 1
            lss3 += 1
            ldi2 += 1
            tud3 += 1
            tss3 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 201), Point(266, 231))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 216), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)            
            bud2 += 1
            bss2 += 1
            bdi2 += 1
            hud2 += 1
            hss2 += 1
            hdi2 += 1
            lud2 += 1
            lss2 += 1
            ldi2 += 1
            tud2 += 1
            tss2 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(236, 278), Point(266, 308))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 293), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud1 += 1
            bss1 += 1
            bdi2 += 1
            hud1 += 1
            hss1 += 1
            hdi2 += 1
            lud1 += 1
            lss1 += 1
            ldi2 += 1
            tud1 += 1
            tss1 += 1
            tdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(114, 161), Point(144, 191))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(129, 176), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud4 += 1
            bss1 += 1
            bdi1 += 1
            hud4 += 1
            hss1 += 1
            hdi1 += 1
            lud4 += 1
            lss1 += 1
            ldi1 += 1
            tud4 += 1
            tss1 += 1
            tdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 161), Point(223, 191))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 176), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud3 += 1
            bss2 += 1
            bdi1 += 1
            hud3 += 1
            hss2 += 1
            hdi1 += 1
            lud3 += 1
            lss2 += 1
            ldi1 += 1
            tud3 += 1
            tss2 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 161), Point(311, 191))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 176), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud2 += 1
            bss3 += 1
            bdi1 += 1
            hud2 += 1
            hss3 += 1
            hdi1 += 1
            lud2 += 1
            lss3 += 1
            ldi1 += 1
            tud2 += 1
            tss3 += 1
            tdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(358, 161), Point(388, 191))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(373, 176), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud1 += 1
            bss4 += 1
            bdi1 += 1
            hud1 += 1
            hss4 += 1
            hdi1 += 1
            lud1 += 1
            lss4 += 1
            ldi1 += 1
            tud1 += 1
            tss4 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 78), Point(311, 108))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 93), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud3 += 1
            bss4 += 1
            hud3 += 1
            hss4 += 1
            lud3 += 1
            lss4 += 1
            tud3 += 1
            tss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(319, 119), Point(349, 149))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(334, 134), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud2 += 1
            bss4 += 1
            hud2 += 1
            hss4 += 1
            lud2 += 1
            lss4 += 1
            tud2 += 1
            tss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(281, 239), Point(311, 269))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 254), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud1 += 1
            bss2 += 1
            hud1 += 1
            hss2 += 1
            lud1 += 1
            lss2 += 1
            tud1 += 1
            tss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(319, 201), Point(349, 231))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(334, 216), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud1 += 1
            bss3 += 1
            hud1 += 1
            hss3 += 1
            lud1 += 1
            lss3 += 1
            tud1 += 1
            tss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 78), Point(223, 108))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 93), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud4 += 1
            bss3 += 1
            hud4 += 1
            hss3 += 1
            lud4 += 1
            lss3 += 1
            tud4 += 1
            tss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(151, 119), Point(181, 149))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(166, 134), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud4 += 1
            bss2 += 1
            hud4 += 1
            hss2 += 1
            lud4 += 1
            lss2 += 1
            tud4 += 1
            tss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(193, 239), Point(223, 269))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 254), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud2 += 1
            bss1 += 1
            hud2 += 1
            hss1 += 1
            lud2 += 1
            lss1 += 1
            tud2 += 1
            tss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(151, 201), Point(181, 231))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(166, 216), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                                    
            bud3 += 1
            bss1 += 1
            hud3 += 1
            hss1 += 1
            lud3 += 1
            lss1 += 1
            tud3 += 1
            tss1 += 1
# 5
    if x >= 263 and x <= 297 and y >= 408 and y <= 442:
        o5 = Rectangle(Point(263, 408), Point(297, 442))
        o5.setFill(color_rgb(125, 125, 125))
        o5.draw(g)
        rfdt0 = Circle(Point(470, 377), 15)
        rfdt0.setFill(color_rgb(0, 0, 0))
        rfdt0.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 52), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            rud4 += 1
            rss4 += 1
            rdi2 += 1
            fud4 += 1
            fss4 += 1
            fdi2 += 1
            dud4 += 1
            dss4 += 1
            ddi2 += 1
            tud4 += 1
            tss4 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 133), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            rud3 += 1
            rss3 += 1
            rdi2 += 1
            fud3 += 1
            fss3 += 1
            fdi2 += 1
            dud3 += 1
            dss3 += 1
            ddi2 += 1
            tud3 += 1
            tss3 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 215), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud2 += 1
            rss2 += 1
            rdi2 += 1
            fud2 += 1
            fss2 += 1
            fdi2 += 1
            dud2 += 1
            dss2 += 1
            ddi2 += 1
            tud2 += 1
            tss2 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 292), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud1 += 1
            rss1 += 1
            rdi2 += 1
            fud1 += 1
            fss1 += 1
            fdi2 += 1
            dud1 += 1
            dss1 += 1
            ddi2 += 1
            tud1 += 1
            tss1 += 1
            tdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(128, 175), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud4 += 1
            rss1 += 1
            rdi1 += 1
            fud4 += 1
            fss1 += 1
            fdi1 += 1
            dud4 += 1
            dss1 += 1
            ddi1 += 1
            tud4 += 1
            tss1 += 1
            tdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 175), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud3 += 1
            rss2 += 1
            rdi1 += 1
            fud3 += 1
            fss2 += 1
            fdi1 += 1
            dud3 += 1
            dss2 += 1
            ddi1 += 1
            tud3 += 1
            tss2 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 175), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud2 += 1
            rss3 += 1
            rdi1 += 1
            fud2 += 1
            fss3 += 1
            fdi1 += 1
            dud2 += 1
            dss3 += 1
            ddi1 += 1
            tud2 += 1
            tss3 += 1
            tdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(372, 175), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud1 += 1
            rss4 += 1
            rdi1 += 1
            fud1 += 1
            fss4 += 1
            fdi1 += 1
            dud1 += 1
            dss4 += 1
            ddi1 += 1
            tud1 += 1
            tss4 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 92), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud3 += 1
            rss4 += 1
            fud3 += 1
            fss4 += 1
            dud3 += 1
            dss4 += 1
            tud3 += 1
            tss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 133), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud2 += 1
            rss4 += 1
            fud2 += 1
            fss4 += 1
            dud2 += 1
            dss4 += 1
            tud2 += 1
            tss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 253), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)            
            rud1 += 1
            rss2 += 1
            fud1 += 1
            fss2 += 1
            dud1 += 1
            dss2 += 1
            tud1 += 1
            tss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 215), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud1 += 1
            rss3 += 1
            fud1 += 1
            fss3 += 1
            dud1 += 1
            dss3 += 1
            tud1 += 1
            tss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 92), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud4 += 1
            rss3 += 1
            fud4 += 1
            fss3 += 1
            dud4 += 1
            dss3 += 1
            tud4 += 1
            tss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 133), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud4 += 1
            rss2 += 1
            fud4 += 1
            fss2 += 1
            dud4 += 1
            dss2 += 1
            tud4 += 1
            tss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 253), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud2 += 1
            rss1 += 1
            fud2 += 1
            fss1 += 1
            dud2 += 1
            dss1 += 1
            tud2 += 1
            tss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 215), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud3 += 1
            rss1 += 1
            fud3 += 1
            fss1 += 1
            dud3 += 1
            dss1 += 1
            tud3 += 1
            tss1 += 1
        
# 6
    if x >= 323 and x <= 357 and y >= 408 and y <= 442:
        o6 = Rectangle(Point(323, 408), Point(357, 442))
        o6.setFill(color_rgb(125, 125, 125))
        o6.draw(g)
        rhdt0 = Circle(Point(470, 377), 15)
        rhdt0.setFill(color_rgb(0, 0, 0))
        rhdt0.draw(g)
        rhdt10 = Circle(Point(470, 377), 10)
        rhdt10.setFill(color_rgb(255, 255, 255))
        rhdt10.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 52), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 52), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)   
            rud4 += 1
            rss4 += 1
            rdi2 += 1
            hud4 += 1
            hss4 += 1
            hdi2 += 1
            dud4 += 1
            dss4 += 1
            ddi2 += 1
            tud4 += 1
            tss4 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 133), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 133), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                       
            rud3 += 1
            rss3 += 1
            rdi2 += 1
            hud3 += 1
            hss3 += 1
            hdi2 += 1
            dud3 += 1
            dss3 += 1
            ddi2 += 1
            tud3 += 1
            tss3 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 215), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 215), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud2 += 1
            rss2 += 1
            rdi2 += 1
            hud2 += 1
            hss2 += 1
            hdi2 += 1
            dud2 += 1
            dss2 += 1
            ddi2 += 1
            tud2 += 1
            tss2 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 292), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 292), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud1 += 1
            rss1 += 1
            rdi2 += 1
            hud1 += 1
            hss1 += 1
            hdi2 += 1
            dud1 += 1
            dss1 += 1
            ddi2 += 1
            tud1 += 1
            tss1 += 1
            tdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(128, 175), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(128, 175), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud4 += 1
            rss1 += 1
            rdi1 += 1
            hud4 += 1
            hss1 += 1
            hdi1 += 1
            dud4 += 1
            dss1 += 1
            ddi1 += 1
            tud4 += 1
            tss1 += 1
            tdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 175), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 175), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud3 += 1
            rss2 += 1
            rdi1 += 1
            hud3 += 1
            hss2 += 1
            hdi1 += 1
            dud3 += 1
            dss2 += 1
            ddi1 += 1
            tud3 += 1
            tss2 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 175), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 175), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud2 += 1
            rss3 += 1
            rdi1 += 1
            hud2 += 1
            hss3 += 1
            hdi1 += 1
            dud2 += 1
            dss3 += 1
            ddi1 += 1
            tud2 += 1
            tss3 += 1
            tdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(372, 175), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(372, 175), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud1 += 1
            rss4 += 1
            rdi1 += 1
            hud1 += 1
            hss4 += 1
            hdi1 += 1
            dud1 += 1
            dss4 += 1
            ddi1 += 1
            tud1 += 1
            tss4 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 92), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 92), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud3 += 1
            rss4 += 1
            hud3 += 1
            hss4 += 1
            dud3 += 1
            dss4 += 1
            tud3 += 1
            tss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 133), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(333, 133), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud2 += 1
            rss4 += 1
            hud2 += 1
            hss4 += 1
            dud2 += 1
            dss4 += 1
            tud2 += 1
            tss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 253), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 253), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)            
            rud1 += 1
            rss2 += 1
            hud1 += 1
            hss2 += 1
            dud1 += 1
            dss2 += 1
            tud1 += 1
            tss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 215), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(333, 215), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud1 += 1
            rss3 += 1
            hud1 += 1
            hss3 += 1
            dud1 += 1
            dss3 += 1
            tud1 += 1
            tss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 92), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 92), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud4 += 1
            rss3 += 1
            hud4 += 1
            hss3 += 1
            dud4 += 1
            dss3 += 1
            tud4 += 1
            tss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 133), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(165, 133), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud4 += 1
            rss2 += 1
            hud4 += 1
            hss2 += 1
            dud4 += 1
            dss2 += 1
            tud4 += 1
            tss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 253), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 253), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud2 += 1
            rss1 += 1
            hud2 += 1
            hss1 += 1
            dud2 += 1
            dss1 += 1
            tud2 += 1
            tss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 215), 15)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(165, 215), 10)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud3 += 1
            rss1 += 1
            hud3 += 1
            hss1 += 1
            dud3 += 1
            dss1 += 1
            tud3 += 1
            tss1 += 1

        
# 7
    if x >= 383 and x <= 417 and y >= 408 and y <= 442:
        o7 = Rectangle(Point(383, 408), Point(417, 442))
        o7.setFill(color_rgb(125, 125, 125))
        o7.draw(g)    
        rflt0 = Circle(Point(470, 377), 15)
        rflt0.setFill(color_rgb(255, 255, 255))
        rflt0.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 52), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            rud4 += 1
            rss4 += 1
            rdi2 += 1
            fud4 += 1
            fss4 += 1
            fdi2 += 1
            lud4 += 1
            lss4 += 1
            ldi2 += 1
            tud4 += 1
            tss4 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 133), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)           
            rud3 += 1
            rss3 += 1
            rdi2 += 1
            fud3 += 1
            fss3 += 1
            fdi2 += 1
            lud3 += 1
            lss3 += 1
            ldi2 += 1
            tud3 += 1
            tss3 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 215), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud2 += 1
            rss2 += 1
            rdi2 += 1
            fud2 += 1
            fss2 += 1
            fdi2 += 1
            lud2 += 1
            lss2 += 1
            ldi2 += 1
            tud2 += 1
            tss2 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 292), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud1 += 1
            rss1 += 1
            rdi2 += 1
            fud1 += 1
            fss1 += 1
            fdi2 += 1
            lud1 += 1
            lss1 += 1
            ldi2 += 1
            tud1 += 1
            tss1 += 1
            tdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(128, 175), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud4 += 1
            rss1 += 1
            rdi1 += 1
            fud4 += 1
            fss1 += 1
            fdi1 += 1
            lud4 += 1
            lss1 += 1
            ldi1 += 1
            tud4 += 1
            tss1 += 1
            tdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 175), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud3 += 1
            rss2 += 1
            rdi1 += 1
            fud3 += 1
            fss2 += 1
            fdi1 += 1
            lud3 += 1
            lss2 += 1
            ldi1 += 1
            tud3 += 1
            tss2 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 175), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud2 += 1
            rss3 += 1
            rdi1 += 1
            fud2 += 1
            fss3 += 1
            fdi1 += 1
            lud2 += 1
            lss3 += 1
            ldi1 += 1
            tud2 += 1
            tss3 += 1
            tdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(372, 175), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud1 += 1
            rss4 += 1
            rdi1 += 1
            fud1 += 1
            fss4 += 1
            fdi1 += 1
            lud1 += 1
            lss4 += 1
            ldi1 += 1
            tud1 += 1
            tss4 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 92), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud3 += 1
            rss4 += 1
            fud3 += 1
            fss4 += 1
            lud3 += 1
            lss4 += 1
            tud3 += 1
            tss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 133), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud2 += 1
            rss4 += 1
            fud2 += 1
            fss4 += 1
            lud2 += 1
            lss4 += 1
            tud2 += 1
            tss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 253), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)            
            rud1 += 1
            rss2 += 1
            fud1 += 1
            fss2 += 1
            lud1 += 1
            lss2 += 1
            tud1 += 1
            tss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 215), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud1 += 1
            rss3 += 1
            fud1 += 1
            fss3 += 1
            lud1 += 1
            lss3 += 1
            tud1 += 1
            tss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 92), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud4 += 1
            rss3 += 1
            fud4 += 1
            fss3 += 1
            lud4 += 1
            lss3 += 1
            tud4 += 1
            tss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 133), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud4 += 1
            rss2 += 1
            fud4 += 1
            fss2 += 1
            lud4 += 1
            lss2 += 1
            tud4 += 1
            tss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 253), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud2 += 1
            rss1 += 1
            fud2 += 1
            fss1 += 1
            lud2 += 1
            lss1 += 1
            tud2 += 1
            tss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 215), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud3 += 1
            rss1 += 1
            fud3 += 1
            fss1 += 1
            lud3 += 1
            lss1 += 1
            tud3 += 1
            tss1 += 1
    
# 8
    if x >= 443 and x <= 477 and y >= 408 and y <= 442:
        o8 = Rectangle(Point(443, 408), Point(477, 442))
        o8.setFill(color_rgb(125, 125, 125))
        o8.draw(g) 
        rhlt0 = Circle(Point(470, 377), 15)
        rhlt0.setFill(color_rgb(255, 255, 255))
        rhlt0.draw(g)
        rhlt10 = Circle(Point(470, 377), 10)
        rhlt10.setFill(color_rgb(0, 0, 0))
        rhlt10.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY() 
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 52), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            rhlt10 = Circle(Point(250, 52), 10)
            rhlt10.setFill(color_rgb(0, 0, 0))
            rhlt10.draw(g)
            rud4 += 1
            rss4 += 1
            rdi2 += 1
            hud4 += 1
            hss4 += 1
            hdi2 += 1
            lud4 += 1
            lss4 += 1
            ldi2 += 1
            tud4 += 1
            tss4 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 133), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            rhlt10 = Circle(Point(250, 133), 10)
            rhlt10.setFill(color_rgb(0, 0, 0))
            rhlt10.draw(g)                        
            rud3 += 1
            rss3 += 1
            rdi2 += 1
            hud3 += 1
            hss3 += 1
            hdi2 += 1
            lud3 += 1
            lss3 += 1
            ldi2 += 1
            tud3 += 1
            tss3 += 1
            tdi2 += 1
            
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 215), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 215), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud2 += 1
            rss2 += 1
            rdi2 += 1
            hud2 += 1
            hss2 += 1
            hdi2 += 1
            lud2 += 1
            lss2 += 1
            ldi2 += 1
            tud2 += 1
            tss2 += 1
            tdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 292), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 292), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud1 += 1
            rss1 += 1
            rdi2 += 1
            hud1 += 1
            hss1 += 1
            hdi2 += 1
            lud1 += 1
            lss1 += 1
            ldi2 += 1
            tud1 += 1
            tss1 += 1
            tdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(128, 175), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(128, 175), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud4 += 1
            rss1 += 1
            rdi1 += 1
            hud4 += 1
            hss1 += 1
            hdi1 += 1
            lud4 += 1
            lss1 += 1
            ldi1 += 1
            tud4 += 1
            tss1 += 1
            tdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 175), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 175), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud3 += 1
            rss2 += 1
            rdi1 += 1
            hud3 += 1
            hss2 += 1
            hdi1 += 1
            lud3 += 1
            lss2 += 1
            ldi1 += 1
            tud3 += 1
            tss2 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 175), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 175), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud2 += 1
            rss3 += 1
            rdi1 += 1
            hud2 += 1
            hss3 += 1
            hdi1 += 1
            lud2 += 1
            lss3 += 1
            ldi1 += 1
            tud2 += 1
            tss3 += 1
            tdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(372, 175), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(372, 175), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud1 += 1
            rss4 += 1
            rdi1 += 1
            hud1 += 1
            hss4 += 1
            hdi1 += 1
            lud1 += 1
            lss4 += 1
            ldi1 += 1
            tud1 += 1
            tss4 += 1
            tdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 92), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 92), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud3 += 1
            rss4 += 1
            hud3 += 1
            hss4 += 1
            lud3 += 1
            lss4 += 1
            tud3 += 1
            tss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 133), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(333, 133), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud2 += 1
            rss4 += 1
            hud2 += 1
            hss4 += 1
            lud2 += 1
            lss4 += 1
            tud2 += 1
            tss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 253), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 253), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)            
            rud1 += 1
            rss2 += 1
            hud1 += 1
            hss2 += 1
            lud1 += 1
            lss2 += 1
            tud1 += 1
            tss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 215), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(333, 215), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud1 += 1
            rss3 += 1
            hud1 += 1
            hss3 += 1
            lud1 += 1
            lss3 += 1
            tud1 += 1
            tss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 92), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 92), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud4 += 1
            rss3 += 1
            hud4 += 1
            hss3 += 1
            lud4 += 1
            lss3 += 1
            tud4 += 1
            tss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 133), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(165, 133), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud4 += 1
            rss2 += 1
            hud4 += 1
            hss2 += 1
            lud4 += 1
            lss2 += 1
            tud4 += 1
            tss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 253), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 253), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud2 += 1
            rss1 += 1
            hud2 += 1
            hss1 += 1
            lud2 += 1
            lss1 += 1
            tud2 += 1
            tss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 215), 15)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(165, 215), 10)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud3 += 1
            rss1 += 1
            hud3 += 1
            hss1 += 1
            lud3 += 1
            lss1 += 1
            tud3 += 1
            tss1 += 1
        
# 9
    if x >= 26 and x <= 64 and y >= 451 and y <= 489:
        p1 = Rectangle(Point(28, 453), Point(62, 487))
        p1.setFill(color_rgb(125, 125, 125))
        p1.draw(g) 
        bfds0 = Rectangle(Point(460, 367), Point(480, 387))
        bfds0.setFill(color_rgb(0, 0, 0))
        bfds0.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 43), Point(261, 63))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud4 += 1
            bss4 += 1
            bdi2 += 1
            fud4 += 1
            fss4 += 1
            fdi2 += 1
            dud4 += 1
            dss4 += 1
            ddi2 += 1
            sud4 += 1
            sss4 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 124), Point(261, 144))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bud3 += 1
            bss3 += 1
            bdi2 += 1
            fud3 += 1
            fss3 += 1
            fdi2 += 1
            dud3 += 1
            dss3 += 1
            ddi2 += 1
            sud3 += 1
            sss3 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 206), Point(261, 226))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud2 += 1
            bss2 += 1
            bdi2 += 1
            fud2 += 1
            fss2 += 1
            fdi2 += 1
            dud2 += 1
            dss2 += 1
            ddi2 += 1
            sud2 += 1
            sss2 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 283), Point(261, 303))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud1 += 1
            bss1 += 1
            bdi2 += 1
            fud1 += 1
            fss1 += 1
            fdi2 += 1
            dud1 += 1
            dss1 += 1
            ddi2 += 1
            sud1 += 1
            sss1 += 1
            sdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(119, 166), Point(139, 186))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud4 += 1
            bss1 += 1
            bdi1 += 1
            fud4 += 1
            fss1 += 1
            fdi1 += 1
            dud4 += 1
            dss1 += 1
            ddi1 += 1
            sud4 += 1
            sss1 += 1
            sdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 166), Point(218, 186))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud3 += 1
            bss2 += 1
            bdi1 += 1
            fud3 += 1
            fss2 += 1
            fdi1 += 1
            dud3 += 1
            dss2 += 1
            ddi1 += 1
            sud3 += 1
            sss2 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 166), Point(306, 186))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud2 += 1
            bss3 += 1
            bdi1 += 1
            fud2 += 1
            fss3 += 1
            fdi1 += 1
            dud2 += 1
            dss3 += 1
            ddi1 += 1
            sud2 += 1
            sss3 += 1
            sdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(363, 166), Point(383, 186))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud1 += 1
            bss4 += 1
            bdi1 += 1
            fud1 += 1
            fss4 += 1
            fdi1 += 1
            dud1 += 1
            dss4 += 1
            ddi1 += 1
            sud1 += 1
            sss4 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 83), Point(306, 103))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud3 += 1
            bss4 += 1
            fud3 += 1
            fss4 += 1
            dud3 += 1
            dss4 += 1
            sud3 += 1
            sss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(324, 124), Point(344, 144))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud2 += 1
            bss4 += 1
            fud2 += 1
            fss4 += 1
            dud2 += 1
            dss4 += 1
            sud2 += 1
            sss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 244), Point(306, 264))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)            
            bud1 += 1
            bss2 += 1
            fud1 += 1
            fss2 += 1
            dud1 += 1
            dss2 += 1
            sud1 += 1
            sss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(324, 206), Point(344, 226))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud1 += 1
            bss3 += 1
            fud1 += 1
            fss3 += 1
            dud1 += 1
            dss3 += 1
            sud1 += 1
            sss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 83), Point(218, 103))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud4 += 1
            bss3 += 1
            fud4 += 1
            fss3 += 1
            dud4 += 1
            dss3 += 1
            sud4 += 1
            sss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(156, 124), Point(176, 144))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud4 += 1
            bss2 += 1
            fud4 += 1
            fss2 += 1
            dud4 += 1
            dss2 += 1
            sud4 += 1
            sss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 244), Point(218, 264))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud2 += 1
            bss1 += 1
            fud2 += 1
            fss1 += 1
            dud2 += 1
            dss1 += 1
            sud2 += 1
            sss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(156, 206), Point(176, 226))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            bud3 += 1
            bss1 += 1
            fud3 += 1
            fss1 += 1
            dud3 += 1
            dss1 += 1
            sud3 += 1
            sss1 += 1
        
# 10
    if x >= 88 and x <= 120 and y >= 451 and y <= 489:
        p2 = Rectangle(Point(90, 453), Point(122, 487))
        p2.setFill(color_rgb(125, 125, 125))
        p2.draw(g) 
        bhds0 = Rectangle(Point(460, 367), Point(480, 387))
        bhds0.setFill(color_rgb(0, 0, 0))
        bhds0.draw(g)
        bhds10 = Circle(Point(470, 377), 5)
        bhds10.setFill(color_rgb(255, 255, 255))
        bhds10.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 43), Point(261, 63))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 53), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)
            bud4 += 1
            bss4 += 1
            bdi2 += 1
            hud4 += 1
            hss4 += 1
            hdi2 += 1
            dud4 += 1
            dss4 += 1
            ddi2 += 1
            sud4 += 1
            sss4 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 124), Point(261, 144))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 134), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)
            bud3 += 1
            bss3 += 1
            bdi2 += 1
            hud3 += 1
            hss3 += 1
            hdi2 += 1
            dud3 += 1
            dss3 += 1
            ddi2 += 1
            sud3 += 1
            sss3 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 206), Point(261, 226))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 216), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud2 += 1
            bss2 += 1
            bdi2 += 1
            hud2 += 1
            hss2 += 1
            hdi2 += 1
            dud2 += 1
            dss2 += 1
            ddi2 += 1
            sud2 += 1
            sss2 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 283), Point(261, 303))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 293), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud1 += 1
            bss1 += 1
            bdi2 += 1
            hud1 += 1
            hss1 += 1
            hdi2 += 1
            dud1 += 1
            dss1 += 1
            ddi2 += 1
            sud1 += 1
            sss1 += 1
            sdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(119, 166), Point(139, 186))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(129, 176), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud4 += 1
            bss1 += 1
            bdi1 += 1
            hud4 += 1
            hss1 += 1
            hdi1 += 1
            dud4 += 1
            dss1 += 1
            ddi1 += 1
            sud4 += 1
            sss1 += 1
            sdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 166), Point(218, 186))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 176), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud3 += 1
            bss2 += 1
            bdi1 += 1
            hud3 += 1
            hss2 += 1
            hdi1 += 1
            dud3 += 1
            dss2 += 1
            ddi1 += 1
            sud3 += 1
            sss2 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 166), Point(306, 186))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 176), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud2 += 1
            bss3 += 1
            bdi1 += 1
            hud2 += 1
            hss3 += 1
            hdi1 += 1
            dud2 += 1
            dss3 += 1
            ddi1 += 1
            sud2 += 1
            sss3 += 1
            sdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(364, 166), Point(383, 186))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(373, 176), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud1 += 1
            bss4 += 1
            bdi1 += 1
            hud1 += 1
            hss4 += 1
            hdi1 += 1
            dud1 += 1
            dss4 += 1
            ddi1 += 1
            sud1 += 1
            sss4 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 83), Point(306, 103))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 93), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud3 += 1
            bss4 += 1
            hud3 += 1
            hss4 += 1
            dud3 += 1
            dss4 += 1
            sud3 += 1
            sss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(324, 124), Point(344, 144))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(334, 134), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud2 += 1
            bss4 += 1
            hud2 += 1
            hss4 += 1
            dud2 += 1
            dss4 += 1
            sud2 += 1
            sss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 244), Point(306, 264))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 254), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)          
            bud1 += 1
            bss2 += 1
            hud1 += 1
            hss2 += 1
            dud1 += 1
            dss2 += 1
            sud1 += 1
            sss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(324, 206), Point(344, 226))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(334, 216), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud1 += 1
            bss3 += 1
            hud1 += 1
            hss3 += 1
            dud1 += 1
            dss3 += 1
            sud1 += 1
            sss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 83), Point(218, 103))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 93), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud4 += 1
            bss3 += 1
            hud4 += 1
            hss3 += 1
            dud4 += 1
            dss3 += 1
            sud4 += 1
            sss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(156, 124), Point(176, 144))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(166, 134), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud4 += 1
            bss2 += 1
            hud4 += 1
            hss2 += 1
            dud4 += 1
            dss2 += 1
            sud4 += 1
            sss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 244), Point(218, 264))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 254), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud2 += 1
            bss1 += 1
            hud2 += 1
            hss1 += 1
            dud2 += 1
            dss1 += 1
            sud2 += 1
            sss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(156, 206), Point(176, 226))
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(166, 216), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            bud3 += 1
            bss1 += 1
            hud3 += 1
            hss1 += 1
            dud3 += 1
            dss1 += 1
            sud3 += 1
            sss1 += 1
# 11
    if x >= 150 and x <= 180 and y >= 451 and y <= 489:
        p3 = Rectangle(Point(148, 453), Point(182, 487))
        p3.setFill(color_rgb(125, 125, 125))
        p3.draw(g) 
        bfls0 = Rectangle(Point(460, 367), Point(480, 387))
        bfls0.setFill(color_rgb(255, 255, 255))
        bfls0.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 43), Point(261, 63))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bud4 += 1
            bss4 += 1
            bdi2 += 1
            fud4 += 1
            fss4 += 1
            fdi2 += 1
            lud4 += 1
            lss4 += 1
            ldi2 += 1
            sud4 += 1
            sss4 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 124), Point(261, 144))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bud3 += 1
            bss3 += 1
            bdi2 += 1
            fud3 += 1
            fss3 += 1
            fdi2 += 1
            lud3 += 1
            lss3 += 1
            ldi2 += 1
            sud3 += 1
            sss3 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 206), Point(261, 226))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud2 += 1
            bss2 += 1
            bdi2 += 1
            fud2 += 1
            fss2 += 1
            fdi2 += 1
            lud2 += 1
            lss2 += 1
            ldi2 += 1
            sud2 += 1
            sss2 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 283), Point(261, 303))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud1 += 1
            bss1 += 1
            bdi2 += 1
            fud1 += 1
            fss1 += 1
            fdi2 += 1
            lud1 += 1
            lss1 += 1
            ldi2 += 1
            sud1 += 1
            sss1 += 1
            sdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(119, 166), Point(139, 186))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud4 += 1
            bss1 += 1
            bdi1 += 1
            fud4 += 1
            fss1 += 1
            fdi1 += 1
            lud4 += 1
            lss1 += 1
            ldi1 += 1
            sud4 += 1
            sss1 += 1
            sdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 166), Point(218, 186))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud3 += 1
            bss2 += 1
            bdi1 += 1
            fud3 += 1
            fss2 += 1
            fdi1 += 1
            lud3 += 1
            lss2 += 1
            ldi1 += 1
            sud3 += 1
            sss2 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 166), Point(306, 186))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bud2 += 1
            bss3 += 1
            bdi1 += 1
            fud2 += 1
            fss3 += 1
            fdi1 += 1
            lud2 += 1
            lss3 += 1
            ldi1 += 1
            sud2 += 1
            sss3 += 1
            sdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(363, 166), Point(383, 186))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud1 += 1
            bss4 += 1
            bdi1 += 1
            fud1 += 1
            fss4 += 1
            fdi1 += 1
            lud1 += 1
            lss4 += 1
            ldi1 += 1
            sud1 += 1
            sss4 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 83), Point(306, 103))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud3 += 1
            bss4 += 1
            fud3 += 1
            fss4 += 1
            lud3 += 1
            lss4 += 1
            sud3 += 1
            sss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(324, 124), Point(344, 144))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud2 += 1
            bss4 += 1
            fud2 += 1
            fss4 += 1
            lud2 += 1
            lss4 += 1
            sud2 += 1
            sss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 244), Point(306, 264))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)            
            bud1 += 1
            bss2 += 1
            fud1 += 1
            fss2 += 1
            lud1 += 1
            lss2 += 1
            sud1 += 1
            sss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(324, 206), Point(344, 226))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud1 += 1
            bss3 += 1
            fud1 += 1
            fss3 += 1
            lud1 += 1
            lss3 += 1
            sud1 += 1
            sss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 83), Point(218, 103))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud4 += 1
            bss3 += 1
            fud4 += 1
            fss3 += 1
            lud4 += 1
            lss3 += 1
            sud4 += 1
            sss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(156, 124), Point(176, 144))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud4 += 1
            bss2 += 1
            fud4 += 1
            fss2 += 1
            lud4 += 1
            lss2 += 1
            sud4 += 1
            sss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 244), Point(218, 264))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud2 += 1
            bss1 += 1
            fud2 += 1
            fss1 += 1
            lud2 += 1
            lss1 += 1
            sud2 += 1
            sss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(156, 206), Point(176, 226))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            bud3 += 1
            bss1 += 1
            fud3 += 1
            fss1 += 1
            lud3 += 1
            lss1 += 1
            sud3 += 1
            sss1 += 1
        
# 12
    if x >= 208 and x <= 242 and y >= 451 and y <= 489:
        p4 = Rectangle(Point(206, 453), Point(244, 487))
        p4.setFill(color_rgb(125, 125, 125))
        p4.draw(g) 
        bhls0 = Rectangle(Point(460, 367), Point(480, 387))
        bhls0.setFill(color_rgb(255, 255, 255))
        bhls0.draw(g)
        bhls10 = Circle(Point(470, 377), 5)
        bhls10.setFill(color_rgb(0, 0, 0))
        bhls10.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 43), Point(261, 63))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 53), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)
            bud4 += 1
            bss4 += 1
            bdi2 += 1
            hud4 += 1
            hss4 += 1
            hdi2 += 1
            lud4 += 1
            lss4 += 1
            ldi2 += 1
            sud4 += 1
            sss4 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 124), Point(261, 144))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 134), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)
            bud3 += 1
            bss3 += 1
            bdi2 += 1
            hud3 += 1
            hss3 += 1
            hdi2 += 1
            lud3 += 1
            lss3 += 1
            ldi2 += 1
            sud3 += 1
            sss3 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 206), Point(261, 226))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 216), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud2 += 1
            bss2 += 1
            bdi2 += 1
            hud2 += 1
            hss2 += 1
            hdi2 += 1
            lud2 += 1
            lss2 += 1
            ldi2 += 1
            sud2 += 1
            sss2 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(241, 283), Point(261, 303))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(251, 293), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud1 += 1
            bss1 += 1
            bdi2 += 1
            hud1 += 1
            hss1 += 1
            hdi2 += 1
            lud1 += 1
            lss1 += 1
            ldi2 += 1
            sud1 += 1
            sss1 += 1
            sdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(119, 166), Point(139, 186))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(129, 176), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud4 += 1
            bss1 += 1
            bdi1 += 1
            hud4 += 1
            hss1 += 1
            hdi1 += 1
            lud4 += 1
            lss1 += 1
            ldi1 += 1
            sud4 += 1
            sss1 += 1
            sdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 166), Point(218, 186))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 176), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud3 += 1
            bss2 += 1
            bdi1 += 1
            hud3 += 1
            hss2 += 1
            hdi1 += 1
            lud3 += 1
            lss2 += 1
            ldi1 += 1
            sud3 += 1
            sss2 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 166), Point(306, 186))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 176), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud2 += 1
            bss3 += 1
            bdi1 += 1
            hud2 += 1
            hss3 += 1
            hdi1 += 1
            lud2 += 1
            lss3 += 1
            ldi1 += 1
            sud2 += 1
            sss3 += 1
            sdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(364, 166), Point(383, 186))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(373, 176), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud1 += 1
            bss4 += 1
            bdi1 += 1
            hud1 += 1
            hss4 += 1
            hdi1 += 1
            lud1 += 1
            lss4 += 1
            ldi1 += 1
            sud1 += 1
            sss4 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 83), Point(306, 103))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 93), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud3 += 1
            bss4 += 1
            hud3 += 1
            hss4 += 1
            lud3 += 1
            lss4 += 1
            sud3 += 1
            sss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(324, 124), Point(344, 144))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(334, 134), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud2 += 1
            bss4 += 1
            hud2 += 1
            hss4 += 1
            lud2 += 1
            lss4 += 1
            sud2 += 1
            sss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(286, 244), Point(306, 264))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(296, 254), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)            
            bud1 += 1
            bss2 += 1
            hud1 += 1
            hss2 += 1
            lud1 += 1
            lss2 += 1
            sud1 += 1
            sss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(324, 206), Point(344, 226))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(334, 216), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud1 += 1
            bss3 += 1
            hud1 += 1
            hss3 += 1
            lud1 += 1
            lss3 += 1
            sud1 += 1
            sss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 83), Point(218, 103))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 93), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud4 += 1
            bss3 += 1
            hud4 += 1
            hss3 += 1
            lud4 += 1
            lss3 += 1
            sud4 += 1
            sss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(156, 124), Point(176, 144))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(166, 134), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud4 += 1
            bss2 += 1
            hud4 += 1
            hss2 += 1
            lud4 += 1
            lss2 += 1
            sud4 += 1
            sss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(198, 244), Point(218, 264))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(208, 254), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud2 += 1
            bss1 += 1
            hud2 += 1
            hss1 += 1
            lud2 += 1
            lss1 += 1
            sud2 += 1
            sss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Rectangle(Point(156, 206), Point(176, 226))
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(166, 216), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            bud3 += 1
            bss1 += 1
            hud3 += 1
            hss1 += 1
            lud3 += 1
            lss1 += 1
            sud3 += 1
            sss1 += 1
    
# 13    
    if x >= 263 and x <= 297 and y >= 451 and y <= 489:
        p5 = Rectangle(Point(263, 453), Point(297, 487))
        p5.setFill(color_rgb(125, 125, 125))
        p5.draw(g) 
        rfds0 = Circle(Point(470, 377), 10)
        rfds0.setFill(color_rgb(0, 0, 0))
        rfds0.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 52), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)            
            rud4 += 1
            rss4 += 1
            rdi2 += 1
            fud4 += 1
            fss4 += 1
            fdi2 += 1
            dud4 += 1
            dss4 += 1
            ddi2 += 1
            sud4 += 1
            sss4 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 133), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            rud3 += 1
            rss3 += 1
            rdi2 += 1
            fud3 += 1
            fss3 += 1
            fdi2 += 1
            dud3 += 1
            dss3 += 1
            ddi2 += 1
            sud3 += 1
            sss3 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 215), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud2 += 1
            rss2 += 1
            rdi2 += 1
            fud2 += 1
            fss2 += 1
            fdi2 += 1
            dud2 += 1
            dss2 += 1
            ddi2 += 1
            sud2 += 1
            sss2 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 292), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud1 += 1
            rss1 += 1
            rdi2 += 1
            fud1 += 1
            fss1 += 1
            fdi2 += 1
            dud1 += 1
            dss1 += 1
            ddi2 += 1
            sud1 += 1
            sss1 += 1
            sdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(128, 175), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud4 += 1
            rss1 += 1
            rdi1 += 1
            fud4 += 1
            fss1 += 1
            fdi1 += 1
            dud4 += 1
            dss1 += 1
            ddi1 += 1
            sud4 += 1
            sss1 += 1
            sdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 175), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud3 += 1
            rss2 += 1
            rdi1 += 1
            fud3 += 1
            fss2 += 1
            fdi1 += 1
            dud3 += 1
            dss2 += 1
            ddi1 += 1
            sud3 += 1
            sss2 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 175), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud2 += 1
            rss3 += 1
            rdi1 += 1
            fud2 += 1
            fss3 += 1
            fdi1 += 1
            dud2 += 1
            dss3 += 1
            ddi1 += 1
            sud2 += 1
            sss3 += 1
            sdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(372, 175), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud1 += 1
            rss4 += 1
            rdi1 += 1
            fud1 += 1
            fss4 += 1
            fdi1 += 1
            dud1 += 1
            dss4 += 1
            ddi1 += 1
            sud1 += 1
            sss4 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 92), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud3 += 1
            rss4 += 1
            fud3 += 1
            fss4 += 1
            dud3 += 1
            dss4 += 1
            sud3 += 1
            sss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 133), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud2 += 1
            rss4 += 1
            fud2 += 1
            fss4 += 1
            dud2 += 1
            dss4 += 1
            sud2 += 1
            sss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 253), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)            
            rud1 += 1
            rss2 += 1
            fud1 += 1
            fss2 += 1
            dud1 += 1
            dss2 += 1
            sud1 += 1
            sss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 215), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud1 += 1
            rss3 += 1
            fud1 += 1
            fss3 += 1
            dud1 += 1
            dss3 += 1
            sud1 += 1
            sss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 92), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud4 += 1
            rss3 += 1
            fud4 += 1
            fss3 += 1
            dud4 += 1
            dss3 += 1
            sud4 += 1
            sss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 133), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud4 += 1
            rss2 += 1
            fud4 += 1
            fss2 += 1
            dud4 += 1
            dss2 += 1
            sud4 += 1
            sss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 253), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud2 += 1
            rss1 += 1
            fud2 += 1
            fss1 += 1
            dud2 += 1
            dss1 += 1
            sud2 += 1
            sss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 215), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)                        
            rud3 += 1
            rss1 += 1
            fud3 += 1
            fss1 += 1
            dud3 += 1
            dss1 += 1
            sud3 += 1
            sss1 += 1
    
# 14    
    if x >= 320 and x <= 360 and y >= 451 and y <= 489:
        p6 = Rectangle(Point(323, 453), Point(357, 487))
        p6.setFill(color_rgb(125, 125, 125))
        p6.draw(g) 
        rhds0 = Circle(Point(470, 377), 10)
        rhds0.setFill(color_rgb(0, 0, 0))
        rhds0.draw(g)
        rhds10 = Circle(Point(470, 377), 5)
        rhds10.setFill(color_rgb(255, 255, 255))
        rhds10.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 52), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 52), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)            
            rud4 += 1
            rss4 += 1
            rdi2 += 1
            hud4 += 1
            hss4 += 1
            hdi2 += 1
            dud4 += 1
            dss4 += 1
            ddi2 += 1
            sud4 += 1
            sss4 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 133), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 133), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud3 += 1
            rss3 += 1
            rdi2 += 1
            hud3 += 1
            hss3 += 1
            hdi2 += 1
            dud3 += 1
            dss3 += 1
            ddi2 += 1
            sud3 += 1
            sss3 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 215), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 215), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud2 += 1
            rss2 += 1
            rdi2 += 1
            hud2 += 1
            hss2 += 1
            hdi2 += 1
            dud2 += 1
            dss2 += 1
            ddi2 += 1
            sud2 += 1
            sss2 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 292), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 292), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud1 += 1
            rss1 += 1
            rdi2 += 1
            hud1 += 1
            hss1 += 1
            hdi2 += 1
            dud1 += 1
            dss1 += 1
            ddi2 += 1
            sud1 += 1
            sss1 += 1
            sdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(128, 175), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(128, 175), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud4 += 1
            rss1 += 1
            rdi1 += 1
            hud4 += 1
            hss1 += 1
            hdi1 += 1
            dud4 += 1
            dss1 += 1
            ddi1 += 1
            sud4 += 1
            sss1 += 1
            sdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 175), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 175), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud3 += 1
            rss2 += 1
            rdi1 += 1
            hud3 += 1
            hss2 += 1
            hdi1 += 1
            dud3 += 1
            dss2 += 1
            ddi1 += 1
            sud3 += 1
            sss2 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 175), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 175), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud2 += 1
            rss3 += 1
            rdi1 += 1
            hud2 += 1
            hss3 += 1
            hdi1 += 1
            dud2 += 1
            dss3 += 1
            ddi1 += 1
            sud2 += 1
            sss3 += 1
            sdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(372, 175), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(372, 175), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud1 += 1
            rss4 += 1
            rdi1 += 1
            hud1 += 1
            hss4 += 1
            hdi1 += 1
            dud1 += 1
            dss4 += 1
            ddi1 += 1
            sud1 += 1
            sss4 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 92), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 92), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud3 += 1
            rss4 += 1
            hud3 += 1
            hss4 += 1
            dud3 += 1
            dss4 += 1
            sud3 += 1
            sss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 133), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(333, 133), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud2 += 1
            rss4 += 1
            hud2 += 1
            hss4 += 1
            dud2 += 1
            dss4 += 1
            sud2 += 1
            sss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 253), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 253), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)            
            rud1 += 1
            rss2 += 1
            hud1 += 1
            hss2 += 1
            dud1 += 1
            dss2 += 1
            sud1 += 1
            sss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 215), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(333, 215), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud1 += 1
            rss3 += 1
            hud1 += 1
            hss3 += 1
            dud1 += 1
            dss3 += 1
            sud1 += 1
            sss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 92), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 92), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)
            rud4 += 1
            rss3 += 1
            hud4 += 1
            hss3 += 1
            dud4 += 1
            dss3 += 1
            sud4 += 1
            sss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 133), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(165, 133), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud4 += 1
            rss2 += 1
            hud4 += 1
            hss2 += 1
            dud4 += 1
            dss2 += 1
            sud4 += 1
            sss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 253), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 253), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud2 += 1
            rss1 += 1
            hud2 += 1
            hss1 += 1
            dud2 += 1
            dss1 += 1
            sud2 += 1
            sss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 215), 10)
            oo.setFill(color_rgb(0, 0, 0))
            oo.draw(g)
            bhdt10 = Circle(Point(165, 215), 5)
            bhdt10.setFill(color_rgb(255, 255, 255))
            bhdt10.draw(g)                        
            rud3 += 1
            rss1 += 1
            hud3 += 1
            hss1 += 1
            dud3 += 1
            dss1 += 1
            sud3 += 1
            sss1 += 1
    
# 15    
    if x >= 380 and x <= 420 and y >= 451 and y <= 489:
        p7 = Rectangle(Point(383, 453), Point(417, 487))
        p7.setFill(color_rgb(125, 125, 125))
        p7.draw(g)
        rfls0 = Circle(Point(470, 377), 10)
        rfls0.setFill(color_rgb(255, 255, 255))
        rfls0.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()        
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 52), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)            
            rud4 += 1
            rss4 += 1
            rdi2 += 1
            fud4 += 1
            fss4 += 1
            fdi2 += 1
            lud4 += 1
            lss4 += 1
            ldi2 += 1
            sud4 += 1
            sss4 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 133), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud3 += 1
            rss3 += 1
            rdi2 += 1
            fud3 += 1
            fss3 += 1
            fdi2 += 1
            lud3 += 1
            lss3 += 1
            ldi2 += 1
            sud3 += 1
            sss3 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 215), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud2 += 1
            rss2 += 1
            rdi2 += 1
            fud2 += 1
            fss2 += 1
            fdi2 += 1
            lud2 += 1
            lss2 += 1
            ldi2 += 1
            sud2 += 1
            sss2 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 292), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud1 += 1
            rss1 += 1
            rdi2 += 1
            fud1 += 1
            fss1 += 1
            fdi2 += 1
            lud1 += 1
            lss1 += 1
            ldi2 += 1
            sud1 += 1
            sss1 += 1
            sdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(128, 175), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud4 += 1
            rss1 += 1
            rdi1 += 1
            fud4 += 1
            fss1 += 1
            fdi1 += 1
            lud4 += 1
            lss1 += 1
            ldi1 += 1
            sud4 += 1
            sss1 += 1
            sdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 175), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud3 += 1
            rss2 += 1
            rdi1 += 1
            fud3 += 1
            fss2 += 1
            fdi1 += 1
            lud3 += 1
            lss2 += 1
            ldi1 += 1
            sud3 += 1
            sss2 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 175), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud2 += 1
            rss3 += 1
            rdi1 += 1
            fud2 += 1
            fss3 += 1
            fdi1 += 1
            lud2 += 1
            lss3 += 1
            ldi1 += 1
            sud2 += 1
            sss3 += 1
            sdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(372, 175), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud1 += 1
            rss4 += 1
            rdi1 += 1
            fud1 += 1
            fss4 += 1
            fdi1 += 1
            lud1 += 1
            lss4 += 1
            ldi1 += 1
            sud1 += 1
            sss4 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 92), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud3 += 1
            rss4 += 1
            fud3 += 1
            fss4 += 1
            lud3 += 1
            lss4 += 1
            sud3 += 1
            sss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 133), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud2 += 1
            rss4 += 1
            fud2 += 1
            fss4 += 1
            lud2 += 1
            lss4 += 1
            sud2 += 1
            sss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 253), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)            
            rud1 += 1
            rss2 += 1
            fud1 += 1
            fss2 += 1
            lud1 += 1
            lss2 += 1
            sud1 += 1
            sss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 215), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud1 += 1
            rss3 += 1
            fud1 += 1
            fss3 += 1
            lud1 += 1
            lss3 += 1
            sud1 += 1
            sss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 92), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud4 += 1
            rss3 += 1
            fud4 += 1
            fss3 += 1
            lud4 += 1
            lss3 += 1
            sud4 += 1
            sss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 133), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud4 += 1
            rss2 += 1
            fud4 += 1
            fss2 += 1
            lud4 += 1
            lss2 += 1
            sud4 += 1
            sss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 253), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud2 += 1
            rss1 += 1
            fud2 += 1
            fss1 += 1
            lud2 += 1
            lss1 += 1
            sud2 += 1
            sss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 215), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)                        
            rud3 += 1
            rss1 += 1
            fud3 += 1
            fss1 += 1
            lud3 += 1
            lss1 += 1
            sud3 += 1
            sss1 += 1
    
# 16    
    if x >= 440 and x <= 480 and y >= 451 and y <= 489:
        p8 = Rectangle(Point(443, 453), Point(477, 487))
        p8.setFill(color_rgb(125, 125, 125))
        p8.draw(g)
        rhls0 = Circle(Point(470, 377), 10)
        rhls0.setFill(color_rgb(255, 255, 255))
        rhls0.draw(g)
        rhls10 = Circle(Point(470, 377), 5)
        rhls10.setFill(color_rgb(0, 0, 0))
        rhls10.draw(g)
        placed += 1
        p = g.getMouse()
        x = p.getX()
        y = p.getY()
        if x >= 226 and x <= 274 and y >= 28 and y <= 76:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 52), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 52), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)            
            rud4 += 1
            rss4 += 1
            rdi2 += 1
            hud4 += 1
            hss4 += 1
            hdi2 += 1
            lud4 += 1
            lss4 += 1
            ldi2 += 1
            sud4 += 1
            sss4 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 133), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 133), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud3 += 1
            rss3 += 1
            rdi2 += 1
            hud3 += 1
            hss3 += 1
            hdi2 += 1
            lud3 += 1
            lss3 += 1
            ldi2 += 1
            sud3 += 1
            sss3 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 215), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 215), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud2 += 1
            rss2 += 1
            rdi2 += 1
            hud2 += 1
            hss2 += 1
            hdi2 += 1
            lud2 += 1
            lss2 += 1
            ldi2 += 1
            sud2 += 1
            sss2 += 1
            sdi2 += 1
        if x >= 226 and x <= 274 and y >= 268 and y <= 316:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(250, 292), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(250, 292), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud1 += 1
            rss1 += 1
            rdi2 += 1
            hud1 += 1
            hss1 += 1
            hdi2 += 1
            lud1 += 1
            lss1 += 1
            ldi2 += 1
            sud1 += 1
            sss1 += 1
            sdi2 += 1
        if x >= 104 and x <= 152 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(128, 175), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(128, 175), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud4 += 1
            rss1 += 1
            rdi1 += 1
            hud4 += 1
            hss1 += 1
            hdi1 += 1
            lud4 += 1
            lss1 += 1
            ldi1 += 1
            sud4 += 1
            sss1 += 1
            sdi1 += 1
        if x >= 183 and x <= 231 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 175), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 175), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud3 += 1
            rss2 += 1
            rdi1 += 1
            hud3 += 1
            hss2 += 1
            hdi1 += 1
            lud3 += 1
            lss2 += 1
            ldi1 += 1
            sud3 += 1
            sss2 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 175), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 175), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud2 += 1
            rss3 += 1
            rdi1 += 1
            hud2 += 1
            hss3 += 1
            hdi1 += 1
            lud2 += 1
            lss3 += 1
            ldi1 += 1
            sud2 += 1
            sss3 += 1
            sdi1 += 1
        if x >= 348 and x <= 396 and y >= 151 and y <= 199:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(372, 175), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(372, 175), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud1 += 1
            rss4 += 1
            rdi1 += 1
            hud1 += 1
            hss4 += 1
            hdi1 += 1
            lud1 += 1
            lss4 += 1
            ldi1 += 1
            sud1 += 1
            sss4 += 1
            sdi1 += 1
        if x >= 271 and x <= 319 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 92), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 92), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud3 += 1
            rss4 += 1
            hud3 += 1
            hss4 += 1
            lud3 += 1
            lss4 += 1
            sud3 += 1
            sss4 += 1
        if x >= 309 and x <= 357 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 133), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(333, 133), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud2 += 1
            rss4 += 1
            hud2 += 1
            hss4 += 1
            lud2 += 1
            lss4 += 1
            sud2 += 1
            sss4 += 1
        if x >= 271 and x <= 319 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(295, 253), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(295, 253), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)            
            rud1 += 1
            rss2 += 1
            hud1 += 1
            hss2 += 1
            lud1 += 1
            lss2 += 1
            sud1 += 1
            sss2 += 1
        if x >= 309 and x <= 357 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(333, 215), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(333, 215), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud1 += 1
            rss3 += 1
            hud1 += 1
            hss3 += 1
            lud1 += 1
            lss3 += 1
            sud1 += 1
            sss3 += 1
        if x >= 183 and x <= 231 and y >= 68 and y <= 116:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 92), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 92), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud4 += 1
            rss3 += 1
            hud4 += 1
            hss3 += 1
            lud4 += 1
            lss3 += 1
            sud4 += 1
            sss3 += 1
        if x >= 141 and x <= 189 and y >= 109 and y <= 157:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 133), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(165, 133), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud4 += 1
            rss2 += 1
            hud4 += 1
            hss2 += 1
            lud4 += 1
            lss2 += 1
            sud4 += 1
            sss2 += 1
        if x >= 183 and x <= 231 and y >= 229 and y <= 277:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(207, 253), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(207, 253), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud2 += 1
            rss1 += 1
            hud2 += 1
            hss1 += 1
            lud2 += 1
            lss1 += 1
            sud2 += 1
            sss1 += 1
        if x >= 141 and x <= 189 and y >= 191 and y <= 239:
            o = Rectangle(Point(450, 357), Point(490, 397))
            o.setFill(color_rgb(125, 125, 125))
            o.draw(g)
            oo = Circle(Point(165, 215), 10)
            oo.setFill(color_rgb(255, 255, 255))
            oo.draw(g)
            bhdt10 = Circle(Point(165, 215), 5)
            bhdt10.setFill(color_rgb(0, 0, 0))
            bhdt10.draw(g)                        
            rud3 += 1
            rss1 += 1
            hud3 += 1
            hss1 += 1
            lud3 += 1
            lss1 += 1
            sud3 += 1
            sss1 += 1
    
    
    p = g.getMouse()
    x = p.getX()
    y = p.getY()
    
    
if lastplay == 1:
    status.setText("Sorry Player 1, \n but Player 2 has beaten you!")
    status.setSize(20)
if lastplay == 2:                   
    status.setText("Sorry Player 2, \n but Player 1 has beaten you!")
    status.setSize(20)
    
#Position 1 ~ (30, 410), (60, 440)
#Position 2 ~ (90, 410), (120, 440)
#Position 3 ~ (150, 410), (180, 440)
#Position 4 ~ (210, 410), (240, 440)
#Position 5 ~ (265, 410), (295, 440)
#Position 6 ~ (325, 410), (355, 440)
#Position 7 ~ (385, 410), (415, 440)
#Position 8 ~ (445, 410), (475, 440)
#Position 9 ~ (20, 410), (70, 495)
#Position 10 ~ (80, 410), (130, 495)
#Position 11 ~ (140, 410), (190, 495)
#Position 12 ~ (200, 410), (220, 495)
#Position 13 ~ (265, 455), (295, 485)
#Position 14 ~ (325, 455), (355, 485)
#Position 15 ~ (385, 455), (415, 485)
#Position 16 ~ (445, 455), (475, 485)

# c1 = (226, 28), (274, 76)
# c2 = (226, 109), (274, 157)
# c3 = (226, 191), (274, 239)
# c4 = (226, 268), (274, 316)
#
# b1 = (104, 151), (152, 199)
# b2 = (183, 151), (231, 199)
# b3 = (271, 151), (319, 199)
# b4 = (348. 151), (248, 199)
#
# a1 = (271, 68), (319, 116)
# a2 = (309, 109), (357, 157)
# a3 = (271, 229), (319, 277)
# a4 = (309, 191), (357, 239)
# a5 = (183, 68), (231, 116)
# a6 = (141, 109), (189, 157)
# a7 = (183, 229), (231, 277)
# a8 = (141, 191), (396, 239)

#if x >= 226 and x <= 28 and y >= 274 and y <= 76:
#    o1 = Rectangle(Point(28,408), Point(62, ))
#    o1.setFill(color_rgb(125, 125, 125))
#    o1.draw(g)

#if x >= 225 and x <= 275 and y >= 200 and y <= 250:
#    b = randint(1, 3)
#    if b == 3:
#        print "Scissors beats Paper, Computer wins!"
#    if b == 2:
#        print "Oh no! It's a tie!"
#    if b == 1:
#        print "Paper covers Rock, you win!"
#if x >= 400 and x <= 450 and y >= 200 and y <= 250:
#    b = randint(1, 3)
#    if b == 3:
#        print "Oh no! It's a tie!"
#    if b == 2:
#        print "Scissors cuts Paper, you win!"
#    if b == 1:
#        print "Rock beats Scissors, Computer wins!"


#q = randint(0, 15)

#p = g.getMouse()
#x = p.getX()
#y = p.getY()

#bfdt = Rectangle(Point(455, 362), Point(485, 392))
#bfdt.setFill(color_rgb(0, 0, 0))
#bfdt.draw(g)
    


# 0,1,2,3
# 4,5,6,7
# 8,9,10,11
# 12,13,14,15



                       
    

#winning_rows = [[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15] # vertical
#               [0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]  # horizontal
#               [0,5,10,15],[3,6,9,12]]                        # diagonal


#board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
#pieces = [a, b, c, d, e, f, g, h, i, j , k, l, m, n , o, p]

##############
#A.I. Process#
##############

p = g.getMouse()
x = p.getX()
y = p.getY()


g.close()