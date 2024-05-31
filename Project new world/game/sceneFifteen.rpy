label endBeginning:
    "You start to awaken from the last file, your heart racing from the experience. You can't believe it. This whole time, these weren't the memories of another; they were your own."
    "That was your dad, and now he's gone. And that entire old world, your world, is soon to be removed from existence, a new one in its place."
    "All those billions of people will cease to be, and billions of new lives will populate the next planet. One that you have been helping to replace this whole time."
    "Your dad, Bri, Pandistone Park all gone. You are stuck as a god forever now. This is your existence for the rest of time, a curse in the guise of a blessing."
    "The world continues to remain blotched and inconsistent. All around you is an inky black void threatening to suck you in and drown you."
    "Your desk, the cubicle, and the whole office are nowhere to be seen."
    "You call out, your voice was hoarse, but you just need someone {i}anyone{/i} to talk to."
    return

label neutralEnd:
    call endBeginning
    menu calloutNeutral:
        "Shout for Charis":
            j "I'll have to do it instead. He doesn't want to see you."
        "Shout for Alan":
            j "I'll have to do it instead. He doesn't want to see you."
        "Shout for Juniper":
            j "Oh? Well, I'm flattered you would call out to me. Not that I can see why you would."
    
    "You want to jump into a flurry of questions. Why had those all been moments of your life? What had happened to the old world? Was it truly gone?"
    "Juniper puts a hand up, and you restrain from asking for it now."
    j "I am here to do your final report. The other two were… less impressed, so I was asked to oversee. We can get through this quickly, so don't worry."
    "Juniper snaps their fingers, and a globe appears. The world, in some ways, looks so familiar; it looks like a ball of water and land. Juniper scans around, looking for specific things to point out before launching into the review."

    if pain:
        j "You chose to keep pain, a fair choice. I'm not sure how much they would agree, though."
        "Juniper extends a finger to point at the globe. You see a person all alone, they can't walk, something happened to their leg, they're screaming in agony for someone to help."
        "You wince at the sound of their wails. Knowing you could have prevented this, you feel a chill down your spine. It's only when a voice breaks through, and you hear someone talk to the injured person."
        "The two speak, and they bond, the well one helping the injured by dressing their wound. In a way, the pain had given them community, a trade to look out for one another now."
        j "Hm, I hope they do better in the future."
    else:
        j "You decided to remove pain, an admirable decision except for the one thing you seemed to miss in that deal."
        "You turn your attention to the globe in front of you as it spins lazily. You look at all the people. They seem so happy and healthy, with no one struggling. How could this be a bad thing?"
        "But then you see it. A limp. Something so small, yet you know what that means. A lack of pain isn't a lack of injury. Just a lost way of noticing such a thing. Juniper stares at you."
        j "You see it now, yes? Pain may be wrong, but a little goes a long way in stopping people from damaging themselves. It makes them stop and think about the damage dealt to their body."
    
    if forests:
        "Juniper seems quick to move on from that and takes a step closer. Their eyes light up a little as they point to a vast patch of forest."
        j "Huh, keeping forests allowed for some new flora and surely some fauna, too."
        "You look closer and see it, the forests teeming with new life unlike any you've ever seen, flowers in vibrant shades and new trees towering. You know, a class of children is being shown around this forest by people intent on caring for it."
        "You keep looking but notice Juniper's eyes have drifted towards the sea. All that's left is a vast expanse of empty water, used as a dumping ground for rubbish. Islands of waste drift lazily around with the tide."
        j "What a waste of space, a planet still mostly water but nothing to utilise it, just a wasteland now."
    elif oceans:
        "Juniper seems quick to move on from that and takes a step closer. Their eyes light up a little as they point to the vast oceans."
        "You see strange new creatures and richer, denser flora sitting under the gentle waves. People seem to flock to the oceans even more to see the sights. People seem to care for more than just the waves and the sand."
        "You can hear someone giving a talk about new discoveries and how, despite lifetimes of looking, there's still so much more to discover down there. You look to Juniper but see their gaze has moved, their face pale."
        "You follow and see why, on the land, there are almost no forests. It has been removed for farming or housing. No one cared enough and now it's nearly gone, the only nature left being the occasional tree."
        j "A shame the old world already had such an expansive ocean. A greater one seems almost unnecessary."
    if fear:
        "Juniper's eyes move to a city, and you follow. You see people acting normally, perfectly in line."
        "Maybe a bit too inline, though, you see people contemplating new things. Someone wants a haircut but is too afraid. Someone wishes to travel but is too scared."
        j "Hm, for some reason, fear not only is present but has been heightened…"
        "That wasn't part of the deal! But the more you look, the more you know it to be true. Everyone seems so afraid of each other and of themselves, holding themselves back from something new."
    else:
        "Juniper is looking at a city, and your eyes follow. You see people interacting with more ease, willing to take a risk on a new friendship, new hobby, or a new life entirely."
        "You also see people a bit too out of control, people stealing with no fear of the repercussions, and people pushing others further and further as there is no reason not to. Juniper narrows their eyes."
        j "When given the freedom from fear, some seem so happy to use it just to cause issues. And what, for fun? For a quick laugh?"
    
    if lies:
        "Your attention is pulled as you hear a voice. Stepping closer, you can make out better. Someone reassuring their friend everything is gonna be okay. You aren't certain it is from the shake in their tone."
        "This seems a small lie, though. Maybe it will protect those who made it, and isn't that important? To have a way through situations like that?"
        "A louder, more demanding voice follows. His tone drips with lies and deceit. A man with a megaphone announces his policies, and the people cheer. Your stomach drops; those policies are too good to be true, and it is a cheap trick to win."
        j "People seem always willing to use whatever cheap trick to get their way, don't they? Though… who am I to judge."
    else:
        "Your attention is pulled as you hear a voice. Two people are whispering. It's something important, something someone else {i}can't{/i} know, or things will go very, very bad."
        "You look beyond these two and realise people are closer-knit. Being unable to lie means everyone is trustworthy. People believe each other because they can't conceive of doing anything else."
        j "This seems… peaceful-"
        "They are interrupted by a desperate voice. You see the two from moments before. One has spilled the beans. You look away before you know the consequences."
    if death:
        "You feel tired of this at this point, so desperately tired you want it all to end."
    else:
        "You feel tired of this at this point, so desperately tired you want it all to end."
        j "I must admit it was an excellent move to keep death. Imagine how packed this place would be without it."
        "You wince, the pain from the choice still fresh. It feels like a lifetime ago you were watching your dad die, yet also only a moment ago. But you suppose they have a point; death keeps a balance."
        "You hear a quiet sob. You know how this works now and refuse to look, covering your ears until it passes. Once all you hear is silence, you look at Juniper, and they meet your gaze."
        "But it seems your final wish, like all others, came true. There really is no end. There is so many people its {i}suffocating.{/i}"
        j "Damn… I'm surprised they can all fit still. That must be becoming a problem already, though."
        "People seem happy to have all those they love with no worry of losing them, but as mentioned, there are far too many of them. Many of you are just sitting around, too old at this point to work, leaving the younger ones impossibly busy."
        "You look away and look at Juniper. They meet your gaze."

    j "Well. I hope you are happy with your world; someone should be at least. It cost a lot to make this, and what was taken for it can never come back."
    "Their tone is sombre as they regard you. They don't even seem disappointed, just apathetic. They don't care about you, and you helped destroy all they cared for."
    j "There is a door to your left. I will leave you here to look over until you wish to return to work. I have been told to inform you of your demotion. You will be assigned a new case after this. So, take it all in now."
    "With that, Juniper leaves, and you stand staring at your new world."
    "As you gaze over the people in it and contemplate never leaving this room, you wonder honestly. Do you like your new world?"

