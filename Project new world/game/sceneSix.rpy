$ f = Character("Dad")
$ bookedGain = False
$ seaGlassGreen = False
$ seaGlassPurple = False

label sceneSix:
    "You close your eyes, remembering how your vision distorted the last time making you feel sick. It will not happen again; you've learnt better now."
    "Last time felt like drowning. You just wanted to fight and keep fighting. If only that would save you from how it felt. This time, you try to keep calm; you are more prepared."
    "It last time was drowning, this time was falling. There was a gentle rush from the file picking up until it felt like you were plummeting down at 1,000,000 miles a minute."

    menu falling:
        "Close your eyes":
            "You keep your eyes squeezed shut. You can't found them what may be going on and it seems far easier to stay calm and focus like this. What you don't know can't hurt you."
            "As the air rushes past your ears, threatening deafen you, you manage to breathe in."
            pause 1.0
            "And out."
            pause .01
            "And in a split second, it stops. You catch up to yourself and feel lightheaded. You don't budge and don't open your eyes, just to take in the sounds."
            "A crunch of shoes on leaves, a friendly laughter, a gentle fond breeze against your ears. Surely, this is it?"
            "You crack open your eyes slowly…"
        "Open your eyes":
            "You can't help it open your eyes. You see everything and nothing all at once. Colors fly past you at impossible speeds blending to white and you struggle to breathe. Why did you have to open your eyes?"
            "Falling through endlessly of nothing as a strange feeling. Even looking down now, you can't see where you are falling to, if anywhere. Maybe there's no target; maybe this is the memory?"
            "The tragic life of a shooting star."
            "No, that wouldn't make sense. You erase yourself for an end you can't see as a scenery changes."
            "You passed the empty void of scattered colors and find yourself surrounded by the stars and planets. It is the most beautiful thing you've ever seen in your eyes search, hungry to take it all in."
            "There's only one thing you don't remember to take in amongst the endless sea of stars."
            "And that is {i}where{/i} you will fall."
            "You don't even consider the question thoroughly before you feel the impact of your eternal fall into the old world."
            "The fall wasn't literal. The lack of reaction from those around you proves as much."
    
    "A familiar voice speaks up. You assume you're with the same person as last time."

    menu samePerson:
        "What a shame":
            "What a shame. It would have been fun to experience more of these lives lived by those in different times and places."
            "It would be fun."
            "But no, you seem tied to this life now, and as you look around, you assume you're tied to this forest, too. You're back in Pandistone Park again. Only this time, the sun is setting."
        "Thank god":
            "Thank God, this would be easier if you got to be the same person repeatedly."
            "Although you barely knew this life, you grew fond of it, and being the same made it easier to fit into this life and not act strange like last time."
            "This memory seems to want you to have a very familiar time as you recognize the spot as Pandistone Park. You're back here again."

    b "Hellooo? Ya spacing out again??"
    "You jump a little and, in the movement, drop something. You realized that you held a stick over a flame, and the fire consumed the sweet treat that was on the end."
    b "Oh! Sorry, I didn't mean to make you jump. You were burning the marshmallow and it had to be saved!"
    "You find a memory in your mind… memory of past marshmallows. It's good to know you can only recall the essential stuff from this person's mind."

    menu marshmallow:
        "Burnt is good!":
            p "Hey, they're better burnt. It adds flavor!"
            b "You're just saying that because you {i}always{/i} burn them."
            p "I always burn them because I like them like that!"
            b "Then why did you chuck it in the fire?"
            "You pause. You can't explain why, of course."
        "Good thing I lost it":
            p "Oh, I burnt it? It's probably better I lost it then."
            b "Shoulda paid more attention, dummy!"
    
    b "Here, a birthday gift."
    "You finally look at her properly, and she seems…older."
    "Last time, she was tiny; you would guess around six or seven? She doesn't seem like a teenager yet but is bigger than before."

    if pHeight == "tall":
        "She's grown, but you're taller than her. You feel a slight ache in your bones, proving you likely have more growing."
    elif pHeight == "medium":
        "You're around the same height, and it's hard to judge as the two of you are sitting down."
    else:
        "You are shorter than her. You remember being around the same height in the past, so she must have had a growth spurt."
    
    "Her hand is outstretched, offering you her stick with one last marshmallow. It is lightly toasted, and your stomach grumbles."
    "You take the stick and chew the marshmallow; Bri seems pleased with herself. Your head turns at the sound of laughter, and you see your dad emerge from the tent."
    "He looks paler than before, his face is gaunt, and his hair is gone. You freeze a moment as the body's memories catch up to you."
    f "You good bud? Look like you saw a ghost?"
    "You can't respond. All you can do is wait as these memories consume you."
    "{i} He's sick. It's serious. He has an alright chance of recovery, but he is still. Now isn't the time, though, you hold your emotions and try to act normal.{/i}"

    menu ghostSight:
        "I saw one!":
            p "Yeah, I saw one! It was right behind you!"
            "Bri visibly jumps at the news, and you see her look around, her eyes wide and fists clenched. After she surveys the space, her eyes narrow at you."
            b "Did you {i}really?{/i}"
            "You stay silent as you fight the urge to laugh."
        "Ghosts aren't real":
            p "No, silly,ghosts aren't real!"
            b "How do {i}you{/i} know? They could be haunting this park at this very minute!"
            "This is the most spooked Bri has been. She seemed so confident in her memories, so seeing it was funny."
    
    f "C'mon, you two, it's time to hit the hay. We can save any potential ghosts for the morning, alright?"
    "Bri seems content with this, and you nod in agreement, the three of you making the way into the small tent. Do you remember the last file? You must have fit in this tent a lot better back then. Now, you were all squished up."
    "You lay in the middle of them, your teeth still sticky from the marshmallow. Before bundling herself in her sleeping bag, Bri drinks the last of her water, and your dad ruffles your hair."
    f "Night, kids! See you bright and early for sunrise."
    b "Oh yeah, I forgot! I can't wait to see it at the beach! Night!"
    "With that, you settle and fall into a comfortable yet dreamless sleep."

    pause 5.0

    "There's a movement to your right, and you hear the squeak of someone shuffling around on an air mattress. You open your eyes and see Bri trying desperately to move quietly and not disturb you two."
    "She looks at you, smiles, and holds a finger up to her lip. You agree to stay quiet, and you start getting ready. You both know how much your dad needs, all the rest he can get."
    "Once ready, you go to your dad to wake him; if you wait much longer, you'll miss the sunrise."
    f "hmmrph huh? Oh, morning."
    "His voice is rougher in the morning, and his eyes open the smallest amount to look at you. You feel a lump in your throat. You don't know why, but you feel like today isn't going as planned."
    f "Give your old man a minute, okay? I'll be out, and we can head down."
    "You and Bri head out and sit on the wooden logs turned benches."
    b "I'm so excited! I hope we get to do this every year forever and ever!"
    "She seems too awake for the early hours, but you feel her enthusiasm rub off on you. Before you can reply, you hear a curse and a fall from inside the tent."
    f "Don't worry, kids, I'm alright…"
    "You see him press his hand against the tent as he approaches the zip. Once it's open, he's dressed and ready. You look to Bri, and she sees something you don't, as she seems prepared for disappointment."
    "Your dad hobbles over to the nearest log and gradually sits himself down. He lets out a reluctant sigh and looks at the two of you."
    f "I'm sorry, but I don't think I can do it today… I should have taken your mum's offer up, Bri, and let her come along. I'm sorry…."
    f "I don't want to hold you two back from your fun, and you're big kids now, so you can go off if you wish."
    "Bri perks up a bit when he says you can still go."
    b "Thanks! I promise we'll be careful. Won't we?"
    "She looks at you expectantly, and she's made up her mind for both of you."

    menu hangoutPath:
        "Stay with dad":
            call dadPath
        "Go with Bri":
            call briPath
    
    u "Would you like to remove nature in the oceans or the forests?"
    "You can't see where to respond, so you find your voice and speak."

    menu remove:
        "The forests":
            "You speak the option out into the air, and the world starts to fall away like leaves falling off a tree."
            "Moments later, you awaken back at your desk."
            $ pCalm += 1
            $ forests = False
        "The oceans":
            "You speak the option into the air, and it feels like a wave washing over the world, erasing it and bringing you back to Shad Tuod."
            $ pChaos += 1
            $ oceans = False
        "Why?":
            p "Why? Aren't they both helpful?"
            "You wait for what feels like an eternity for a response, for a sign, for {i}anything{/i}"
            pause 2.0
            "But nothing comes."
            jump remove

            


