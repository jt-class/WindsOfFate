label chapter5:
    
    scene rainFlood with fade
    "The storm raged on, and in that moment..."
    
    show mari_def with dissolve
    "Mari made her final choice. Without a second thought, she grabbed..."

    # Choice Screen - Aurora's hand or Josh's arm
    menu:
        "Aurora's Hand":
            jump Aurora_Path

        "Josh's Arm":
            jump Josh_Path
    
label Aurora_Path:
    scene sleeping with dissolve #change scene to staircase
    "She pulled her towards the staircase that led to the fourth floor of the building."
    "They had no time to waste. The floodwaters were rising fast, and the structure was already groaning under the strain of the storm."

    scene hallway_raining with fade #No PNG
    "As they reached the landing of the fourth floor, the chaos was worse than they had anticipated."

    scene stormWindow with fade 
    "The windows had shattered, and rain poured into the hallways, turning the floor into a slippery mess."
    "Papers and debris flew around them as the wind howled like a living beast, threatening to tear the building apart."

    scene hallway_raining with fade #No PNG
    
    show aurora_panting with dissolve #No PNG
    a "Mari, we’re almost there! We just need to make it to the roof!"
    hide aurora_panting with dissolve #No PNG

    scene sleeping with dissolve
    "But before they could take another step, a familiar figure emerged from the shadows, blocking their way."

    scene hallway_raining with fade #No PNG
    show bellatrix_def with dissolve #No PNG
    "Bellatrix Wilkes, the girl who had tormented Mari for as long as she could remember, stood in front of them with a wicked smile."
    "Her drenched hair clung to her face, and her eyes glinted with malice."
    
    show bellatrix_mocking with dissolve #No PNG
    b "Going somewhere, Mari?"
    b "You really think you can escape this?"
    b "You think you can save everyone?"
    hide bellatrix_def with dissolve #No PNG
    hide bellatrix_mocking with dissolve #No PNG

    show bellatrix_def at left with dissolve #No PNG
    show mari_grit_teeth at right with dissolve  #No PNG
    m "Get out of our way, Bellatrix. This isn’t the time."

    show bellatrix_smirking at left with dissolve #No PNG
    b "Oh, but it is. You’ve always thought you were so special with your powers, didn’t you?"
    b "But look at you now. You’re as helpless as the rest of us."
    hide bellatrix_smirking at left with dissolve #No PNG
    hide mari_grit_teeth at right with dissolve  #No PNG

    show bellatrix_def at left with dissolve #No PNG
    show aurora_angry at right with dissolve  #No PNG
    a "We don’t have time for this, Bellatrix. Move, or we’ll make you."
    hide bellatrix_def at left with dissolve #No PNG
    hide aurora_angry at right with dissolve  #No PNG

    show bellatrix_laugh with dissolve  #No PNG
    b "HAHAHAHA!"
    hide bellatrix_laugh with fade  #No PNG

    show bellatrix_def at left with dissolve  #No PNG 
    b "Make me? You think you can just run up to the roof and fix everything with your little powers?"
    b "You’re a joke, Mari."
    show mari_angry at right with dissolve #No PNG 
    m "You don’t understand what’s at stake, Bellatrix. This isn’t about us." 
    m "It’s about everyone."
    show bellatrix_coldly at left with dissolve  #No PNG 
    b "I don’t care. You’ve always had everything, and I’ve had nothing."
    b "If this city drowns, so be it. At least I’ll be free of you."

    scene sleeping with dissolve #change scene to staircase
    "That was it. Mari had had enough."
    "To be continued"

label Josh_Path:
    scene sleeping with dissolve #change scene to staircase
    "Without hesitation, she grabbed Josh’s arm pulling him up the stairs"
    "They both moved quickly, their footsteps echoing in the empty building as they raced toward the fourth floor."
    "The floodwaters were rising, creeping higher with every passing second, but Mari knew they couldn’t stop."

    scene hallway_raining with fade #No PNG
    "As they burst through the door to the fourth floor, the chaos they encountered was overwhelming."

    scene stormWindow with fade 
    "The windows were shattered, allowing torrents of rain to pour into the hallways."
    "Water pooled on the ground, mixing with broken glass and scattered debris."
    "The storm raged outside, making the entire building tremble beneath its force."

    scene hallway_raining with fade #No PNG
    
    show josh_panting with dissolve #No PNG
    j "Mari, we’ve got to hurry! We can’t stay here much longer!"
    hide josh_panting with dissolve #No PNG

    scene sleeping with dissolve
    "The roof was just one more flight of stairs away, but as they made their way toward the stairwell, they found someone waiting for them."
    "Out of the shadows, a figure stepped forward."

    scene hallway_raining with fade #No PNG
    show bellatrix_def with dissolve #No PNG
    "Bellatrix Wilkes, her wet hair was plastered to her face, and a look of cold satisfaction gleamed in her eyes"

    show bellatrix_mocking with dissolve #No PNG
    b "Going somewhere, Mari?"
    b "You really think you can escape this?"
    b " From me?"

    scene sleeping with dissolve #change scene to staircase
    "To be Continued"
    hide bellatrix_def with dissolve #No PNG
    hide bellatrix_mocking with dissolve #No PNG
  
    return