label alanEnd:
    menu calloutAlan:
        "Shout for Charis":
            "Suddenly, someone puts their hands around your eyes"
            u "Guess who!"
            u "Took too long, it's Alan!"
        "Shout for Alan":
            a "Boo! It's me in the flesh."
        "Shout for Juniper":
            "Suddenly, someone puts their hands around your eyes"
            u "Guess who!"
            u "Took too long, it's Alan!"
    
    a "So, I'm supposed to go through this report with you. For some reason, it was assigned to me. I think the others were too lazy, to be honest. But I think you did pretty decent choices, not as good as if it was me, of course, haha, but from the top!"

    if pain:
        a "First on the list is pain, dunno why you decided to keep this one, to be honest... it literally only hurts people like it's in the name."
        "Alan points at the globe, to a person all alone. They can't walk, they're missing a leg, they're screaming in agony for someone to put them out of their misery. How could this be a good thing?"
        "He seems angry yet somewhat excited to be proven right."
        a "See? Look at that poor person. Like, what did you think was gonna happen??"
        "You wince at the sound of their wails. Knowing you could have prevented this, you feel a chill down your spine. It's only when a voice breaks through, and you hear someone talk to the injured person."
        "The two speak, and they bond, the well one helping the injured by dressing their wound. In a way, the pain had given them community, a trade to look out for one another now."
        a "See, not only are they in pain, but they also have to get someone else involved to help them. Someone else has to go through the effort of taking care of someone who will do nothing else for them due to pain."
    else:
        a "Pain is first on the list. It only hurts people, to be honest, thank god you removed it"
        "You turn your attention to the globe in front of you as it spins lazily. You look at all the people. They seem so happy and healthy, with no one struggling."
        "But then you see multiple people being rushed to the hospital. They all caught a deadly disease from each other, but no one knew until it was too late. The only symptoms were pain and eventual death. You turn to see Alan turned red with guilt."
        a "H-HEY, n-not every choice can be perfect! The others benefit humanity way more than what I bet Charis or Juniper would've chosen!"
        "Alan quickly tries to find something else to talk about"
    
    if forests:
        "Suddenly, Alan notices a patch of forest."
        a "Ooh, look over there! A forest! I mean.. looks like a forest I guess. Definitely prefer oceans… think about what the coral would've looked like…"
        a "Kinda a dumb question in general, like why do we need to choose only one, who's in charge of this shit?"
        "You look closer and see it, the forests teeming with new life unlike any you've ever seen, flowers in vibrant shades and new trees towering. You see a class of children being shown around this forest by people intent on caring for it."
        "Alan points out the sea, seemingly mad about what could've been"
        a "Look how boring the sea is now! What did they do to it! I blame Charis. And you can't even drink from it cus of the salt or something. It's literally useless!"
        "The sea has become a giant mass of empty water and has turned into a dumping ground for humanity. Islands of waste drift lazily around with the tide."
    elif oceans:
        "Suddenly, Alan notices the beautiful coral completely covering the ocean floor."
        a "Oooh, look at that coral!"
        "His eyes light up as if this is what he's always wanted."
        "You see strange new creatures and richer, denser flora sitting under the gentle waves. People seem to flock to the oceans even more to see the sights. People seem to care for more than just the waves and the sand."
        "You can hear someone giving a talk of new discoveries, how, despite lifetimes of looking there's still so much more to discover down there."
        a "This choice definitely paid off. I loved this question. It was so fun to do and kinda irrelevant, which made it funny. And look at what happened from it!"
        "You look over to see a plain and empty patch of land with almost no forests. All the forests were removed for housing or farming. No one cared enough, and now it's almost gone, with only nature left, the occasional tree."
        a "Look how boring the land is. I mean, I'll miss it, sure, but.. look at the ocean! "

    if fear:
        a "Ah, fear… yeah, this one pisses me off... think about all the bad things this does to people, and you think we should keep it?"
        "Alan looks over to see someone standing in the corner at a party, clearly too fearful of going over and talking to their crush or to make new friends."
        a "See, look at them. People are so lonely now because they fear speaking to strangers."
        "Alan turns to see someone's house being broken into, and they are carrying a gun. The residents run to lock themselves in the bathroom and immediately call the police. They fear for their life at this moment."
        a "Well… that's quite a rare event. The pros outweigh the cons on this one. When was the last time your house got broken into?"
    else:
        a "Thank god fear's gone. This has never done anything good for anyone…"
        "Alan looks over to see a big group of friends hanging out. One of them goes up to their crush, very confidently confesses, and gets a kiss."
        a "Aww, good for them, see how much happier people are now and how much more confident they are now they have no fears?"
        "Alan turns to see someone's house being broken into, and they are carrying a gun. The residents don't care, as they don't feel fear."
        a "I mean… it's not like fear would've helped them. I mean, the intruder had a gun. What would fear have done for them?"
    
    if lies:
        a "You're telling me you {i}like{/i} when someone lies to your face? Man, you're weird…"
        "Alan points out a woman sobbing in her arms. She just got cheated on by her husband."
        a "He told a terrible lie.. and now look at his wife. She's the victim of his terrible lie."
        "You point out someone else on the side of the road. They're smiling and happy, as they just got complimented by a stranger, despite the stranger telling the truth about the compliment."
        a "They may be happy, but they're happy because they think it's the truth, but it's not. "
    else:
        "Alan catches the eye of a couple having an argument. Someone just confessed to his wife that he cheated. They quickly get over it because he confesses and explains the situation in detail."
        a "See, look at that happy couple. Things like that only come from telling the truth constantly."
        "You notice two strangers having a fight on the side of the road. One asked the other if their new haircut looked good, and they said it was ugly and they'd look better bald, which was the truth."
        a "Well… don't ask questions you can't handle the answer to, I guess. Kinda walked into that one… I mean, look at that ugly trim."
    
    if death:
        a "Pretty sure Charis thinks I only wanna keep this because I like gore… like he needs to think about the economy or something, man…"
        "You look to the left and see a family crying. Their granddad just got diagnosed with cancer. They know he doesn't have long left."
        a "That's sad.. but would you rather this, or he never dies?"
        "Alan aggressively points over to a young child trapped in a lion enclosure at the zoo. The zookeepers notice and promptly shoot the lion, killing it and saving the kid."
        a "If that lion couldn't die… that kid could be limbless for the rest of their life, and that life would be endless."
    else:
        a "Death is pretty important. I think you messed up here, to be blunt."
        "You look to the left and see a happy old man. He just got diagnosed with cancer, yet he knows he's not going to die, so he continues his life as usual, happy with all the money and wisdom he's gotten over all his years."
        a "Yeah, that's cool, but look at this."
        "Alan looks towards a lion, gnawing a group of elderly peoples legs off, in the middle of a crowded street. Despite the amount of trauma to their body, they never die. "

        if pain:
            a "They may be in pain for the rest of their life." 
        else:
            a "At least they don't feel pain."
        
        a "There's an overpopulation of every species now. No death applies to all species, including the ones that attack humans."
        a "All species are doing what they evolved to do. Survive by any means necessary. Yet they can't die, so all they're doing now is overpopulating the earth. "

        if not pain:
            a "but hey, at least the people don't feel the endless pain they're in."


    a "So, uh, that's the end of the report. You did pretty decent, I'd say. I mean, I've seen worse, but I'd definitely make a few changes in your choices."
    a "So Charis is kind of mad at some of your choices. I think he's just jealous, to be honest. But he did say he wants to speak to you tomorrow, as he's going to sleep. He sleeps super early. Like, what a weirdo, ha."
    a "Anyway, yeah, is this just a dumb room without lights or something for the atmosphere? Yeah, it sounds dumb, ask Charis. The door is right behind you, just go to your cubicle, you know do whatever. Hang on, let me get that for you."
    "Alan hits a switch, and suddenly, the lights come on, and you're in a surprisingly small broom closet with a wonky projector projecting a live stream of you, the earth you created, onto the wall."
    "As you gaze over the people in it and contemplate never leaving this room, you wonder truly. Do you like your new world?"

