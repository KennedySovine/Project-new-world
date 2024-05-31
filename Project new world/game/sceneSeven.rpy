$ s = Character("Server")
$ foodState = "Solid"

label sceneSeven:
    "The whole process seems much smoother this time as you breathe out, and the gentle hum of the office focuses you back to yourself."
    "This process was already so much easier. You can only guess one day, slipping into these files may be as simple as breathing. Leaving, too, was easier physically, though a part of you longed to be back in those woods."
    "Another louder, more stubborn part of you, however, is hungry."

    if seaGlassGreen:
        "You place the green sea glass on your desk. You're thankful for the girl who gave it to you. The small trinket does brighten up the place."
    elif seaGlassPurple:
        "You place the purple sea glass on your desk. It's less shiny in the office than in the sun, but it's still a beautiful reminder of the file and the time you spent."
    
    if bookedGain:
        "You thumb throught the bird book, many parts are circled and underlined, notes scrawled in with biro. You can't help but smile as you place it on your desk."
        
    "You peer your head out of your cubicle to see a concession of gods flowing in the exact directions. For a moment, your hunger is ignored as you study them."
    "Now that you have spent time with humans, you can see all the little ways the gods aren't human. Yes, some have horns or halos, wings, or tails. But some have eyes that are just a little too bright."
    "Others have skin that is just a touch too flawless, almost plastic. It's just how they walk and move through the space for others. The movement lacks some humanity."
    "Your stomach demands your attention again, and you join the parade of gods, hoping they are heading to this fabled lunch break."
    "The liminal office makes way for an equally liminal lunchroom in due time. The area feels more colourful because of those inhabiting it, but alone, it still has the hazy feel of the rest of Shad Tuod."
    "You join a queue and pick a beige tray off the stack; you glance to get a semblance of your options, but it is hard to see from here."
    "There is someone behind the counter; it is almost impossible to see them as the colours of their dress match the endless walls almost perfectly. They speak in an uninterested tone."
    s "Solid, liquid or gas?"
    p "Huh?"
    "That is… not the question you were expecting to be asked about food, to say the least. The server raises an eyebrow."
    s "Pretty simple choice. Solid. Liquid. Gas"

    menu foodState:
        "Solid":
            "You pick solid. Foods are generally solid, right??"
            "The server acknowledges your decision by grabbing some tongs and putting… something on your tray."
            "You gotta hand it to her. It is, in fact, a solid. And there's not much else to it."
            "You move, not wanting to hold up the line."
            $ foodState = "Solid"
        "Liquid":
            "You pick liquid, imagining a soup better than whatever 'solid' is."
            "If a food can only be described as a solid, that {i}must{/i} be a bad sign."
            "The server picks up a ladle and spoons a… liquid from a pan."
            "You apologise to her in your head because she was right. The only fitting description for this is liquid."
            "You move along. Be careful not to spill the liquid."
            $ foodState = "Liquid"
        "Gas":
            "Gas?? Really?? Sure, for science."
            "You see the server roll their eyes at your request, and they move to a cupboard in the back of their kitchen, taking a sleek, simple box from it."
            "They place it on the tray and hand it back to you."
            "Inside must be it. Your meal. The gas."
            "You give a nod and move out of the way."
            $ foodState = "Gas"
        
    "You look around the room. Many gods seem to be returning to their desks with their food, but a few sit on the plastic-looking lunch tables."
    "You spot Charis first; he has a book propped open, and his cat next to him is lapping at his tray of liquid. Alan sits a few tables over, with a bottle of whiskey by his side to wash down the solid on his tray."

    menu lunchTable:
        "Sit with Charis":
            call charisLunch
        "Sit with Alan":
            call alanLunch
        "Sit with Juniper" if oldworldInterest:
            call juniperLunch
        "Catch up with Juniper" if strikes >= 2:
            "Juniper doesn't register you trying to follow them, seemingly content to ignore you."
            p "Hey!"
            "You call out, and for a moment, it seems they won't even turn around to give you any attention. They wave a hand to you in dismissal."
            j "I eat my lunch alone {pName}, go enjoy some other company."
            "Stunned, you pause, Juniper using the time to get out of the eye line and back to their desk. You aren't sure if you've done something to bother them or if they're always like this. You look around once more…"
            jump lunchTable
    
    "You trudge back to your desk, and you're full, but the food is bland and leaves your mouth tasteless and barren. You imagine having that every day, the different forms finally having some appeal for the variety."
    "Before you sit down, spot it on top of your desk. A new file."
    "You pick it up and slide into your chair, taking a second to read the title:"
    "OW_NG_CASE-8_CLIFF"
    "You consider a moment what the title could mean, but don't dwell too long before opening the file…"

