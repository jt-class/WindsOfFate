#Album Screen

init python:
    gallery = Gallery()

    gallery.button("Storm") #Name of the button
    gallery.image("storm") #The Photo that will show once unlocked
    gallery.condition("persistent.storm") #Condition to unlock the Photo

screen album_UI:
    tag menu
    add "bg"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        grid 4 4:
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            add gallery.make_button(name= "Storm", unlocked = "sample", locked = "locked")
            spacing 15

    textbutton _("Return"):
        style "return_button"
        action Return()
        
        xalign 0.1


