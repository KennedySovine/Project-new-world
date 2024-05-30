include "characters.rpy"

$ nosey = False

init python:
    import random

    def randomStyle():
        styles = ["gothic", "cute", "modern"]
        return random.choice(styles)

label nameInput:
    $ pName = renpy.input("What is your name?").strip()
    $ p = Character(pName)
    return

label stayText:
    menu staying_menu:
        "'I'd like to hear what's going on. From {i}all{/i} of you.'":
            show j basic at right with moveinright
            #show c basic at left with moveinleft
            "Juniper and Alan share a smug look, Juniper taps Charis on the shoulder."
            j "C'mon Charis even they want us to stay just get on with it already and we can get back to work."
            "Charis lets out a long sigh, he clearly hadn't wanted this to go this way."
            c "Fine..."
        "'If Charis wants to tell me I'm happy to listen to him.'":
            #show c basic at left with moveinleft
            #show a basic at right with moveinright
            "Charis looks to you, surprised but pleased to hear your verdict."
            "The other two look slightly less pleased, but Alan looks determined."
            a "Look I don't care if you want me here, I'm staying. Got it?"
            "Juniper nods in agreement, the two clearly happy to walk all over Charis. Whatever worries they had previously been long gone."
            "Charis fumbles over their words, trying desperately to find a way to get them to leave but eventually settles."
            c "Fine... but just keep quiet."
        "'Can someone just tell me what's going on?'":
            "The three look over to you, for once unified as all share a sense of empathy."
            "They've all been in your shoes but the way you spoke reminded them instantly of some long-forgotten pasts. They look at you apologetically."
            show j basic at right with moveinright
            j "Go on Charis... floors yours."
    return

