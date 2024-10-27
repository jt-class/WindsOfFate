# The script of the game goes in this file.

# Chapter 0 - Prequel

# Declare characters used by this game. The color argument colorizes the name of the character.
# Siguro dito nalang naten idedefine isa-isa yung mga pangalan ng characters
define m = Character("Mari")
define a = Character("Aurora")
define j = Character("Josh")
define k = Character("Kurt")
define l = Character("Larry")

# Transitions
define blink = Fade(0.1, 0.05, 0.1, color="#000")

# Persistent/Flags - used for record the stats permanently or for unlocking/locking content.
define persistent.storm = False
define persistent.chapter1 = False
define persistent.aurora = False
define persistent.power = False

#label splashscreen: # Intro before main menu
#    $ renpy.movie_cutscene('videos/splash.webm')
#    pause 2.0
#    return


label start():

    $ persistent.chapter1 = True

    transform wakeup_blur: # Transitions # Blur the scene to indicate waking up in a daze
        xalign 0.5
        yalign 0.5
        pause 1.0  # Pause for 1 second to simulate waking up delay

    transform wakeup_focus: # Transition to simulate blinking and focusing slowly zoom out to represent focusing
        linear 1.0 zoom 1.0  
    
    # The game starts here.
    # play music ""
    scene Intro_BG1 with fade
    pause 3.5
    scene Intro_BG2 with fade 
    pause 3.5

    "This game is in work of progress, anything will be changed later on"

    # These display lines of dialogue.
    scene sleeping with fade
    "August 24, 2024 Mari Luzviminda, a 17-year-old girl from the Philippines"

    # Introduction # This shows a character sprite. A placeholder is used.
    scene blurred_room at wakeup_blur 
    "wakes in the middle of a violent super typhoon." 
    scene sleeping with blink
    scene room at wakeup_focus
    pause 2.0 
    scene sleeping with fade
    scene stormWindow

    "The wind howls like a living thing, and the rain lashes against her window with a force that makes the glass rattle."
    
    "The house around her groans as if struggling to stay together. Confused and frightened, 
    Mari stumbles out of bed, her heart pounding as she tries to make sense of the chaos."

    show mari_def with dissolve
    m " Oh no, what's happening? It feels like this storm will kill us all."
    m " The wind is howling so loud, and the house is shaking. I can’t believe how strong the rain is hitting the window."
    m " I have to get out of here!"

    # Choice Screen - When the player was given a choice, this will represent to.
    menu:
        "Leave":
            jump leave

        "Stay":
            jump stay


label leave:
    m "I want to get out of here"
    hide mari_def
    
    jump outside

label stay:
    m "I need to check something first"
    hide mari_def

    scene room_night with dissolve
    "As Mari descends to her parent's room... "

    show mari_def at right with dissolve
    m "Mom? Where are you?"
    " As the storm raging outside and her mom remains unseen..."
    m "Mom was not here, i have no choice but to go outside..."
    hide mari_def
    
    jump outside

label outside:

    scene rainFlood with fade
    "The storm outside is unlike anything she’s ever seen"
    "The world beyond her window is a blur of water and wind"
    
    # scene bg_bendingStructure
    "she can barely make out the shapes of buildings and trees bending under the force of the typhoon."
    # show mc_reachPhone
    show mari_def
    "She tries to reach for her phone, but there’s no signal, no way to call for help. A deep sense of dread settles in her stomach."

    m "I can’t see anything outside. It’s all just a blur of water and wind."
    m "I can't even reach my phone—there’s no signal. This dread... it's suffocating."
    m "I don’t know what to do. How can I call for help?"


    "As she stands frozen, trying to figure out what to do, something strange happens."

    "Her vision blurs and suddenly, she’s overwhelmed by a vivid image. A vision that feels too real to be just a figment of her imagination."
    hide ph with dissolve
    scene rooftop_rain_vision with dissolve
    "She sees herself standing on the rooftop of the ESTIAI University, the tallest structure in her city, which is now known as ESTIAI University."
    
    show mari_def at left with dissolve
    m "What is this?"
    m "My vision is blurring"

    scene rooftop_rain with dissolve
    m "and now I’m on the rooftop of the STI building"
    m "Is... this a dream?"
    m "The city is completely submerged. How could this happen?"

    show mari_def at center with dissolve
    "From this high vantage point, she looks out over the city of Dasmariñas, and what she sees makes her blood run cold."
    m "This is awful. The city is underwater, and there’s so much debris"
    m " People are drowning, clinging to rooftops, and being swept away."

    # play music ""
    m "The sound of the storm is drowning out everything. It’s all so devastating."

    scene rooftop_view with dissolve
    "The entire city is submerged under floodwaters. Streets she once knew are now rivers, churning with debris—cars, broken furniture, and uprooted trees."
    "The water is everywhere, drowning everything in its path."

    return