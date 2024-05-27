# Characters
define j = Character("Juniper")
default j.Name = "Juniper"
default j.Height = "tall"

define c = Character("Charis")
default c.Name = "Charis"
default c.Height = "medium"

define a = Character("Alan")
default a.Name = "Alan"
default a.Height = "short"

define p = Character("")
define u = Character("???") #used when a character is unknown by name

#player character
define pc = Character("")
default pc.Height = "medium"
default pc.Nosey = False
default pc.Name = "Y/N"
default pc.aLover = False
