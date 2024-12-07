# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mari")

define a = Character("Aurora")

define j = Character("Josh")

define k = Character("Kurt")

define l = Character("Larry")


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
    #Chapter 1 Introductions
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

    #this is an example for selection and it is not included in the story
    #cuz i want to know what are the processes of selections menu
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
    

    show Aurora scared at right
    a "Mari! Over here! The water’s rising too fast! We’re trapped! Help us, please! We need to get out of here before it’s too late."
   
    show Josh scared at left
    j "Mari, don’t give up on us! We’re stuck, and the water’s coming up so quickly. I don’t know how much longer we can stay here."
    
    show Kurt scared at center
    k "Mari, hurry! The water’s getting higher, and it’s so cold. We’re losing our grip"

    hide Aurora scared at right
    hide Josh scared at left
    hide Kurt scared at center

    show bg Aurora_Josh_Kurt_Trap
    m "There they are—Aurora, Josh, and Kurt. "
    show mari worried
    m "They’re trapped, and I can’t reach them."
    show bg water_too_strong
    m "The water’s too strong."
    show bg vision_Aurora_Josh_Kurt_swept
    m "Oh no, I see it again—the vision of them being swept away. I can’t let this happen."
    hide mari worried

    #idk what to do here and what to show 
    "he turns a corner and spots a group of her closest friends—Aurora Averill, Josh Majica, and Kurt Hendrix."
    "Relief floods through her, but it’s short-lived. They’re trapped, the water already up to their waists, and the current is too strong for them to move. "
    show bg mari_reaching_Aurora_Josh_Kurt
    "Mari tries to reach them"
    show bg mari_being_push_back
    "but the force of the water is overwhelming, pushing her back."
    
 
    show bg vision_dragged_underwater
    m "The vision is happening again. The water is rising, and they’re being dragged under."
    play music "peoplescream.mp3"
    show bg time_rewinding
    m "Their screams... I can hear them. I can’t save them. Time is rewinding, but it’s all playing out the same. Why can’t I change anything?"
    
    "Panic surges through her, and then, without warning, she has another vision."
    show bg water_surge_faster
    "She sees the water surge even higher, sweeping her friends off their feet, dragging them under."
    show bg people_disappear
    play music "people_scream_short.mp3"
    "Their screams for help are cut short as they disappear beneath the surface, swallowed by the flood."
    "The vision is so real, so immediate, that it leaves Mari reeling."

    show bg mari on the ground crying
    m "I failed. I saw the flood,I tried, but it wasn’t enough (sobbing). My friends are gone. I’m left here with nothing but this power that couldn’t help. I have to keep moving. I have to reach the university."
    show bg_friends_drowned
    "She loses hope all of to her friends as they drown in the abyss of the Flood"
    show bg_on_starcase_glowing_Hand
    "as she tried to reach to the top of the University the glow in her hands intensifies."
    show bg_mari_raise_hand
    "Instinctively, she raises her hand, willing herself to do something, anything, to save them."
    show bg_world with shaking
    play music "timerewinds.mp3"
    "The world around her shudders, and suddenly, time rewinds."
    show bg_before_surge
    "The water recedes slightly, and she’s back to a moment before the surge. But even with this second chance, she can’t reach them in time. "
    show bg vision_dragged_underwater
    "The scene plays out exactly as she saw it—her friends are swept away, their bodies disappearing into the dark, swirling water."
    show bg instrance_ESTIAI
    m "Finally, I’m at the university. The entrance is underwater, but I have to push through. I have to climb."

    show bg vision
    #idk what vision she was taking about it is about this friends that he didn't save or another vision
    "I can’t stop now. I need to get to the rooftop. I need to see if my vision was true."

    show bg mari_collapses_glowing_hand
    "Mari collapses to her knees"
    show bg mari_collapses_fading_hand
    "the glow in her hands fading as exhaustion and grief wash over her."

    #$ renpy.movie_cutscene('happinings.webm')
    #what if video nalang dito pakita or bg ground about dito?
    "The power to rewind time was real, but it wasn’t enough. Her friends are gone, lost to the storm, and she’s left alone in the rising water, their final screams echoing in her mind."

    show bg mari_on_rooftop
    m "I’m on the rooftop. The city is completely submerged. My friends are gone, my home is destroyed."
    show bg mari_looking_at_glowing_hand
    #pov sana kung meron dito
    m "This thing in my hand... What am I going to do now?"

    show bg mari_standing_up
    "Desperate and broken, Mari forces herself to her feet. She has to keep moving, has to survive, if only to make sense of what’s happening to her."
    show bg ESTIAI building
    "The vision of the ESTIAI University building, still standing above the flood, drives her forward."
    show bg mari_struggling_to_water
    "She stumbles through the water, each step harder than the last, as the storm continues to batter the city."
    show bg mari_on_rooftop
    "She finally reach the Top of the building, she sees all of the houses and people washed away by the flood and she is the only survivor"
    
    #idk what emotion should i put here
    show mari
    m "What is the reason why did you give me this vision??"

    #di ko alam kung ano yan
    show bg relapse
    show mari crying
    "crying as she remembers how her friends die drowning"


    #needed to fix

    #CHAPTER 1.2: 
    "The Butterfly’s Mask AUGUST 14,2024 ( A week before it happens) Exhausted, grief-stricken, and confused, Mari’s world fades to black as she loses consciousness."
    show rooftop with blink
    show classroom at wakeup_focus
    pause 2.0 
    scene classroom with fade
    scene classroom
    "When Mari awakens, she’s no longer on the rooftop. She’s back. she wakes up in the classroom where she sees her classmates and friends, she cant believe what she dream " 
    show mari confuse
    m "Where am I? Back in the classroom? It felt so real—was it just a dream or a mere Nightmare? a dream in another dream"
    show glowing hand
    m"but My hands still glow. I can’t stay here. I need answers. I need to figure out what’s happening to me."  
    hide glowing hand

    show bg pov_on_hands
    "She looks down at her hands, half-expecting the glow to be gone, but it’s still there, faint but undeniable. Panic sets in. She can’t stay here, not like this, not knowing what’s happening to her."
    show bg classmates_looking
    "Ignoring the curious glances of her classmates, including Victoria Viotto, Ian Trongcoso, Emma Pierce, and Dylan Piece, who are usually quick to bully her,"
    show bg mari_leaving_the_classroom
    "Mari bolts from the room, her mind reeling with the memories of the storm, the loss of her friends, and the terrifying power she doesn’t understand. "
    
    show mari worried
    m "I’m leaving. My classmates are staring, and I can’t explain this. I don’t understand what’s going on with me. I have to find out. I have to get out of here and find some answers." 
    
    show bg third_person_Classrooom
    "Larry Villarreal, her professor, watches in confusion as she flees, not knowing what to do. Larry Villarreal watched in confusion as Mari Luzviminda bolted from the classroom. His brow furrowed in concern. "
    show bg Classroom
    show Larry confuse
    l "What just happened?"
    l "Why did she run out like that?"
    l "Is everything alright?"

    show Larry worried
    "With a worried glance around the room, Larry began to gather his thoughts."
    show bg running_Mari
    "Meanwhile, Mari raced down the hallway, her heart pounding with a mix of fear and determination."
    show bg pov_stange_butterfly
    "The strange butterfly was still fluttering ahead of her, guiding her through the chaos in her mind."
    show mari worried
    m "I need to follow this butterfly. Maybe it’s leading me to something important."

    show bg_mari_entered_restroom
    "She followed the butterfly to the nearest restroom. "
    show bg_mari_restroom_hands_Flickered 
    "The faint glow in her hands flickered in the dim light. As she entered, she noticed the faucet over the sink. She turned it on, letting the water flow freely, creating a gentle but growing flood on the bathroom floor. "
    show bg_growing_flood_on_the_bathroom floor
    play music "running water"
    "The sound of the running water seemed to calm her racing thoughts"
    show bg_mari_worried_growing_flood_on_the_bathroom_floor
    "though the rising water was beginning to worry her. Mari watched as the water pooled around her feet, rising steadily."
    show bg_pov_batterfly_landed_on_mari_wrist
    "The butterfly landed delicately on her wrist"
    show bg_batterfly_landed_on_mari_wrist_flap_wings
    "its wings fluttering softly." 
    show bg_pov_batterfly_landed_on_mari_wrist
    "Mari stared in awe as the insect seemed to settle there, and with a sudden, inexplicable sensation" 
    show bg_pov_batterfly_landed_on_mari_wrist_become_tatto
    "a small blue butterfly tattoo appeared on her wrist, exactly resembling the one that had guided her. " 
    show mari confuse
    m "What is this? Why is this happening to me?"
    show bg_third_person_view_bathroom
    "Before she could fully grasp the significance of the tattoo, the restroom door swung open."
    show bg_third_person_view_bathroom_aurora_shock
    "Aurora Averill, running late, burst in, her eyes widening in shock as she saw the flooded restroom. " 

    #idk what emotion to put here
    show Aurora
    a "Mari, what’s going on? The water"

    show bg_third_person_view_bathroom_aurora_slipped
    "Aurora’s foot slipped on the wet floor, and she lost her balance."
    show bg_aurora_hit_head_head_the_floor
    "She fell hard, hitting her head against the tile with a sickening thud."
    show bg_aurora_body_on_the_floor
    "The impact was brutal, and Aurora lay unconscious, her body still and unmoving amidst the rising water. "
    show bg_mari_widened_eye
    "Mari’s eyes widened in horror as she witnessed the scene."
    show bg_mari_embrasing_aurora
    "The reality of Aurora’s death, the same death she had feared, hit her with a wave of helplessness."
    show mari worried
    m "No! Not again! I have to do something!"
    show bg_mari_embrasing_aurora_rasing_hand_with_the_tattoo
    "In a panic, she raised her hands, the glowing light intensifying as she desperately wished to undo the tragedy."

    #video pwede siguro add dito o e play?
    show bg_world_shimmered 
    "The world around her shimmered, and time began to rewind.The water receded, the butterfly vanished from her wrist, and Aurora’s body was lifted from the floor as if being pulled backward in time."
    show mari shock
    m "I can’t believe it’s happening again. Is this power really going to save her?"
    show bg classroom
    "Before Mari could fully comprehend the situation, she found herself back in the classroom, sitting at her desk."
    show bg clock
    "The clock ticked away, and everything seemed to have returned to normal."
    show bg Aurora_classmate
    "Aurora, along with her other classmates, was present, chatting and laughing as if nothing had happened. "
    show bg pov_hands
    "Mari looked down at her hands, no longer glowing, and saw that the tattoo had disappeared."
    show mari confuse
    m "Am I back in the classroom? Was it all just a dream? Did I really go back in time?" 
    show bg mari confuse
    "Confused and exhausted, Mari looked around the classroom, trying to piece together the fragments of her fragmented memories. The class continued as if nothing unusual had occurred."
    #yung camera angel pagmagtratransform na yung character sa anime
    show bg mari_close_up_face
    "Mari’s heart raced with the realization that she had somehow rewound time again, but the exact nature of her powers remained a mystery."
    show bg mari_calm
    "She took a deep breath, struggling to steady her nerves."
    show bg mari_determined
    "With a determined resolve, she knew she had to understand her abilities and what had led her to this point. She needed answers, and she couldn’t waste any more time." 
    show mari determined
    m "I need to find out what’s happening to me. I have to understand this power and what it means."
    #third person view sana
    show bg mari_Stood_up_from_her_desk
    "Determined to uncover the truth, Mari stood up from her desk, her mind racing with the possibilities of what lay ahead."
    #muka ni mari with classrooom bg na may upoan at lamesa nanaka tayo siya
    show bg mari_Stood_up_from_her_desk_face_
    "The classroom seemed oddly normal, but Mari was far from reassured."
    #video sana kung pede
    show bg past_exp
    "She had experienced a devastating glimpse into the future and managed to alter it, but the mystery of her powers was only beginning to unfold."
    show bg mari_left_classroom
    "As Mari left the classroom, she knew her journey was far from over.She had to delve deeper into the enigma of her abilities and uncover the truth behind the visions and the strange, glowing power she possessed."
    #when the main character do some moves in ending movies
    #like when the main character loss power
    #but on last seconds of the movie use power
    show bg mari_left_classroom_back_with_Glowing_hand
    "The path ahead was uncertain, but Mari was ready to face whatever challenges awaited her."

    return
    #The chapter ends with Mari fleeing the school, desperate for answers, and terrified of what she might discover.

    #Next is chapter 2

    # This ends the game.
label stay:
    show mari concern
    e "its better here to be safe from flying yero"

    return
