# The script of the game goes in this file.

# characters
define m = Character("Minji")
define s = Character("Sooyoung")
define k = Character("Krystal")
define ku = Character("Kumi")
define hr = Character("Haerin")
define y = Character("Yujin")
define t = Character("Taeri")
define sw = Character("Sunwoo")
define hs = Character("Haseul")
define r = Character("Ricky")
define v = Character("Vera")
define j = Character("Jimin")

#relationship variables
default minji_rel = 40
default sooyoung_rel = 50
default kumi_rel = 50
default haerin_rel = 50
default yujin_rel = 60

#company_stats
default haseul_rel = 0
default haseul_break_choice = False

# The game starts here.

label start:
#Prologue : Opening Scene
    scene bg room
    show minji:
        fit "contain"
        xsize 500
        xalign 0.75
        yalign 0.05
    show krystal:
        fit "contain"
        xsize 500
        xalign 0.25
        yalign 0.05

    # These display lines of dialogue.

    hs "Excuse me- Krystal-ssi."
    k "Huh-"
    k "{i}Manager-nim taps a paper cup filled with tea. She clicks her tongue and holds it out again to me.{/i}"
    hs "Come on. Drink this."
    k "{i}It’s steaming. I suppose that’s one way to try and kill my jet lag.{/i}"
    k "Thank you…"
    k "{i}2 hours of sleep be damned. Hot tea is the worst kind of wake up alarm, yet also the most effective.{/i}"
    k "*gulp*"
    hs "Do you know what your schedule is for the day?"

menu:
    "Yes":
        jump openq_yes
    "No":
        jump openq_no

label openq_yes:
    $ haseul_impressed = True
    k "Yes, I had some time to review it during the taxi ride here."
    hs "Good. I’ll let you collect yourself for a moment, but I expect you to start training within 5 minutes."
    k "Sure, I can do that."
    jump openq_done

label openq_no:
    $ haseul_impressed = False
    k "Uhh…I don’t think so. Did you send it to me yesterday?"
    hs "Yes. Please check it on SuDaTalk before you go to the gym."
    hs "I know you just landed, but I expect you to put in the same effort as everyone else in today’s training."
    hs "Is that clear?"
    k "Yep, I understand."
    jump openq_done

label openq_done:
    k "{i}Typical Haseul. If our company was a ship, she would’ve easily been mistaken for the captain.{/i}"
    hs "Oh and Krystal."
    k "Yes?"
    hs "Welcome back."
    k "Thanks. It’s nice to see you again."

    scene bg room
    show krystal:
        fit "contain"
        xsize 500
        xalign 0.25
        yalign 0.05

    k "{i}She only nods, ever the professional, before leaving me in the lobby on my own.{/i}"
    k "{i}5 more minutes…and then it’s time for regular life to leave my grasp once again.{/i}"

#Prologue : Gym w/ Yujin
    scene bg room
    show krystal:
        fit "contain"
        xsize 500
        xalign 0.25
        yalign 0.05
    
    k "{i}Fitness is rather underrated in KPop.{/i}"
    k "{i}Sure dance practice and vocal sessions can knock the life out of you, but the workouts the company puts us through are something else.{/i}"
    k "{i}Maybe that’s just our company though, and their sadistic love of total body workouts.{/i}"
    k "{i}Already after my first set of side planks, everything in my body is on fire.{/i}"
    "Oh! You're back"

    show yujin:
        fit "contain"
        xsize 705
        xalign 0.85
        yalign 0.04
    
    k "Hey Yujin. Ya I just got back this morning."
    y "Wow. And Haseul’s already putting you to work like the rest of us."
    k "Guess...you could say that."
    k "Ai-…definitely didn’t miss these in Toronto."
    y "How long have you been here for?"
    k "Just started. You want to do the rest together?"
    y "Sure, I can join you for a few sets."
    k "{i}Yujin’s company makes the torture less apparent.{/i}"
    k "{i}Like me, she’s no stranger to these workouts, having been at the company just a few months longer than me.{/i}"
    k "{i}And while she might not look it, she could go toe to toe with anyone when it comes to her abs.{/i}"
    k "Come on, last crunch until you’re finished."
    y "*huffs*"
    k "Way to finish strong. Do you need your water?"
    y "No…I’m okay…"
    y "How…How do you still…have so much energy?"
    k "I don’t know if I’d call it that."
    k "If we weren’t on the ground right now I’d want to pass out."
    y "Well try and keep going. I think we have a few more ab exercises."
    k "Oh man. Definitely didn’t miss those."
    k "{i}Yujin just laughs. If this was arm day, it would be a totally different story.{/i}"
    k "{i}But I guess being able to lift 40 kilograms isn’t super helpful when it comes to dancing for up to 8 hours straight.{/i}"
#if possible, insert scene change here
    y "Oh. Did Haseul tell you the news?"
    k "Uhh, I don’t think so. What happened?"
    y "While you were gone, two new trainees joined the company."
    k "Huh. That’s surprising."
    k "{i}New trainees at Y-Squared are rare. Or at least, for me they are.{/i}"
    k "{i}I was the newest one who joined, and I’ve only been here for half a year.{/i}"
    k "Were there auditions while I was gone?"
    y "I don’t think so. Sooyoung was saying that they came from one of the Big 4, but you know how she can be with these things…"
    k "Ya. But it’s not impossible."
    k "Maybe Sajang-nim made a deal with one of the companies."
    y "Maybe."
    y "They moved into the dorm last week, but I haven’t had many chances to talk to them yet."
    y "Manager-nim told me that they’re supposed to join my vocal practices, but I guess that hasn’t happened yet."
    k "I’m sure we’ll get to know them eventually."
    k "Unless things have changed in two weeks, so many of our schedules are all of us together."
    y "That’s true."
    k "Is there anything else I should know?"
    y "No, that was it. I wish I could tell you more, but they weren’t really introduced to the rest of us."
    y "They just showed up to practice one day and Sajang-nim asked Sooyoung and Kumi to show them around."
    k "Huh…"
    k "Well now that I’m back, maybe we’ll get one."
    y "If you have that kind of power, can you ask manager-nim to cut down on my cardio?"
    k "Sure I’ll see what I can do."
    k "{i}Yujin laughs, shaking her head as she gets on her elbows to do a plank.{/i}"
    k "{i}Moments like these make sore knees and exhausted lungs worth it.{/i}"
    k "{i}They take the edge off of coming back from a pain-free stress-free break.{/i}"
    y "Okay. One last set?"
    k "Three more minutes of hell sounds doable."
    y "1, 2, 3. Up!"
#fade out

    # This ends the game.

    return