label dadPath:
    p "I want to stay with you, Dad… sorry, Bri, we can go another time."
    "Bri stands in silence, emotionless, for a few seconds. You find it hard to gauge precisely how she's feeling."
    "As though nothing had happened, her usually bubbly personality reappears, and she smiles at you and your dad."
    b "Looks like I'll be seeing the sunset alone this year. I'll catch you two later. Save pancakes for me, will you?"
    "And with that, she speeds off into the woods, her excitement to catch the sunrise getting the better of her. You hope she understands, but does your dad?"
    f "You can hurry after her and still catch up, bud. Don't hang around here, just for my sake. I'll be fine."
    "He smiles to reassure you that it's okay to leave him be, but you see him still hobbling around. He shouldn't be alone."

    menu reasoning:
        "Stay because you want to spend time with him":
            p "It's true. I could have rushed off with Bri, but it is a tradition. But it wouldn't be the same without you, Dad."
            "You sound much more natural this time compared to the first case file. The words come more naturally to you, as though you know the right things to say and how you fit into these memories."
            p "Besides, Bri keeps our tradition of viewing the sunrise at the beach, and I get to experience a new memory of seeing the sunrise from here with you."
            "It's true; these memories are a treat to you now, and your fears about them are squashed. Sure, the pain from the last time was a shock, but you also get to live."
            "You get to escape the stuffy offices and experience the world for yourself through another's memories."
            f "I appreciate that, bud. I'm glad you're not ashamed to hang around with your old man. Though maybe that'll come soon, what about you becoming a teenager?"
            "He chuckles to himself and pats you on the back. You feel his happiness thanks to your desire to be with him out of love, not just pity."
            f "I'm glad to have you in my life. And once these chemo treatments are finally kicking in, I'll have the energy again to do all the things you've had to miss out on."
            "So, the worries were correct: your dad has a form of cancer. This must have occurred between the scenarios, which explains the dad's slenderer frame."
            p "I can't wait for you to get better, too. I'm looking forward to doing all those things together again."
            "It's true; you yearn to experience more of these memories. More of these first-time experiences are in the real world. Without memories of your own life, these shared memories are so valuable."
            f "But for now, let's appreciate what he ran here. We may not be at Pandistone Point, but there's beauty to be found all around us."
        "Stay because you are worried about him":
            p "I wasn't going to leave you here all alone when you were clearly in such pain. What if you needed help, and I wasn't here to get it?"
            "He looks away from you, glancing over the ground before returning to your face."
            f "You don't need to worry over me like I'm on death's door, bud. Though, I'll admit the cancer has hit me harder than I expected."
            "So, your fears were valid. The man's gaunt face and skinnier frame were because of the cancer."
            f "I know it's scary: believe me. I've never thought about my own mortality until the last year, but the chemo is helping. The doctors are doing everything they can to fight this."
            f "When I get better, we can do everything I must miss out on again. I just got to get through these challenging years of treatment first."
            "The smile reforms on the man's face, and although he's paler and his features sullener, the same warmth you felt in the first memory you entered shines through."
            f "But that's enough about that depressing business. Let's appreciate all the beautiful things around us, hey? Focus on this moment rather than dwell on what could be."
        "Chase after Bree":
            "You decide to chase after Bri, feeling assured that your dad will be okay."
            p "You're sure you'll be okay?"
            f "I'll be as fine as a fiddle; now hurry along, pal. I know this sunrise tradition is important to you and Bri. You don't want to miss it now, do you?"
            "It's true; you don't want to miss it, and spending more time with Bri is enticing. You feel in your gut this is the last you'll see of your dad this time."
            "The feeling builds, but you must stay positive and hope to see him again in a future case file."
            p "I love you, Dad!"
            "You call back as you hurry off; seeing your dad smile and wave as you head off fills your heart with joy."
            f "I love you too!"
            "He shouts back. You may not exactly be this man's kid, but you can't help but feel the warmth and love from this person's memories."
            "You eventually catch up to Bri, which is a miracle considering how fast she was powerwalking to get to the beach."
            b "Your old man going to be alright? You didn't have to rush after me, did you know? This was just important; traditions are important to me…"
            "You hear the note of concern from her tone, and it pleases you to know that although she went off alone, she didn't hold it against you."
            p "He's going to be okay. My dad is stronger than we give him credit for. You've got your camera, right? We'll snap him a photo so he doesn't have to miss out on the view this year."
            b "Nice thinking, we'll do just that. Now, enough jabbering, or there won't be a sunrise to photograph."
            "Bri takes your hand, and you both hurriedly traverse the woods to compensate for lost time."
            "You pass through the green leaves; the walk isn't too far, and soon, you find yourself on a slight stretch of beach. It's been kept clean and tidy, a well-preserved pocket of nature."
            "You listen to the gentle lap of the waves, the salty air on your tongue, and you savor it for the moment, enjoying the calm."
            jump aboutWorld
        
    "You put the kettle over the fire to boil some water to make tea for you and Dad. You ensure he is comfortable in his camping chair and sits on a nearby log."
    "Your dad looks at you with a smile on his face."
    f "I want to ask you something. There's no wrong answer, I promise."
    f "Take a look around you, and take everything in. What is it that you notice the most?"
    "You take a moment to consider this request. You are feeling quite at peace in this serene campsite spot."
    "The birds tweet and caw from the trees, and you look up to them and see them nesting nearby amongst the gently swaying branches and rustling leaves."
    "You can hear the trickle of water from a nearby stream that leads to the ocean. You picture the flowing stream and the wildlife that must drink from it."
    "You can also feel the soft moss on the log you are sitting on. There are mushrooms nearby, too, stretching up from the moist undergrowth; you wonder if they're edible."

    menu senses:
        "Sounds":
            call sounds
        "Sights":
            call sights
        "Feel":
            call feel
    
    "You notice the kettle over the fire is now coming to a boil. Move it off the flames and fill two camping cups with hot water. You add a teabag to each cup and give them a little stir."
    "You reach inside the cold bag and retrieve the milk carton. You fill up your dads cup with a small amount of milk; as you know, he likes a strong cup of tea."
    "Wait…"
    "How did you know that was how he takes his tea?"
    "You can only assume that the more memories you experience, the more external information about the surrounding events is available."
    "But how will you take your tea?..."
    
    menu tea:
        "A little milk":
            "As you finish pouring, your dad gives you a thumbs up, signaling his fatherly approval."
            f "I'm glad you picked up making a good cup of tea from your old man."
            f "I don't get people who drink tea that's a weak strength."
        "A lot of milk":
            "As you finish pouring, your dad pulls an exaggerated flabbergasted face."
            f "Blimey, you think you've got enough milk in there?"
            f "You make your tea as weak as a gnats piss. You're entirely wrong, but I still love you though."
            "You laugh, finding it funny that your choice of tea strength upset your dad."
        "A fair amount of milk and some sugar":
            "Your dad shakes his head as you shake some sugar into your tea."
            f "I can't take sugar in my tea. I find it makes it too sweet to me. Funnily enough, though, your mum took it similarly to that."
            "You smile. Even though you never knew her, some of her preferences must have been passed down to you."
            f "The strength is tolerable, though. It would be unforgivable if it were sugar and a weak cup of tea."
            "He laughs heartily, and you smile back, glad to enjoy a brew with your dad."

    "Your mind briefly returns to Bri, who, at this point, will have reached the beach. You hope she doesn't hold your decision to stay against you. It was a difficult decision with no correct answer."
    "Hopefully, suppose you continue to traverse this person's memories. In that case, you will come across Bri again and have the opportunity to get to know her more."
    "Your dad snaps you out of your thoughts."
    f "Hey buddy, look… it's finally time for the sunrise!"
    "You look upwards and are struck by the sun's rays piercing the trees. Striking silhouettes of the tree branches and their leaves are cast upon the ground of the campsite."
    "The birds begin a symphony of chirping and tweeting as the sun's rays cast upon their nests. Their cheerful cacophony welcomes in a brand-new day."
    f "Thanks again for staying with me. It… It means a lot to me. I hope we'll get many more summers together here. Next time, I hope I'll be able to make it to Pandistone Point."
    "You almost don't mind missing the sunrise on the beach. This moment with your dad amongst all this nature was priceless."
    "A strong gust of wind blows through the clearing, and several birds take flight above you. As they shifted the branch's weight, several loose leaves detached and began to twirl and glide down."
    "As they fall, time seems to slow down. You appreciate them dancing and whirling down towards the ground."
    "Then, just above you, the leaves entirely stop, frozen in motion. You turn to your dad, who is also wholly motionless. It seems your time in this memory is sadly at an end."
    "The birds, the breeze, the trees, and the stream all fall silent and cease to live anymore. The illusion of reality is shattered, and it's time to decide again."
    "It's not fair; you don't want to go back. At first, you thought these situations were trickery or hallucinations. But now you know them as the realest things you have ever felt."
    "If only you could stay and continue this life and simply forget that this is not your reality. But you can't; this is a whisper of a life long gone, a world soon to be reduced to nothing."
    "You look back up to the suspended leaves and notice the one closest to you appears to have writing scribbled onto it."

