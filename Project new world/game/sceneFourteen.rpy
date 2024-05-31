label sceneFourteen:
    "BEEP"
    pause 1.0
    "BEEP"
    pause 1.0
    "BEEP"
    pause 1.0

    "Your head is ducked down, and you are staring at the floor."

    menu look:
        "Look up":
            "You manage to lift your heavy head. Your stomach feels sick as your eyes meet the man in the bed."
            "You wonder for a moment if the grief you feel is the bodies or yours. In this moment, you think the disconnect more than ever before. This moment is private. It shouldn't be yours."
            "He gives you all the smiles he can muster. Do you remember how he looked last file? How can he manage to look {i}worse?{/i} The smile, backed up by the far too infrequent beeps, proves one thing."
            "He is still alive at this moment."
        "Stay looking down":
            "You trust this body you've been borrowing; they don't want to see this, and you don't either."
            "In this moment, you remember just how much this body isn't yours, how you're just a visitor in these moments. The most you can hope for is that your being here doesn't take them away."
            "Because if there's one thing that isn't reassuring, it's the slow beeping that signals an end."
            "You hear his breathing; it's shallow, but with nothing else to focus on, it rings loud in your ears."
            f "Hey… kiddo."
            "Your eyes drift up to meet his, and you're immediately taken aback."
    
    f "You um… seen a ghost? Looking a bit pale…"
    "You want to scream at him, at the gods, at anyone. This isn't {i}fair{/i}. Why must it be like this?"

    menu dadNeed:
        "Do you need anything?":
            f "I think a nurse is coming soon, so I can hold off, maybe just some water?"
            "You nod and stand up slowly, your legs shaky and unstable. You pick up his glass with trembling hands, and it sits alongside some flowers, and a get well soon card."
            "You manage to peek at the words inside the card. It's from Bri's parents. She hasn't signed it. Of course, she hasn't. She'd have to be here to do that."
            "You pass him his water, and he gives a weak nod in thanks."
        "How are you feeling?":
            f "To be honest… not the best. I'm only just up, and I want another nap… I'm tired."
            "You bite the inside of your cheek and taste a metallic rush of blood. You don't want him to sleep. You can guess how this memory ends, and sleep seems to be a danger."
            f "But hey… The doctor said they have some new trial thing? Next week or so? Just gotta hold on ‘til there, and then we can go camping again."
            "His words fall flat at soothing you. It's nice he's trying, at least."
        "Don't worry about me":
            "He looks away out the window. You follow his gaze and see a well-kept garden; at least he's been moved to a better room. Memories resurface of you sitting in that garden with your dad on the better days."
            f "I have to worry about you, kid. That's my job…"
            "He lets out a weak cough, and you cringe at the sound."
            f "How about a deal we both get to worry about each other? That way shouldn't be it, hey?"
            "All you can do is nod. Maybe it's a fair deal, all things considered."
        "You can't find the words to say":
            pass
    
    f "Anyway… tell me how you've been getting on. Have you seen Bri recently?"
    "Last memory, something had changed, and she was just gone. You try to recall the memories between then and now, but there's nothing. She hasn't come back."
    "Before you can respond, there's a knock at the door, and a nurse lets herself in"
    n "Hello? I just need to do some checks. If you wouldn't mind giving us ten minutes?"
    f "Don't worry, bud. Just come and say bye before you have to head off. Alright?"
    "The nurse gives you an expectant look, and you nod back to her and your dad before leaving the room."
    "You step out of the room and sink to crouch on the floor. You're hyperventilating."

    menu feelingDad:
        "You feel disconnected":
            "You feel more disconnected to the body than usual; you don't have to feel all this."
            "This isn't you; who are you to witness this moment? Who are you to take it from this person?"
            "In some ways, it doesn't matter. This world will be gone soon, so no matter what happens at this moment, it won't last long. It may as well not happen."
        "You want to go back to the hall of gods":
            "You spend most your time there longing for these memories, but this time, you want nothing more than the sterile, empty office; it would be better than these sterile, empty halls."
            "You want to see the other gods; you want them to care about you beyond the decisions you make."
        "You feel too much":
            "Your chest feels tight, and you try to regain your composure. He's not looking good, but maybe you just have to press on and believe."
    
    "You manage to calm yourself; you want to talk to someone, but who's even left? Who would even want to talk to you?"
    "Your dad is dying, and the only other person is Bri… You hurriedly get your phone out of your pocket and thumb through your contacts. Right at the top, there she is. Of course."

    menu callBri:
        "Call Bri":
            "You press her contact and hold your phone up to your ear, shuffling a bit to be more comfortable on the cold hard floor."
            "The phone rings…"
            "And rings…"
            "And just when you think of hanging up, you hear a crackle and a voice on the other side."
            b "Hello?"
            "You didn't really expect her to pick up, and for a second, you're silent before finding your words."
            p "Hi, uh- it's me."
            b "I know I have your number saved still… what's up?"
            
            menu whatsUp:
                "I miss you":
                    "Bri doesn't say anything for a long time, you double-check to see if she's even still on call, but her name is still there."
                    b "I… miss you too. Sorry I've been gone so long. I just--I can't face you right now. I {i}failed{/i} you."
                    "You hear her voice wavering; you've both been holding back a lot clearly."
                    b "I wanted to help. I really did. It's why I'm here, why I do medicine. I couldn't just sit there and… and I know you never asked for it, but God, I had to for all of us."
                    b "I've been a bad friend, but I wouldn't do now any different. I assume you're calling because... it's almost over, isn't it?"
                    p "Yeah…"
                    b "I can't help you there. Talk to my parents, though. You know they love you and wanna help you through this. Mum told me you were still having money troubles don't be shy to stay with them."
                    "There's a lull in the conversation. Both waiting for the other to speak."
                    b "Text me if… if there's a funeral. I would like to go. I need to go back to work now. I'll talk to you then."
                    "You don't feel much better after that. If she also misses you, why is she still so cagey and distant? Why have you lost everything from those memories?"
                "My dad's dying":
                    b "I know."
                    p "No, like-"
                    b "I {b}know{/b} okay!? I have studied this for the last few years, and I know his odds of survival more than I know how my favourite recipes are these days! I know I haven't been there, but I've cared!"
                    "You're stunned into silence, and you really have no idea how much she cares, even if she is only willing to do it from a distance."
                    b "I'm sorry I failed… I wanted to push the research forward, I tried to find new treatments, the cure, anything! I just… I don't want him to die either…"
                    b "I have to go back to work now, okay? Text me when the funeral is, and we can talk then."
                    "With that, you hear a click and feel worse than you did before. It is a shame that to see your friend again, the worst possible must happen. It isn't fair."
        "You dont want to talk to her right now":
            "She made her choice years ago; she's gone, and she put no effort into seeing you or your dad."
            "Why would you even bother trying to communicate? She probably wouldn't pick you up, and if she did, she'd just shut you down."
    
    "Your mind wanders to your work; you found a new job in the space in between, but the pay is terrible, you aren't sure how you're going to make this all work."

    if helpJuniper:
        "The only relief you feel is knowing that after all this, you get to go to your old life. You rub your thumb over the necklace around your neck, hoping your life is better than this one."
    else:
        "The only relief you feel is knowing that after all this, you get to go back to Shad Tuod"
    
    "The nurse exits the room and sees you on the floor."
    n "You're okay to go back now… I advise you to say anything you need to today."
    "Your stomach drops. This is it. "
    "Your dad is going to die. "
    "Your best friend doesn't want to speak to you."
    "You barely have a job."
    "You have nothing left."
    "You give a slight, brave nod and head back into the room. He looks the same as before, but it's clear he knows it too. This is likely it."
    f "[pName]…"
    "You freeze. How did you miss this? How did he {i}never{/i} say your name?! This could be a coincidence; you could just share a name, but at this moment, it feels like he's addressing you and no one else."
    "It was your life all along. You feel a teardrop as the pieces fall into place. Bri is {b}your{/b} friend. She abandoned {b}you{/b}, and now your dad is, too, because everyone leaves you in the end!"
    f "[pName] hey hey… Don't cry, alright? Your dads here…"
    "Those words just make you cry more. That separation of yourself from this moment was the main thing keeping you stable; apparently, now you're all one and the same, and everything hurts."
    f "Oh, kid… There's good news, alright? There's a new treatment available. I agreed to try it tomorrow if, uh…"
    "He leaves the last words unspoken, but you know. It's if he lives to tomorrow."
    p "What are your chances of…"
    "You can't even finish the sentence and your dad winces a bit as he delivers you the news."
    f "To make it through tonight? They aren't too bright. But your dad's a fighter. I'll make it through, and we'll go camping yeah? You, me and Bri, like when you were kids…"
    "You drop your gaze from him, staring at the floor. He doesn't say anything for a moment. All you can hear is the beep of his heart rate. The only proof he's still here."
    "And then, it slows."
    "You try desperately to look up, but you find your eyes glued to the floor. Is he dying? Is it truly the end? Or is time just stopping, or does he survive?"

    
    if helpJuniper:
        call fourteenJuniper
    
    "The drone of a flatline rings through your ears, and slowly the floor tiles morph into the words:"
    "Would you like to remove death?"

    menu removeDeath:
        "Remove death":
            "This grief, this agony, you never want to feel anything like it again. You shuffle your foot onto the option to remove death."
            "You feel the moment start to slip away, and you sigh in relief, ready for this nightmare to be over."
            $ pCalm += 1
            $ death = False
        "Keep death":
            "Even after all this pain, you can recognise it's needed. It's the circle of life, after all. Can't have life without death."
            "You feel the moment start to slip away, and you sigh in relief, ready for this nightmare to be over."
            $ pChaos += 1
            $ death = True


label fourteenJuniper:
    "And is it worth risking? Is it even worth coming back to this life?"
    "You rip the necklace off in one swift motion and hold it up, ready to throw. Time is slowing, and each beep sounds more and more like a flatline. You feel your heart pound in your chest and."

    menu necklace:
        "Throw it":
            "You punt it onto the floor with all the anger and sadness your body has built up over the last few memories. The gods have been so ready to destroy this world, and clearly, theres are problems."
            "But, like Juniper wants to fix this world, you want a chance to fix this life. It's broken, but you wouldn't trade it for a life in that office in a million years."
            "You make a silent prayer to Juniper; you aren't sure the gods work like that, but you hope they hear you one final time."
            "As the stone hits the ground and shatters, so does your mind. A splitting headache courses through your skull, and you keel over in pain. You remember so much. You remember {b}everything.{/b}"
            "But it's all too much, and you pass out."
            return
        "Don't throw it":
            "You drop your hand. You don't want this life. You feel bad for going against Juniper and pray they can understand. You don't want to have to fix this life. Old world be damned."