label charisEnd:
    call endBeginning
    menu calloutCharis:
        "Shout for Charis":
            "You shout out to the kind god. You know he wouldn't let harm befall you. His conscience wouldn't allow it."
            c "I'm here, my friend. It's going to be okay."
            "You feel his arm on your shoulder, and the black goo begins to subside, light starting to pierce through the dark mass. Eventually, your sight stabilises. You realise you are suspended in space."
        "Shout for Alan":
            "You shout out for the chaotic god. Surely, in all this madness, he must be involved nearby."
            c "I'm sorry, my friend. Only I shall be joining you at this time. Try to relax yourself, it should all stabilise shortly. And believe me, Alan is not exactly stable anyhow."
            "It seems that Alan is out of the picture for the time being."
        "Shout for Juniper":
            "You call out for Juniper. You get the feeling that if everything is out of balance, they would be the one to set things right."
            c "Apologies, my friend Juniper is otherwise indisposed at this time. It has fallen on me to join you as we oversee the new world's fruition. Try to calm yourself. It's all okay."
            "Juniper clearly has other pressing matters at this time."
    
    menu reactionCharis:
        "Did you know those memories were mine?":
            c "The memories were chosen for encapsulating optimal opportunities to showcase both the benefits and drawbacks of a set choice."
            p "Did you know or not, Charis!"
            c "Honestly… No. Some people experience memories of a different person, while for others, the memories are from different individuals in every case file."
            p "So why were they my memories! Why didn't I know!"
            c "When you become a god, you are meant to lose all aspects of your earthly ties. You keep your intelligence and communication skills but lose your memories and interests."
            c "That said, it is possible to regain your mortal memories. I, for example, was eventually able to overcome the mental block and reconnect with my earthly self."
            p "So you remembered, too?"
            c "It took hundreds of years, mind you, mentally training myself to reignite the nodes of my brain that were intended to remain forever dormant."
            c "In your case, the trauma of the death case file was enough to break the perception filter and reconnect those memories with your god's psyche."
        "It was me, Charis. Those memories were mine.":
            c "I was concerned that may have been the case. I thought it unusual that you continued to experience the life of a single mortal."
            p "You should have told me, Charis."
            c "Truthfully, I wasn't sure about my hypothesis and didn't wish to draw attention to something that may have been mere happenstance."
            p "He died, Charis. My dad died in the hospital bed, and I never realised till that point that I had a whole life before with him. I can never go back now, never say my final goodbyes."
            c "I'm sorry, my friend. But don't look at these journeys as a punishment. They allow you to see all those you loved one more time before the old world is overwritten."
            c "In a way, it is a blessing that your father was able to spend his final moments by your side. I only wish that I could have said goodbye to my wife and sons."
            c "By the time I remembered their existence, they had been dead for centuries. I had no means of reliving those times so vividly, such as you did."
            c "To have seen them one more time would have meant the world to me. To traverse those memories again would be have been priceless."
            "It's true, although it hurt so deeply to experience that shocking revelation just as you were losing your father, at the same time, these case files let you live. To see the good and the bad of life."
    
    p "Where are we anyways?"
    c "Well, my friend, you are looking at the fruits of our labour. The new world built around your choices."
    p "How are we walking in space? How are we even breathing or talking?"
    "The wise god chuckles and waves his hand as if to brush off the incongruities of the matter."
    c "We are gods, are we not? If we wish it to be possible, we merely deem it so."
    p "Fair point."
    c "The purpose of this display is for us to debrief this project mentor to the student."
    p "You never said I was a student."
    c "Well, in terms of godhood, I have a few hundred years extra experience, don't I, my friend. Logistically speaking, this debrief shall place me as the mentor and you as the trainee."
    c "But don't worry, after all this, I reckon you are due for a promotion. But we'll delve into that when the time comes. For now, let's review your work."
    c "Let us see what your world is like…"

    if pain:
        c "Your first decision… Well, it didn't fill me with the utmost confidence, I'll admit. I couldn't fathom why someone with the power to remove pain would choose to keep it."
        "You seemed to have disappointed Charis with your very first choice."
        c "It's a shame. Really, the world could have been so much better if you had just removed the concept of pain. Here's a live vision showing the consequences of that."
        "Sure enough, a mirage of the world below appears before you, showing a little girl running in the park. She falls down and begins to cry loudly as the blood starts to form on the skin's surface."
        "However, although the pain the girl is experiencing is hard to watch, a young boy comes over, helps the girl up, and supports her to a bench. Pain is tough, but it brings people together."
    else:
        c "Your first decision was a wise one. Removing pain was an excellent choice, albeit an obvious one really. Even so, this was when I knew you could be trusted to call the shots."
        "It seems Charis favours your verdict from the very first case file."
        c "All the people down there will have a much higher quality of life due to the fact they are free from the shackles of pain."
        c "We can see visions related to your choices. For example, here is a live showcase of the effects of removing pain. It will showcase all the effects of the choices, good and bad."
        "It's true; related visions appear, such as one homing in on a little girl running in the park who falls down and scrapes her knee. Instead of crying, she gets straight back up and joins her friends."
        "At the same time, the vision seems to suggest that this girl won't treat this wound due to her indifference to it. What if it were to get infected? This could cause issues later, right?"
    
    if forests:
        c "With the second file, you did choose well. The forests are a wealth of life and nature. Had these been lost, the world would truly have been lesser for it."
        "Charis seems pleased that you have chosen to keep the world's forests and nature over the oceans."
        "A new vision forms, this time showing people walking through the woods as you once did in the old world. They marvel at the birds and flowers."
        "However, the oceans seem to be neglected. The sea is far more littered, and conservation efforts to protect it seem to be lessened. The world as a whole seems disinterested in it."
    elif oceans:
        c "Personally, I didn't agree with your insistence on selecting the oceans over the forests. So much of the ocean is undiscovered and dangerous. The woods are accessible to all."
        "Charis shows frustration with your second choice in this process."
        "The woods are overgrown with moss and weeds and left unoccupied. The birdsong is absent, and people avoid the woods now. They aren't cosy. They are unsettling."
        "However, the sea is more alive than ever. People love visiting the ocean, and many more efforts are made to fight pollution and conserve the water and the life in it."
        "You see people swimming, scuba diving, surfing, and taking boats on the sea."

    if fear:
        c "I'll admit the fear choice can be quite subjective. I'm pleasantly surprised that you chose to keep it. Fear keeps people in check and prevents people from doing evil."
        "You still surprised that Charis is inclined towards a world in which people can still suffer from fear. But you understand the reasoning of why he might lean this way."
        "Yet again, visions flood your field of view, showcasing how the choice to keep fear has affected this new world."
        "People are still cautious about things and wary of trusting strangers. This is positive in that the crime rate is lowered since the fear of consequences keeps people in check."
        "A more negative aspect, however, is that people are more anxious about going out of their comfort zone, and this prevents them from trying new things or making new friends."
        "You see one girl wanting to go up and admit her crush to a boy, but she backs away, her fears getting the better of her."
    else:
        c "I won't hold the fear choice against you too harshly. In truth, a world without fear sounds wonderful. However, sans fear, those with violent tendencies will show no restraint."
        "Charis seems indifferent about this decision. It seems the positives and negatives of this choice are fairly well balanced. However, you still glean that he would have preferred fear to remain."
        "The world is certainly more chaotic without fear. People talk more confidently and speak their mind more often. This can lead to more conflict and crime, unfortunately."
        "However, you notice one case where somebody is cliff jumping with their friends, and they are all having a good time without fear, making them worry about social ostracisation. "
    
    if lies:
        c "Whilst I normally agree with your judgement, this one has perplexed me. Perhaps there is a logic to a sweet lie, but surely the world would be better if all lies were abolished."
        "Charis is disappointed with your choice here, but you still believe that lies are a necessary part of society."
        "The visions show how politicians continue to lie and deceive and how scammers continue to separate people from their hard-earned cash."
        "However, you also notice how an grandad is lying about how he's enjoying playing a video game with his grandson."
        "Perhaps this man is so happy to be bonding with the child he'll lie about his discomfort for them to be happy."
    else:
        c "I'm glad you cut out the poison, which is lies from the new world. Surely it shall thrive under an honest and communicative population."
        "Charis is glad that the new world has removed the possibility of lying. You hope he is right. Surely, lying can only cause issues in the end, right."
        "Apparitions of the people below float before you, and the politicians and state heads are far more openly communicative and for the people."
        "On the downside, you see people abusing someone because they are different. Without lies, people are unable to hide their unseemly biases and beliefs, and this leads to more harm."
    
    if death:
        c "I'm confused as to why you would keep death. Surely, the kindest choice you could make for this new world would be to unshackle them from grief, loss, and fear of death."
        "Charis disapproves of your decision to keep death in the new world. You believe death to a necessary part of the cycle of life, and hopefully, he understands this opinion."
        "As the visions appear before your eyes, you see the consequences unfold. Life seems mostly the same as the old world in this regard."
        "You see a funeral for a loved one who passed from old age. The people are incredibly upset, but they have come together to celebrate the life of someone and tell stories of their connections."
        "Murder is still a huge issue, and many thousands still die on the frontlines of conflicts across the world."
    else:
        c "Ah, and so we reach our final outcome. You chose wisely on this one, as I knew you would my friend. Look how much better the world is without the fear of loss."
        "Charis is glad you chose in the same way he would have now. All that is left is to observe these last visions showcasing the outcome."
        "Families are no longer stricken by the grief of loss, and so households are much larger now. Funerals and tears are no longer the norm, and violent crime is much less prevalent."
        "However, overpopulation has become a widespread issue. People are being required by law to stop procreating, and the homelessness and drug epidemics are only getting worse."

    c "So, my friend, how do you feel about the new world you help form. Was it everything you hoped it would be?"

    menu opinionCharis:
        "Im happy":
            c "I'm so glad you agree with me on that front. It's an incredible thing we've done. All these people will have much better lives thanks to your efforts."
            c "With that all out of the way, let us return to the hall of gods to discuss what comes next."
        "Change some things":
            c "It is always at the point of no return that people see the errors in their thinking. It is okay, my friend. What we've made is still beautiful in its own way, flaws and all."
            c "With that all out of the way, let us return to the hall of gods to discuss what comes next."
        "I want to go back to the old world":
            c "I wish it were possible. Believe me, I once thought the same. But that world is truly gone now, only existing as a memory amongst us gods."
            c "With that all out of the way, let us return to the hall of gods to discuss what comes next."

