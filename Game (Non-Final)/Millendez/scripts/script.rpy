# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the name of the character.
define m = Character("Mari")
define blink = Fade(0.1, 0.05, 0.1, color="#000")
define persistent.storm = False

##label splashscreen: # Intro before main menu
##    $ renpy.movie_cutscene('videos/splash.webm')
##    pause 2.0
##    return

label start:

    transform wakeup_blur: # Transitions # Blur the scene to indicate waking up in a daze
        xalign 0.5
        yalign 0.5
        pause 1.0  # Pause for 1 second to simulate waking up delay

    transform wakeup_focus: # Transition to simulate blinking and focusing slowly zoom out to represent focusing
        linear 1.0 zoom 1.0  
    
    # The game starts here.
    scene Intro_BG1 with fade
    pause 3.5
    scene Intro_BG2 with fade
    pause 3.5

    # These display lines of dialogue.
    scene sleeping with fade
    "August 24, 2024 Mari Luzviminda, a 17-year-old girl from the Philippines"

    # Introduction # This shows a character sprite. A placeholder is used.
    scene blurred_room at wakeup_blur 
    "wakes in the middle of a violent super typhoon." 
    show sleeping with blink
    show room at wakeup_focus
    pause 2.0 
    scene sleeping with fade
    scene storm

    $ persistent.storm = True

    "The wind howls like a living thing, and the rain lashes against her window with a force that makes the glass rattle."
    "The house around her groans as if struggling to stay together. Confused and frightened, 
    Mari stumbles out of bed, her heart pounding as she tries to make sense of the chaos."

    show mari freakout
    m "Oh no, what's happening? It feels like this storm will kill us all."
    m "The wind is howling so loud, and the house is shaking. I can’t believe how strong the rain is hitting the window."
    m " I have to get out of here!"

    # Choice 01 - When the player was given a choice, this will represent to.
    menu:
        "Leave":

            jump leave

        "Stay":

            jump stay

label leave:
    show mari brave
    m "Mari has been freed from the wilderness"

    return # This ends the game.

label stay:
    show mari concern
    m "its better here to be safe from flying yero"

    return # This ends the game and will return to main menu.