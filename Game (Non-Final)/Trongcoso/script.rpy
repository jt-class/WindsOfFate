# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mari")

define a = Character("Aurora")

define j = Character("Josh")

define k = Character("Kurt")

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
    show mari freakout with dissolve
    m "Oh no, what's happening? It feels like this storm will kill us all."
    m "The wind is howling so loud, and the house is shaking. I can’t believe how strong the rain is hitting the window."
    m "I have to get out of here!"

    menu:
        "..."

        "Leave":

            jump leave

        "Stay":

            jump stay

            
label leave:
    show bg outside storm
    "The storm outside is unlike anything she’s ever seen"
    "The world beyond her window is a blur of water and wind"
    show bg bending structure
    "she can barely make out the shapes of buildings and trees bending under the force of the typhoon."
    show bg reach phone
    "She tries to reach for her phone, but there’s no signal, no way to call for help. A deep sense of dread settles in her stomach."
    show mari worried
    m "I can’t see anything outside. It’s all just a blur of water and wind."
    m "I can't even reach my phone—there’s no signal. This dread... it's suffocating."
    m "I don’t know what to do. How can I call for help?"

    show bg stand frozen in storm
    "As she stands frozen, trying to figure out what to do, something strange happens"
    "Her vision blurs, and suddenly"
    "she’s overwhelmed by a vivid image—a vision that feels too real to be just a figment of her imagination."
    "She sees herself standing on the rooftop of the ESTIAI University, the tallest structure in her city, which is now known as ESTIAI University."
    show mari Confused
    m "What is this?"
    m "My vision is blurring"
    show bg blurred STI
    pause 2.0 
    show bg roof top STI
    m "and now I’m on the rooftop of the STI building"
    m "Is this a dream?"
    m "The city is completely submerged. How could this happen?"

    show bg flooded
    "From this high vantage point, she looks out over the city of Dasmariñas, and what she sees makes her blood run cold."
    
    show mari worried
    m "This is awful. The city is underwater, and there’s so much debris"
    show bg disaster aftermat
    m " People are drowning, clinging to rooftops, and being swept away." 
    play music "soundofstorm.mp3"
    m "The sound of the storm is drowning out everything. It’s all so devastating."
    #fix sequence
    show bg city underflood
    "The entire city is submerged under floodwaters. Streets she once knew are now rivers, churning with debris—cars, broken furniture, and uprooted trees."
    "The water is everywhere, drowning everything in its path."
    play music "criespeople.mp3"
    "Mari can hear the distant cries of people, their voices muffled by the roar of the storm."
    show bg people on the roof
    "Some are clinging to rooftops, others are being swept away by the relentless current. The scene is one of utter devastation."
    show bg room
    m "I’m back in my room, but that vision... it felt so real. "
    show hands glowing
    m "My hands are glowing, but I don’t understand why.I can’t stay here; I have to get to the ESTIAI University building. It might be my only chance."
    hide hands glowing

    show mari gasping breath
    "The vision is so intense, so real, that it leaves Mari gasping for breath when it finally fades."
    show bg city underflood
    "She’s back in her bedroom at her house, but the memory of the flooded city lingers in her mind, too vivid to ignore. "
    
    show mari shock
    show glowing hand
    "She looks down at her hands, and to her shock, they’re glowing with a soft, eerie light."
    "She doesn’t understand what’s happening, but she knows one thing—she can’t stay here."
    hide glowing hand
   
    show bg room
    show mari
    m "If the city is going to flood like in my vision, the ESTIAI University building might be the only place high enough to stay safe. I need to get out of here."
    hide mari
    show bg flooded
    "The memory of the ESTIAI University building, standing tall above the floodwaters, pulls her into action. 
    If the city is going to flood like in her vision, the ESTIAI University building might be the only place high 
    enough to stay safe."
    show bg mari rushes out
    "She rushes out of her house, into the storm, the glow in her hands pulsing as if guiding her through the chaos."
    
    show bg streets into rivers
    show mari worried
    m "The streets are turning into rivers. The rain is relentless."
    play music "peopleshouting.mp3"
    m "People are shouting, and the water is rising too quickly."
    m "I have to get through this chaos and make it to the university. I have to survive."
    hide mari worried
        
    show bg streets into rivers
    "Outside, the world is already falling apart. The streets are turning into rivers, the rain coming down so hard it feels like it might tear through her skin."

    play music "cries_of_people.mp3"
    "She can hear the cries of her neighbors, the panicked shouts of people trying to escape. But the water is rising fast, faster than anyone can react."
        
    show bg streets into rivers
    show mari worried
    m "Everything around me is destroyed—cars are half-submerged, power lines are sparking, and trees are uprooted. "
    m "This place is a nightmare. I need to get to my friends, but the storm is making it impossible."
    hide mari worried
    
    show bg mari fights through storm
    "As Mari fights her way through the storm, she sees signs of destruction everywhere—cars are half-submerged, their headlights flickering weakly in the water; 
    power lines are down, sparking dangerously; trees have been torn from the ground, their roots exposed like broken limbs. The world around her is a nightmare come to life."
    
    show bg Aurora_Josh_Kurt_Trap
    show Aurora scared at right
    a "Mari! Over here! The water’s rising too fast! We’re trapped! Help us, please! We need to get out of here before it’s too late."
   
    show Josh scared at left
    j "Mari, don’t give up on us! We’re stuck, and the water’s coming up so quickly. I don’t know how much longer we can stay here."
    
    show Josh scared at center
    k "Mari, hurry! The water’s getting higher, and it’s so cold. We’re losing our grip"

    m "There they are—Aurora, Josh, and Kurt. They’re trapped, and I can’t reach them. The water’s too strong. Oh no, I see it again—the vision of them being swept away. I can’t let this happen."
    
    "he turns a corner and spots a group of her closest friends—Aurora Averill, Josh Majica, and Kurt Hendrix."
    "Relief floods through her, but it’s short-lived. They’re trapped, the water already up to their waists, and the current is too strong for them to move. "
    "Mari tries to reach them, but the force of the water is overwhelming, pushing her back."
    
    m "The vision is happening again. The water is rising, and they’re being dragged under. Their screams... I can hear them. I can’t save them. Time is rewinding, but it’s all playing out the same. Why can’t I change anything?"
    
    "Panic surges through her, and then, without warning, she has another vision."
    "She sees the water surge even higher, sweeping her friends off their feet, dragging them under."
    "Their screams for help are cut short as they disappear beneath the surface, swallowed by the flood."
    "The vision is so real, so immediate, that it leaves Mari reeling."

    m "I failed. I saw the flood,I tried, but it wasn’t enough (sobbing). My friends are gone. I’m left here with nothing but this power that couldn’t help. I have to keep moving. I have to reach the university."
    
    "She loses hope all of to her friends as they drown in the abyss of the Flood, as she tried to reach to the top of the University the glow in her hands intensifies."
    "Instinctively, she raises her hand, willing herself to do something, anything, to save them. The world around her shudders, and suddenly, time rewinds."
    "The water recedes slightly, and she’s back to a moment before the surge. But even with this second chance, she can’t reach them in time. "
    "The scene plays out exactly as she saw it—her friends are swept away, their bodies disappearing into the dark, swirling water."
   
    m "Finally, I’m at the university. The entrance is underwater, but I have to push through. I have to climb. I can’t stop now. I need to get to the rooftop. I need to see if my vision was true."
    
    "Mari collapses to her knees, the glow in her hands fading as exhaustion and grief wash over her."
    "The power to rewind time was real, but it wasn’t enough. Her friends are gone, lost to the storm, and she’s left alone in the rising water, their final screams echoing in her mind."

    m "I’m on the rooftop. The city is completely submerged. My friends are gone, my home is destroyed."
    m "This thing in my hand... What am I going to do now?"

    "Desperate and broken, Mari forces herself to her feet. She has to keep moving, has to survive, if only to make sense of what’s happening to her."
    "The vision of the ESTIAI University building, still standing above the flood, drives her forward."
    "She stumbles through the water, each step harder than the last, as the storm continues to batter the city."
    "She finally reach the Top of the building, she sees all of the houses and people washed away by the flood and she is the only survivor"
    
    m "What is the reason why did you give me this vision??"

    "crying as she remembers how her friends die drowning"
    return


    # This ends the game.
label stay:
    show mari concern
    e "its better here to be safe from flying yero"

    return