label sceneOne:
    scene bg office
    "You bolt up awake, your mind foggy but already aware that something is wrong and this is not where you were before."

    menu calm:
        "Take a moment":
            "You take a moment to breathe and compose yourself, no point trying to solve anything when this stressed."
            "You don't remember much but you remember how to calm yourself you breathe..."
            "And out..."
            "In..."
            "And out..."

        "Focus":
            "You immediately focus on your surroundings, trying to figure where you are..."
            "Your mind races back to remember where you were, it was somewhere soft and comfortable."
            "Somewhere nothing bad should be able to happen but something did happen."
            "That's what had made you so afraid. But this was not that place, maybe that place was just a bad dream."

        "Call out for help":
            p "Help!" with vpunch
            "You call out, hoping for anything to happen."
            "Your voice echoed, hearing yourself over and over for what felt like an eternity."
            "It made you feel dizzy and truly, utterly alone."

    "You look around at the strange place you found yourself in. Hazy fluorescent light seems to emanate from everywhere. It feels strangely clinical."
    "You stand up and a warm stale breeze slowly drifts past, seemingly never-ending."
    "You noticed desks in cubicles, most seem to have small trinkets upon them."

    menu desk:
        #Juniper desk path
        "Desk with mysterious plants":
            "You move towards the desk with a few fake plants of a species you don't seem to recognise."
            call juniperDesk
        "Desk with a cat perched on it":
            "You go to the desk with a cat perched, eyeing up a bottle of ink, ready to give it a hit over a mess of documents."
            call charisDesk
        "Desk with snacks and drinks":
            "You move towards the desk with junk food and drinks, and a half-drunk bottle of whisky."
            call alanDesk
    hide j basic
    #hide c basic
    #hide a basic
    #show c basic at right with moveinright
    "Charis smooths out his robes and quickly rummages to find a piece of paper on his desk. He hands you a file and printed in big, red text on the front it reads:"
    "PROJECT NORTH"
    c "It is about time I formally welcome you to Shad Tuod. To put it simply, this is the Office of the Gods."
    c "Here is where we work, overseeing and managing the world and its people, making sure everything runs smoothly."
    c "Recently, however, things haven't been running {i}quite{/i} as smoothly as they should be."
    "Alan scoffs and Juniper rolls their eyes. They seem to think this is the understatement of the century."
    "Charis wavers a little at their reaction before continuing."
    c "That's why we've brought you in. All of us...well, we can't agree on what to do, so you're here to decide for us."
    c "You're here to help us form a new world and rejuvanate the old. You're here to help us with Project North."

    menu reactionOne:
        "Why me?":
            p "Why me? What makes me different?"
            c "Because you're a good person and we can trust your choice to be true."
            show j basic at left
            j "You have...a connection to the old world that we deem worth exploring."
            #hide c basic
            #show a basic at right
            a "Because you're the {i}chosen one{/i}, destined to save the world from its own destruction."
            "The other two shoot Alan a look. You hope it was a joke."
            hide j basic
            #hide a basic
            jump reaction
        "I don't want to":
            p "What if I don't want to? Why can't I go back?"
            #show a basic at left
            a "Go back where? Go on, tell me one thing about yourself. Tell me where you're going back to."
            "Juniper scowls behind him and Charis lets out a gasp, but you barely notice as your mind begins to spiral."
            "It was cruel, but it was true. You try to remember who you were, where you came from, but it's all a blur. There's nothing."
            show j basic at right
            j "When a god is made, their old life is lost. You can't go back...I'm sorry."
            #hide a basic
            #hide j basic
            jump reaction
        "The old world?":
            p "What's so wrong with the old world?"
            #show a basic at left
            a "It's broken and dying; that's a stupid question."
            #show c basic at right
            c "Whilst there is some beauty in that world, it has been corrupted. We know we can do better, we just need your assistance in that matter."
            "The two of them look at you as if you're the answer to all their questions. Juniper folds their arms and looks away, not wanting to get involved."
            #hide a basic
            #hide c basic
            jump reaction
        "Agree":
            p "Alright, let's get started."
            pass
        
    #show c basic at right
    c "Alright, we will take you to your desk shortly. There you will find a file. Please open it and you will experience a tale from the old world."
    c "This will help you guide you to a choice, and what you decide will impact the new world we build."
    c "So be careful what you pick. There's no going back..."
    #hide c basic
    "The three of them walk you to your desk. You spot it immediately because it is completely empty aside from the file."
    "You feel a weight in your pocket and stick your hand in to find out what it is."

    menu pocket:
        "A snake ring":
            "You pull out a black snake shaped ring that curls around your finger. It has a few red gems ingrained on it."
            "You slip it on, pleased to see it fits your fingers with ease before taking it back off."
            "You place it on your desk. It feels more like you now."
            $ pStylestyle = "goth"
        "An old phone":
            "You pull out an old phone with a cracked screen with no battery. A charm of a cute character dangles off it."
            "You thumb over the buttons and turn it to see the charm. It's worn out and clearly well loved."
            "You place it on your desk. You feel less alone with the character here."
            $ pStylestyle = "cute"
        "A set of earbuds":
            "You pull out a set of fancy earbuds in a sleek white case. You think you can hear music playing from them."
            "You open the case and put a bud in your ear. A nice song is playing that you don't recognise."
            "You place the case on your desk. It's a bit less empty now."
            $ pStylestyle = "modern"
        "Leave it":
            "You leave it for now, but whatever it was immedialty dissapears from your pocket."
            $ pStylestyle = randomStyle()

    "You look at the file on your desk with renewed interest and pick it up. On the front, it reads:"
    "OW_NG_CASE-1_PAIN"
    #show c basic at right
    c "We will wait just outside for you to finish. Thank you again for your help with all of this."
    #hide c basic
    "You nod. Once they step outside, you open the file and begin to read."
    return

