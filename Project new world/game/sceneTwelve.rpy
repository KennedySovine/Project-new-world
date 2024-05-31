$ jobLie = False;
$ briLie = False;

label sceneTwelve:
    "The journey into the realm of memories is much smoother this time. You are well experienced in this process by this point."
    "You decide to keep your eyes open this time, trying to decipher the quickly flashing images of the old world."
    "They flash faster and faster, and your mind suddenly twinges with a sharp pain. Memories flood in of the events taking place between this new scenario and the last one."
    "Usually, you are putting together the pieces of what had changed between the memory events. However, this time, the happenings after the prior and before the current are clear."
    "As you awaken, you appear to be sitting in a waiting room of a hospital building. The corridors are pretty sterile and clinical, and nurses in face masks are walking up and down the halls. "
    "Years have passed since your last case file, and in that time, things seem to have gotten much worse. All the dire happenings flood over you, and you take the time to process them."
    "Your dad's heath has sadly declined, and he is now hospitalised while the doctors continue to treat him as best as they can."
    "You've given up on any aspirations of going to university, instead getting a retail job to pay the bills. What about with Dad in the hospital? When he was out of the hospital, you had to become his carer."
    "Bri had disappeared from your life when she went to university herself; she had chosen to study medicine. And this choice had taken her far away, and she was far too busy lately."
    "Unfortunately, due to your exhaustion and poor mental health, your performance at work had dropped, and in turn, when the time to cut jobs came, yours was first on the chopping block."
    "Being currently unemployed, you are unsure if you'll be able to pay for the house expenses. You've desperately been trying to find another job, but so far, you haven't heard anything back."
    "This latter development is the most recent, meaning your dad doesn't know about it. He's surely got enough on his plate trying to fight this cancer… Should you tell him?"
    "The memories you've gained over the past few years tell you this is his ward, so surely it's logical to presume you are here to visit your dad."
    "As though to confirm your hypothesis, a nurse exits the room adjacent to your chair and turns to you."
    
    n "Sorry to keep you waiting; your father is ready for visitation now. If his pain spasms come back, I'm just down the hall in the C-1 room or press the red assistance button if I'm not there."
    "You look at your dad's room. He's in C-4. At least he has his own room. You figure your dad would appreciate having privacy during this tough time."
    n "He had a rough night yesterday, unfortunately, and so he's quite tired today, so try not to overwhelm him too much. He's really looked forward to seeing you though."
    n "I'll leave you be now; just remember C-4 if you need anything. Oh, and the kitchen room is just down the corridor to the right if you want to make any tea or get any biscuits."
    n "Just don't forget to make his tea too weak like Nurse Doris did the other week. I never heard the end of it!"
    "The lady laughs and heads off to the left of your dad's room. You are glad the staff are quite friendly, as since you've been so busy with working you haven't had much time to visit."
    "At least he had some friendly company during this whole ordeal. And even if the tea was weak, you knew your dad would appreciate the gesture and really take it in good grace."
    "You turn the handle of your dad's room. A wave of anxiety floods you, delving into all the things you've had to process so quickly, and now you may be asked about them by your dad."
    f "Hello bud… It's really good to see you! Sorry it took so long; Nurse Sarah was just getting me changed and cleaned up before you arrived. I just wish I could do it myself, to be honest."
    "You try to hide your shock at the appearance of the man laid out before you. He truly is all skin and bones. His face was so pale and gaunt, and his skin so frail and veiny."
    f "I appreciate everything they do, of course, but I just wish I could be independent again. I hate feeling like such a hindrance."
    "His voice is hollow, lacking its usual warm enthusiasm. It's rather croaky and hoarse. Cables are strapped all over his arms and head, feeding him blood and oxygen."
    "A monitor is beeping to the left of his bed, monitoring his vitals measured from the myriad cables snaking their way around his body."
    f "I wish I could go outside with you and get some fresh air. But hopefully, there will be time for that in the future."
    "You look out the window and are saddened to see that the only view from this third-floor window is the concrete tower of the ER building. There are no trees, no birds, no breeze."
    "You think back to how free you felt at the beach and at Pandistone Park. In stark contrast, this cramped, sanitised room felt like a prison. And you'd only been here a few minutes."
    "For your dad, it had been over a year. This was his life, these four walls and the company of nurses and doctors."
    "Instead of laying on a blanket, looking up to the birds, trees, and sky up above, your dad spent your birthday looking up at the blank white ceiling of the wardroom."
    f "That's enough about me, though; sorry to be such a downer. How have you been, kiddo?"
    "What do you tell him? He clearly has enough on his plate. But if you don't tell the truth and things get worse, you may lose the house. Where would you stay? Where would you go?"
    "Your dad's pretty much the only person you can confide in, especially with Bri being so distant. Surely, some fatherly advice could help, but is it best to tell him the truth?"
    f "You okay, bud? How's it been? Is that store manager still giving you grief?"

    menu jobHonest:
        "Tell him the truth":
            "You think about how best to deliver this unfortunate news. You consider if you should just lie, but you've always been honest with your dad; you can't stop now."
            p "Dad, the thing is… Frank… well Frank laid me off…"
            "Your dad seems confused. He takes a moment to process that statement and then asks you:"
            f "Wait, are you saying you lost the job?..."
            "His already pale face seems whiter than ever, and his eyes express a hint of fear. It's not too late to backtrack and lie to your dad. But should you continue telling the truth or peddle back?"

            menu jobTruthSub:
                "Double down and continue":
                    p "I'm sorry, Dad, but it's true. Jobs needed cutting from our store, and Frank decided to lay me off last week. I didn't want to text you about it as it would only worry you more."
                    p "That's why I decided I would tell you when I next saw you in person. I'm sorry…"
                    "Your dad reaches out and takes your hand as you sit down on the chair next to his bed."
                    f "It's okay… I know this is a scary situation, but we'll work out a way to get through it. I'm glad you were honest with me, bud. I'll try to think of some solutions before you leave today."
                    "The burden of the truth has now been lightened, and you are no longer feeling the guilt of keeping this to yourself."
                    f "For now, let's try to talk about something a bit more optimistic."
                    $ jobLie = False
                "Back peddle and lie":
                    p "Woah, Dad, don't worry. He laid me off from being a customer assistant. I'm still in the company; I just transferred to a different role… I'm on warehouse and backdoor duty now."
                    f "You had me scared there for a minute. I'm glad that wasn't the case; if you lost that job, we'd be in a real pickle. I just have to hang in there a bit longer till I get better."
                    "You feel awful about concealing the truth from your dad, but you can't deny being relieved to see the anxiety wash away from your dad's face."
                    p "Yeah, backdoor work sucks. Pulling all those cages is definitely going to do a number on my wrists and back, but a job, a job, as you always said."
                    f "Absolutely, and I couldn't be prouder of you for benching your own dreams to help through all this just for my benefit. I only wish I could help ease the burden."
                    "His words twist another dagger into your heart. You simply resolve yourself to remember that this sweet lie is for his benefit. What could he possibly do to help in his current state?"
                    f "Anyhow, let's not dwell on that awful job. Plenty of nicer things to catch up on, right, bud? "
                    $ jobLie = True
        "Lie about your job":
            "You compose the narrative for your tall tale in your head; provided you are confident in your execution, your dad will be none the wiser."
            p "These days, Frank's been a real nightmare. He's always on my case, saying I'm not pulling my weight or that I could be more efficient. You know how it is…"
            f "They're lucky to have you, really. With everything on your plate lately, I'm so proud of you for stepping up and dropping everything else to support us."
            "Your dad's words hit you hard. The truth is, Frank let you go last week. You're not supporting anything right now, and if things don't turn around soon, you could lose the house."
            p "I don't know what I'd do if I lost that job, Dad… What if I couldn't pay for the house?"
            "You hope that by posing the situation as hypothetical, you can garner your father's perspective on it without actually needing to disclose the truth to him."
            f "You don't need to worry about that kid. You've got that job. And so long as you do your best, you'll get through this. As soon as I'm better, I can start working again and ease that burden."
            menu jobLieSub:
                "Double down and continue":
                    p "Yeah, I suppose you are right. No need to worry about it now."
                    "You can't bring yourself to confess your lie. You allow your dad to live in a reality where the only thing he must worry about is getting better."
                    f "Absolutely, I know you are doing everything you can, and I couldn't be more proud bud. I'm glad I raised you right."
                    "Did he, though? Here, you are lying to your own dad to protect him from the harsh truth that he may have no home to return to."
                    "You remind yourself that in his current state, it would be selfish to dump all these worries and fears onto him, given everything else he's dealing with. He would understand."
                    "And if you get another job in time, he'll never have to know you lied… So long as you can get work before it's too late…"
                    $ jobLie = True
                "Come clean":
                    p "Dad… I didn't know how to tell you, but I lost my job."
                    "You try to word it as best as possible, but it's so hard to come clean to the man lying in the bed before you. He looks so puzzled at what you said."
                    f "Wait, I'm confused… Didn't you say Frank was just being harsh on you, or did he really fire you?"
                    "You compose yourself and take a deep breath…"
                    p "Not fired; he laid me off last week… Job cuts were needed, and mine was sacrificed. I didn't want to worry you. I've been looking for new work every day, I promise."
                    f "You didn't need to lie to me… It's okay to be honest with me, even if it's bad news… But this is an awful situation…"
                    "You aren't sure if your dad is bitter that you lied to him, but you at least feel clear in your conscience that you came clean from your lie before it was too late."
                    f "Give me some time to think about it, and maybe I can suggest some good ideas before you leave today. Try not to worry about it now, bud. We'll get through this."
                    $ jobLie = False
    
    "With the job discussion behind you, for now, your dad changes the topic to something he hopes would be more positive."
    f "So… How are things going with Bri and her university course? I bet she's missing you, being so far away. The next time she's back down, you should bring her over for a visit."
    "Of course, he accidentally mentions another sore spot, expecting it to be a positive topic compared to the job debacle."
    "In reality, you haven't heard from Bri for several months now. Your few messages over that period have been mostly ignored, and when answered, they were usually brief."
    "She's far away from here, with her other friends and has likely made new ones, too. She's busy with her studies, and you and your dad are, sadly, probably just a hazy memory right now."
    "You recollect your shared experiences with Bri and the past memories you relived. It was such a shame that your friendship seems to have fizzled out at this point."
    "You truly liked her. She was so adventurous and kind. The good times you had together were countless, and your dad was rather fond of her, too."
    "This truth isn't as heavy as the jobs, but still, should you tell it? Isn't it better to have your dad believe you and Bri have stayed in touch? Not have him worry about you being all alone?"

    menu briHonest:
        "Tell him you and Bri have lost touch":
            p "The truth is, Dad, I haven't heard from Bri for a long time now. I've tried to stay in contact, but we've kind of lost touch."
            f "You never told me that. I'm sorry I didn't know."
            p "Well, what with everything else we had to deal with I guess Bri just never came up. I'm sure she's doing fine, really; she's probably just busy with uni work and her other commitments."
            f "I hope so, but still… I would have hoped she'd still try to keep in touch, considering she knows everything you and I have been going through. I mean, her parents still live here."
            f "Surely she must visit during the half-terms?"
            "It's true; it's pretty bizarre that even during the uni breaks, you've never seen or heard from Bri despite her likely coming home to visit her mum and dad."
            p "I think her way of coping is to knuckle down and absorb herself in her studies. She really wants to help the world. I guess she just needs time to focus."
            f "I guess so, but it's still really sad to hear. Growing up, you two were inseparable. I hope you can fix things…"
            "You told your dad the truth. This one wasn't as hard to reveal, although part of you still wonders if it could have been better to just gloss over your loss of contact."
            $ briLie = False
        "Tell him Bir is doing well":
            "You consider what you might say had you and Bri stayed in touch better…"
            p "She's doing good. She's met lots of new people on her course, and she's getting on well with her flatmates."
            f "You had a chance to meet up recently. She must have been on a break from uni, right?"
            "This lie is a little harder to tell; it's one thing to presume how someone's doing, and it's another to fabricate your direct involvement with them."
            p "Yeah, we met up at the beach for some ice cream and chips about a month ago. She's just been so busy with uni work and other commitments. But she's doing well, really."
            $ briLie = True

            if not jobLie:
                f "Hey, if you and Bri are still close, then I'm sure her parents might be able to help you with your job situation. You could see if Bri's dad has any vacancies in his department."
                f "And if things get bad, I'm sure Mr. and Mrs. Foster would take you in. With Bri gone for uni, I'm sure they are lonely at the moment. I bet they wouldn't charge much rent."
                "Your lie about Bri leads your dad to suggest you're not sure you can follow through with it. Since you and Bri lost touch, you doubt her parents will be especially welcoming."
                p "I don't know, Dad; I think that might be a lot to ask of them. I'm sure they've got a lot to deal with before adding me to the equation."
                f "Nonsense, I'm good friends with them, after all. I can ring them first and go over the whole situation for you if you're worried about that?"

                menu briLieSub:
                    "Come clean":
                        p "Well, the truth is. I might have exaggerated how close Bri and I still are."
                        f "Did you have an argument?"
                        p "Not exactly… We just drifted apart, I guess. We lost touch…"
                        "Your dad seems perplexed that you would lie about something so simple."
                        f "There's no need to pretend everything is okay if it isn't. I just thought it could help with your job situation, but I guess if you and Bri aren't close anymore, that's a no-go."
                        f "Just promise to be honest with me from now on, okay?"
                        p "I promise…"
                        "But is this promise the truth? Or just another lie?"
                        $ briLie = False
                    "Deflect the phone call":
                        p "Nah, it's okay, Dad. I'll sort everything out. You just focus on getting better; no need to worry about me…"
                        f "If you are sure, bud. But I'll always worry about you. I can't help but worry about that. It's what dads do."
                        p "I appreciate it, Dad, and I really love you. I just want you to rest up and get better as soon as possible. I'll sort everything else out."
                        f "I love you too, kiddo. I'm glad you at least have some options now. I was so scared before."
                        "Truthfully, the Bri's family option isn't really viable given your loss of contact to Bri. But this lie at least eases your dad's fears for your well-being and safety. Surely that's a good thing?"
                        "Right?"
                        $ briLie = True
    
    "After addressing these two points of contention, you continue to talk with your dad about general things."
    "He asks how you've been eating and if you've watched anything good on TV; he also mentions all the things he'd like to do together once he gets out of the hospital."
    f "I don't want to die here…"
    "This comes out of nowhere and throws you slightly aback."
    f "I want to go to Pandistone Park again. I want to see the birds, see the sunrise… You'll go with me, won't you?"
    f "If they say I'm not going to make it… I'd like to go there with you… One last time…"
    f "Would you do that for me? Let me pass amongst the nature, where I can feel close to her again… Please don't let me die here alone…"
    "This request is very upsetting to you. Your dad is in no state to even get out of bed, let alone make his way to the park. It's simply impossible…"
    "What do you say? Do you agree to a request you most likely can never fulfil if his health declines? Or be honest and admit it's impossible and just hope for him to get better?"

    menu finalRequest:
        "Lie and tell him you will":
            p "You just keep in touch, okay… and if the nurse's verdict is that you only have a few days left… Well, I'll make sure to get you there, okay..."
            p "You'll get to that park… and you'll be with mum again… In the end, at least…"
            f "Thanks, bud. I can't wait to see it again, even if it is the last time."
            p "Don't talk like that; you could still get better. Let's hope for the best, hey?"
            f "Quite right, let's just wait and see. I'm glad you came here today, bud…"
            "The man smiles as he closes your eyes, and he seems at peace now. He seems to be drifting off to sleep, finally succumbing to the exhaustion he's endured."
            "It's true, you believe he will reunite with your mum in the end. But an afterlife version, not the one on earth. It just won't be possible; you hope he'll understand when the time comes."
            "This lie is kindness, the kind of lie that allows the flame of hope to continue to flicker, even if the absence of oxygen surrounding it means it will inevitably extinguish."
            "When that time comes, you will deal with the consequences, but for now, your guilt over your lie is outweighed by your dad sleeping contently, thanks to your actions."
            "As you let go of his hand. And begin to get ready to leave the room, time crawling to a halt. It's time to make a decision."
        "Turn him down":
            p "Dad… I can't make that promise… The condition you're in now. It wouldn't be possible. The nurses would never discharge you like this."
            p "And a wheelchair would never get you through the forest; I certainly wouldn't be able to carry you without hurting you."
            "You try to explain your reasoning with as much logic and facts as possible to convey your decision to decline his final request."
            f "Yes… I suppose it was a foolish idea… You're right…"
            "You feel as though you have shattered his hope of ever escaping this reality, closing in on him. You feel sick, but you could not lie about this to him. You believe a promise made must be kept."
            p "We'll go to the park, Dad, we will. When you get better, we'll go there, more than we did before. We'll appreciate every moment we get to live together."
            f "I hope that comes to pass… I'm so scared it won't, though…"
            p "We just need to have hope, Dad. The doctors and nurses are working around the clock to fight this thing. I'll visit as much as I can, too, to keep your spirits up!"

            if jobLie:
                f "I understand you are busy with your job, so don't worry about visiting every day. I'll bet you are as exhausted as I am."
                "He chuckles, though you both know he is far worse off than you are right now. And this job he's imagining you slaving away at doesn't even exist for you anymore."
            else:
                f "If you come over tomorrow, I can help you with your job search. We can use my laptop to browse the job sites. Once we send some more applications off, you'll feel a little better."
                "He smiles reassuringly; even though he has so much to deal with himself, he's still willing to use what little strength he has to help you. "

            if briLie:
                f "If you could bring Bri along with you next time, that would make me feel a lot better. Even if I can't see the woods, having her here would bring those happy memories back."
                f "She should be finishing for the year in a couple of weeks, so drop her a call and tell her your old man can't wait to catch up!"
                "You look away, realising your lie about Bri has seeded false hopes in your dad's mind. The way things are with Bri right now, you find it unlikely she would come…"
                p "If she's accessible at all, I'll try to make something possible. But no promises… "
            else:
                f "Please try and fix things with Bri if you can… I'd like to see her again, especially if I don't make a recovery…"
                p "Please don't talk like that dad…"
                f "But, if I don't… I'd like to see her again one last time. And I'd like to leave knowing you aren't alone in this world, bud. It's no secret that she's been your only real friend in life so far."
                "It's true; you've met other people at work and through school and even interacted with Bri's other friends on occasion. But those people have always been acquaintances at most."
                "The bond you had with Bri was unbreakable, or so you thought."
                if bracelet:
                    "You fiddle with the purple bracelet Bri gave you so long ago now that you have to make adjustments to it to ensure it still fits your arm as you grow."
                    "You wonder if Bri still wears the one you got… Hopefully, it's not too late to mend your relationship."
            
            "Your dad's eyes seem to be drooping, likely tired after having a rough night from the pain he endures."
            f "I'm feeling exhausted, bud. Do you mind if we call it there for today? I think I'm going to sleep for a bit before dinner if that's okay?"
            p "No worries, Dad, I'll pop by again as soon as I can."
            f "I love you, kid, and I always will."
            p "I love you too, Dad, always and forever."
            "As you let his hand go and his eyes fully shut, time seems to slow down, and you know where things are heading from here."
    
    "As your dad sleeps, the heart rate monitor beeps get longer until they resemble the continuous beep of a flatline. Your stomach twists with anxiety, but you know it's just time-stopping."
    "Soon, all sound halts, and any movement ceases. You are alone in the room now with a decision to make."
    "You hear the door handle rattling and jolt up, terrified that some presence is with you in this frozen world."
    "A nurse walks in with a clipboard, entirely ambivalent to the bizarre situation."
    n "Do you want to remove lies from the world?"
    "She speaks in an emotionless and level tone."
    "You realise that this nurse is this memory decision catalyst. She isn't an actual human, just a mechanism for retrieving your choice."
    "This whole memory was to test you on whether you would lie for your dad's sake or tell the truth but cause him more emotional pain and worry."

    menu removeLies:
        "Remove lies":
            "A world without lies could be better. People would always be honest with each other, no more secrets, no more guilt. Although it was hard to give your dad the honest truth, it was right."
            "Yet would it have been better to have told a sweet lie, or at least have the option available to do so when necessary? Some lies come from a place of kindness. To avoid causing pain."
            $ pCalm += 1
            $ lies = False
        "Keep lies":
            "A world needs lies. Sure, some lies are cruel and hurtful. Yet others are lies of kindness, much like those which eased the worries and fears of your dad."
            "Yet, lies cause so much pain. All the sneaky politicians, cheating spouses, and criminals who get away with the pain they cause through lying. Without lying, would things be better?"
            $ pChaos += 1
            $ lies = True