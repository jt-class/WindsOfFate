# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Mari")
label splashscreen:

    $ renpy.movie_cutscene('splash.webm')

    return
# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image sleeping = "bg black.png"  # Solid black screen
    image blurred_room = "bg blur ceilingbedroom.png"  # Blurred background
    image room = "bg ceilingbedroom.png"  # Clear background
    image bedroom ="bg bedroom with bed.png"
    image storm = "bg storm in window draw.png"

    define blink = Fade(0.1, 0.05, 0.1, color="#000")
    # Transitions
    # Blur the scene to indicate waking up in a daze
    transform wakeup_blur:
        xalign 0.5
        yalign 0.5
        pause 1.0  # Pause for 1 second to simulate waking up delay

    # Transition to simulate blinking and focusing
    transform wakeup_focus:
        linear 1.0 zoom 1.0  # Slowly zoom out to represent focusing
 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    scene sleeping 
    with fade
    "August 24, 2024 Mari Luzviminda, a 17-year-old girl from the Philippines"

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
    e "Oh no, what's happening? It feels like this storm will kill us all."
    e "The wind is howling so loud, and the house is shaking. I can’t believe how strong the rain is hitting the window."
    e " I have to get out of here!"

    menu:
        "..."

        "Leave":

            jump leave

        "Stay":

            jump stay

            
label leave:
    show mari brave
    "Mari has been freed from the wilderness"

    # This ends the game.
label stay:
    show mari concern
    "its better here to be safe from flying yero"

    return