label briPath:
    p "Yeah, let's go! Thanks, Dad!"
    "Your dad offers you a tired smile. Bri turns back to him and sees something you seem to miss in his expression."
    "Whatever she sees, she shakes it off, determined to see the sunrise."
    b "Thanks! We'll stay safe!"
    "And with that, she takes your hand, taking you a new direction through the woods."
    "You pass through the green leaves; the walk isn't too far, and soon, you find yourself on a slight stretch of beach. It's been kept clean and tidy, a well-preserved pocket of nature."
    "You listen to the gentle lap of the waves, the salty air on your tongue, and you savor it for the moment, enjoying the calm."

    menu aboutWorld:
        "Stay forever":
            "A part of you wishes to stay here forever, the gentle summer breeze on your face."
            "Even if those you've spoken to can see it, you think there's beauty to this world, and you hope some of that beauty can move to the new."
            "Standing here with a friend looking out at the waves, you wonder if a new world is really necessary; surely this one can be fixed?"
        "Back to Shad Tuod":
            "You wouldn't mind being back in Shad Tuod. It feels like a waste of time to go through these memories."
            "Isn't your purpose to create something new here? Aren't they striving for a change?"
            "This world may be pretty, but they've all said it: it is broken and rotten and will be gone soon, so why grow attached?"
        
    b "Hey?? You spaced out again; you'll end up on the moon at this rate."
    "Your attention snaps back to this life you're in, and you give Bri a smile. Regardless, it seems worth keeping things as normal as possible in this life. You need to start paying attention."
    "You notice Bri is holding her hands behind her back."

    menu investigate:
        "Ask her what she found":
            p "What are you hiding behind your back?"
            "Her cheeks redden at the accusation, and she looks away, keeping her hands firmly behind her back."
            b "Nothing!! I found nothing at all!"
            "You try to peer around and see her hands, but she always evades your gaze. Eventually, you give up, hoping she will show her hand later."
            "You see her slyly put her hand into her pocket and drop it to her side, empty now of anything."
        "Don't ask":
            "She puts her hand in her pocket as casually as she can muster and drops her hands to her side."
    
    b "I saw a rock pool over there. We should go see if there's anything cool!"
    "You nod, and she leads you both towards the rocks that separate the sides of the beach from the rest of the world."
    "She steps carefully, and you follow her movements, not wanting to slip. Eventually she stops and crouches, looking into the clear shallow pool curiously. You kneel beside her, and you see..."

    menu rockPool:
        "Something green in the water":
            "You focus on it, assuming it to be seaweed. Bri takes a closer look, too, her face right up close to the pool."
            b "It's an an-"
            b "..."
            b "An Anenen-"
            "She frowns, annoyed at her own stumble over the word."
            b "The anemo- what is it?!!"
            "Clearly frustrated, you decide to put her out of her misery and say anemone."
            b "Yeah! It's that."
            jump rockPool
        "Something pink, moving slowly":
            "You stare at the creature, seeing its pointed shape. You finally announce:"
            p "A starfish!"
            "Bri gasps and watches it move with you. It is lovely to be with someone new to this world, someone who wants to explore it all as much as you do."
            jump rockPool
        "Something purple and still":
            "You gently reach your hand into the water and pick it up, a weathered piece of sea glass shining bright in the newly emerging sun."
            "You move it around in your palm. The edges have been weathered away by the tides. You hold it up but can't see through its frosted exterior."

            menu seaGlass:
                "Offer it to Bri":
                    "You hold the glass out on your palm, and she gasps, taking it quick before you can change your mind."
                    b "It's my favorite color!! Thank you!!"
                    "She seems to remember something and searches her own pockets quickly."
                    "With beaming pride, she presents another piece of sea glass, less shiny as it's dried up in her pocket but still pretty. The olive-green glass is dropped into your palm, a perfect trade."
                    $ seaGlassGreen = True
                "Pocket it":
                    "You like the colour; it could surely make your desk space nicer."
                    $ seaGlassPurple = True
            jump rockPool
        "Something sandy moving with some speed":
            "Bri gasps as you point toward the well-disguised creature."
            b "A crab!!"
            "The two watch as it scurries about, eventually ducking beneath a rock to never be seen again."
            jump rockPool
        "Look away as the sun is coming up":
            pass
    
    "You give Bri a nudge. She looks confused for a second, then figures it out. The two of you look towards the sun as it coats the world in a golden glow."
    "You both shuffle to sit down, silence aside from the sound of the sea lapping at the sand and the occasional sound of breathing."
    "You could stay like this forever; part of you thinks you might. After all, nothing has gone wrong yet? What could they possibly ask you to alter in this file?"
    "The silence is broken when Bri shuffles to see you better."
    b "I'm sorry your dad couldn't be here… I feel kinda bad for leaving him behind, but also… this has been fun."

    menu dadBehind:
        "Don't feel bad":
            "You don't feel that bad. You're having fun."
            "You were old enough to do these things by yourself, plus you had been here before clearly, and Bri knew the way by heart."
            "If your dad had wanted you to stay, he could have said so. A bit of guilt was hanging over you, but you wouldn't trade it for not being here."
            "You were having fun; you never wanted this to end."
            p "It's fine, he didn't mind. Plus I'm having fun with you."
            "Bri smiles and bashes her shoulder against yours playfully."
            b "Awww, thanks! I'm having fun, too!"
        "Feel bad":
            "It had been in the back of your mind, eating at you. You'd been feeling guilty. You kind of wished you'd stayed."
            p "We shouldn't have left him behind… he's probably all sad and alone."
            "You mumble this to yourself, but Bri hears you, a worried look on her face as she pulls you into a side hug."
            b "Hey… It's gonna be alright. We'll get back and make him something nice for breakfast, okay?"
            "You nod, but something nags at you. Things can't be all fine."

    b "Y'know… I was thinking recently and don't know if being a chef is for me."
    "You're taken aback by that. When she says it, all you can remember is a childhood full of insistence that she would cook for rich and famous people or open a pub or something, but it always involved cooking."
    b "Shocking, I know, right? I realized I liked it when we were in science before we broke up for summer. I might try to do something to help people."
    b "Don't worry, though. I'll still cook for you sometimes, though! When we're older, we can live in a house together and take turns!"

    menu briLife:
        "Why did you change your mind?":
            "Bri considers the answer momentarily, struggling to find the words she's happy to share with you."
            b "Because… I want to help people; I want to be able to make new medicines and cures and make people better."
        "Are you sure?":
            b "Yes."
            "Her face is the most serious you've ever seen; she's already been hard to deter for other much more minor things, so you gather that there's nothing you can say that would make her budge on this."
        "Why not both?":
            "Bri looks sheepish for the first time and runs a finger through her dark, curly hair."
            "Because uh- I like science, but I'm not that good yet… miss said if I wanted to do it properly, I'd have to get like… the best grades, and right now I'm just a liitttllee bit off that so-"
            "You cast your mind back and can recall sharing grades in the past. You remember she is slightly underexaggerating the gap between the grades."
            "So yeah, I'll still cook for my family and you and your dad sometime, but nothing too fancy any more!"

    "She stands up before you can quiz her anymore, and you drop it, getting up alongside her and following her back to the sand."
    "You look out to the waves, the golden shimmer of the sun reflected on them. You'd been here longer than expected, and it was probably time to return soon."
    "You keep your eyes on the waves as they appear to slow, eventually reaching an unnatural stop. You turn immediately to your companion, who is also frozen in time. "
    "You look around frantically. Surely, this is the end, but where's the option? You’re just {i}stuck.{/i}"
    "You glance over the sand and see something you didn't see before. A pristine sandcastle covered in shells."
    "You approach it gingerly, hoping this is it. Being here is nice, but being stuck in the moment is uncanny. You'd take the stale breeze of Shad Tuod over this."
    "By the sandcastle, you see it, written in the sand in an elegant cursive handwriting:"

