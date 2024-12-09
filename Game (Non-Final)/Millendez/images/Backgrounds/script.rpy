# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mari")

image Room_MC_Day = "Backgrounds/Room MC Day.png"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can add a file (named either "bg room.png" or "bg room.jpg") to the images directory to show it.
    scene Room_MC_Day with fade

    # This shows a character sprite. A placeholder is used.
    show mari happy with dissolve

    # Character's dialogue.
    m "You've created a new Ren'Py game."
    m "Once you add a story, pictures, and music, you can release it to the world!"
    m "This visual game was made in renpy engine."
    m "This Created for the subject Game Developlent by BSIT 4.1C"

    # This ends the game.

    return
