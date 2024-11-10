﻿# The script of the game goes in this file.

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
# For Chapter Selection
define persistent.chapter1 = False
define persistent.chapter2 = False
define persistent.chapter3 = False
define persistent.chapter4 = False
define persistent.chapter5 = False

# For Album Pictures
define persistent.storm = False

# For Unlocking Character Profiles
define persistent.aurora = False
define persistent.bellatrix = False
define persistent.ian = False
define persistent.mary = False
define persistent.noel = False
define persistent.aluna = False
define persistent.josh = False
define persistent.kurt = False
define persistent.jennie = False
define persistent.larry = False
define persistent.victoria = False
define persistent.nathan = False
define persistent.emma = False
define persistent.dylan = False
define persistent.corazon = False

# MC Powers/Game Conditions
define persistent.MC_power = False
define persistent.Play = False

#label splashscreen: # Intro before main menu
#    $ renpy.movie_cutscene('videos/splash.webm')
#    pause 2.0
#    return


label start():

    $ persistent.chapter1 = True
    $ persistent.Play = True

    $ persistent.aurora = True
    $ persistent.bellatrix = True


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

    # play music "soundofstorm.mp3"
    m "The sound of the storm is drowning out everything. It’s all so devastating."

    scene rooftop_view with dissolve
    "The entire city is submerged under floodwaters. Streets she once knew are now rivers, churning with debris—cars, broken furniture, and uprooted trees."
    "The water is everywhere, drowning everything in its path."

    # play music "criespeople.mp3"
    "Mari can hear the distant cries of people, their voices muffled by the roar of the storm."
    # show bg people on the roof
    "Some are clinging to rooftops, others are being swept away by the relentless current. The scene is one of utter devastation."
    # show bg room
    m "I’m back in my room, but that vision... it felt so real. "
    # show hands glowing
    m "My hands are glowing, but I don’t understand why.I can’t stay here; I have to get to the ESTIAI University building. It might be my only chance."
    # hide hands glowing

    # show mari gasping breath
    "The vision is so intense, so real, that it leaves Mari gasping for breath when it finally fades."

    m "I need to go back to my house!"

    # show bg city underflood
    scene stormWindow with fade
    "She’s back in her bedroom at her house, but the memory of the flooded city lingers in her mind, too vivid to ignore. "

    show mc_mari at center with dissolve # mari shock
    "She felt something in her hand"

    #scene glowing hand
    "She looks down at her hands, and to her shock, they’re glowing with a soft, eerie light."
    "She doesn’t understand what’s happening, but she knows one thing—she can’t stay here."
    # hide glowing hand
    
    #show bg room
    scene rooftop_rain_vision with dissolve
    show mc_mari at center with dissolve
    m "If the city is going to flood like in my vision"

    scene rooftop_rain with dissolve
    m "the ESTIAI University building might be the only place high enough to stay safe. I need to get out of here."
    
    #hide mari
    #show bg flooded
    scene rooftop_rain with dissolve
    "The memory of the ESTIAI University building, standing tall above the floodwaters, pulls her into action. 
    If the city is going to flood like in her vision, the ESTIAI University building might be the only place high 
    enough to stay safe."
    
    #show bg mari rushes out
    scene rainFlood with fade
    "She rushes out of her house, into the storm, the glow in her hands pulsing as if guiding her through the chaos."
    
    #show bg streets into rivers
    #show mari worried
    scene rainFlood with fade
    show mc_mari at center with dissolve #worried
    m "The streets are turning into rivers. The rain is relentless."
    #play music "peopleshouting.mp3"
    m "People are shouting, and the water is rising too quickly."
    m "I have to get through this chaos and make it to the university. I have to survive."

    scene rooftop_rain with fade
    "Outside, the world is already falling apart. The streets are turning into rivers, the rain coming down so hard it feels like it might tear through her skin."

    # play music "criespeople.mp3"
    "She can hear the cries of her neighbors, the panicked shouts of people trying to escape. But the water is rising fast, faster than anyone can react."

    # show bg streets into rivers
    # show mari worried
    scene rooftop_rain with fade
    show mc_mari at center with dissolve #worried
    m "Everything around me is destroyed—cars are half-submerged, power lines are sparking, and trees are uprooted. "
    m "This place is a nightmare. I need to get to my friends, but the storm is making it impossible."
    # hide mari worried

    #show bg mari fights through storm
    "As Mari fights her way through the storm, she sees signs of destruction everywhere—cars are half-submerged, their headlights flickering weakly in the water; 
    power lines are down, sparking dangerously; trees have been torn from the ground, their roots exposed like broken limbs. The world around her is a nightmare come to life."


    #show Aurora scared at right
    a "Mari! Over here! The water’s rising too fast! We’re trapped! Help us, please! We need to get out of here before it’s too late."

    #show Josh scared at left
    j "Mari, don’t give up on us! We’re stuck, and the water’s coming up so quickly. I don’t know how much longer we can stay here."
    
    #show Kurt scared at center
    k "Mari, hurry! The water’s getting higher, and it’s so cold. We’re losing our grip"

    #hide Aurora scared at right
    #hide Josh scared at left
    #hide Kurt scared at center

    #show bg Aurora_Josh_Kurt_Trap
    m "There they are—Aurora, Josh, and Kurt. "
    #show mari worried
    m "They’re trapped, and I can’t reach them."
    #show bg water_too_strong
    m "The water’s too strong."
    #show bg vision_Aurora_Josh_Kurt_swept
    m "Oh no, I see it again—the vision of them being swept away. I can’t let this happen."
    hide mari worried

    return 