label sounds:
    p "I'd say I notice the sound the most. When you tune out your thoughts and focus on the sounds, there are some beautiful noises around you."
    f "There is, isn't there. What's your favorite sound?"

    menu noises:
        "The stream":
            "You mention the calming sound of the trickling water nearby as it flows down the incline back to the ocean."
            f "That's one of my favorites too. I'm glad you picked up on it. It's pretty easy to tune out."
            f "When I'm feeling anxious, I often listen to rain with the window open when I can't sleep at night. Or if it's not raining, I can play water sounds on a CD."
            f "I've been doing that more and more lately. It helps to wash away the worries and fears from my mind, quite literally."
            "He laughs, and you realize this is supposed to be a classic dad joke. You can't help but smile as you roll your eyes."
            f "You should try it sometime, bud. I'll lend you one of the CDs. I know this past year must have also been a lot for you. I'm always here to talk if you need to; that's what Dads do best."
            "You think it's commendable that your dad is concerned just as much for your well-being as his, even while he's the one in a much stricter situation right now."
            $ bookedGain = False
        "The leaves":
            "You comment on the gentle breeze, which makes the trees' branches sway slightly, rustling the leaves."
            f "Ah, I suppose I don't it so much myself. But it's an exciting choice, nonetheless."
            f "I love the feel of the wind as it weaves through my fair or brushes against my cheek. It's one of those things that makes you feel alive, know what I mean?"
            "You know more than you could say. The breeze here is better night and day than the stuffy office rooms that make up the hall of the gods. You wish you could stay longer."
            p "I love the feel of the breeze, too, Dad. You can also smell the sea in the wind, and it's very refreshing."
            "The thought of the sea brings your mind back to Bri. You are missing out on spending time with her on the beach. Your choices have taken those potential memories away from you now."
            "However, part of you is glad to be here, with your dad. Taking in all these sensations is doing you good. It lets you be truly alive, even if it is only a small window into someone else's existence."
            $ bookedGain = False
        "The birds":
            f "I was hoping you'd say that! That was your mother's favorite thing about coming to Pandistone Park."
            call momBirds