label juniperLunch:
    "You go to Juniper's table, but their eyes never leave you. They say nothing as you sit opposite them."
    menu confrontJuniper:
        "Staring?":
            p "Why are you staring at me?"
            "Juniper narrows their eyes, though it's hard to tell if it's in enjoyment or annoyance."
            j "Am I? I think you're seeing things."
            "Their tone is dry, but whatever they're looking for in you, they clearly haven't found enough of it yet, but they're still searching."
        "Sit silent and stare back":
            "You sit silent and stare back. Two can play at this game."
            "You meet their yellow eyes and stare into them, the two of you locked in a silent battle you could only hope to win…"
            "You sit like this for a moment, both staring intensely. Both are entirely silent. Juniper raises an eyebrow, a quiet question that you refuse to answer."
            "Their eyes crinkle at the corner in amusement."
            j "I am glad to finally have someone interesting here. Maybe all this business won't be a waste of time…"
        "Avert your eyes":
            "You avert your eyes and hope they say something."
            "Even looking away, you can feel their intense gaze looking at you, searching for… something."
            "You aren't sure what they could want? Did you do something wrong? You feel your cheek redden under their scrutinising gaze."
            j "Oh- sorry, did I make you uncomfortable?"
            "Genuine embarrassment laces their tone, but they don't move their gaze. Whatever it is they want seems more important than some simple social rejection."
        
    "Juniper finally averts their stare and quickly looks to the rest of the room. Your eyes follow, and you realise the room has got busier. Still, everyone seems content to leave you two outsiders to yourselves."
    j "How have your trips been to the old world?"
    "Considering the stares from a moment ago, the question feels almost too simple and carefully crafted so as not to raise suspicion. Indeed, that look wasn't just for this."

    $ strikes = 0
    menu oldWorldJun:
        "It's been fun":
            p "They've been fun, I've enjoyed the old world."
            "Juniper seems satisfied with that answer and gives a slight hum of approval. You feel like you're in an exam you didn't study for. You just want to reach the answer, but hopefully, this is the way."
        "Why are you asking?":
            p "Why are you asking? What do you {i}really{/i} want??"
            "Juniper rolls their eyes and leans forward to speak to you in a quieter, hushed tone."
            j "If you want to get anywhere, answer my questions, and you may receive answers to yours. Play this game with me, and I may play that game with you. Is that a deal?"
            "They lean back in their chair again, looking more comfortable and expecting an answer."
            jump oldWorldJun
        "I don't like it":
            p "I don't like it that much; I prefer it here."
            "Juniper drops their look to their folded hands on the table, seeming far less interested than before."
            $ strikes += 1

    j "Well, how are you feeling about making a new world? It must be a lot of responsibility…"
    "Their eyes are bright; you pause momentarily, searching for the key to all this but can't find it."

    menu newWorldJun:
        "Looking forward to it":
            p "I am looking forward to making it. The projects have been fun so far."
            "Juniper shrugs, their interest in you dissipating."
            j "Hm. Well, I hope you make a world you like in that case."
            $ strikes += 1
        "Its a lot of responsibility":
            p "It feels like a lot of responsibility. Why me?"
            "Juniper gives you a sympathetic look."
            j "Why anyone? Why are any of us up here? Why is it {i}you? {/i} that is beyond all of us."
        "There's nothing wrong with the old one":
            p "I still don't see what's wrong with the old one. It seems nice."
            "Juniper gives an approving nod."
            j "A rare opinion held in this place; it would be better for you to keep it quiet."
            "You consider all you've heard from them so far, how they've reacted to the other two's determination for a new world and wonder for a moment if they speak from experience."

    j "And well…"
    "They pause momentarily, tossing what you assume may be the final question around in their head."
    j "How do you feel about being here forever? After the new world is born, you'll be spending forever here at Shad Tuod. Forever can be… slow here."
    "You hadn't fully considered that, and you spend a moment considering how you feel about it."
    "The gods you've met, the chance to explore people's lives… but was it worth chasing and experiencing those lives just to end up back here in this endless hazy corridor."
    "And surely being here, you were immortal, right? Juniper and Charis at least seemed wise beyond the people in the memories. Maybe a greater lifespan allowed for that."

    menu shadOpinion:
        "I like it":
            p "I like it! Getting to live forever and go through memories is easy."
            j "Hm. I suppose it is an easy life, isn't it?"
            "They seem disappointed in you. They were expecting for, {i}dreaming{/i} for something else clearly. But you have no way of telling what that could be."
        "It will grow on me":
            p "It may grow on me. Do you like it?"
            j "It has its charms; some of the people are tolerable, and I have got to live many more lives than one normally would."
            j "The immortality though… the blandness… these things aren't overly to my liking, I must admit. Still growing on me, I suppose, after all this time."
            "You imagine they've been here a while; they seem to know everything about it. It surprises you that someone could be somewhere so long and still feel such a disconnect."
        "I dont know where I'm from":
            p "I'm not so sure… I don't know where I'm from, though, so I can't say if I want to go back."
            "Juniper nods, and at this moment, you feel more understood than you can ever remember feeling."
            j "Yes, it is… regrettable that you can't remember. I don't know either. None of us are supposed to…"
    if strikes >= 2:
        "Their interest seems thoroughly lost in you, and you watch them pick up their tray."
        j "Well, I hope your new world is going well. You likely won't see as much of me now as Charis and Alan aim to keep an eye on you."
        "You struggle to find something to say. They're already halfway out of the room."

        menu speakUpJun:
            "What do you want from me?":
                "You're so desperate to know they want"
                "They stop in their tracks as all the chatter in the silence falls away, and you feel your cheeks redden. You need to know it's worth it."
                "They turn slowly to look at you, and you can somehow hear them over the pounding of your heart in your ears."
                j "..."
                j "Why would I want anything from {i}you?{/i}"
                "They turn back and walk out abruptly. Slowly, the conversation picks back up, and you resign to eating your lunch alone, ignoring the curious eyes of the gods around you."
            "What is your problem?":
                "They stop in their tracks as all the chatter falls away, and you feel your cheeks redden. You need to know it is worth it."
                "They turn slowly to look at you, and you can somehow hear them over the pounding of your heart in your ears."
                j "..."
                j "If you don't leave me alone, you'll be my problem."
                "They turn back and walk out abruptly. Slowly, conversation picks back up. You resign to eating your lunch alone, ignoring the curious eyes of the gods around you."
            "Let them walk away":
                "You let them walk away; they aren't worth your time."
                "Their footsteps echo in your mind. You're annoyed at whatever all that was. You feel like you lost something but never really got a chance."
                "Oh well, you could work just fine without them."
        jump lunchTable
    
    else:
        j "What if…"
        "They pause to look around again, satisfied they lean in closer; you can see the furrow of their brow as they fight past the paranoia they feel."
        j "What if you didn't have to deal with making a new world? What if we could just… pull some strings and save the old…"
        "You hold your breath."
        p "How is this possible?"
        j "I have never fully finished this research, but once a new world was brought up, I found a personal project to save it. I believe I am close, but…"
        j "Once you were picked, I lost motivation. It was far too late. There is no way you'd give up this opportunity, I thought. I hadn't clearly stalled them all for long enough."
        j "But from what you've said, I believe you could be interested in saving that world. If it is saved, you can do something the rest of us can't."
        "There's a twinge of sadness in their voice, of longing for whatever this thing is. They clearly wanted it themselves yet have been forced to offer it to you."
        j "You can… go back."
        "Your mind stops, go back? Going back implies you had a connection to that world that was far more significant than previously explained. Juniper sees your confusion and gives you a moment."

        menu whatJuni:
            "Why can't I remember?":
                j "None of us can, or at least as far as I know."
                j "Many of us have managed to pick up pieces of our old lives through memories we have experienced. But I don't think any of us will be able to find the complete picture."
                j "I have been lucky to find some scraps in my time here. I have been here a long time, though, so it is unlikely you know what you'll be going back to. But maybe it will be worth finding out."
                "You consider this, going back to a life you can't remember to escape this life here, it was hard to say if the risk would be worth that…"
                jump whatJuni
            "Are all the gods from there?":
                j "As far as we know, yes, we only have memories stored of that world, so it's unlikely anyone was from anywhere else."
                j "We are quite uninformed ourselves. Many like to act like we're all-powerful, but we're just the middlemen. There is something bigger than us; we just can't fully conceive what or who that may be."
                "You nod, finding that idea not too surprising. The gods didn't seem to know an awful lot about anything and had no massive power to speak of."
                jump whatJuni
            "Who was I?":
                j "A fair question. One I can't answer, though."
                "Before you can ask why, they put a hand up and continue."
                j "I don't know. Likely, you won't know until you get back. I can't promise you you'll return to a good life, but I can promise one more worth your time than being up here."
                jump whatJuni
            "You have nothing else to ask":
                pass
        
        j "Oh- this has taken too long, so please let me know…"
        "Their voice is desperate. They took a risk on you and gave you the power to expose them to everyone else. You can tell none of this was done lightly; this was their last chance to save the world."
        "They've always been so stoic and uncaring, yet now you see they just thought their option had no chance. The others were busy betting on your new world, and Juniper was the only one grieving the old."

        menu saveWorld:
            "Help":
                p "Yes, I'll help you."
                "Juniper's eyes swell with joy. You are almost surprised this is the same unbothered god you met so recently."
                "They take your hands and give them a squeeze. Their joy was unconfined; you've given them a new hope, a way to save what they love."
                j "I will give you all the pieces. Keep an eye out for me. {i}Thank you.{/i}"
                "They drop your hands and leave into the crowd; you sit for a moment, stunned at all you learnt and what you agreed to do before standing up."
                $ helpJuniper = True
            "Don't get involved":
                p "No, I don't want to be involved."
                "Juniper makes a pained noise; this was their final shot, but it had missed. They steal themselves but refuse to meet your eye."
                "They say nothing else and disappear into the crowd of gods, back to their desk."

