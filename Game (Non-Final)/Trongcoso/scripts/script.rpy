# The script of the game goes in this file.

# Chapter 0 - Prequel

# Declare characters used by this game. The color argument colorizes the name of the character.
# Siguro dito nalang naten idedefine isa-isa yung mga pangalan ng characters
define m = Character("Mari")
define a = Character("Aurora")
define j = Character("Josh")
define k = Character("Kurt")
define l = Character("Larry")
define mom = Character("Mari’s Mom")

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
    hide mc_mari

    #show bg mari fights through storm
    "As Mari fights her way through the storm, she sees signs of destruction everywhere—cars are half-submerged, their headlights flickering weakly in the water" 
    "power lines are down, sparking dangerously trees have been torn from the ground, their roots exposed like broken limbs. The world around her is a nightmare come to life."


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
    show mc_mari at center with dissolve 
    m "They’re trapped, and I can’t reach them."
    #show bg water_too_strong
    m "The water’s too strong."
    #show bg vision_Aurora_Josh_Kurt_swept
    m "Oh no, I see it again—the vision of them being swept away. I can’t let this happen."
    hide mc_mari

    #idk what to do here and what to show 
    "she turns a corner and spots a group of her closest friends—Aurora Averill, Josh Majica, and Kurt Hendrix."
    "Relief floods through her, but it’s short-lived. They’re trapped, the water already up to their waists, and the current is too strong for them to move. "
    #show bg mari_reaching_Aurora_Josh_Kurt
    "Mari tries to reach them"
    #show bg mari_being_push_back
    "but the force of the water is overwhelming, pushing her back."
    
    show mc_mari at center with dissolve 
    #show bg vision_dragged_underwater
    m "The vision is happening again. The water is rising, and they’re being dragged under."
    #play music "peoplescream.mp3"
    #show bg time_rewinding
    m "Their screams... I can hear them. I can’t save them. "
    #play music "rewind.mp3"
    m "Time is rewinding, but it’s all playing out the same. Why can’t I change anything?"
    hide mc_mari

    "Panic surges through her, and then, without warning, she has another vision."
    #show bg water_surge_faster
    "She sees the water surge even higher, sweeping her friends off their feet, dragging them under."
    #how bg people_disappear
    #play music "people_scream_short.mp3"
    "Their screams for help are cut short as they disappear beneath the surface, swallowed by the flood."
    "The vision is so real, so immediate, that it leaves Mari reeling."

    show mc_mari at center with dissolve #sad?
    #show bg mari on the ground crying
    m "I failed. I saw the flood,I tried, but it wasn’t enough (sobbing). My friends are gone. I’m left here with nothing but this power that couldn’t help. I have to keep moving. I have to reach the university."
    hide mc_mari
    #show bg_friends_drowned
    "She loses hope all of to her friends as they drown in the abyss of the Flood"
    #show bg_on_starcase_glowing_Hand
    "as she tried to reach to the top of the University the glow in her hands intensifies."
    #show bg_mari_raise_hand
    "Instinctively, she raises her hand, willing herself to do something, anything, to save them."
    #show bg_world with shaking
    #play music "timerewinds.mp3"
    "The world around her shudders, and suddenly, time rewinds."
    #show bg_before_surge
    "The water recedes slightly, and she’s back to a moment before the surge. But even with this second chance, she can’t reach them in time. "
    #show bg vision_dragged_underwater
    "The scene plays out exactly as she saw it—her friends are swept away, their bodies disappearing into the dark, swirling water."
    #show bg instrance_ESTIAI
    show mc_mari at center with dissolve
    m "Finally, I’m at the university. The entrance is underwater, but I have to push through. I have to climb."
    hide mc_mari
    #show bg vision
    #idk what vision she was taking about it is about this friends that he didn't save or another vision
    "I can’t stop now. I need to get to the rooftop. I need to see if my vision was true."

    #show bg mari_collapses_glowing_hand
    "Mari collapses to her knees"
    #show bg mari_collapses_fading_hand
    "the glow in her hands fading as exhaustion and grief wash over her."

    #$ renpy.movie_cutscene('happinings.webm')
    #what if video nalang dito pakita or bg ground about dito?
    "The power to rewind time was real, but it wasn’t enough. Her friends are gone, lost to the storm, and she’s left alone in the rising water, their final screams echoing in her mind."
    
    show mc_mari at center with dissolve #sad?
    #show bg mari_on_rooftop
    m "I’m on the rooftop. The city is completely submerged. My friends are gone, my home is destroyed."
    #show bg mari_looking_at_glowing_hand
    #pov sana kung meron dito
    #show mc_mari at center with dissolve #concern?
    m "This thing in my hand... What am I going to do now?"
    hide mc_mari

    #show bg mari_standing_up
    "Desperate and broken, Mari forces herself to her feet. She has to keep moving, has to survive, if only to make sense of what’s happening to her."
    #show bg ESTIAI building
    "The vision of the ESTIAI University building, still standing above the flood, drives her forward."
    #show bg mari_struggling_to_water
    "She stumbles through the water, each step harder than the last, as the storm continues to batter the city."
    #show bg mari_on_rooftop
    "She finally reach the Top of the building, she sees all of the houses and people washed away by the flood and she is the only survivor"
    
    #idk what emotion should i put here
    #show mari
    show mc_mari at center with dissolve #sad
    m "What is the reason why did you give me this vision??"
    hide mc_mari

    #di ko alam kung ano yan
    #show bg relapse
    #show mari crying
    "crying as she remembers how her friends die drowning"



    #needed to fix

    #CHAPTER 1.2: 
    "The Butterfly’s Mask AUGUST 14,2024 ( A week before it happens) Exhausted, grief-stricken, and confused, Mari’s world fades to black as she loses consciousness."
    
    scene blurred classroom at wakeup_blur 
    scene sleeping with blink
    scene classroom at wakeup_focus
    pause 2.0 
    scene sleeping with fade
    scene classroom
    "When Mari awakens, she’s no longer on the rooftop. She’s back. she wakes up in the classroom where she sees her classmates and friends, she cant believe what she dream " 
    #show mari confuse
    show mc_mari at center with dissolve
    m "Where am I? Back in the classroom? It felt so real—was it just a dream or a mere Nightmare? a dream in another dream"
    #show glowing hand
    m"but My hands still glow. I can’t stay here. I need answers. I need to figure out what’s happening to me."  
    #hide glowing hand
    hide mc_mari

    #show bg pov_on_hands
    "She looks down at her hands, half-expecting the glow to be gone, but it’s still there, faint but undeniable. Panic sets in. She can’t stay here, not like this, not knowing what’s happening to her."
    #show bg classmates_looking
    "Ignoring the curious glances of her classmates, including Victoria Viotto, Ian Trongcoso, Emma Pierce, and Dylan Piece, who are usually quick to bully her,"
    #show bg mari_leaving_the_classroom
    "Mari bolts from the room, her mind reeling with the memories of the storm, the loss of her friends, and the terrifying power she doesn’t understand. "
    
    show mc_mari at center with dissolve
    #show mari worried
    m "I’m leaving. My classmates are staring, and I can’t explain this. I don’t understand what’s going on with me. I have to find out. I have to get out of here and find some answers." 
    
    #show bg third_person_Classrooom or the classroom_frontDesk.png
    scene frontdesk
    "Larry Villarreal, her professor, watches in confusion as she flees, not knowing what to do. Larry Villarreal watched in confusion as Mari Luzviminda bolted from the classroom. His brow furrowed in concern. "
    #show bg Classroom
    #show Larry confuse
    l "What just happened?"
    l "Why did she run out like that?"
    l "Is everything alright?"

    #show Larry worried
    "With a worried glance around the room, Larry began to gather his thoughts."
    hide frontdesk
    #show bg running_Mari
    scene hallway
    "Meanwhile, Mari raced down the hallway, her heart pounding with a mix of fear and determination."
    #show bg pov_stange_butterfly
    "The strange butterfly was still fluttering ahead of her, guiding her through the chaos in her mind."
    
    menu:
        "..."
        "Follow the Butterfly":

            jump Follow

        "Ignore":

            jump Ignore

    return 