label sights:
    f "Well, I can't deny there's undoubtedly a lot to see here. It never gets boring. What's your favorite thing to see here, bud?"

    menu sightsSub:
        "Fungi":
            "You point out the intriguing fungi and shrooms growing in the more moist and shady areas of the campsite area."
            f "They certainly are pretty bizarre, aren't they?"
            p "Are they edible?"
            f "Well, it's a little-known fact, but all mushrooms are edible. Some are just only edible once…"
            "He snorts at his terrible joke, and you can't help but laugh."
            f "Truthfully, I don't know if those are or not, so best just to leave them be. But it's nice to appreciate them even if you can't use them."
            f "It's kind of poetic that even devoid of light and warmth life still grows. Even in the face of adversity, nature can overcome it. It is an excellent metaphor for life itself; tough times help us grow."
            "It's true. Sometimes, we grow through learning and preparing. But at the same time, life can throw some serious curveballs your way, and overcoming these can help you change."
            $ bookedGain = False
        "Trees and Plants":
            "You gesture towards the trees and plants, explaining that the way some of them tower high above makes you feel relatively insignificant."
            f "They certainly are tall, aren't they? But these trees have taken decades to reach such impressive heights."
            p "Is there a way to tell how old a tree is?"
            f "Typically, you can't tell without cutting down a tree. You see, the rings on the stump of a cut tree tend to signify the age."
            f "But these trees, I reckon some of them must be over one hundred years now, make us seem relatively young in comparison."
            "You laugh, but now that you think about it, you realize your dad is quite old. When you first saw the man, you reckoned him to be about 45, but he's likely now around 50, given the age growth of Bri."
            "You are saddened to think that the time with your dad is so limited, both from aging and potentially cancer. You wish you had more time like this to live while you can."
            $ bookedGain = False
        "The birds":
            "You mention how the birds seemed the most striking among the other sights."
            f "I was hoping you'd mention the birds bud. Truthfully, the birds were your mother's favorite thing about coming here."
            call momBirds