label alanLunch:
    "He puts down his bottle of whiskey as you approach him and take the seat opposite. He lounges back in his chair, getting comfortable."
    a "What was it this time?"
    p "It was between nature in the sea and the forests."
    a "Ha! As if it's worth bringing any of the nature from that good-for-nothing junkyard. What was your choice, though?"
    if oceans:
        "You respond that you kept nature in the oceans."
        "Alan considers this a moment before giving an approving grin."
        a "Hey, if it must be either, that one's far more interesting. There is loads of weird stuff down there. The people can barely be bothered to explore it all. Maybe this will make ‘em care."
        a "	Plus forests are just so damn {i}boring{/i} like what's the point in them? Nothin' that's what. You just have birds and stuff, no sharks or anything."
        if chaos == 2:
            "You feel a kinship with Alan; it seems you two agree in more ways than one, and you wonder if that'll continue. You feel comfortable enough to ask some questions."
    elif forests:
        if chaos == 0:
            a "Ugh, go sit with Charis if you're gonna suck up to him so much."
            "You frowned; it wasn't like you had picked his choices on purpose! It was just the ones you wanted."
            "Seeing you aren't gonna budge, Alan lets out a groan of complaint but doesn't ask you to move again."
            a "Why, though?? They're so dull; they're just some birds and some flowers."
            "You go to speak up, but he interrupts you."
            a "Y'know what? I don't even care! This, at least, is a small one to mess up. Don't test my patience on the bigger ones, though. This world needs to be worth the work…"
            "You nod a little, not wanting to anger him. You just wanted to enjoy your lunch…"
            a "You need to start thinking differently, alright? Where's the fun in a world with nothing weird? Nothing new to explore? You're gonna have a boring world of boring people."
            a "Think about how much was down there and how much wasn't known! That could have entertained your planet for a lifetime. Now they just have some stupid {i}flowers{/i}"
            "You dread to think of his response to something he deemed more serious; he seemed annoyed enough for something apparently small."
    
    menu alanChat:
        "Tell me what you want in the files?":
            p "Is there any way you can tell me what you want when I'm in the files?"
            "Alan stops bringing the whiskey bottle to his lips when you suggest this. You see his mind working a mile a minute as he mutters to himself."
            a "Juni could- no, they wouldn't tell me that, and I can't- UGH!"
            "You jump a little as he escapes his quiet contemplation."
            a "Nope! Not happening! Juni has knowledge of the files you got for some reason, but I'm not allowed to know, or I'll ‘threaten the poor guy and make them pick your choices."
            "He rolls his eyes as if the idea is completely outlandish."
            jump alanChat
        "I'm supposed to pick for myself?":
            "Alan scowls at you, not a fan of being called out like this."
            a "You are, yes, that's why you go in there. Am I not allowed to chat with you afterwards? Is that a crime?"
            a "If Charis or whoever didn't want me to talk to you, you'd be on far more lockdown. You can still make your decisions; I'll just push you to the {i} right {/i} options."
            "He looks away and takes a bite of his food, his face redder than before."
            jump alanChat
        "Why do you care?":
            a "Because this is everything we've been working on since! Forever!"
            a "Look, I'm one from the newer bunch, but I still feel like I've been here too long, and nothing happened. We're supposed to have had a new world by now, but there's nothing!"
            a "Do you know how dull it is to be in here all the time? Cuz if you don't know you will do so, stay tuned."
            "It made sense, being here all the time and having nothing new to do. A new world would likely mean new jobs to do and just a fresh start, which was clearly favoured."
            jump alanChat
        "Nothing else to ask":
            pass
    
    "You both eat in silence for a while until a bell rings, and Alan gets up, stretching his arms above his head."
    a "Back to it, hey? See ya around."
    "With a short wave, he heads off to his desk."

