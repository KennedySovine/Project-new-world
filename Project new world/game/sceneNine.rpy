include "characters.rpy"

label againstCharis:
    "As you fade back into reality, you hear a quiet sigh as footsteps approach you."
    c "Hello, [pName]. I'd like to talk to you for a moment."
    p "Sure Charis, what is it?"
    c "I am supposed to be impartial on these things. But I also want to help you create the best world you possibly can because I {i}know{/i} you can make something amazing."
    c "Have you gotten used to your job yet? Have you figured out how everything works?"

    menu usedJob:
        "Yes":
            pass
        "No":
            c "Ah, well, that may explain it…" 
            c "To remind you: you are here to make a new world and help us finalise some of the design aspects."
            c "To do so, you have those files. The decisions made in them determine what gets removed or kept… even if it probably should be maintained."
            "There was a hint of resentment laced in his tone. Clearly, he wasn't fond of that last one."
    
    c "I am curious to know, how do you envision your new world? What's lead you to the decisions you've made?"
    
    menu newWorldEnvision:
        "Chaos":
            p "I want a world full of chaos!"
            "Charis winces and starts to fidget with his hands on impulse. This was clearly not what he was hoping for."
            c "Is that your ideal world, one of chaos? Or are you just curious about what might happen and willing to play with the lives of others to fulfil that curiosity?"

            menu a:
                "Yes":
                    "Charis lets out a sigh and seems disappointed. You don't care an awful lot, though."
                    c "That is… regrettable to hear. I hope you can find the need for some peace in your world. It will help make everything smoother, surely… less dangerous."
                    c "I just wish this new world would be happy. I feel like a failure; though I didn't aid in designing the old, I have let it fall into this irreparable state. So please reconsider if that is worth it."
                    c "Please consider if all that pain and suffering and all the damage done will be worth the 'fun' you may get."
                    "Charis seems uncomfortable and rubs a hand over the back of his neck. He disapproves of your methods, though this is far from a surprise."
                    c "Well… if you do reconsider, I wouldn't mind getting to know you more in the future, but as it stands, I should really return to work."
                    "He doesn't give you time to respond and walks off."

                    "You remain unshaken and look at your desk. A new file, as always, though this one feels heavier. You inspect the cover, and it reads:"
                    "OW_NG_CASE-6_FR4UD"
                    "You notice that numbers have been skipped again. It doesn't matter, though, at this point, you know what to expect, the same life. With that, you open the file"
                    return
                "I'm just curious":
                    "He seems surprisingly forgiving of that and gives you a slight nod."
                    c "Understandable; we can all be curious. I know I have been before. Some scenarios I have lived and then replayed in my head, trying to figure out how it would end…"
                    c "Regardless, though, we must consider the authentic lives impacted by these, okay? These files will affect all residents of the new world, so don't treat this lightly, okay?"
                    c "Maybe try to pick the better option in future and simply dream of what the other option has in store. That can be equally as thrilling, I'm sure."
                    "You are a lot less sure."
                    c "Well… pick well in the future. I have other work to see to now."
                    "He gives a small wave, and you respond with the same before he ducks and walks away."
        "I want a world that's the same as the old.":
            c "Well, what would be the point in that? Aren't we trying to make a new one and improve it?"
            c "I'm sure you've seen some good in that world, believe me, but we must still be willing to innovate and expand. We must be willing to change, and this has all been for {i}nothing.{/i}"
            c "I can understand using the old one as a template, but we must make it better. Besides removing pain… that was important to that world, it kept things in check. Even if it feels terrible, it is essential."
            "He looks to you expectantly, hoping clearly for something, for some massive revelation. He doesn't seem to find it and looks away."
            c "Well… Just consider it, okay."
            c "If you strive too much for the old world, other gods may not take to you as kindly. We all want change here, and almost all of us do."
            "You cast your mind back to those you met at the start. Alan and Charis both seemed keener on change than you so that only left Juniper…"
            "Charis gives you a small wave and ducks out of your cubicle. You turn to your desk and see a new file. Something in it feels different; you pick it up, and it feels heavier. The cover reads:"
        "A world where most people are happy most of the time.":
            "Charis seems sympathetic to your goal. Any disappointment is replaced with pity."
            c "A noble goal… An excellent goal to strive for in many ways. But alas, I don't think you're going about it the right way…"
            c "To remove fear in striving for a happy world… Fear may be bad at the moment, but it can help lead to greater happiness."
            c "The pride in overcoming a fear… The relief of knowing it kept you safe and protected, that it kept you out of harm. All those things are important."
            "He pauses a moment and considers you closer."
            c "I am very familiar with fear… some days, my life is ruled by it..."
            "You hear a lick of resentment in his voice, but then a tiny smile covers his face."
            c "But it has its use, and I can still be happy with it, you, see? Anyway, I must return to work now… Make the right decision."
            c "He leaves quickly, his own fear overtaking in this scenario. You can't see how he wants this when it impacts him so clearly. Not that removing it will affect his fear."
            c "You look back at your desk and see a file. You touch it and wince a little. Something is different here. There's something strange with this one. You read the title:"
        "A perfect world, and everyone is always happy":
            "Charis pauses a moment. They had expectations, but clearly, that was not one."
            c "That is… optimistic, and I appreciate that you would strive for such. But in such a case, why would you remove fear?"
            c "There will always be those in your world willing to tarnish it and make it imperfect. Fear would have stopped them if applied correctly."
            c "I just hope you can achieve your goal with such a powerful tool in your power. To reach perfection, you must be willing to keep some things that, on the surface, may cause issues but will hold it all together."
            "You consider his words; your choice had seemed so simple when striving for perfection, as the rejection and pain from the fear had felt far from perfect."
            "He sees your contemplation and gives you a nod."
            c "I must return to work, do consider what I said."
            "With that, he leaves you with your thoughts, though you are distracted from them the moment you turn to your desk and a new file sits on the desk. There is a weight to it as you read:"
    jump SIXEND