label feel:
    "You try your best to explain how the forest felt most striking to you."
    f "Which feeling strikes you the most?"

    menu touch:
        "Wind":
            "You mention the pleasant sensation of the breeze flowing against your arms and face."
            f "I love the feel of the wind as it weaves through my fair or brushes against my cheek. It's one of those things that makes you feel alive, know what I mean?"
            "You know more than you could say. The breeze here is better night and day than the stuffy office rooms that make up the hall of the gods. You wish you could stay longer."
            p "I love the feel of the breeze, too, Dad. You can smell the sea in the wind, too."
            "The thought of the sea brings your mind back to Bri. You are missing out on spending time with her on the beach. Your choices have taken those potential memories away from you now."
            "However, part of you is glad to be here, with your dad. Taking in all these sensations is good; it lets you be truly alive, even if it is only a small window into someone else's existence."
            $ bookedGain = False
        "The moss and logs":
            "You mention how the feel of the surfaces around you makes you feel grounded and how satisfying it is to run your fingers along the textured grooves."
            "Everything here is so natural. When you go back to the stuffy industrial office of the gods, everything is so artificial and perfect. Smooth desks, doors, floors, and walls."
            "It's devoid of life and personality. Being able to escape that and experience the wonders of nature in this earth forest is a great gift, though you know your time here is quite limited."
            f "Interesting choice bud. It's a nice feeling to feel something real and be somewhere natural."
            f "Since I was cooped up in a cramped office cubicle for most of my life, I always appreciated escaping into the woods on my time off."
            "Much like your dad would have to return to the office after their holidays, you too will have to return to work soon with the gods. You'll likely also have another choice to make quickly…"
            "What could they possibly ask you to decide next? Last time, it was pain. This time? Sickness? Birds?"
            "There was no way to know until the time came, so you push the thoughts aside and continue to enjoy the moment while it lasts."
            $ bookedGain = False
        "A bird's feather":
            "You raise your hand to your dad and show him the feather you've been twiddling with your fingers since you've been talking."
            f "Now, that's an exciting choice. I wish I could tell you what bird that is from, but honestly, I never knew as much about birds as your mother did; she was an expert."
            call momBirds

