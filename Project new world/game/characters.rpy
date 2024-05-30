init python:
    class Player:
        def __init__(self, name, height, aLover, style, chaos, calm, save):
            self.name = name
            self.height = "medium"
            self.aLover = False
            self.style = "random"
            self.chaos = 0
            self.calm = 0
            self.save = False

# World Choices
define pain = True
# Images 
image bg office = "images/officeBG.png"
define bg_black = Solid("#000000")
define bg_white = Solid("#FFFFFF")

# Characters
define j = Character("Juniper")
image j basic = "images/juniperSprite.png"

define c = Character("Charis")

define a = Character("Alan")

define p = Character("")

define u = Character("???") #used when a character is unknown by name

define f = Character("Father")

define b = Character("Bri")

#player character
define player = Player("Y/N", "medium", False, "random", 0, 0, False)
define p = Character(player.name)