#decision 1
label Follow:
    #show mari worried
    scene school_hallway
    show mc_mari at center with dissolve
    m "I need to follow this butterfly. Maybe it’s leading me to something important."
    hide mari_def
    #show bg_mari_entered_restroom
    "She followed the butterfly to the nearest restroom. "
    #show bg_mari_restroom_hands_Flickered 
    "The faint glow in her hands flickered in the dim light."
    hide hallway
    #temporary scene
    scene restroom
    "As she entered, she noticed the faucet over the sink. She turned it on, letting the water flow freely, creating a gentle but growing flood on the bathroom floor. "
    #show bg_growing_flood_on_the_bathroom floor
    #play music "running water"
    "The sound of the running water seemed to calm her racing thoughts"
    #show bg_mari_worried_growing_flood_on_the_bathroom_floor
    "though the rising water was beginning to worry her. Mari watched as the water pooled around her feet, rising steadily."
    #show bg_pov_batterfly_landed_on_mari_wrist
    "The butterfly landed delicately on her wrist"
    #show bg_batterfly_landed_on_mari_wrist_flap_wings
    "its wings fluttering softly." 
    #show bg_pov_batterfly_landed_on_mari_wrist
    "Mari stared in awe as the insect seemed to settle there, and with a sudden, inexplicable sensation" 
    #show bg_pov_batterfly_landed_on_mari_wrist_become_tatto
    "a small blue butterfly tattoo appeared on her wrist, exactly resembling the one that had guided her. " 
    #show mari confuse
    show mc_mari at center with dissolve
    m "What is this? Why is this happening to me?"
    hide mari_def
    #show bg_third_person_view_bathroom
    "Before she could fully grasp the significance of the tattoo, the restroom door swung open."
    #show bg_third_person_view_bathroom_aurora_shock
    "Aurora Averill, running late, burst in, her eyes widening in shock as she saw the flooded restroom. " 

    #idk what emotion to put here
    #show Aurora
    a "Mari, what’s going on? The water"

    #show bg_third_person_view_bathroom_aurora_slipped
    "Aurora’s foot slipped on the wet floor, and she lost her balance."
    #show bg_aurora_hit_head_head_the_floor
    "She fell hard, hitting her head against the tile with a sickening thud."
    #show bg_aurora_body_on_the_floor
    "The impact was brutal, and Aurora lay unconscious, her body still and unmoving amidst the rising water. "
    #show bg_mari_widened_eye
    "Mari’s eyes widened in horror as she witnessed the scene."
    #show bg_mari_embrasing_aurora
    "The reality of Aurora’s death, the same death she had feared, hit her with a wave of helplessness."
    #show mari worried
    show mc_mari at center with dissolve #freakout?
    m "No! Not again! I have to do something!"
    hide mari_def
    #show bg_mari_embrasing_aurora_rasing_hand_with_the_tattoo
    "In a panic, she raised her hands, the glowing light intensifying as she desperately wished to undo the tragedy."

    #video pwede siguro add dito o e play?
    #how bg_world_shimmered 
    "The world around her shimmered, and time began to rewind.The water receded, the butterfly vanished from her wrist, and Aurora’s body was lifted from the floor as if being pulled backward in time."
    #show mari shock
    show mc_mari at center with dissolve #shokt?
    m "I can’t believe it’s happening again. Is this power really going to save her?"
    hide mari_def
    hide restroom
    scene classroom
    "Before Mari could fully comprehend the situation, she found herself back in the classroom, sitting at her desk."
    #show bg clock
    "The clock ticked away, and everything seemed to have returned to normal."
    #show bg Aurora_classmate
    "Aurora, along with her other classmates, was present, chatting and laughing as if nothing had happened. "
    #show bg pov_hands
    "Mari looked down at her hands, no longer glowing, and saw that the tattoo had disappeared."
    #show mari confuse
    show mc_mari at center with dissolve #confuse
    m "Am I back in the classroom? Was it all just a dream? Did I really go back in time?" 
    hide mari_def
    #show bg mari confuse
    "Confused and exhausted, Mari looked around the classroom, trying to piece together the fragments of her fragmented memories. The class continued as if nothing unusual had occurred."
    #yung camera angel pagmagtratransform na yung character sa anime
    #show bg mari_close_up_face
    "Mari’s heart raced with the realization that she had somehow rewound time again, but the exact nature of her powers remained a mystery."
    #show bg mari_calm
    "She took a deep breath, struggling to steady her nerves."
    #show bg mari_determined
    "With a determined resolve, she knew she had to understand her abilities and what had led her to this point. She needed answers, and she couldn’t waste any more time." 
    #show mari determined
    show mc_mari at center with dissolve #determine
    m "I need to find out what’s happening to me. I have to understand this power and what it means."
    hide mari_def
    #third person view sana
    #show bg mari_Stood_up_from_her_desk
    "Determined to uncover the truth, Mari stood up from her desk, her mind racing with the possibilities of what lay ahead."
    #muka ni mari with classrooom bg na may upoan at lamesa nanaka tayo siya
    #show bg mari_Stood_up_from_her_desk_face_
    "The classroom seemed oddly normal, but Mari was far from reassured."
    #video sana kung pede
    #show bg past_exp
    "She had experienced a devastating glimpse into the future and managed to alter it, but the mystery of her powers was only beginning to unfold."
    #show bg mari_left_classroom
    "As Mari left the classroom, she knew her journey was far from over.She had to delve deeper into the enigma of her abilities and uncover the truth behind the visions and the strange, glowing power she possessed."
    #when the main character do some moves in ending movies
    #like when the main character loss power
    #but on last seconds of the movie use power
    #hallway nalang siguro
    #show bg mari_left_classroom_back_with_Glowing_hand
    "The path ahead was uncertain, but Mari was ready to face whatever challenges awaited her."
    hide classroom #change if meron na assets

    return