label momBirds:
    "It dawned on you that in all this time, you hadn't considered where a mother to this person you inhabited was in these memories."
    "You take it that she was out of the picture in some way; perhaps she passed away, or they had separated. You didn't wish to pry, as it would raise concerns about why you didn't know."
    f "We used to set out a blanket not far from where we are now and just look up at the sky and listen to the birdsong. She could identify a bird just by its song, can you believe that?"
    f "She had this book of birds, and we would try to tick off a few more entries every visit. She'd log all the ones she spotted on each trip."
    "You shake your head in awe of this woman you never knew; you wish you could have met her. She seems like a mystery you will never solve."
    f "Here, why don't you take a look? I've bought it with me every year, but I can't bring myself to write in her place. That was always her job, and she took it seriously."
    "He hands you a small, weathered book of birds. As you thumb through it to the back, you find the back pages filled with neat cursive writing."
    "These pages are tallying the various birds spotted on trips to Pandistone Park dating back to 1971."
    f "The sunrise on the beach was one tradition I wanted to continue. But honestly, filling that book in while we were camping, well, that one was even more special to me."
    f "Without her, it just wasn't the same, but I always take it with me, you know. Having it in my pocket and listening to the birdsong… It just makes me feel like she's still here."
    "A tear begins forming in the corner of your dad's eye, but he quickly wipes it away and composes himself."
    $ bookedGain = True