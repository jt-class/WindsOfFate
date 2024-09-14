# The script of the game goes in this file.

#Splash Screen
label splashscreen:
    scene black
    with Pause(1)

    $ renpy.movie_cutscene('temporary_splash.webm') #Temporary Splash Screen Logo

    scene black
    with Pause(1)

    return

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Girl", image="sample_girl")
define a = Character("Boy", image="sample_boy")
image background = "sample.jpg"

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene background 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    

    # Display the sample_girl image with full opacity
    show sample_girl at right
    show sample_boy1 at left 

    e "You've created a new Ren'Py game."
    hide sample_boy1 at left
    hide sample_girl at right

    show sample_boy at left
    show sample_girl1 at right

    a "Once you add a story, pictures, and music, you can release it to the world!"
    hide sample_boy at left
    hide sample_girl1 at right

    show sample_girl at right
    show sample_boy1 at left 
    e "Wow! I cant wait to see you complete the game."

    hide sample_boy1 at left
    hide sample_girl at right

    show sample_boy at left
    show sample_girl1 at right

    a "It’s going to be fantastic! Let me know if you need any help along the way."

    # This ends the game.

    return
