
$f = Character("Dad")
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

    if player.height == "tall":
        "She's grown, but you're taller than her. You feel a slight ache in your bones, proving you likely have more growing."
    elif player.height == "medium":
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