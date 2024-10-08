#Album Screen

init python:

    gallery = Gallery()

    gallery.button("Storm") # Name of the button
    gallery.image("stormy") # The Photo that will show once unlocked
    gallery.condition("persistent.storm") # Condition to unlock the Photo (Requires persistent)

screen album_UI:
    
    tag menu

    add "bg" # background image (at PhotosAlbum.rpy)

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        grid 4 4:
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
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")

            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")

            spacing 20

    textbutton _("Return"):
        action Return()
        xalign 0.1
        xoffset 10
        yalign 0.9
        


