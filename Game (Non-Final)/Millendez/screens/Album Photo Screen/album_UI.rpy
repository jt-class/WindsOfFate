#Album Screen

init python:

    gallery = Gallery()

    gallery.button("Storm") # Name of the button
    gallery.image("stormy") # The Photo that will show once unlocked
    gallery.condition("persistent.storm") # Condition to unlock the Photo (Requires persistent)

screen album_UI_M(album_UI_M = True, album_UI_2 = False, album_UI_3 = False, album_UI_4 = False, album_UI_5 = False):
    
    tag menu

    add gui.main_menu_background
    add ovl_tablet

    text "Photo Album" xalign 0.5 yalign 0.1:
        font gui.interface_text_font
        color '#f224e8'
        size 80
    text "Photos you ulocked thoughout the game" xalign 0.5 yalign 0.2:
        font gui.interface_text_font
        color '#ffffff'
        size 40

    hbox xalign 0.5 yalign 1.5:
    
        if album_UI_M and not album_UI_2 and not album_UI_3 and not album_UI_4 and not album_UI_5:
            
            grid 5 5:

                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            
                # Spacing must be inside the grid
                spacing 50

        elif album_UI_2:

            grid 5 5:

                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")

                # Spacing must be inside the grid
                spacing 50
        
        elif album_UI_3:

            grid 5 5:

                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")

                # Spacing must be inside the grid
                spacing 50

        elif album_UI_4:

            grid 5 5:

                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")

                # Spacing must be inside the grid
                spacing 50

        elif album_UI_5:

            grid 5 5:

                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
                

                # Spacing must be inside the grid
                spacing 50
    
    use album_UI_Menu

    textbutton _("Return"):
        action Return()
        xalign 0.1
        xoffset 10
        yalign 0.9

screen album_UI_Menu():

    tag menu

    style_prefix "navigation"

    hbox:

        # Position of each chapter menu
        xalign 0.5
        xoffset 10
        yalign 0.9

        hbox:
            spacing 30   
            textbutton _("Chapter 1") action ShowMenu("album_UI_M")
            textbutton _("Chapter 2") action ShowMenu("album_UI_2")
            textbutton _("Chapter 3") action ShowMenu("album_UI_3")
            textbutton _("Chapter 4") action ShowMenu("album_UI_4")
            textbutton _("Chapter 5") action ShowMenu("album_UI_5")

screen album_UI_2():

    tag menu

    use album_UI_M (album_UI_2 = True)

screen album_UI_3():

    tag menu

    use album_UI_M (album_UI_3 = True)

screen album_UI_4():

    tag menu

    use album_UI_M (album_UI_4 = True)

screen album_UI_5():

    tag menu

    use album_UI_M (album_UI_5 = True)