#decision 2
label Ignore:

# "DECISION 2: JOSH PATH TO MARI Context: (She will see the butterfly but she will not mind it, then if she doesn't go to the comfort room or restroom aurora will not see her and later on die): 
# and josh will ask her whats wrong (Josh path), she will flee the room to go home but along the way she will see the butterfly again and that's the time the butterfly will unified with her, 
# she will lost consciousness and when she wakes up she is in her room and her mom will said that Josh brought her home cause he sees her lying on the street, going home) 
# The chapter ends with Mari fleeing the school, desperate for answers, and terrified of what she might discover. SCRIPT Mari’s head spins as she sits in the classroom, 
# heart pounding, her hands faintly glowing. The classroom is alive with chatter, but all she can think of is the vision—the storm, the loss, the glow."

    #Mari (internally)
    scene classroom
    show mc_mari at center with dissolve #angry?
    m "That vision… What’s happening to me? My hands are still glowing. I need answers. I need to figure out what’s going on, but I can’t focus here."
    hide mc_mari
    "A butterfly flutters into her field of vision, just like before. But this time, she hesitates, eyes lingering on it."

    #Mari (internally)
    show mc_mari at center with dissolve #angry?
    m "No… I won’t follow it this time. I need to keep my head clear."
    hide mc_mari
    "Instead of leaving, she stays at her desk, gripping its edges as the butterfly flits past her. She watches it disappear down the hall but forces herself to stay put."

    "Josh Reyes, who sits a few seats away, notices Mari’s tension. Concerned, he walks over and kneels beside her desk."
    
    #show josh concern at right with dissolve
    j "Mari, are you okay? You look like you’ve seen a ghost. What’s going on?"

    #Mari (anxious, trying to dismiss him):
    #show mari anxious at left with dissolve
    show mc_mari at center with dissolve
    m "Nothing, Josh. I’m fine, I just… need a moment."
    hide mc_mari
    #Josh (persistent)
    #show josh presistent at right with dissolve #presistent or worried?
    j "Come on, Mari. I know when something’s wrong. You’re shaking. You don’t have to pretend."

    #scenes
    "Mari tries to brush him off, but Josh isn’t budging. She glances at him, her breath catching as flashes of her vision return—the storm, the destruction, Aurora’s death."

    #Mari (softly, overwhelmed)
    #show mari overwhelmed at left with dissolve
    show mc_mari at center with dissolve
    m "I don’t understand it, Josh. Something’s wrong with me… I keep seeing things that haven’t happened yet… but they feel so real. And… my hands…"
    hide mc_mari
    #he looks down at her hands, the glow now fading. Josh’s eyes widen in confusion but also concern. OUTSIDE. SCHOOL GROUNDS – DAY
    hide classroom
    scene street_home
    "Mari bursts through the school doors and sprints out onto the street. Her breath comes in short gasps as she runs. She doesn’t know where she’s going—only that she needs to escape."
    "As she turns a corner, the world blurs around her. She feels the pressure building inside, a mix of fear and exhaustion. Her mind flashes back to the vision of the storm, her friends' faces, and the glow of her hands."

    #Mari (internally, panicking)
    #show mari panicking at left with dissolve
    show mc_mari at center with dissolve
    m "What is happening to me? Why can’t I stop seeing it? Why can’t I stop seeing it?"
    hide mc_mari
    #show bg mari going home
    "She slows down, her breath shaky. As she continues walking home, a familiar flicker of movement catches her eye."
    #show bg mari going home with butterfly
    "The butterfly—the same one she ignored earlier—reappears, its wings shimmering in the evening light. It hovers in front of her, as if waiting for her to follow."

    #Mari (internally, confused)
    #show mari confused with dissolve
    show mc_mari at center with dissolve
    m "You again… but why? What do you want from me?"
    hide mc_mari
    #
    "This time, she can’t resist. She reaches out to it, and the butterfly flutters closer, landing gently on her arm. Her skin tingles as it crawls onto her wrist. Before she can react, the butterfly dissolves into her skin, sending a wave of dizziness through her body."
    
    show street_home with blink
    show street_home at wakeup_focus
    pause 2.0 
    scene street_home with fade
    scene blink
    show mc_mari at center with dissolve
    m "No… not again…"
    hide mc_mari
    #show road with blink
    #show road at wakeup_focus
    "The world spins, and her legs buckle beneath her. She collapses onto the sidewalk, the last thing she sees being the butterfly’s glow fading as everything goes black."
    #scene black

    #IN. MARI’S BEDROOM – NIGHT
    #show bg evening sun casting
    "Mari awakens in her bed, the faint glow of the evening sun casting soft shadows across her room. Her head feels heavy, but the first thing she notices is the absence of the glowing hands. She’s safe. She’s home."

    "Before she can process how she got there, her mother walks in, a worried look on her face."
    
    #Mari’s Mom (relieved)
    #show mari's mom happy at right with dissolve
    mom "Mari, you’re awake! I was so worried."

    #Mari (groggy, confused)
    #show mari confuse at left with dissolve
    m "Mom… how did I get here? I was… on the street…"

    #Mari’s Mom (sitting beside her)
    #show bg mari and mom at bed?
    mom "osh brought you home. He found you unconscious on the way and carried you all the way here. He said you fainted."

    "Mari blinks, trying to remember. The last thing she recalls is the butterfly and then… nothing."

    #Mari (quietly, to herself)
    m "Josh… he brought me home…"

    #show bg mari's mom brushes her hair?
    "Her mother brushes a strand of hair from Mari’s face, concern still lingering in her eyes."

    #Mari’s Mom (gently)
    mom "Do you want to talk about what happened? You scared me, Mari."

    #Mari (shaking her head, still processing):
    #show idk
    m "I don’t know, Mom. I just… I need to figure it out."

    "Her mother nods, giving her a comforting pat on the hand."
    #show mari's mom at right with dissolve
    mom "Alright, sweetie. Just rest for now. We can talk later."

    "As her mother leaves the room, Mari lies back on the pillow, staring at the ceiling. Her mind races with questions about the butterfly, her powers, and why everything feels so strange. She glances down at her wrist, half-expecting the butterfly tattoo to reappear, but there’s nothing."

    #Mari (determined, quietly)
    #show mari at left with dissolve
    m "I need answers. I can’t keep running."

    #wake up backwards function?
    "She closes her eyes, exhaustion pulling her into sleep once more. But this time, she knows her journey for the truth has only just begun."
    return
