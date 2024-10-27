define page_num = "Page 1"
define j1Page1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nEtiam convallis ultrices nibh id consectetur. Mauris facilisis,\naugue quis rhoncus auctor, nisi elit mattis magna, "
define pic_journal1 = "gui/butterfly_side.png"

screen scrapbook(journal_screen = True, collectibles_menu = True, character_info = True):

    tag menu
    add "gui/bg_journal.jpg"

    hbox:
        style "scrapbook_menus"

        textbutton _("Journal") action ShowMenu("journal_screen")
        textbutton _("Collectibles") action ShowMenu("collectibles_menu")
        textbutton _("Characters") action ShowMenu("character_info")

    if journal_screen and collectibles_menu and character_info:

        textbutton _("Return"):
            action Return()
            xalign 0.9
            xoffset 10
            yalign 0.9


screen journal_screen():

    tag menu
    use scrapbook

    use p1Journal1

    hbox:
        style "journal_nav"
        textbutton _("Previous") action Return()
        textbutton _("Next") action Return()

    text page_num color "#000000":
        font gui.interface_text_font
        xoffset 80
        yalign 0.9

screen p1Journal1():

    hbox:
        xalign 0.8
        yalign 0.5
        add pic_journal1

    vbox:
        yalign 0.2
        text "January 01, 2024" color "#000000":
            style "journal_info"

    vbox:
        yalign 0.6
        spacing 50
        text j1Page1:
            style "journal_info"
        text j1Page1:
            style "journal_info"
        text j1Page1:
            style "journal_info"


style scrapbook_menus:
    xalign 0.1
    yoffset 60
    spacing 134

style journal_nav:
    xoffset 555
    spacing 168
    yalign 0.9

style journal_info:
    color "#000000"
    font gui.interface_text_font
    xoffset 100
    yalign 0.3
    

