init python:
    class Player:
        def __init__(self, name, height, aLover, style):
            self.Name = "Y/N"
            self.Height = "medium"
            self.aLover = False
            self.style = "random"
#Images 
image bg office = "images/officeBG.png"
# Characters
define j = Character("Juniper")
image j basic = "images/juniperSprite.png"

define c = Character("Charis")

define a = Character("Alan")

define p = Character("")
define u = Character("???") #used when a character is unknown by name

#player character
define player = Player("Y/N", "medium", False, "random")
