

# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mari")

image Intro_BG1 = "Transitions/Intro1.PNG"
image Intro_BG2 = "Transitions/Intro2.PNG"

image sleeping = "Backgrounds/bg black.png"
image blurred_room = "Backgrounds/bg blur ceilingbedroom.png"  # Blurred background
image room = "Backgrounds/bg ceilingbedroom.png"  # Clear background
image bedroom ="Backgrounds/bg bedroom with bed.png"
image storm = "Backgrounds/bg storm in window draw.png"
define blink = Fade(0.1, 0.05, 0.1, color="#000")

label splashscreen: # Intro before main menu
    $ renpy.movie_cutscene('videos/splash.webm')
    return


label start:

    transform wakeup_blur: # Transitions # Blur the scene to indicate waking up in a daze
        xalign 0.5
        yalign 0.5
        pause 1.0  # Pause for 1 second to simulate waking up delay

    # Transition to simulate blinking and focusing
    transform wakeup_focus:
        linear 1.0 zoom 1.0  # Slowly zoom out to represent focusing

    # The game starts here.
    scene Intro_BG1 with fade
    "An Unknown Studio Presents"
    scene Intro_BG2 with fade
    "Developed By Bachelor of Science in Information Technology 4.1C"

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
    "The wind howls like a living thing, and the rain lashes against her window with a force that makes the glass rattle."
    "The house around her groans as if struggling to stay together. Confused and frightened, 
    Mari stumbles out of bed, her heart pounding as she tries to make sense of the chaos."

    show mari freakout
    m "Oh no, what's happening? It feels like this storm will kill us all."
    m "The wind is howling so loud, and the house is shaking. I can’t believe how strong the rain is hitting the window."
    m " I have to get out of here!"

    # Choice 01 - When the player was given a choice, this will represent to.
    menu:
        "..."

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