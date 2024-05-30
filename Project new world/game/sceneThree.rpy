include "characters.py"

$ juniSearches = False
$ futureFriend = False
label sceneThree:
    "You make your decision and immediately feel like you're travelling far too fast. You might throw up."
    "Before you get a chance to you suddenly see mto grind to a stop, back under the artificial lights of the office."

    menu outside:
        "The air is stale":
            "You notice just how stale and still the air is here after getting to be outside."
            "It feels like a waste to trade the fresh air in your lungs for the stagnant air of the office."
        "The colors":
            "You miss all the colors; it was all so bright, and here is just dull"
            "The hazy yellowish glow of everything feels so bland now that you've seen a bright world of blues and greens."
        "The people":
            "You miss those people, Bri and the person who seem to be your dad. In a way, they were comforting."
            "It felt nice to be cared for…It was nice to be loved. You think to the gods up here: they've been polite, yes, but none have felt truly close yet."
    
    "You're brought back to yourself when you hear something slam on your desk. You can't help but jump and catch Alan's eye. He takes his hand away from your desk and you see a glass of water." with vpunch
    a "Drink up. What did you pick?"
    "You blink a couple of times,needing a moment to be yourself again. Whatever that was had felt so real. It almost felt wrong to be here now."
    a "Helllooo? Earth to [player.name]? Tell us what you picked."
    "You hear a noise of complaint come from Alan as if someone gave him a light hit"
    j "I know you two struggle to wait five whole minutes, but give them a break. Don't you remember your first file? Didn't almost feel like the end of the world?"
    "A grumble resonates from Alan and you look around at your company for Charis who seems embarrassed after Juniper's call out. You wonder why these two care so much and you wonder why Juniper doesn't."
    j "Drink your water. Is there anything else you may need?"

    menu reaction:
        "Freak out":
            p "What the {i}hell{/i} was that?! Did you guys drug me or something?"
            c "We would never!It was just a memory, you see? A scenario from the old world to help you decide on features in the new."
            a "Budget doesn't allow us to make from nothing, so we must take from what we've got. That lump of rock hasn't been worthwhile."
            c "Exactly, you simply experienced the memories of someone from that planet. You'll get more comfortable in them eventually. Juniper was right, though; we should've been more careful."
            c "I'm sorry for the apparent lack of care expressed. If you need anything, do tell."
        "Why am I back?":
            p "Why am I back here? It was so nice there..."
            "You see the corners of Juniper's eyes crinkle as if they're smiling. Though, it's hard to tell for sure with their face mask."
            j "Yes, it is… But there cannot be your home. We belong here."
            a "Yeah, don't get too attached to it. We just need it to make the new one."
            j "Juniper freezes, a wave of emotion going over them. Their eyes look onto you watching you more carefully than before."
            $ juniSearches = True
        "No response":
            "You sit in stunned silence. This was all too much."

    a "Well, you're fine now. So what did you pick?"
    "You look between the three of them; two so eager for a response that you are certain is going to disappoint."

    if pain:
        "You explained that you kept pain. Alan seems immediately smug while Charis seems far from pleased with that result."
        c "But why? Didn't you {i}feel{/i} it? Surely after feeling it, you can see why we have no need for such a thing--"
        "You wince, remembering how it felt. You can imagine in the grand scheme of life, the hurt you felt was minimal, and the pain would only increase in future actions."
        c "Another world to be played with that amount of suffering...Gosh, I can't found them why that must be the case..."

        menu keepResponse:
            "Apologize":
                "You apologize, feeling the guilt wash over you. Charis had a way of making you feel like everything had gone terribly wrong."
                p "I'm sorry… Yeah, it was bad, but we need it,right? That's why it was in that world in the first place…"
                c "The old world is just {i}littered{/i} with mistakes and errors, and--I can understand where you're coming from, but don't be afraid to make changes. They can be vital to this…"
                "You feel like a child being schooled. Not familiar feeling since the memory. You try to brush off the guilt. You aren't a child; you made a decision you saw right."
            "Try to explain":
                "You tried to explain, hoping he will hear your reasoning."
                p "Surely it's needed? If people can't feel pain, how will they know they're hurt? People could damage themselves a lot more."
                "Charish shakes his head in immediate dismissal. He doesn't seem to care for your justifications. He doesn't even care to really listen."
                "It feels like talking to an overly anxious brick wall."
                c "I'm incredibly disappointed you would view it that way…"
            "Stay silent":
                "You don't think he's going to change his mind, and you don't care. He has his opinion, and you yours."
                c "You won't even defend your choices? Well then, I have nothing more to add. I need some time alone."
        
        "Charis gives a small bow and excuses himself; you see him fervently picking at his hands as he leaves you with Alan and Juniper."
        "Alan immediately lets out a laugh. There's a blend of cruelty, enjoying it, though it's impossible to say, which is favored."
        a "I knew you were the one for the job! Keep it up, and don't worry about the old man."
        a "You learn to work past the guilt he tries so very hard to make you feel. And hey, I think you did good, so!"
        a "He won't ever understand, so no point in making him. Anyways, I have a bottle with my name on in celebration. See ya!"
        "Alan walks away."
    else:
        "You explained that you removed pain. Charish seems satisfied with that answer, and Alan lets out a groan."
        a "Seriously? Where is the fun in that? If there's no pain, every idiots gonna break their arm and not even notice!"
        "You didn't think about it that way; about pain being a communicator from body to mind looking for help. But, why does it have to feel {i}that{/i} bad? Surely removing it, people would find other ways of finding a break?"
        a "If there's no pain, there's no gain! Can't believe you chose that."

        menu removeResponse:
            "Apologize":
                p "Sorry, I didn't know you guys cared. He told me to pick what I wanted."
                a "Yeah? Well, pick better next time, or we are not gonna get along, you hear me?"
                "You know, not wanting to anger him. He seems to be one mistake away from a much more explosive reaction."
                "He narrows his gaze at you, and you're bubbling away, yet he takes the peace offering and leaves it there."
            "Explain":
                p "Hey, it really hurt! I don't want anyone else to feel the way I did there."
                a "Oh, grow up. People need to feel that or will never get anywhere. Pain makes people move; it makes things change."
                "At this rate, your 'pretty' little world is going to be a waste of resources. Just a pretty picture with no substance."
            "Stay silent":
                "You see no reason to justify what you did. What's done is done."
                a "See? You can't even get a reason! Next time, make the right decision, all right?"
                a "Don't make your world, some boring utopia; might as well of what Charis do it, then."
        
        "With that, Alan storms off, stomping away, clearly needing some time to himself. Despite everything, Charis still seems pleased."
        c "For what it is worth… Thank you. I believe you've saved many from a lifetime of pain. Yes, it could be a helpful sign, but is it worth it? I don't believe so, and I am glad you see the same."
        c "I think you did the right thing here. The people of your world will learn to live without pain and will get the blessing to never experience it."
        "Charis picks at his hands, seeing you're still a bit on edge. He gives you a smile."
        "I will leave you be, but well done on the good work today. I think we can make a beautiful world together: All of us."
        "With that, he gives you a nod and leaves you be."
    
    "You looked at the last of your company. Juniper seems thoroughly uninterested in the result you picked. They seem instead to be looking at you, searching for {i}something{/i}."

    call juniConvo

    j "Your new file should be appearing soon. I know it may hard after what they said, but be sure to follow how you feel."
    j "Don't be pressured to appease either of them. We all had to make this compromise to let you decide for us and they shouldn't sway you from being impartial."
    j "Just focus on what you see and feel in the files. Let the words and actions in them carry you to your answers. Don't worry about the other to hear and what they will say to you."
    "You give a nod. It won't be easy, you imagine. They both clearly want things in a very particular way, but that's why they need you. You must be the decider and you must settle this."
    "Juniper gives you a small wave, seeming content to leave you by yourself now."
    j "Let us know if you need anything. Your next file will appear soon and after that is lunch."
    "You feel your stomach grumble at the sound of food and hope the file comes quick. As the heavy sound of Juniper's footsteps finally fade, you look to your desk and the file is there as if it have been waiting there all along."

    if bracelet:
        "Before you read it, you feel the weight of something in your pocket. After inspection, you find the friendship bracelet Bri gave you. You hold it close for a moment, glad to have something else in the space. You place it on your desk."
    
    "With the heavy hand, you left the file and read the case name."
    "'OW_NG_CASE-3_CAMP'"
    "You can't help what happened to file two. Maybe you got lost somewhere? Or, perhaps, the numbers don't mean much at all…"
    "There's no saying, this will be the same life as the last. You may be someone completely different…"
    "You suppose there's only one way to find out; so you open the file. It's lighter than last time and you let it wash over you like a gentle breeze."

