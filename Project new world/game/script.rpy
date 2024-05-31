include "characters.rpy"

# The game starts here.
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
    call sceneNine
    call sceneTwelve
    call sceneThirteen
    call sceneFourteen
    
    if helpJuniper:
        call juniperEnd
    elif calm >= 4:
        call charisEnd
    elif chaos >= 4:
        call alanEnd
    else:
        call neutralEnd