label juniperDesk:
    "You step gingerly into the cubicle; it feels like an invasion, but there's no one there."
    "Immediately, the air feels slightly fresher and you take a moment to marvel in it, sensing this is a rarity."
    "There's no computer on the desk, only a few loose pieces of paper and a file with a word stamped on it."
    "C O N F I D E N T I A L"
    "Some drawers sit below the desk with one slightly ajar."
    menu noseyJ:
        "You check the papers on the desk.":
            "You glance down at some of the loose papers, skim reading a couple of them."
            "They seem to be files on different... people? A picture sits in the top corner of each page and then their name in scratchy cursive lettering next to it."
            "The people are unlike anything you've seen before."
            "Pitch black holes for eyes, twisting horns sprouting from their heads, unnaturally sharp teeth in an unnaturally sharp smile. Something distinctly unhuman about them all."
            "The pages note several things, personal relations, grudges and the like between these beings."
            "You hear footsteps and immediately drop the papers, quickly organising them as you found them."
            $ nosey = True

        "You thumb through the confidential file.":
            "'PROJECT NORTH' is written on the first page, a blocky lettering as if written on a typewriter."
            "Notes in red pen accompany in a scratchy hard to read handwriting, a few words are underlined: 'New World' 'Recycled' 'Waste Prevention'."
            "A photo sits in the file, a young girl stares up from the photo with a toothy grin, a name scribbled out below her."
            "You hear footsteps and haphazardly close the file and step away from it."
            $ nosey = True

        "You tug open the drawer and rummage through it.":
            "Theres a small hole in the drawer, upon opening you identify this must be the source of the fresh air."
            "A small bonsai tree wrapped neatly around itself sits in the drawer; it lacks the fake plastic sheen of the other plants."
            "You think it is the prettiest and loneliest thing you've ever seen. An ode to something you can't fully comprehend."
            "A well-worn letter sits next to it, its hard to make out words from the messy cursive but you manage to decipher:"
            "'My love will follow you through every world.'"
            "You hear footsteps and immediately slam the drawer shut, the loud bang audible over the footsteps."
            $ nosey = True

        "You stay put but don't touch anything, hoping whoever works here returns":
            "Minutes pass, it feels like an eternity but eventually you hear footsteps."
            $ nosey = False

    show j basic at right with moveinright
    "A person rounds the corner and stares at you. Despite your surprise to see them, they seem entirely unbothered at your sudden appearance."
    "They survey the room, and you take in their appearance: They stand incredibly tall."
    menu heightJ:
        "It was rare you met someone taller than you. It makes you feel slightly uneasy.":
            $ pHeight = "tall"

        "They are a decent amount taller, not unheard of as you're average height.":
            $ pHeight = "medium"

        "You are quite short; it feels like they tower over you.":
            $ pHeight = "short"

    "You follow where their yellow goat-like eyes go. It's the only part of them that is easy to follow on account of their dense bulky layers of clothes."
    "A thick cloak sits heavy on their shoulders. It's messy with twigs poking out, almost as if growing from the cloak itself." 
    "Their ears resemble those of a goat and poke out from their tangled messy brown hair."

    if nosey:
        "They notice their space has been disturbed and narrow their eyes at you, a wave of guilt washes over you as they stare you down"
        u "Do not touch my things."
        "You nod hurriedly, not wanting to bother the imposing figure any further."
        "They look away, seemingly content to let it go for now."
    u "I imagine this is all quite confusing, I must admit I didn't expect you to stray to my desk first of all places."
    "Their voice is gravelly and their tone hard to discern. You can't tell if they're proud or disappointed you strayed this way."
    "You realise you've been holding your breath since they got here."
    "They address you properly, offering a hand to shake. You notice the tips of their medium brown hands going to a rusty red colour as if stained."

    menu greetingJ:
        "Shake their hand":
            "You shake their hand, lost for words and just following along."
            "They seem to assess your handshake, giving you a small nod at your cooporation."
            "They clasp their other hand over the top of yours and give it a small squeeze: an attempt at reassurance."
        "Ask where you are":
            p "Where am I?"
            "You ask as you clasp onto their hand desperately."
            u "That will be answered in due time..."
            "They take their hand from yours, wiping it on their cloak before inspecting it and dropping it down to their side."
        "Do nothing":
            "You stand there unresponsive; this is all too much."
            u "Hm not much for handshakes? That is fine"
            "They seem genuinely unbothered, at least somewhat understanding of your current situation."

    call nameInput

    j "My name is Juniper. I am not here to be your guide, though I am flattered you found your way to my office."
    j "You are welcome if you ever need a breath of fresh air. I found that the hardest thing to adjust to- just how stale the air here is."
    j "You may not remember how you got here or what's going on. I would help but advising you is not a job I have been entrusted with. Charis made sure of that."
    "There is a hint of resentment in their voice at the mention of this Charis."

    menu optionsJ:
        "You'd rather Juniper teach you. They seem safe":
            pass
        "You're thankful they aren't teaching you. They seem off in some way.":
            pass
        "You don't care who teaches you at this point. You just want someone to help you out.":
            pass
    
    j "Anyway, let me lead you to Charis. He should be back from lunch by now."
    "You follow Juniper silently. The previously empty desks are now full of people, though there is something unhuman about them all."
    "Some type away on computers whilst others have typewriters or books and quills. One you pass even had a chisel and a rock."
    "They all seem busy and pay you no mind."

    u "Hey Juni!"
    "A voice shouts out, followed by a noise of complaint as something hits Juniper square in the face."
    "Juniper scowls, you follow their gaze and see someone with short spikey red hair."

    if pHeight == "short":
        "They seem to be around your height."
    else:
        "You appear to be taller than them."

    u "C'mon, grow up! It's what you asked for earlier."
    "Juniper glares at the stranger a moment before shrugging, reaching down to pick up what you now see to be a snack."
    "The stranger seems ready to head back to work before they see you and a hint of interest crosses their face."
    u "You got to the new guy before Charis did? Oh, you're not hearing the end of that."
    j "For the record, Alan, they came to me first, I'm just escorting them there. Besides he'd rather they meet me then {i}you{/i}."
    "The tension between the two of them feels friendly, but it is hard to say for sure."
    "This 'Alan' looks between the two of you."
    a "Well I may as well join you two to see him. Can't have him preaching too much goodness, can we?"
    j "As if we'll manage to get a word in about it..."
    "Alan laughs sarcastically but seems to agree, stepping into place behind you as the three of you walk."
    hide j basic with moveoutright

    "You approach a desk that is covered from top to bottom in books. A cat glances at you, curious at the new face."
    "Thick hardback books are stacked onto every possible surface, cluttering up the space and making it feel much smaller than Juniper's cubicle."
    show j basic at right with moveinright
    "Juniper steps into their cubicle space first and you follow with Alan behind you."
    "You see a hunched over pale figure wearing pale silky robes. He seems to be older than the two you met previously, though it is hard to say for sure."
    "He looks frail and weak, though the appearance isn't helped stood near Juniper."

    c "Juniper something has gone horribly wrong! Our new friend they're {i}nowhere{/i} to be found! I looked where they were supposed to appear and the lunch hall and-"
    "Juniper puts out a hand, trying to stop his endless nervous babble."
    j "Relax, they came over to my desk and I don't care enough to explain all this to them."
    c "What do you mean they--oh."
    "Charis looks over to you for the first time and seems to relax a little, one of many stresses finally leaving his mind."
    a "Yeah, we got them here in one piece and everything."
    c "Ah yes well- thank you for that."
    "You figure Charis wants the other two to leave for this conversation but holds off asking them directly instead opting to pick at his hands."
    "This seems like the sort of battle he's had many times before with these two, you gather it's a battle he rarely wins."

    call stayText
    return

