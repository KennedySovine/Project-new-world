include "characters.rpy"

$ s = Character("Server")
$ foodState = "Solid"
label sceneSeven:
    "The whole process seems much smoother this time as you breathe out, and the gentle hum of the office focuses you back to yourself."
    "This process was already so much easier. You can only guess one day, slipping into these files may be as simple as breathing. Leaving, too, was easier physically, though a part of you longed to be back in those woods."
    "Another louder, more stubborn part of you, however, is hungry."

    if seaGlassGreen:
        "You place the green sea glass on your desk. You’re thankful for the girl who gave it to you. The small trinket does brighten up the place."
    elif seaGlassPurple:
        "You place the purple sea glass on your desk. It's less shiny in the office than in the sun, but it’s still a beautiful reminder of the file and the time you spent."
    
    if bookedGain:
        "You thumb throught the bird book, many parts are circled and underlined, notes scrawled in with biro. You can't help but smile as you place it on your desk."
    
    ...

    s ...

    menu foodState:
        "Solid":
            ...
            $ foodState = "Solid"
        "Liquid":
            ...
            $ foodState = "Liquid"
        "Gas":
            ...
            $ foodState = "Gas"
        
    ...

    menu lunchTable:
        "Sit with Charis":
            call charisLunch
        "Sit with Alan":
            call alanLunch
        "Sit with Juniper" if oldworldInterest:
            call juniperLunch
        "Catch up with Juniper" if strikes >= 2:
            ...
            jump lunchTable
    
    ...

label juniperLunch:
    ...

    menu confrontJuniper:
        "Staring?":
            ...
        "Sit silent and stare back":
            ...
        "Avert your eyes":
            ...
        
    ...

    $ strikes = 0
    menu oldWorldJun:
        "It's been fun":
            ...
        "Why are you asking?":
            ...
            jump oldWorldJun
        "I don't like it":
            $ strikes += 1

    ...

    menu newWorldJun:
        "Looking forward to it":
            ...
            $ strikes += 1
        "Its a lot of responsibility":
            ...
        "There's nothing wrong with the old one":
            ...

    ...

    menu shadOpinion:
        "I like it":
            ...
        "It will grow on me":
            ...
        "I dont know where I'm from":
            ...

    if strikes >= 2:
        ...

        menu speakUpJun:
            "What do you want from me?":
                ...
            "What is your problem?":
                ...
            "Let them walk away":
                ...
        jump lunchTable
    
    else:
        ...

        menu whatJuni:
            "Why can't I remember?":
                ...
                jump whatJuni
            "Are all the gods from there?":
                ...
                jump whatJuni
            "Who was I?":
                ...
                jump whatJuni
            "You have nothing else to ask":
                pass
        
        ...

        menu saveWorld:
            "Help":
                ...
            "Don't get involved":
                ...
    return

label alanLunch:
    ...

    if oceans:
        ...
        if chaos == 2:
            ...
    elif forests:
        if chaos == 0:
            ...
    
    menu alanChat:
        "Tell me what you want in the files?":
            ...
            jump alanChat
        "I'm supposed to pick for myself?":
            ...
            jump alanChat
        "Why do you care?":
            ...
            jump alanChat
        "Nothing else to ask":
            pass
    
    ...

label charisLunch:
    ...
    menu catLunch:
        "Pet cat":
            ...
        "Avoid cat":
            ...
    
    ...

    if oceans:
        ...
    elif forests:
        ...
    
    if calm >= 2:
        ...
    
    menu charisChat:
        "Tell me what you want in the files?":
            ...
            jump charisChat
        "I'm supposed to pick for myself?":
            ...
            jump charisChat
        "Why do you care?":
            ...
            jump charisChat
        "Nothing else to ask":
            pass

    ...
    return