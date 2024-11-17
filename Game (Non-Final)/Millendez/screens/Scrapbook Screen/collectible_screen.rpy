screen collectibles_menu():

    tag menu
    use scrapbook

    hbox:
        xalign 0.5
        yalign 0.3
        spacing 359

        vbox:
            imagebutton action ShowMenu("c1_collect"):
                idle chap_button_idle
                hover chap_button_hover         
            text "Chapter 1" style "text_pos"
        vbox:
            imagebutton action ShowMenu("c2_collect"):
                idle chap_button_idle
                hover chap_button_hover         
            text "Chapter 2" style "text_pos"
        vbox:
            imagebutton action ShowMenu("c3_collect"):
                idle chap_button_idle
                hover chap_button_hover         
            text "Chapter 3" style "text_pos"

    hbox:
        xalign 0.5
        yalign 0.8
        spacing 359

        vbox:
            imagebutton action ShowMenu("c4_collect"):
                idle chap_button_idle
                hover chap_button_hover  
            text "Chapter 4" style "text_pos"
        vbox:
            imagebutton action ShowMenu("c5_collect"):
                idle chap_button_idle
                hover chap_button_hover
            text "Chapter 5" style "text_pos"

screen c1_collect():

    tag menu
    use scrapbook (collectibles_menu = False)

    hbox:
        yalign 0.2
        xoffset -100
        add collect_frame at Transform (xsize = 750)
        text "Chapter 1: The Beginning" style "collect_chap"
        
        
    textbutton _("Back") action ShowMenu("collectibles_menu"):
        xalign 0.9
        xoffset 10
        yalign 0.9

screen c2_collect():

    tag menu
    use scrapbook (collectibles_menu = False)
    
    hbox:
        yalign 0.2
        xoffset -100
        add collect_frame at Transform (xsize = 750)
        text "Chapter 2: ????" style "collect_chap"

    textbutton _("Back") action ShowMenu("collectibles_menu"):
        xalign 0.9
        xoffset 10
        yalign 0.9

screen c3_collect():

    tag menu
    use scrapbook (collectibles_menu = False)

    hbox:
        yalign 0.2
        xoffset -100
        add collect_frame at Transform (xsize = 750)
        text "Chapter 3: ????" style "collect_chap"

    textbutton _("Back") action ShowMenu("collectibles_menu"):
        xalign 0.9
        xoffset 10
        yalign 0.9

screen c4_collect():

    tag menu
    use scrapbook (collectibles_menu = False)

    hbox:
        yalign 0.2
        xoffset -100
        add collect_frame at Transform (xsize = 750)
        text "Chapter 4: ????" style "collect_chap"

    textbutton _("Back") action ShowMenu("collectibles_menu"):
        xalign 0.9
        xoffset 10
        yalign 0.9

screen c5_collect():

    tag menu
    use scrapbook (collectibles_menu = False)

    hbox:
        yalign 0.2
        xoffset -100
        add collect_frame at Transform (xsize = 750)
        text "Chapter 5: ????" style "collect_chap"

    textbutton _("Back") action ShowMenu("collectibles_menu"):
        xalign 0.9
        xoffset 10
        yalign 0.9

style collect_chap:
    font gui.interface_text_font 
    color "#000000" 
    xoffset -625

style text_pos:
    xalign 0.5
    yoffset -50
    font gui.interface_text_font
    color "#000000"
    