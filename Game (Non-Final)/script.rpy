# Declare characters used by this game.
define m = Character("Mari", color="#ff9999")   # Mari Luzviminda
define a = Character("Aurora", color="#99ccff") # Aurora Averill
define j = Character("Josh", color="#a3c2ff")   # Josh, if Mari keeps her powers secret

# The game starts here.

label start:

    # Scene begins with Mari in the school hallway
    scene bg school_hallway with dissolve

    m "I have to talk to Aurora... I can't keep this secret any longer."

    "Mari stumbled through the school hallways, her thoughts swirling with confusion and fear. She had witnessed a terrible future and managed to rewind time, but the weight of this power was overwhelming."

    m "I need to find Aurora... she'll understand."

    # Transition to the meeting at the gazebo
    scene bg gazebo with fade

    "Mari found Aurora waiting at their usual spot – an old, secluded gazebo in the city park. It had always been a sanctuary for them, a place for shared secrets and solace."

    # Show Mari and Aurora sprites
    show mari neutral at left
    show aurora concerned at right

    a "Mari, what’s going on? I’ve been worried sick."

    "Mari’s gaze was intense as she struggled to find the right words. She knew this conversation would change everything."

    m "Aurora, there’s something I need to show you. It’s... it’s important!"

    # Presenting the decision to the player
    menu:
        "Tell Aurora about the power":
            $ mari_reveals_power = True

            m "I’ve discovered I can see glimpses of the future... and I can rewind time."
            
            a "You’re telling me that you can actually see the future and alter events?"

            m "Yes, but I know it sounds unbelievable. I need to show you how it works. Please, trust me."

            # Mari demonstrates her powers
            "Mari focused on a small stone lying on the ground, and with a wave of her hand, it levitated briefly before returning to its original place."

            a "This is incredible. I’ve never seen anything like it."

            m "There’s more. I can also rewind time. It’s... a bit more complicated."

            a "Rewind time? How does that even work?"

            "Mari picked up a small plant, dropped it, and then rewound time to see it gently return to its original state."

            a "So, you can actually go back and change things?"

            m "Yes, but it’s not always easy. I tried to save my friends before, but I couldn’t change everything. I thought that if I could understand this better, maybe I could make a difference."

            a "Mari, this is extraordinary. It’s also deeply unsettling. You need to be cautious with this ability."

            m "I know... I don’t fully control it yet. But I needed to show you, so you’d believe me."

            a "We’ll figure this out together. You’re not alone in this, Mari."

            "They sat in silence, the weight of Mari's revelation pressing down on them. The gazebo, once a place of comfort, now felt like a war room where something monumental was unfolding."

            jump next_scene

        "Keep the power secret for now":
            $ mari_reveals_power = False

            m "I can't tell you everything right now. Something strange is happening to me, Aurora."

            a "What do you mean? Is it something serious?"

            m "I don’t even know how to explain it. I just... I need more time to figure it out."

            a "Mari, you’re scaring me. You know you can trust me, right?"

            m "I do trust you... but I can’t say anything yet. Please, just give me some time."

            "Aurora’s face showed concern and confusion, but she nodded slowly."

            a "Alright, Mari. I’ll give you space, but promise me you’ll tell me when you’re ready."

            m "I promise."

            # Transition to Josh's curiosity
            scene bg school_hallway with dissolve

            "The next day, Mari noticed Josh watching her closely. She had always known him as Aurora’s friend, but lately, his curiosity seemed focused on her."

            j "Mari, are you alright? You’ve been acting strange lately."

            m "I’m fine, Josh. Just... a lot on my mind."

            j "If you ever need to talk, I’m here. Aurora’s worried about you, and so am I."

            "Mari tried to smile, but inside, the pressure of keeping her secret was building."

            jump next_scene

label next_scene:
    # End the scene or continue the story here
    scene bg room with fade

    "This is the end of the demo. More chapters to come!"

    return