label charisDesk:
    "You enter the cubicle, finding the cat to be its only inhabitant. Though it pays you little mind, distracted by its cleansing ritual."
    "With the first steps out of the way, you take it in fully. Grand towers of books grow up from the floor. Consisting mainly of thick hardbacks."

    menu heightC:
        "The books are almost as tall as you are":
            "You peer down at the towering tomes. There's a wealth of material covering wars, ethics, science, technology, even cookbooks."
            $ pHeight = "tall"
        "The books are on level with your head":
            "You are almost impressed with the sheer quantity of reading materials contained within the compact cubicle space, even if disorganized."
            $ pHeight = "medium"
        "The books tower above you like giants.":
            "You are careful not to knock into any of them. Partly from fear that you'd meet your unfortunate demise beneath their heavy embrace."
            $ pHeight = "short"

    "You look back to the desk. It is adorned with various trinkets, parchment, ink bottles, and rather large amount of cat hair. Not to mention even more books."
    "As your gaze meets the centre of the desk, a file catches your attention. It's resting beneath the paw of the cat, but you can make out the letters '-DENTIAL'."
    "The cat looks at you with an almost pensive look."

    menu curiousC: #aLover is for animal lover
        "You move the cat's paw to get a closer look at this file":
            "The cat hisses, judging your inability to satiate your curiosity. And to be fair, the saying goes that the curiosity killed the cat."
            "The cat does relent, retracting its paw, and allowing an uninhibited view of the file. You now see that it reads 'CONFIDENTIAL'. "
            "Additionally, there's a title to the document: 'OW_NG_CASE-1_PAIN'. "
            "Before you can have time to open the file, you hear footsteps approaching. You scramble to move yourself back to the front of the desk and compose yourself."
            $ nosey = True
            $ pLover = False
        "You reach your hand out gently to pet the cat":
            "Whilst the document is certainly appealing, you can't help but want to greet the furry feline that is your first contact in this mysterious place."
            "The cat sniffs at your hand, acting as your judge. Clearly it deems you to be of good character, as it begins nuzzling your hand, and emits a heartwarming purr."
            "You begin to hear footsteps. You turn to face the entrance, but you cannot bring yourself to retract your hand from the adorable purring cat."
            $ nosey = False
            $ pLover = True
        "You keep your distance, not wishing to come across as nosey":
            "The cat looks at you with a more relaxed expression, now stretching out to fully cover the document."
            "Any chance to read it has now been lost beneath its furry mass. You hope that in time you'll be able to gain the answers to your many questions."
            "If only you could find someone to talk to. As nice as the cat's company is, it doesn't make for a great source of information."
            "As if to answer your internal pleas, the sound of footsteps begins to reach your ears."
            $ nosey = False
            $ pLover = False

    #show c basic at right with moveinright
    "Eventually, after an agonising wait someone enters the cubicle. You take a moment to observe the hunched individual."
    "He's wearing white silken robes, with golden embellishments. He has old fashioned sandals on his feet, explaining the loud footsteps from the clopping wood."
    "The bespectacled individual now meets your gaze. Their eyes look incredibly tired, their face well worn."

    if nosey == True:
        u "Whilst I understand you must be quite confused at this time; I would suggest you do not rummage through what is not yours."
        "You feel your face redden in shame. You can hear the tinge of disappointment in the old man's voice. "
        u "I'm willing to accept your curiosity given the circumstances. But my peers may not be quite so forgiving. Don't worry, it's only natural to have questions, and me and Alexios won't tell."
        "You gather that Alexios is the cat. The fellow forms a meek smile, and you feel he won't hold this against you."

    if pLover == True:
        u "Ah, I see you've met Alexios. He's a great judge of character you know, so he must like you to be purring such a storm."
        "The old man chuckles to himself and forms a smile so warm that you can't help but reciprocate."
        u "That said he can be quite a rascal sometimes. Particularly… when it comes to knocking ink upon my parchment."
        "He darts across the table to prevent Alexios from toppling a glass vial of ink with his paws. For someone so frail he was surprisingly fast."

    if nosey == False and playr.SaLover == False:
        u "Thank you for waiting so patiently. I'm glad you aren't the type to go rifling through a fellow's possessions when left unattended."
        "The man smiles to himself, seemingly satisfied in the fact that you showed restraint when given the temptation."
        u "That said, feel free to make yourself comfortable, I assure you Alexios does not bite."
        "He gestures towards the furry feline sprawled across his desk space."

    u "Anyways, I'm sure you've got a lot of questions for me, so let's get introductions out of the way, shall we?"

  
    call nameInput
    c "My name is Charis, and you've already met Alexios my cat."
    "Charis extends his hand out, gesturing you to shake commemorating your arrival to this unusual place. He seems earnest with his intentions, but this whole situation is unusual."

    menu meetingC:
        "You reach your hand out, and shake it smiling back.":
            c "I was worried you'd find it difficult to adapt to such an overwhelming situation, but I'm glad you are willing to put trust in others."
            "His smile grows, he seems to appreciate your friendliness. You both drop the handshake."
        "You take a step back, unsure if you can trust Charis.":
            "The man's smile begins to fade, and his arms slowly drops. He is a little disappointed though quickly renews himself."
            c "I know this is a lot for you to take in, but there is nothing to fear. I have only your best interests at heart."
            "The smile returns, though it doesn't reach his eyes. With that formality over, you can finally get some answers."
        "You meekly extend your hand to shake, but you aren't sure how to feel.":
            "The man squeezes your hand and reaches his other hand to hold yours reassuringly."
            c "It's okay to feel confused or unsure. It was once me in your very same position. Try not to worry too much, I assure you it will all become clearer in time."
            "He lets your hands go gently, and gestures you towards the cubicle exit. It's presumably time to get some answers that could help ease your worries."

    c "As much as I would love to answer all your questions myself, I couldn't bring myself to be so selfish."
    "You glean the hint of reluctance in Charis's voice."
    c "There are others who have awaited your arrival, and they wish to meet you too. Let's not keep them waiting. As soon as we're all together, we'll answer your questions."
    "You follow Charis out of the cubicle and back into the room of desks."
    "Once out the cubicle you hear a voice below out from behind..."
    #show a basic at left with moveinleft
    u "Oi, Charis. You gonna introduce us or what! Or are you planning on hogging the newbie to yourself."
    "Charis winces as the loud individual calls to him."
    c "Ah, Alan. Whilst I appreciate your urgency, it may be advisable not to startle our new guest whilst they adapt to all this."
    "You look at this Alan character as he catches up to you."

    if pHeight == "tall":
        "Alan seems to be rather short in comparison to yourself and Charis, although Charis's hunch does reduce his overall height."
    if pHeight == "medium":
        "You are a little taller than Alan, though shorter than Charis if you account for his hunch."
    if pHeight == "short":
        "Alan seems to be around your height, and a bit shorter than Charis, you gather Charis would be taller, if only they weren't so hunched over all the time."
            
    a "Yeah, yeah whatever. I knew you'd be the first to find 'em anyways. Course if we did find 'em before you, I'd never here the bloody end of it."
    "Alan rolls his eyes; you get the feeling they likely enjoy winding one another up."
    c "Now that I've found you, we need to locate Juniper, and then we can get started with initiation."
    a "Oh boy, I can't {i}wait{/i} for initiation. Wouldn't want to miss that for the world. Literally."
    "You sense the searing sarcasm from Alans remark. Charis chooses to ignore Alans comment, and you continue."
    #hide a basic with moveoutleft
    "You eventually reach another cubicle, and Charis asks you and Alan to wait a second while he gets Juniper."
    show j basic at left with moveinleft
    "Eventually, a new figure exits the cubicle alongside Charis. They have striking yellow eyes, and ears which you can only relate to that of a goat, poking out from their messy brown hair."
    u "It's nice to make your acquaintance."
    "Their voice is rather deep and gravely compared to what you expected, and you struggle to discern what they are saying at first."
    j "I am Juniper. I'd answer the questions you have, but I know how Charis wants to have that honour."
    "Juniper shoots Charis a knowing look, and he shuffles a bit, clearly knowing that they are accommodating his wishes perhaps against their own."
    c "I appreciate everyone allowing me to guide this initiation. Now we are gathered, lets head back to my desk to get started."
    hide j basic with moveoutleft
    #hide c basic with moveoutright
    "You walk in silence back to Charis's cubicle. Your mind whirring from all these new faces and places that don't seem to fit together."
    "Charis gestures you to come in, and so the four of you enter."
    #show c basic at right with moveinright
    c "Now that you've all been introduced, I don't mind if we begin initiation with just us two. But it's up to you of course."
    "You figure Charis wants the other two to leave but holds off saying, instead opting to pick at his hands."

    call stayText
    return

