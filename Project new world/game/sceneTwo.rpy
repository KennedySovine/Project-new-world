include "characters.py"

# Variables
$ trust = False
$ concern = False
$ playerRan = False
$ dadForgive = False
$ bracelet = False

label sceneTwo:
    scene bg office
    $ b.name = "???"

    "Your mind is already whirling with all the new information you have to process. An office of the gods and the stars, with you being their new initiate. And Charis, Juniper, and Alan too."
    "You get the feeling they all have their own desires and motivations, and that you'll be pivotable to their fruition or failures. What a responsibility."
    "However, you have no time to further process this whole situation as your head suddenly twinges with a bizarre sensation and your vision begins to blur and contort."
    "As far as you know, you never used drugs before, but this experience now could only be comparable to taking hallucinogenic substances."
    "Did the gods drug you? Was this all some ploy to trick you? Your consciousness was fading in and out, and you begin to panic a little, unsure of what is happening and what is real and fake."

    menu relax:
        "Try to relax":
            "You try to calm yourself; you have to trust them."
            "As your breathing calms, your heartrate normalises. You put your trust in Juniper, Charis, and Alan. This must just be part of the process."
            "The hall of gods fully fades, and in its place an entirely different realm begins to form around you."
            "It's quite beautiful really. You take a deep breath, and smile as you inhale the scene of fresh pine trees, and the overgrown summer grass. "
            $ trust = True
        "Panic":
            "You begin to shout and call for help."
            "Your heart rate accelerates, and your vision grows blurrier. Your head aches with a sharp pain, making you scream out in agony."
            "Though your vision is so faint and faded, you make out the silhouette of someone in front of you, and you can just about make out their voice."
            c "It's okay, I'm here. Try to control your breathing. Everything is going to be okay, just try your best to relax. The first time is always quite overwhelming."
            "You feel Charis take your hand, trying to reassure and calm you."

            menu panicChoice:
                "Trust Charis":
                    "You stop your struggling and try to ease your breathing. Your heartrate is still elevated, but it's beginning to stabilise."
                    c "That's it, you are going to be okay. I'll be here as you make the journey. There's nothing to be afraid of, enjoy this experience it is a blessing to traverse what once was."
                    "What does he mean? What once was? You are perplexed by this whole ordeal, but when you open your eyes to reply to him…Charis is nowhere to be seen."
                    "Instead, all around you are towering trees. The office cubicle you were once in is all gone, and the chair you once sat upon is now a large rock. "
                    $ trust = True
                "Struggle":
                    "You thrash and struggle, but it's no use. You feel Charis doing his best to hold you in place. Is this to stop you from escaping? Or to stop you from hurting yourself? You're not so sure."
                    "You lose the last of your strength and the office fades from your vision. Around you now is a vast green forest."
                    "You'd almost be in awe if it wasn't for the anger and resentment you felt for being tricked by these gods."
                    $ trust = False
    
    #scene bg forest
    "Your vision is fully clear now, as are all your senses. You are completely bewildered; you can smell the fresh pine trees and hear the birds contently chirping."

    if not trust:
        "You shake your head; you know this isn't real. Whatever they drugged you with is powerful. There must be a way to wake up."
        "If not, you may simply have to wait out the duration of the hallucination."
    else:
        "You smile as you glance back and forth. So many wonderful sights, smells, and sensations on your fingertips to process."
        "You have no idea how this is possible, but it is an incredibel experience to finally be free outdoors from the stuffy office of the gods."
    
    "You hear a voice calling to you. You turn around to face the souce and see a beaming child walking towards you into the clearing."
    #show bri basic at right
    "They have slightly tanned skin, and the most striking eyes which seem to glow as the light bounces off them. They also have curly, dark brown hair, which is tied up with a hairband."
    u "There you are! Your dad told us not to wander off! You're gonna get us in trouble."
    "Dad? As far as you can tell, the yare referring to this person as being {i}your{/i} dad. You're confused; how does this person know you? Isn't this just a hallucination?"

    menu info:
        "Ask where you are":
            player "Where am I?"
            b "You feelin' okay? We're in Pandistone park, of course. Y'know...for your birthday? We came here last year too. You love being in the woods, silly."
            "You don't remember these woods. Surely, such a spectacular sight would resonate in your memories, but it is as though it is your first time in this place."
            "It might be wise to pretend you remember things which you don't, or else you may lose the trust of this person."

            menu infoChoiceOne:
                "Pretend you remember":
                    player "Of course I remember, how could I not?"
                    b "You have a weird sense a'humor, you know that?"
                    "It seems she has let go of her concerns for your current wellbeing."
                    $ concern = False
                "Admit you don't remember":
                    player "I have no idea where that is, or why I'm here."
                    b "When your dad catches up, I'll get him to give you some water. You might be getting dehydrated or something."
                    "The girl evidently thinks you are acting unusually to how she would expect, but you have no idea how to act. This is your first meeting."
                    $ concern = True
                    if not trust:
                        "Besides, she's not real anyways; merely a fignment of your hallucinating imagination. Your real goal should be to escape this mind game and return to those gods who screwed you over."
        "Ask who she is":
            player "Who are you?"
            b "Luke, I am your father..."
            "They laugh, but your face tells them you aren't following along with the reference they seem to be making."
            b "You doin' okay...? How many fingers am I holding up? Is it your eyes or your memory that's playing up?"
            "The barage of questions doesn't help with your confusion, and they seems to be able to tell this."
            $ b.name = "Bri"
            bri "It's me, Bri. Y'know, your best friend! Or, I guess, Briannah if that helps you remember, but I prefer Bri..."
            "Bri? You dont recall having a best friend, or any friends for that matter. Yet, this girl seems adamant that you are close."

            menu infoChoiceTwo:
                "Pretend you remember":
                    player "Of course, Bri. I was just pulling your leg!"
                    b "You had me worried there for a minute, y'know. I'm glad you're alright."
                    $ concern = False
                "Admit you don't remember":
                    player "I don't remember a Bri. Are you sure I know you?"
                    b "I'm really worried about you. When your dad catches up, I'll get him to make sure you're not unwell..."
                    $ concern = True
            if not trust:
                "Whatever they doped you with must be powerful enough to create such a character in your mind."
                "They look and sound so realistic, but they did say they were gods after all. Palour tricks like this must be child's play to them...literally."
        "Ask for the date":
            player "What's todays date?"
            b "The date? Real funny. You been replaced by some kind of alien?"
            
            menu alien:
                "Tell the truth":
                    player "I'm not an alien, I came from the stars. A hall of gods in fact, who oversee the earth."
                    if not trust:
                        "Perhaps this will finally break you out of the this illusion. If you can break the narrative being told, you can snap this character out of their script."
                        b "Ah, I see. Okay, let me get into character..."
                        "The girl clears her throat and changes her body language."
                        $ b.name = "Bri"
                        b "Greetings mighty sky god! I'm Briannah, but you can call me Bri. You must be confused from your travels. The date is the 15th of July, 2003."
                        "It's no use trying to tell her the truth. She'll either think you've done mad, or believe it to be fictional roleplay. At least you have an idea of the time you are experiencing now."
                        b "I remember the date because it's my bestest friend's birthday!"
                        "She seems to be referring to you as her best friend."
                        $ concern = False
                "Be an alien":
                    player "Greetings, earthling. I am Xb-LIV9-Gl3D of the Quantar region."
                    b "Nice to meet you..."
                    "She snorts laughing."
                    # b.name = "Bri"
                    b "Yep, I'm not even gonna try to repeat that name, sorry. But, I am Briannah of the planet earth. It is an honor to be your first contact. The star date is the 15th of July, 2003."
                    "Your lie seemed to work. A clever ruse to extract the date from this Briannah without rasing concern to your true nature."
                    $ concern = False
                "Ignore the question":
                    player "Just tell me the date already. I don't have time for games."
                    b "Gee, somebody woke up on the wrong side of the bed today, huh? It's your birthday, isn't it..."
                    "She expects you to know this information. Yet, when you think about it, you have no idea when your birthday is."
                    b "You really don't remember...? Well, its the 15th of July, 2003. Once your dad reaches us, I'll get him to make sure you're okay. You aren't looking too god. Just stay put for now."
                    $ concern = True
                    "It seems your bluntness has caused the girl to become concerned about your wellbeing and state of mind."
    "A new voice enters the clearing; a shout from not too far behind where your supposed friend entered the area."
    u "{player.name}! .... Briannah! ... Are you there?!"
    "The girl turns to face the voice and cups her hands around her mouth to shout back."
    $ b.name = "Bri"
    b "Over here! We're just ahead of you!"
    "Bri shouts back, attracting the attention of the figure in the near distance, who is now hurrying over."
    #show f basic at left with moveinleft
    u "Thank goodness you are alright; I was so scared. Didn't I tell you to not run off too far ahead. I could have lost you in these woods forever."
    b "I'm sorry. I tried to tell them to slow down and head back to you. I said 'Your dad will be mad if you go off too far'."
    "This man is apparently your dad. Again, no recollection of memory of this person, so you remain silent for now."
    f "It's okay, Bri. It's my kid that I'm agrier at right now. I know you aren't to blame."
    "He turns to you"
    f "What were you thinking? You realize how bad this could have been? You could have gotten lost, or hurt, or worse. I can't believe you would be so reckless."
    f "Enough standing there and looking at the ground! Speak up! What do you have to say for youself?!"

    menu fatherChoice:
        "Apologize":
            player "I'm sorry, everything is just so overwhelming. I wanted to be alone for awhile to process things."
            
            if concern:
                b "I have to admit, they seem a little weird today. I think the birthday is overwhelming them and they might need some water. They were quite confused just now."
                "Briannah seems to back you up and tries to defuse the situation with your dad."
                b "Also...I kinda...maybe told them I'd race them to Pandistone lookout..."
                "You get the feeling that Bri is not being entirely truthful here. It seems her concern for you has led her to cover for your actions."
                f "You did what? So, you weren't as discouraging as you said you were! You do realize this park is 15 kilometers wide."
                b "Well, I didn't mean to cause a fuss...I just wanted to have fun with them on their birthday. We knew the way to Pandistone lookout: promise!"
                f "Okay, okay. Look, I don't mean to shout, I just...I couldn't bear to lose them, or either of you. Heaven knows I would never hear the end of it from the Fosters..."
                "You guess that they are Bri's parents."
                f "Let's just head on to the lookout. We've gone a little off track, so try to be careful, kids."
                "Bri rushes ahead, perhaps upset that she has to take the brunt of the man's anger in your place."
                f "Slow down, Bri! This hill is too steep to be moving that fast...!"
                "Bri turns to look at the man and almost smugly, says..."
                b "I'll be fine, I do this all the ti--"
                "Before she can finish, she trips backwards on a jutting stone in the ground. You grab out to try to stop her form falling and in turn, she manages to grab a tree branch and regain her balance."
                "However, you have nothing to support your own weight, having thrown youself forward to save the girl. Now, you are tumbling at an alarming rate down the hill."
                "As you near the botton, your foot slams into a jutting rock, injuring your ankle." with vpunch
                "Meanwhile, your head bumps into the firm ground, causing a bump to begin to form." with vpunch
                #show bg forest with renpy.blur((5, 5), 1)
                "Your heart faces, and your vision blurs. You feel the pain...How can this be? This isn't real, right? How can it feel so painful...?"
            else:
                f "What did you want to process? You were having a great day, or, at least I thought you were. I don't know what to do to make you happy..."
                "You don't know what to say. You have no affinity to this man, and yet he speaks of you as his own."
                f "I'm just trying my best! I always have. I'm sorry I can't give you the perfect life, I really am...I just wanted you to have a good birthday. I know you must have a lot on your mind."
                "You see a tear begin to roll down the man's face."
                f "I'm sorry for raising my voice. Let's just get to the lookout and try to put this behind us."
                "As you walk down the steep hill, you hear the man sniffling, clearly still upset that he believes to have failed you."
                "While you and Bri walk ahead down the steep hill, you turn to check on the man."
                "As you begin to turn back, your foot slips into a hole in the terrain, causing your ankle to twist."
                "You react to the pain, but the rest of your body begins to careen down, sending you rolling towards the bottom of the hill at an alarming rate."
                "As you reach the bottom, your head thumps onto the solid try mud, leaving you with a soon-to-be bump on your head." with vpunch
                "How is this possible? Your ankle singes with pain, and your head is thumping from the impact...Surely, pain is impossible in this illusory world...?"
            $ playerRan = False
        "Get Away to Think":
            "This is all too much. You need to get away from these people and think about this situation."
            "You bolt off into the distance, with no real goal or direction in mind. You just want out of this hallucination, and away from these bizarre people inside your head."
            "It's all just a dream..."
            "It's just a dream..."
            "It's a dream..."
            "..."
            "...is it a dream?"
            "As you run, you feel your heart racing, the wind flowing through your hair, your breath growing more strained from the exertion."
            "Your legs are certainly shorter than you remember, and your hands are smaller too. You are certainly in the form of a child. All of your senses tell you this is real, but it can't be."
            "Maybe you just need to wake yourself up somehow; something to awaken you from this drug induced stupor."
            "As you think, your focus wanes from your running feet. You neglect to watch where you are going."
            "Your foot gets caught by a root, sending you tumbling to the ground and twisting your ankle." with vpunch
            "You scream in agony as you feel the pain of the twisted food and raise your fingers to massage the bump which is now forming on your grazed temple."
            "You were sure this was all a trick, an illusion or memory of a time once long ago. But, all the sensations you've felt, both positive and negative, have led you to believe this is very mich real."
            $ playerRan = True
    
    if playerRan:
        "Bri and your father soon appraoch, having likely tracked you from your screams after the injury."
        f "Are you okay? I'm so sorry, {player.name}. I've already ruined your birthday by shouting at you and now you're hurt because of me...!"
    "It makes no sense how this pain can feel so authentic and real. You were in the office, reading the case file. There's no way you could really be on earth in another body...right?"
    "You feel the tears running down your cheeks caused by the pain of having twisted your ankle."
    f "Please forgive me...I know I'm not perfect, but I love you with all of my heart, and I always will. I thought Pandistone would be the perfect way to spend your birthday..."
    "You are in a tough situation. The pain is burning, you have no means of help besides this man claiming to be your father. Do you ease his worried? Lie to make them feel better?..."
    "You are clearly in this scenario to play a role; to live an experience. Do you continue to fight against it, or should you embrace the character you control, and ease the conflict?"

    menu role:
        "Embrace the Role":
            player "It's okay, dad...I...I love you too. I know you--you only wanted me to have a good day...I just haven't been feeling like myself..."
            "You try to get across what you think will best east the man's sorrows between labored breaths and grunts of pain."
            "For the first time, you see a pained smile cross the man's face, due to his worries for your safety. You feel a warmth in your heart: a bond to them that you didn't feel until now."
            $ dadForgive = True
        "Avoid the Role":
            "You look away from him, unable to face him in this moment. You can't bring yourself to lie to him, or to pretend to be someone you're not."
            f "I understand...you must be feeling horrible. We'll talk more later...Just know--I'm here for you..."
            "The man seems really hurt that you would ignore his attempt to mend the situation. Even then, his love for you seems to overcome this emotional pain."
            "It seems whoeevr you are in this scenario, be it a figment of your mind, or a real person, they care for you deeply. He is your father now."
            $ dadForgive = False
    
    f "I suppose this is the first time you are ever feeling pain like this, right, champ?"
    "You just nod as the pain is too much to talk anymore."
    f "Pain sucks, but it's somethign we need to teach us to care for ourselves. We learn through pain where our limits are, and what not to do."
    "As he says this, you find it hard to fathom why someoen would want pain. You feel horrendous in this agony."
    "He begins to massage your injured ankle and applies some ointment from his backpack."
    f "I always come prepared. I always knew one day I'd need to help you if you fell..and like now, I'll always be here to help you back up."
    f "Pain doesn't last forever; time heals all wounds, as some say."
    "You appreciate him talking to you to distract you from your pain. You notice Bri coming over and crouching down beside you."
    b "I'm sorry your birthday turned out a bit sucky...but, at least we still got to spend the day together! There's something I wanted to give you, actually...I was gonna wait, but..."
    "Bri puts her hand into her pocket and brings out what appears to be a bracelet. it looks liek the one on her own arm, though a bit more cudely made."
    b "I made this to match the friendship bracelet you got me last year. I mean, we gotta have a pair, right? No matter where we go, or what pain we go through, we'll always have each other."
    "The girl smiles and offers the bracelet to you. Meanwhile, your father is struggling to lift you without hurting you."

    menu braceletChoice:
        "Accept":
            player "Thanks...Bri...This is a really--really thoughtful gift--"
            "You convey your thanks between the twinges of sharp pain."
            player "I-I'll treasure it...forever..."
            if dadForgive:
                "Bri's face beams with a wonderful smile, and you feel a warmth inside, much like the one you felt when telling your father you loved him."
            else:
                "Bri's face lights up with a lovely smile. This makes you feel a little warm inside. You feel a bond forming with her, which you haven't felt before."
            $ bracelet = True
        "Decline":
            player "Nows...nows not really the best time...could you--help me up?"
            "You just about make out as you grunt and groan while your father continues to struggle to lift you up."
            b "Oh...yeah, sorry...Just thought it might a' cheered you up..."
            "Bri puts the bracelet back in her pocket, trying to hid her disappointment. She now uses both of her hands to help life you up."
            $ bracelet = False
    
    f "Right, now that you're back on your feet, it's time we get you to a hospital. We're going to have to leave Pandistone lookout for this year, kids."
    b "It's okay, no worried! Let's just get them to the hospital so they can get help. Then, the pain will be gone in no time!"

    "As the two support you back to the main path, your consciousness begins to fade in and out. You are unsure if this is the pain or if it's something to do with the gods."
    "It seems like it's been forever since you saw them. Were they just a dream? Perhaps this really is the reality and those bizarre gods were just a nightmare."
    "Eventually, you lose the last of your strength and you drift away into a hazy sleep."
    scene bg_black with fade
    pause 2.0
    scene bg_white with fade
    "Instead of the hall of gods, you are instead in an entirely white void. There's no sound, wind, sensation...nothing. You are alone in this void."
    "A soothing female voice begins to call to you, but you can't loate its source."

    
    menu removePain:
        u "Do you want to remove pain?":
            "Yes":
                menu removeConfirm:
                    u "Are you sure you want to remove pain from the world?":
                        "Yes":
                            $ pain = False
                            $ player.calm += 1
                        "No":
                            jump removePain
            "No":
                menu removeConfirm:
                    u "Are you sure you want to keep pain in the world?":
                        "Yes":
                            $ pain = True
                            $ player.chaos += 1
                        "No":
                            jump removePain
            "What?":
                u "Before you can continue, you must choose...Yes?...or...No?"
                "Do you want to remove pain from the world?"
                menu confirm:
                    "Okay":
                        jump removePain
                    "Why?":
                        u "This is the purpose of your presence. To make the decisions that will shape the new world. Take your time, and choose wisely, but in the end you must decide."
                        jump removePain