label againstAlan:
    "Your vision fades back to the office. The journey had been getting smoother. Still, upon arrival, you immediately had a splitting headache."
    "You hear a voice yelling at you, seeming either angry or disappointed. You can't tell which one it is. You aren't sure which is worse."
    a "Christ, what a shit decision that w-"
    "Alan cuts himself off before taking a deep breath and a swig of whiskey from the bottle that he seems to have manifested out of the blue."
    "Alan continues talking but louder. He doesn't pause for anything, not even air, as you see his face turn as red as his hair."
    a "WHY WOULD YOU KEEP THAT DAMN TRAUMATIC feeling~~"
    "Alan loses his breath suddenly, takes another one in, and recovers quickly. He looks at you; the anger dissipates slightly, but the disappointment is clear as day."
    a "Okay, so basically, [pName], your job is to {i}improve{/i} the pre-current world, not make it worse and uh- wait, so why did you make that decision, to begin with now? I'm curious, no judgment-"
    "You feel like there is, in fact, some judgment as you justify your response."
    
    menu justifyAlan:
        "Fear is essential":
            p "I felt fear was an essential emotion to life. What if something is suspicious, and I need to think that it's a bad thing to do?"
            a "Dude, when has fear ever done {i}anything{/i} good for you?? The amount of times it's cost me friends and cute girls- dude, what is this logic- just- I'm having trouble understanding-"
            a "Fear just gets in the way of fun! Stops you meeting new people! Going on rollercoasters! Jumping into the ocean!"
            "You flinch a little at that. You're almost sure he doesn't know the entire contents of the file, but that still hit a bit too close to home."
            "I HATE fear! You can't make friends with it. It's so dull; how am I supposed to have fun with anxiety or fear holding me back??"
            "He composes himself a second when he looks at you and lets out a huff."
        "I thought it was important":
            a "I mean, dude, like, when has fear ever done anything good for you? Constantly weighing you down an' stopping you from doing fun stuff."
            a "Like you get invited somewhere cool, but your brain just freezes! There's no working with that, y’know…"
            "You pause a moment. After the last file, this was a thing you were {i}very{/i} aware of, you'd felt it, and it had eaten you up from the inside out."
            "Yet still, you saw a purpose for fear, even after all that."
        "Yeah, that was a bad call":
            a "Well, yeah, like, you know? Fear always stops people from doing fun stuff, so why'd you want that? Boring world if you ask me. Shame we can't go back now; you see the reason."
            a "Like, think about this what if you want to hang out with some people, but you just freeze? I'm sure you realise {i}now{/i}, but it's too little too late get your head screwed on right before the next one, alright?"
            "You knew all too well that feeling, wanting to do something, but you just can't. You were wishing you could go back, but it was too late now…"
    
    a "I mean, come on; this can't be something you wanna keep for the future, mate…"
    a "Fear just sucks the life out of you and kills all the joy in life."
    "You hear footsteps, and Alan pauses, both listening to the quiet shuffles that approach you. Charis rounds the corner and looks between the two of you. You wonder if he'll stand up to Alan."
    c "Alan, please don't give [pName] bad ideas…"
    a "Chary, why would you possibly think I'm giving them bad ideas? I only had good ones, and I never had a bad idea in my life."
    "Charis turns to you, clearly hoping to ignore Alan and seems pleased when he looks at you."
    c "[pName] just know I am glad; fear is an integral part of life to stop bad des-"
    a "Charis, I've got this sorted? Okay?"
    "He says in a condescending tone. The two stare at each other for a moment, both wanting nothing more than for the other to leave. Charis starts to pick at his hands and ducks his head."
    "He sighs, then walks off, gritting his teeth. Once he gets out of earshot, Alan turns his attention back to you."

    a "See, that right there is {i}fear!{/i}"
    a "He can't even tell me why fear is reasonable without showing fear, makes it damn hard for him, doesn't it??"
    "Alan says as he chuckles slightly. He looks at you like he's never seen anyone dumber."
    a "Look, just- don't do something stupid like that again, okay? If you keep messing up, we're gonna have a real hard time getting along with you and me."
    "You nod, wanting to get him off your back at this point."
    "You see his eyes linger at your desk for a moment, and you turn to see a new file, too."
    a "I dunno what that one is… but I trust you not to mess it up. Got it?"
    "His tone is dripping with threat, but he is also hidden somewhere where you hear some fear."
    "He stomps off, not waiting for an answer, his footsteps echoing as you turn back to the file."
    "You touch it, it feels different than the ones before; something about it feels off, and it's impossible to ignore. Still, you read the title:"
    jump SIXEND




label SIXEND:
    "OW_NG_CASE-6_HO4XES"
    "You notice that some numbers have been skipped, assuming this is the same life, of course, which at this point would only make sense."
    "You push that thought out of your mind for now and try to go back to the conversation you just had as you flip open the file."