label alanDesk:
    "You step into the cublicle and notice an immediate smell of body odour."
    "No one is there, but you have this overwhelming feeling of being watched."
    "You notice tons of small holes in the desk, and in the middle of them a butterfly knife is stabbed into the wood."
    "On the desk is two consoles and a gaming player, all stacked on top of one another, with a gaming laptop beside them. They're all paired with a cheap, tiny monitor with a black spot in the corner."
    "Hidden in the pile of half empty crisp packets, you notice a red flashing light, and upon looking closer..."
    u "BOO!" with vpunch
    #show a basic at right with moveinright
    "Suddenly, a heavy looking figure jumps up behind you."

    menu heightA:
        "You are quite tall; it feels rude to look down on them.":
            $ pHeight = "tall"
        "They are a decent amount shorter, not unheard of as you're average height.":
            $ pHeight = "medium"
        "It was rare you met someone shorter than you.":
            $ pHeight = "short"

    u "I saw you on the hiddel camera. Don't think I don't have security now. You're new so I'll let you off...or will I?"
    "He grins at you, shooting you a wink. He seems slightly annoyed but doesn't seem like he's trying to threathen you."
    u "Anyway, why're you at my desk? This isn't how people normally introduce themselves. I don't even know your name!"

    call nameInput

    u "'aight [p], so what makes you think you can creep around my desk for?"
    "He chuckles and gives you a playful push."

    menu apologyA:
        "Apologize":
            p "I was just curious. Sorry."
            u "Well, curiosity kills the cat, don't it? Well, not that you can--ah, never mind."
        "Question":
            p "Where am I and why am I here?"
            u "Woah there, one question at a time. So, basically, something something you work for us now, we'll work out the nitty gritty later."
            u "Anyways, Charis always gets pissy when I say too much. Something about an NDA? Apparently, we have laws up here or summ'in."
        "Joke":
            p "I was trying to nick your PC. Looked like I could get a good profit out of it."
            u "Ahh, you see, that's what the cameras are for: catching lil' rats like you!"
    
    a "Oh, by the way, the name's Alan. Since you're new, I'll have to take you to Charis 'cause apparently, he doesn't trust me with new people. Eh, but you look like you're still alive so I dunno what his problem is."
    "You both start to walk over to a desk. It is covered in plastic flora, some unlike any you've ever seen before."

    if pHeight == "tall":
        "On the way, you see another tall individual and hear them whispering 'Oh God' to themselves."
    else:
        "On the way, you see a giant of a person and hear them whispering 'Oh God' to themselves."
    
    show j basic at left
    a "Oh hey, Juni!"
    "Alan chucks a pack of crisps from his pocket to Juni"
    u "Thanks. But what are you doing with this new guy? Alan, I swear if you leaked anything important--"
    a "Of course I didn't, Juni, what do you take me for? Charis has yapped enough about it to me already."

    if pHeight == "short":
        a "I caught this little {i}rat{/i} snooping around my desk all thanks to my CCTV."
    else:
        a "I caught this giant {i}rat{/i} snooping around my desk all thanks to my CCTV."
    
    u "Ugh, not your CCTV. I don't understand why you're so obsessed with privacy. Also, don't call me Juni. It's childish, Al."
    a "Hey! Don't use my bit against me. You're the one with secret documents just on your desk with 'CONFIDENTIAL' on, as if that's not gonna make people {i}more{/i} tempted to look at them..."
    u "Well, it's worked so far. Also, shouldn't you be taking the new guy to Charis so he can get them sorted and introduced? That is your job, after all."
    a "Yes {i}Juni{/i}. I was about to do that but because I'm {i}such{/i} a {i}great{/i} friend, I remembered to give you the crisps you asked for, remember?! Also, I think you'll find our job description is to--"
    u "I know what our job description is, but the new guy doesn't and that's for Charis to explain. What your name anyways?"
    "'I'm [p]', you say."
    "Juniper reaches out to shake your hand. You see the tips of their medium brown hands fake to a rusted red color as if stained."
    j "That's a nice name. Nice to meet you, [p]. I'm Juniper. Anyways, we should take you to Charis. I'm sure he's already worrying."
    a "Yep, and that's your problem now, I've got shit to do; Bye!"
    "He starts to walk off, but Juniper grabs him by the scruff of his neck."
    "A noise of complain escapes him, but Juniper seems undeterred."
    j "Hey, I'm not dealing with them alone; we'll take you to Charis."
    "Alan grumbles in quiet protest, but the two lead you to Charis' desk."

    hide j basic with moveoutleft
    #hide a basic with moveoutright
    "As you approach, you see a space littered with books. A cat sits atop them looking at you with keen eyes."
    "You see a hunched over, pake figure wearing pale, silky robes. He seems to be older than the two you met previously, thought you can't say for sure."
    "He looks frail and weak, though the appearence isn't helped stoof near Juniper. He comes up to you."

    #show c at right with moveinright
    c "Hello, Im Charis. It is nice to meet you. I'll be taking care of you from now on."
    menu introC:
        "Greet him":
            "Hi, I'm [p]."
            c "Nice to meet you [p]"
        "Question him":
            p "Where am I and what's going on?"
            c "I am sure this is all confusing, but I'll answer in due time. I must first explain how we do things around here."
    "Charis pauses as if waiting for your other companions to leave the conversation, but he holds off asking them directly, instead opting to pick at his hands."
    menu stay:
        "Let the two stay":
            "You like having the other two. Charis doesn't interest you too much."
        "Don't say anything":
            "You want to hear Charis out, but don't want to get involved with the drama."
    "Charis lets out a sigh when the other two don't budge, resigned to have them spectate."
    return                                                                                                                                                                                                             