label juniperEnd:
    "You wake up panting. You're sweaty and far too warm."
    "You bolt up suddenly, a squeak under you as you jolt around. Where the hell are you now? Was Juniper lying?"
    "Your eyes adjust to the light. It's hazy and blocked by a green hazy wall… the wall of a tent. With a start, you jump off your squeaky air mattress and throw the nearest pair of shoes on."
    "You unzip the tent hurriedly, desperate to see what's on the other side. You can remember it all now, every trip to this park, sat in this tent, every moment with your father and every moment with Bri. They must be here. There is no other way."
    u "Woah, what's with you and finding ghosts in this park {pName}?"
    "The familiar voice of your father rings through your ears. And there he is, still quite frail but he's stood up tending to a fire cooking some sausages. He's {i}alive{/i} by some damn miracle."
    menu dadInteract:
        "Run up and hug him":
            "You squeeze him tight, knocking the air out of his lungs as he hugs you back fiercely."
            f "You good kiddo? I'm here alright, don't worry, I'm not going anywhere."
            "You don't let go, you can't let go, what if he goes? What if none of this is real? You want this moment to last a lifetime."
        "Stare at him":
            f "Hello? Earth to {pName}??"
            "He laughs at you, assuming this is some joke, but you still can't believe it. He was almost dead, only the smallest chance. Yet here you were."
            "He locks eyes with you, giving you a reassuring look. He's here."
        "Start Sobbing":
            f "Oh, kiddo. Do you have a nightmare?"
            "He walks up to you and carefully brushes the tears from your eye with his sleeve. He tries to keep up, but you're crying far too fast for him, and he lets out a low chuckle."
            f "Don't worry, okay? I got you, we're here for you…"
            "He rubs your shoulder, and you manage to find your breath and calm your tears."
        "Walk up casually":
            "He gives you a funny look. He can tell something is off the moment you move."
            f "You pulling some sorta prank? C'mon, I may be better, but it is still meant to prank your old dad."
            "You're reassured when you hear him say it. He's better now. Thank god."
    
    "He jumps a little and ducks back to the fire to turn the sausages over in the pan. You see, they're a little burnt, but you can't find a reason to worry about that."
    "You're here, and he's here. Obviously, some time has passed because he's better, but honestly. That's better than having to wait for it yourself."
    u "Found some more wood for the fire! I am getting this breakfast if it kills me!"
    "It had been a while since you heard this voice in person, and you immediately turned to see the source."
    "Bri is all grown up. You can only assume you are, too. Her hair is cut short, a slightly grown out bob. Her hair looks damaged by heat but still has some curl to it. The ends are dyed a pale lavender."
    "The friendship bracelet from all those years back slides down her wrist. Her clothing is more tamed from when you were teens and a bit more suitable for camping."
    f "Should of left it for you, master chef. I've properly charred these sausages."
    "Bri walks over and peers at them, grimacing a moment before attempting to look more appreciative."
    b "Look, if you've done good enough, they'll still taste alright. And it's Doctor Master Chef to you, old man."
    "Her tone is light and playful. You feel at ease, like you're a kid again. Bri sees you and, as always, notices that you're off."
    b "You alright? We didn't wanna wake you too early, so I sorted the wood out cuz I'm your favourite."
    "She gives you a cheerful smile. She seems lighter and more carefree than before."

    menu briInteract:
        "I missed you...":
            "Bri gives you a funny look, clearly amused by that."
            b "I know we're still getting over the disappearing act of my early twenties, but if you're struggling a night without me, things may be worse than I thought."
            "Her tone is teasing but not cruel. She's clearly amused and, if anything, seems to appreciate the care. "
        "Run up and hug her":
            b "Woah! Who are you, and what did you do with {pName}? It's been ages since you've hugged me are you possessed?"
            "You can tell the jest isn't a complaint as she wraps her arms around you fiercely, holding you close for a while before letting go."
        "Act normal":
            "Bri raises an eyebrow as she surveys you. She knows something is up clearly but is deciding whether to press it. In her younger years, you knew there would be no questioning."
            b "Fine! Keep your secrets. I didn't need to know them anyway!"
            "She seems genuinely unbothered."
    
    f "You two ready for breakfast now? It's gonna get cold."
    "Bri's attention is immediately reset to the food, and she grabs the purple plastic plate she's used on these trips since she was a kid and helps herself to some food before sitting down."
    "You follow along, easing into being in your body again. Unlike in the memories, it feels right. For a moment, you ponder whether it was just a bad dream. A really bad dream."
    "You sit down on the log and feel something in your pocket pressed against your leg. You take it out and find an old necklace, perfectly intact, a post-it notes crumpled up next to it."
    "You think of Juniper for a moment. They let you get out and save the old world. You can't imagine the grief they must be hearing from Charis and Alan. You squeeze the pendant in a silent thanks."
    "It was clear Juniper hoped to go back to this world themselves but was held back. You hope they watch you now live your life to the fullest."
    "As you eat your food and listen to your dad and Bri laugh amidst the birdsong, you're sure of one thing."
    "You couldn't have made a better world than this."