$ jn = Character("Juniper's Note")
label sceneThirteen:
    "You return from the memories of the old world feeling more disheartened than usual. Usually, you would be saddened to leave the old world. But this time, things were so upsetting."
    "You fear for the next case file… What if things didn't get better? What if a new job isn't found? If the cancer gets too bad to cure?"
    "You can't dwell on what-ifs and possible futures. After all, these are all memories of one who came before. This world will soon be but a memory, replaced by something new."
    "You hear the clearing of a throat outside your room, and a familiar sheepish voice begins to address you."
    c "Uh… Greetings friend, I take it you have made your next choice. Would you have any qualms if I were to enter? We have much to discuss after all…"

    menu greetingThir:
        "Welcome the old man into the cubicle space":
            p "Come on in, Charis, there's no need to loiter outside. Take a seat. You haven't been waiting too long, have you?"
            c "Oh, not at all. Many thanks, my dear friend. I always appreciate such courteous behaviour. If only Alan were so thoughtful…"
            "The man grimaces, thinking of the countless faux-pars his poorly regarded colleague makes. "
        "Tell him you need some time alone":
            p "That last memory. Well, that was a lot to process. Would you mind giving me a little time to compose myself?"
            c "Whilst I understand entirely, I must insist it's most pressing we address this matter post haste."
            "It seems that you won't be able to get rid of Charis that easily. Whatever he's here to address you with, it must be imperative. "
    
    c "Anyhow, back to the matters at hand. How did the lies case file go? How did you render your verdict on the new world?"

    if not lies:
        p "I decided to remove lies from the new world Charis."
        c "That's excellent news! Honestly, my friend, I did not doubt that you would arrive at the correct decision."
        p "It wasn't easy. In that memory, it would have been far more accessible to tell lies to avoid the pain of the truth. But overall, the world will probably be better with more honesty."
        c "Precisely, lies and deceit hold no place in a true paradise. Nothing good can come from speaking falsely, only heartbreak, pain, duplicity, and loss."
        p "I hope that's true; part of me is still unsure if I chose correctly."
        c "Silence those nagging naysayers in your mind, my friend. I assure you this choice will benefit all in the new world. Just wait and see. "
    else:
        p "I decided to keep lies in the new world Charis"
        c "Ah… I see. Well, I suppose you see lies as having some merit on occasion. Perhaps the odd sweet lie being kinder than a bitter truth."
        p "Yes, precisely that. Some people need to lie, not to hurt others but to protect themselves or the feelings of others."
        c "I must say, I had expected you would remove lies. The false tongues of politicians and criminals cause much pain. A world without lies would have been so wonderful."
        p "Are you saying I made the wrong choice?"
        c "Well, all I am saying is that sometimes our minds are so set on the good of a concept that they are numbed to all the drawbacks. In this case, perhaps you misjudged."
        "You are well aware by now that the man clearly doesn't like conflict, and even still, he can't hide his disappointment in your choice."
        c "But enough on that. In truth, there is more to discuss about the new world and your role in it."

    c "In all honesty, I'm more here to address the state of the new world. In fact, it's a lot closer than you might have expected."
    c "The truth is, this following case file is the last. Therefore, the last decision you make will be the final step in this process. After, the new world will be brought forth into creation."
    "You expected there to be more. Is it really that time already? You had hoped to have more time, time to reflect on the old world and to have lived in it more before it all got so dreary."
    c "This is the final case file. Remember that this decision will have monumental consequences for all the lives of the new world. It is paramount that you decide carefully."
    "He reaches inside his flowing robes and brings forth the last file. This time, it is all black, with red writing. The title simply reads ‘Final Case – “REDACTED”'."

    if calm < 3:
        c "Truthfully, your decisions thus far have left me somewhat anxious as to how this new world will take form."
        c "You seem to have acted in favour of chaos rather than championing calm. I understand that this process is a lot to undertake, but billions of lives rest on your choices."
        c "With this last decision, hopefully, you can heed my words and see the path which is just and proper. Perhaps it is not too late to salvage this whole situation."
        c "That is all I have to say on this matter for now, my friend. Just heed my words wisely, and all shall be well—best of luck to you."
    else:
        c "In all honesty, your decisions thus far have filled me with confidence. You have a wise head upon those shoulders."
        c "Ever since you arrived, our moral compasses would align for most matters. Sure, the occasional choice may perplex me, but in general, you've acted in the interest of calm."
        c "It could have been easy to simply play god, quite literally. And sew chaos in the lives of these billions of people. But you've shown remarkable restraint and empathy."
        c "This last choice will have an unspeakable impact on all lives yet to come. And so, one last time, I advise caution on your part. Do not choose lightly. This will change everything."
        c "That is all I have to say on this matter my good friend. Best of luck to you on this last voyage into the old world."
    
    "With that, Charis makes his exit. He leaves you to dwell on all that he has said and all that has been done so far."
    "This last decision will be the biggest, apparently, but what could be a choice so extreme to have Charis worried like that."
    "In any case, there is no point in beating around the bush anymore. You might as well get started."

    if helpJuniper:
        "Before you get started, you notice something on your desk that is most peculiar. A post-it note appears to have been stuck near your chair, with some form of jewellery sitting beside it."
        "It's hidden under the previous case files, so you are lucky that you spotted it before entering the last file."
        "You don't remember Charis placing such an object whilst he was in the cubicle, and his moral principles likely wouldn't have allowed him to enter while you were in the memory."
        "You highly doubt Alan is the type to be gifting trinkets and writing little notes, either. In fact, you aren't even sure as to how literate the hot-headed god is in the first place."
        "Therefore, the most likely candidate would be Juniper, but what is this, and why was it placed here, out of the view of the other gods?"
        "You move the older files away to get a better look at the two new items on your desk. The jewellery is, in fact, one of Juniper's necklaces. But why would she give it to you?"
        "The pendant appears to be constructed from copper and is wrapped around a strikingly bright blue gem. The string which holds the pendant is incredibly weathered and frail."
        "You reckon this piece to be both incredibly delicate and extremely valuable. You have never seen anything quite like it. Especially not so up close. It seems to glow as you move nearer."
        "You begin to read the note to try and gather what this is all about and why it seems to have been placed with so much secrecy."
        jn "It turns out I had the final piece of the puzzle all along. Smash this in your lowest moment. I believe it will get better, as I believe it will for you."
        jn "Enjoy your life for those of us who can't. Know I will always watch over you. Saying this, I hope you never have to see me again. -Your friend, Juni'"
        "You are confused by the note. What does it mean? Smash this in your lowest moment? They hope you never see them again."
        "You want to ask them about these things, but at the same time, you get the feeling if they could openly give you the answers you seek, they wouldn't have to be so indirect to get this to you."
        "Your only choice for now is to place the necklace on, hide the note in your pocket, and begin the final case file. Perhaps things will be more apparent once this whole process is at an end."
        "You turn the cover of the file open and ready yourself to be immersed in the final memories of the old world. Is this really the end?"
    else:
        "You place the last case file down on your desk and begin to unbind the cover. Whatever you do now, the new world is right around the corner."
        "Have the choices you've made along the way been the right ones. What will Charis make of your world? Or Alan? One believes in the calm, while the others desires chaos."
        "Your mind turns to Juniper. They have always been somewhat more elusive and harder to read than the other two. You never really got to know what they wanted for this world."
        "Perhaps you'll one day find out, although it is probably a little too late now to find out, given the circumstances. Any choices you have made are already set in stone."
        "You open the case file now, a pit in your stomach forming from the immense pressure of one last massive decision. "
        