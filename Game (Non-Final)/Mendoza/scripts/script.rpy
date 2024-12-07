# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mari")
define a = Character("Aurora") 

# Chapter 5: Revelations/Exodus (Aurora's Path)
label start:

    scene stormy_sky with fade  #sky background filled with dark clouds
    "The sky churned like a living beast, casting deep shadows over Nectarville as the typhoon raged on." 

    scene rooftop with fade # bg for rooftop
    show Mari happy
    "Mari stood atop the roof of ESTIAI University, the tallest structure in the city, her hands glowing with the familiar yet terrifying power of time."
    "The wind howled, nearly drowning out the sounds of the floodwaters below, crashing through the streets and sweeping away everything in their path."

    show Mari happy at left with move
    show Aurora happy at right with dissolve
    "Beside her, Aurora watched the destruction unfold, her voice barely audible over the storm." 

    #Dialogue
    show Aurora displeased at right
    a "Mari, we have to do something! The city is going under.... This storm—it’s worse than anything we’ve ever seen."

    "Mari’s heart pounded in her chest. She had seen this moment countless times in her visions, and no matter how hard she tried, the future always brought her back to this rooftop, to this impossible choice. The weight of it was unbearable."

    show Mari shouting at left
    m "I’ve tried, Aurora. I’ve tried everything! No matter what I do, it all leads back here."
    a "(grabbing Mari’s arm)... You can’t give up! There has to be a way. You have the power, Mari. You just need to use it." 

    "Mari turned to Aurora, her best friend, the girl she loved more than anyone in the world. The thought of losing her was unbearable. But the thought of sacrificing everything else—the city, their friends—was just as devastating."
    
    show Mari scared at left
    m "(voice breaking)... But what if… what if I can’t? What if no matter what I choose, someone has to be lost?"
    show Aurora determined at right
    a "We’ll figure it out. You’re not alone in this."

    scene heavy_storm with fade
    "The storm’s fury seemed to intensify, the wind whipping around them as if urging Mari to act."

    scene flooded_city with fade
    "Below, the city of Nectarville was already submerged in places, the floodwaters climbing higher and higher, swallowing homes, cars, and lives."
    "She could hear the faint cries of the people trapped below, and her heart ached with the weight of their desperation."

    pause(0.5)

    scene rooftop with fade
    show Mari scared at left with dissolve
    m "It’s happening again. Just like in my vision… it’s all happening again."
    
    show Mari at center with move
    "She took a step back, her eyes scanning the horizon, the chaotic scene playing out before her exactly as she had seen it before."
    "The power in her hands surged again, the familiar pull of time beckoning her to rewind, to try again. But how many times had she tried? How many times had she failed to change the outcome?"

    hide Mari scared with dissolve
    show Aurora shouting at right with dissolve
    a "Mari, we’re running out of time! You can’t hesitate now!"

    show Mari scared at left with dissolve
    "Mari felt the pressure mounting. She knew Aurora was right—there was no more time to second-guess herself."
    "The storm was relentless, and soon the city would be completely submerged. She had to act, but every choice felt like a trap."

    m "(She looked into Aurora’s eyes, her heart breaking)... I’m scared."
    show Aurora comfort at right with dissolve
    a "I know. But you’re the only one who can stop this. You have to trust yourself."

    hide Mari scared with dissolve
    hide Aurora comfort with dissolve
    "Mari’s mind raced, the possibilities spinning around her. She could feel the weight of every decision pressing down on her—each choice pulling her in a different direction, each with its own devastating cost. No matter what she did, someone would pay the price."
    "She turned her gaze to the city, her chest tightening with the crushing reality of what was at stake. If she rewound time again, there was no guarantee she could save everyone."
    "And what if she couldn’t save Aurora?"
    "What if this was the last time she could even try?"

    show Mari whispering at center with dissolve
    m "(whispering)... How do I choose? How do I decide who to save?"

    "The glow in her hands intensified as her power reached its peak. She could feel the storm pushing back against her, a force of nature as unstoppable as time itself."
    "The wind howled, and the floodwaters surged higher. The city was slipping away, drowning beneath the weight of the storm."
    
    hide Mari whispering with dissolve
    pause(0.5)
    show aurora desparate with dissolve
    a "Mari, please! Whatever you’re going to do, do it now!" 

    scene bg with fade
    "The choice loomed before her, as vast and terrifying as the storm itself. Mari knew that this was it—the moment she had been dreading. She couldn’t rewind anymore. She couldn’t run from the decision."
    "She looked at Aurora, her heart breaking with the knowledge that whatever she did, someone would be lost."
    "The storm raged on, and in that moment, Mari made her final choice."

    menu:
        "Sacrifice Her Lover":
            jump lover
        "Sacrifice the Town":
            jump town 
        "Sacrifice Herself":
            jump herself

    # This ends the game.

label lover:
    "To be continued"
label town:
    "To be continued"
label herself:
    "To be continued"
    return