label charisLunch:
    "You go up to Charis."
    "Charis spots you as you approach and offers you a wave. The cat's ears perk up, and he goes to investigate you."
    menu catLunch:
        "Pet cat":
            "You let the cat approach and pet it."
            "The cat purrs gently, rubbing its face into the palm of your hand, happy for the fresh attention."
            "Charis looks pleased as he watches the two of you interact."
            c "I am glad the two of you get along. He isn't supposed to, but on occasion, he roams the halls alone. Do let me know if he escapes to your desk."
            "The cat looks at you innocently."
        "Avoid cat":
            "You take a small step from the cat and keep away."
            "Charis seems understanding and gestures with his hand to the cat, which returns to him. The cat jumps up onto his shoulders and reclines around them, Charis utterly unphased."
            c "It is good to see you. Do not worry about him. He is always a little troublemaker."
            "Charis pets the cat under his chin before turning his attention to you."
    
    "Charis gestures for you to sit, and you take the bench opposite him. There's calmness as the two of you eat quietly for a moment. After a moment, he clears his throat to ask."
    c "So… I must ask what was it between this time?"
    p "It was between nature in the seas and the forests."
    c "Ah, that is an interesting one. I can't say that is something I expected from one of those files. They were supposed to be more… feelings, but that works too. And has a clear answer, hm?"

    if oceans:
        c "Ah."
        "He shoots you a disappointed look before trying to avert his gaze, deciding if the confrontation would be worth explaining."
        c "The ocean and the things in it… they can be so dangerous. Even the smallest creatures often pack a massive punch, so it is no wonder all the scary tales come from the sea."
        c "It is full of the unknown, and although the waves may be relaxing, the things under those waves are often far from friendly…"
        "He pauses a moment, seemingly happy to fall into silence. You take the time to ask some questions."
    elif forests:
        "He looks at you expectantly, and you answer that you picked forests."
        "He beams with pride as he looks at you, happy to see you agree with his verdict that he deemed so obvious."
        c "Exactly! Think of just how calm and tranquil the forests can be… birds chirping, leaves crinkling under your foot. It's a place where many find calm and solace, so isn't such a place important?"
        c "And besides the oceans are um- interesting. Many dangerous creatures down there, so it is no surprise all the worst tales come from those on or near the sea."
    
    if calm >= 2:
        "You feel a connection to Charis; the two of you get along so easily and have similar views of the world. You decide he's the most sensible option to ask some questions."
    
    menu charisChat:
        "Tell me what you want in the files?":
            p "Is there any way you can tell me what you want when I'm in the files?"
            c "Oh… Oh! That is a good idea. Maybe I could do that? Let me think a moment."
            "He goes quiet, clicking his fingers to keep his mind on track. You watch his look shift from hopeful to disappointed, and eventually, he lets out a sigh and shakes his head."
            c "No, to be truthful, I was only allowed to be informed of the first file's subject matter, so I can't tell you in advance, nor can I travel there with you."
            c "It was a good idea, though. If I find a way, I will let you know."
            jump charisChat
        "I'm supposed to pick for myself?":
            c "well, yes, but… you can't be selfish in your choices. You have to think of who your choices will truly affect, and that's the people living in the new world."
            c "You will be up here to observe, but they will have to deal with the consequences, so think of them as you decide. You are here to be a tiebreaker. At least consider both sides thoroughly and don't act rashly, okay?"
            jump charisChat
        "Why do you care?":
            "Charis gasps a little, clearly surprised at the question. He thinks the answer is the most obvious thing in the world."
            c "Because this new world deserves a fresh start! The last one is so… messed up that there's nothing to even salvage. And it has taken us so {i}long{/i} to fix this. I worry if this next world is broken, it will take far too long to fix it."
            c "We don't have the energy to just make a new one again if this goes wrong, okay? So please be serious about all this…"
            jump charisChat
        "Nothing else to ask":
            pass

    "The two of you continue to eat, occasionally making light conversation but, for the most part, quieter than before. Charis seems distracted, and you have your own things to think about."
    "You hear a bell ring, and Charis moves to get up, a routine he is clearly familiar with."
    c "Thank you for sitting with me today. I don't get the chance to do that with others often."
    c "We must return to work now. I assume you will have a new file. I may come to see you again after, but regardless, I trust you will pick well."
    "He gives you a smile and walks away. You move to get up."
    return