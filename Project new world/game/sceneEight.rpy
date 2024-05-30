include "characters.py"

$ cookies = False

label sceneEight:

    "You start to read the words on the file, and your vision blurs. Now, it's a familiar and comforting feeling. This feeling means you're out of the office. This feeling means you get to live."
    "Fuzzy laughter comes around you, and you scrunch your hand slightly, feeling paper that seems to be holding something. As your eyes start to focus, you look down and see a greasy paper cone filled with chips."
    "A familiar, tanned hand reaches into the cone and fishes around. You look up and see Bri smiling at you."

    menu friendly:
        "After all these encounters, you still weren't sure about her.":
            pass
        "You got along with her fantastically and hoped the files with her would never end.":
            pass
        "You didn't like her much, but this person seemed to, so you'd put up with her for now.":
            pass

    b "Hey, you good? You space out a bit there."
    "She nudges you with her shoulder, and you give her a nod before looking around."
    "You smell the sea salt and look over, realizing you and Bri are halfway to the cliff top."
    "You look to your left and can see the town far away down in the valley, with rides spinning on the pier and a constant shuffle of ant-sized people making their way around."
    "You can see the beach, the clear waves lapping at the pale sands. It is one of those days that can only be described as perfect."
    "Bri's hand reaches out to take another chip."

    menu stealing:
        "Smack her hand away":
            "She scowls, but the corners of her mouth rise into a grin."
            b "C'mon, we agreed to share!"
            "She reaches over again, and you swat her away, laughing at your triumph. She seems defeated momentarily before a devious look goes over her face."
            b "Oh well, if you don't let me have one, you can't have one of the cookies I made during the last picnic. I made this batch this morning and think I've finally perfected it."
            "You narrow your eyes at her now; this is a real dilemma."

            menu giveIn:
                "You can have some":
                    p "Fine, you can have some, but I had better get the best cookie."
                    "She seems satisfied with that answer and offers you a hand to shake on the deal. You take it, and she dives back into the cone of chips with renewed joy."
                    b "Pleasure doing business with you as always, my friend. I will give you the goods once the others arrive and we get to the spot."
                    "The two of you laugh together and stuff chips into your mouth."
                    $ cookies = True
                "Get some yourself":
                    p "Nope, I'm sticking with these; you should have gotten some yourself."
                    b "booooo, you're no fun."
                    "Bri sticks her tongue out at you childishly. You can't help but return the gesture before you both break out into a smile."
                    $ cookies = False

        "I paid for these":
            b "Yeah, and the whole point of 'let's go for a picnic with our friends and share our food' is that we {i}share our food{/i}."
            b "You paid for those, I made cookies, and God knows what the other two are bringing, but where's the fun if we keep it all to ourselves?"
            p "Shouldn't we save these for when the other two get here?"
            "She rolls her eyes at you. You have a point, but still, she doesn't seem happy about it."
            b "Fine then, but you better make sure they don't get cold!"
            "You nod to her, and the two of you seem united again in the quest to get the chips warm. The other two being here would make that a lot easier…"
            $ cookies = False
        "Share the cookies":
            "Bri takes a small triumphant handful and cheers before popping one into her mouth."
            b "Thanks. I was doing quality control, right? If the other two hurry up, we should be able to get them there warm."
            "Bri seems to have a reasonable amount of concern about the temperature of the chips, which was, to say, very concerning."
            "She takes the cone from you, taking one last chip before folding it around them, wrapping the jacket she ditched, and chucking them into her rucksack."
            $ cookies = True

    "You hear two bikes approaching, one repeatedly ringing their bell and the other shouting, though you can't listen to what they're saying from here."
    "You and Bri turn to look at them. The first you see is a girl, maybe a little older than you, whose name you remember to be Caitlin. Her bike is old and busted up, but she still makes it up faster than her companion."
    "Blonde hair pokes out from under her black helmet, and she waves a long, slender, freckle-covered arm in greeting."
    "You see the boy soon after; he looks the same age as Caitlin, and you remember his name is Miles. His bike is newer and painted in a bright electric blue."
    "His hair is just above his shoulders, though his helmet still covers much of it. He lifts an arm to move his fringe out his face, and you see him almost topple over."
    "Bri waves at the two of them enthusiastically, and you can't help but offer a hand up in greeting, too. Miles' breath is heavy from the uphill cycle."
    "He offers a weak wave before folding his head in his arms to recover his breath. In comparison, Caitlin seems perfectly fine and gives you a toothy smile."
    cait "Hey, you two! Long time no see, it's good to catch up!"
    "Caitlin and Miles were more Bri's friends than yours. You don't dislike them, but like most, they seem more interested to know her than you."
    "You feel a slight jab of resentment at that, but in the end, you have Bri no matter what and surely that counts for something."
    b "Yeah, it's been ages. Let's give Miles a second, and then we can head up."
    "You and Caitlin nod, your attention back on the shorter man."

    menu bikes:
        "You and Bri had both brough your bikes":
            "You go to grab your bike."
            call bikeChoice
            "After ensuring it's okay, you wait for Miles to recover, and the other two chat idly. He eventually gives a thumbs up, and you head off."
            "It's not a long cycle the rest of the way and you all stay pretty quiet, focused on getting up. You look out again at the dazzling ocean to the side of you, and in no time, you reach the picnic spot, and everyone gets off their bike."
        "You brought your bike.":
            "Bri had hopped on the pegs of your bike on the way up."
            "You give your bike a look over."
            call bikeChoice
            "You ride up. You're the slowest, but it was to be expected with two of you on the bike. Your dad always worries about the pegs, saying that one of you could get into an accident one day, but you didn't really believe it."
            "You focus on cycling though, determined to prove him wrong."
            b "Wow… look over there, it's beautiful."
            "You briefly take your eyes off a path to appreciate the view; the ocean is always beautiful at this time of year."
            "Soon after, you reach the picnic spot, and Bri hops off. You follow."
        "Bri brought her bike.":
            "You had hopped on the pegs of Bri's bike on the way up."
            "Bri goes over to pick up her purple bike and chucks your helmet. You just about manage to catch it."
            "She inspects her bike quickly, giving a slight nod once she deems it okay and takes a seat on her mountain bike. She gestures to you, and you get on the pegs of her back wheel, putting your hands on her shoulders to hold yourself stable."
            "As she cycles up, focused on the path, you look again to the ocean. It's the best you've ever seen."
    
            menu briOcean:
                "Tell Bri to look":
                    p "Hey Bri, look."
                    "She looks over quickly, and you see a smile creep over the part of her face you can see."
                    b "Nice day, huh?"
                    "You squeeze her shoulders in agreement, and soon after finding yourself at the top of the cliff, you hop off before she does."
                "Keep it to yourself":
                    "You keep it to yourself and appreciate the view."
                    "You take it all in, and a smile covers your face, but not long after, it's over, and you hop off the bike, letting Bri get off."
    
    "You all get off your bikes, the other two dusting off quickly, clearly wanting to get to the food."

    if pHeight == "tall":
        "You are the tallest of the lot, though Caitlin is a close second, with Miles being short."
        "Bri stands taller than you saw in the last memory, though she's still average height. Her hair was different, though you realise it's been dyed a deep purple. Her favourite."
    elif pHeight == "medium":
        "Caitlin stands taller than you, and there's not much between you and Miles, although he is the shortest of the lot."
        "Bri stands at most an inch taller than you; you recall being taller than her. Maybe she's catching up. Her hairs is different, you realise; it's been dyed a deep purple. Her favourite."
    else:
        "You and Miles stand at a similar height, though you are dwarfed by Caitlin, who's much taller than all of you."
        "Bri is always taller, but she is just average height. You notice, finally, that her hair is different. It's been dyed purple. Her favourite."

    "All the bikes get locked to a tree before your party sits at the old, weathered bench that crowns this cliff. The chair is hot, and you feel your skin stick to it immediately in the heat."
    b "Right, what have we all got? I'm {i}starving{/i}."
    m "You're not looking all that starved."
    "His tone is teasing, and he gives her a playful poke. She gasps with fake shock and gives him a slight shove."
    b "Hey! If I'm gonna be a professional chef, I've gotta make sure what I make is good-"
    "She pauses momentarily, a wave of sadness washing over her before she brushes it off. The other two don't seem to notice, but you always notice when she's off."
    b "And besides, you're all skin and bone, Miles. Maybe we should be speeding this up so you don't waste away in front of us."
    "Caitlin rolls her eyes at the bickering and fishes the food from her rucksack. A big bag of crisps, already half open and some cans of lemonade grace the table."
    "You put the chips on the table, taking one. They've cooled down a bit, but they're still okay."
    "Bri chucks a Christmas chocolate tin on the table that you assume has something else inside. She also grabs out some Tupperware containers full of sandwiches. She slides one closer to you with a slight nod."
    "Miles has a bag of pick-a-mix sweets, and once they grace the table, everyone digs in, taking a little bit of everything as they chat."
    b "We did a good job, you lot. This was a great idea, Caitlin."
    cait "It wouldn't have been a good idea if you brought lousy stuff. Thanks for the chips. They're good."
    "It wouldn't have been a good idea if you brought lousy stuff. Thanks for the chips. They're good."
    "You remember your other moments so far; it's only really been you, Bri and your dad. Even if this isn't your life, you'd like to see this person less lonely."
    "You all continue to eat and chat, talking about returning to school soon, what you've been up to, and just catching up."

    if not cookies:
        "Bri sticks to her guns initially and doesn't let you have a cookie; you're starting to think she is serious, but then you catch her stealing your chips."
        p "Hey! You've stole some now, so it's only fair."
        b "how dare you say I'd steal? I would never!"
        "Bri speaks between mouthfuls of {i]your{/i} chips, a teasing smile on her face as she slides the tin of cookies over to you. You savour it, a fair payment for a handful of chips."
    else:
        "Bri hands you one of the cookies she made from the tin. The chocolate chips in them are slightly melted from the heat, making them even better. You savour the taste. There's nothing this good back in Shad Tuod."
    
    m "So I was at the arcade recently and won some stuff, you guys want something?"
    "The other two nod."

    menu item:
        "Ask what he has":
            p "Yeah! What have you got?"
            m "Here, have a look."
            "He presents a small bag of trinkets and leftover change, but one thing catches your eye."

            if pStyle == "cute":
                "A small plushie of a seagull, even if they're annoying, the plush is adorable."
            elif pStyle == "goth":
                "A small bottle of black nail polish, yours is almost out, so this would save you some effort."
            elif pStyle == "modern":
                "A small games console hanging off a keychain, you can't tell what game it could be, but you'd like to find out."
            "You make your preference known and Miles gives you a nod."
            m "Good choice, but this wouldn't be fun if I handed it over? You gotta do rock paper scissors."
            "You think that goes against offering, but with the other two egging you on, you turn to face each other to get your prize."
            m "You ready? Rock!"
            m "Paper!"
            m "Scissors!"
            m "Shoot!"

            menu RPS:
                "Rock":
                    "He puts up paper and covers your hand with a playful grin."
                    m "Aw, sorry, better luck next time."
                "Paper":
                    "He puts up paper and pauses at the draw before shrugging and handing you your prize."
                    m "I'll give you the win on a draw, I don't want this junk anyway."
                "Scissors":
                    "He puts up a paper, and you mime, cutting his hand in victory, and he passes you your winnings."
                    m "Ah, you got me, enjoy it. You earned it."

        "Don't ask":
            p "Nah, I think I'm good."
            "Miles shrugs"
            m "Suit yourself, and I'll keep my treasures."

    "As you finish the last few chips, Bri stretches her arms before taking a few steps nearer the cliff's edge."
    "She peers into the water below as if inspecting it, her face concentrated before turning to you with a toothy grin and a thumbs up."
    b "It's a good day for cliff jumping, c’mon guys!"
    m "Oh, sweet! Yeah, that sounds like great fun. We should all jump in together."
    "Silence falls as the two wait for your and Caitlin's verdict. You feel a weight in your stomach like you'll be sick. You do {i}not{/i} want to do this."

    menu fears:
        "Fear of heights":
            "You're scared of the height. It's a long way down."
            "You can just picture it now, looking down over the cliff face, knowing you must jump all the way down. You'll feel okay once you hit the water, but there's an eternity between the jump and the impact."
            "You wished you had met on the beach instead, but there was nothing to jump off."
        "Fear of the ocean":
            "You're worried about what could be under the waves; there is no doubt it was sharp."
            "The water may be nice, but there was still always a murkiness to the sea around here. No doubt there were jagged rocks just waiting to pierce through you."
            "You have no clue how deep the water is here or what was under it, and you didn't want to find out the hard way."
        "Fear of drowning":
            "You're scared of it going wrong. What if you drowned?"
            "You struggle to breathe even thinking about it, almost as if your lungs and throat are already clogging with the cold, isolating water at the cliff's bottom."
            "You try not to picture it getting swept away beneath the unforgiving waves. But it's the only thing you can think about."
        "Fear of something happening to someone else":
            "You're scared something will happen to someone else, and you'll have to do something to save them."
            "Bri can swim well enough, but what about the other two? It's easy to underestimate the currents in the ocean, and someone could easily get swept away."
            "And what if someone bashed themselves on the way down? You didn't want to think about dragging a bloodied, unconscious friend all the way to the beach. You couldn't help but think, what if you couldn't do it in time."
        "General Fear":
            "You can't place why you're afraid, but the ball of anxiety in your stomach won't go away."
            "You can't place it, but your gut tells you this could go very quickly and go wrong in many severe ways."
          
    "Before you can verbalise your worries, Caitlin speaks up, shaking her head."
    cait "No, are you two crazy? That's so dangerous I'm not doing that."
    "Miles rolls his eyes at her, and Bri folds her arms. You know what she's like now; she'll keep pushing until Caitlin breaks. All you can do is hope Miles doesn't back her up."
    m "Oh my god, it's just some water. Caitlin, grow up. Besides, I've done this before, and it's been fine. You trust me, right?"
    b "Yeah, c'mon, this will be fun! You wouldn't want to miss out, would you? Besides next week, me, {i}Hazel{/i}, and some others are meeting up to do this. She'd think you're so cool if you join us."
    "You see Caitlin's face redden at the mention of this Hazel, and she pauses, thinking it through a bit more."
    "You make a silent wish that she stands her ground; it'll be much harder to get out of it if she doesn't. She shuffles her feet before looking Bri in the eyes."
    cait "Alright, but if you drown, I'm not saving you."
    "Miles cheers and Bri seems satisfied until her gaze lands on you. She spots the fear immediately. She knows you far too well, more than you know yourself."
    b "I know that look. You can't bail on me now! You asked me to get you out of your comfort zone, and now is one of those times."
    m "God, you lot are all so childish. It's just a bit of a jump; what's there to fear?"
    "With all their expectant eyes on you, a new fear emerges. You can see it now: they all jump down, it's all fine, and they don't come back up for {i}ages{/i}, and you would have blown your chance to make friends."
    "They'd grab an ice cream and maybe get distracted at the arcade, only coming back up for the bikes as the sunset. They'd all don matching keychains, and you'd be left out."

    menu overcome:
        "No":
            p "Sorry guys, I can't do it."
            "Miles waves a hand as if to dismiss you, clearly getting bored and wanting to get to it. Caitlin seemed in a rush, too; it was hard enough to steel her nerves. She obviously doesn't want to wait for you to do the same."
            "That of course, left Bri, who seems unimpressed with your answer."
            b "C'mon, you'll have fun. Just stop worrying."
            "Their eyes are still on you, and it seems abundantly clear you are ruining their fun."
            b "You {i}asked{/i} me to invite you today. You can't just bail on me now! It's been fun, so why stop it now?"
            b "So once again, I'll ask, are you in?"
            "You feel a lump in your throat, you can't get any words out, and you feel like you're failing yourself. Why won't you just do it? But you know why: This is far too scary."
            menu confirmNo:
                "Don't do it":
                    "You shake your head; you're not doing this."
                    "Bri sighs, clearly disappointed. You think it's a bit of an overreaction, but you still can't ignore the guilt creeping over you. You did ask her, and now you won't even make the most of it."
                    "You retreat to the bench to make your decision even more evident. But the others don't even care. They aren't looking at you anymore. They're laughing together."
                    "You watch as the three of them link hands and jump over before you can hear a splash, though you feel time slow."
                    "Your heart skips a beat. What if they did get hurt? What on earth would the next memory even be?"
                    "You see the option in front of you. There is no point worrying about the following file until you're back in Shad Tuod."
                "Do it":
                    "You nod reluctantly. You can't believe you're doing this."
                    "You are feeling far too much to process what happens next fully. You hear cheering and what seems to be a splash."
                    "You feel a hand wrap around yours and squeeze it. It is supposed to be reassuring, though it isn't working."
                    "You feel your feet move, and time seems to slow. The memory has ended, and you're suspended high over the ocean. You feel like you may die."
                    "You look up quickly to see the option, wanting to make it quick."
        "Yes":
            p "Fine…"
            "Miles seems glad. Clearly, he was getting impatient. Caitlin gives you a sympathetic smile. It was clear enough you also weren't a fan, and she seems reassured that you're in it together."
            "Bri looks at you with a satisfied look. She knows you wouldn't want to miss out. Even if it still scared you."
            "You step closer to the edge and look over at the waves below. You can hear your heart pounding in your chest. Why are you doing this? Surely, it won't be worth it."
            b "Okay, you two go first, and then we will."
            "She points at you to go with her, and you nod. Miles seems glad at the chance to go and takes Caitlin's hand."
            m "Ready?"
            "Caitlin looks at him, her head shaking slightly, but Miles either doesn't notice or cares. As he runs and jumps off with an enormous cheer, Caitlin goes with him."
            "You're standing too far back to see their fate, and the anxiety is eating you up. You want to back out, but it's far too late now. You can't leave Bri to do this alone."
            b "I've got you, yeah? You know I won't let anything bad happen to you."
            "Her confidence soothes you only a little; there's not much power a teenage girl has compared to the ocean, but fitting in will be worth it. It'll be worth it to make friends."
            "You breathe in..."
            "Then out"
            "Bri finds your hand, and she speaks; you can't hear her over your heart pounding in your ears."
            "You feel her step forward. Taking you with her."
            "You step too, following."
            "Another step: you feel like you're going to throw up."
            "One more, your vision feels like it's going blurry."
            "Last one, nothing feels real anymore, and you jump up."
            "Time seems to slow; this jump appears to be lasting a lifetime."
            "Somewhere along the way, you shut your eyes. You peek them open and realise you've frozen; the moment has ended. Your body is still absolutely wracked with fear as you look down at the water now below you."
            "But that doesn't matter now as you see an option appear in front of you:"
    
    "Would you like to remove fear?"

    menu removeFear:
        "Yes":
            "You reach a still shaky hand to the option, which cements that this is the right decision."
            "The fear of jumping and missing out both tugged on you too far and now you never want anyone to be in that situation again."
            "Your option is accepted, and you feel the memory start to fall away."
            $ fear = False
            $ pChaos += 1
        "No":
            "Although today had been hard, everything seemed to scare you; undoubtedly, that was still important?"
            "You were scared to jump because you could die. You were also scared to be alone. And wasn't it important to feel that even if it hurts?"
            "You reach forward, and your option is accepted. You feel the memory start to fall away."
            $ fear = True
            $ pCalm += 1


label bikeChoice:
    menu bikeStyle:
                "Mountain bike":
                    "It's a mountain bike, reasonably practical for where you were going"
                    "You like having a bike to get through more challenging terrain, though when on paths, you often end up a bit slower than others."

                "BMX bike":
                    "It's a BMX, not the most practical, but you often do tricks, not longer rides like these."
                    "As you pick it up, you give the handlebars a light pat to reassure the bike that it can soon return to its usual stunts after today."

                "Road bike":
                    "It's a road bike, helpful for getting to school and the shops, but not as much on this cliff."
                    "You make a mental note to ride carefully and avoid any bigger rocks. A dirt gravel road leads the way to the top, so you cross your fingers and hope it is smooth."
                    
                "Hybrid bike":
                    "It's an old hybrid bike. It does a good job of getting you around."
                    "This bike was your dad's. You remember he cleaned it up for you and fixed it a few years ago. It was helpful and reliable for most things, and you were glad you had it."