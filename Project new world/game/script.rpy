﻿# The game starts here.
label start:
    call sceneOne
    call sceneTwo
    call sceneThree
    call sceneSix
    call sceneSeven
    call sceneEight
    if not fear:
        call againstCharis
    else:
        call againstAlan