label juniConvo:
    if juniSearches:
        "Whatever it is, they seem to find it, and they regard you more seriously than they did before."
        j "What did you like about the old world?"
        "The question is so blunt that it startles you. You think back to the memory in the file and what you experienced."
        menu oldWorld:
            "The people":
                p "I liked the people. I met a girl who is my friend, and a man who was my father. They cared for me."
                "Juniper gives a knowing look, so they seem distant in a way. Perhaps their mind is cast back to the files of their own, maybe?"
                j "I have met my fair share of people in files; some have been the subjects, friends, parents, lovers...in all cases, you get to experience the love they feel. There is nothing quite like it."
                j "Up here, a lot of relationships feel...transactional. They want you on their side or they want your expertise. It's always something like that, but it's never friendship for the sake of it."
                
                menu friendship:
                    "Charis and Alan":
                        p "Are Charis and Alan not your friends?"
                        j "Not in any meaningful, no."
                        j "I suppose Charis may lend me a book once in a while… And if I find one in a file, I'm sure to bring it to him. I guess Alan is fond of me on occasion. He brings me snacks, which he doesn't do for most."
                        j "If that is friendship, then maybe…Though, some differences make it harder for any of us to be truly close."
                        j "Maybe that's why they wanted you? To bridge the gap that divides us all…"
                    "We could be friends":
                        p "Maybe we could be friends?"
                        "You see the corner of their eyes crinkle."
                        j "Maybe one day. I do not know you well enough for this yet."
                        j "Once this is all over, ask me again, and I'll let you know if the two of us are friends."
                        "They wink. You find the answer, not overly satisfying and remember to ask in the future."
            "The forest":
                p "I like the forest I was in; the air felt clean."
                "Juniper lets out a small home, as if picturing it. They seem to truly be in peace at that moment in their imaginary forest."
                j "Yes, the nature is lovely, isn't it? I've had files from many parts of the world. The number of things I have seen, such as the variety of nature, is nice."
                j "Once you get a taste of the air down there, being up here feels like breathing in water."
                j "Try to get yourself a plant of some kind. Real ones are found upon, but not impossible to bring up."
                "You know that the advice. The idea fresh air sounds worth it for a little rebellion."
            "The colors":
                p "I like the colors of the world; it was beautiful to look at."
                "Juniper laughs. It's a gravity sound that you imagine not many have heard before you."
                j "The colors? I suppose I understand. Up here is quite dull once you get used to it."
                j "I may just pay more attention to the colors next time I have a file to review. Thank you for pointing them out; It is something I forgot my love for."
                "You can't help but smile. You're glad to remind them of another source of joy previously overlooked and forgotten."

        j "Well, thank you for answering. The others lack an appreciation for that world; to hear someone care is a rare and special treat."
    else:
        "Whatever it is, they don't find it. They're searching gaze drops from you to the floor."
    j "I am sorry they are like this. They're focused on their goals and they forget the people and the humanity needed in these situations."
    j "Although, I guess it is easy to forget your humanity went up here too long."

    menu newWorld:
        "What did you want me to pick?":
            j "What did I want--Oh yes, that"
            "Considering just how much the other two cared, you're surprised that Juniper seems to completely forgotten."
            j "Well, I suppose both have their merits. Pain as communicator is important, but why does it have to feel so bad? It gets pain a lot of power that men are willing to exploit."
            j "It feels bad, but it is also proof you survived whatever hit you and it didn't hit hard enough; you can keep living. You may need rest in time, but you're ultimately alive."
            j "So, I suppose, keep it. It has enough merits in the old world at least."
            jump newWorld
        "Why do they care so much about this?":
            j "Juniper can't help but laugh a little at this. They seem glad you asked such a question."
            j "Because it has taken many years to even reach this point. This world was supposed to be recycled forever ago, but they are also indecisive."
            j "The other gods largely side with Alan or Charis on most matters, with some floating in between. Side with one is to side with chaos itself and to side with the other is to side with calm."
            j "They all want this world to follow the mold they set out: no compromises."
            j "So you are, in a way, are that compromise."
            jump newWorld
        "Why do they all want a new world so much?"
            j "Hmm...It's hard to say."
            j "Looking at those two, the reasons are simple. Alan thinks everything on that world is rotten and spoiled: to controlled with little real freedom."
            j "On the other hand, Charis sees the mess they've made. That world has been dying for years with only recent attempts from those inhabiting it to save it."
            j "If those on the world don't care for it, why should we? That is the logic they follow. Everyone else has given up on it and we should too."
            p "Do you think that we should give up on it?"
            "Juniper pauses a moment, considering their answer carefully."
            j "That is the only opinion to have. You would be wise to share it too."
        "You decide not to ask anymore":
            pass