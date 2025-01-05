# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Minji")
define s = Character("Sooyoung")
define k = Character("Krystal")
define ku = Character("Kumi")
define hr = Character("Haerin")
define y = Character("Yujin")
define hs = Character("Haseul")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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

    hs "Excuse me- Krystal-ssi."
    k "Huh-"
    k "{i}Manager-nim taps a paper cup filled with tea. She clicks her tongue and holds it out again to me.{/i}"
    hs "Come on. Drink this."
    k "{i}It’s steaming. I suppose that’s one way to try and kill my jet lag.{/i}"
    k "Thank you…"
    k "{i}2 hours of sleep be damned. Hot tea is the worst kind of wake up alarm, yet also the most effective.{/i}"
    k "*gulp*"
    hs "Do you know what your schedule is for the day?"
    k "Yes, I had some time to review it during the taxi ride here."
    hs "Good. I’ll let you collect yourself for a moment, but I expect you to start training within 5 minutes."
    k "Sure, I can do that."
    k "{i}Typical Haseul. If our company was a ship, she would’ve easily been mistaken for the captain.{/i}"
    hs "Oh and Krystal."
    k "Yes?"
    hs "Welcome back."
    k "Thanks. It’s nice to see you again."
    k "{i}She only nods, ever the professional, before leaving me in the lobby on my own.{/i}"
    k "{i}5 more minutes…and then it’s time for regular life to leave my grasp once again.{/i}"

    # This ends the game.

    return
