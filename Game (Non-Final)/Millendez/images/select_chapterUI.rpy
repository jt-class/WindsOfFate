screen select_chapter():

    tag menu
    add gui.main_menu_background
    add ovl_tablet

    text "Select Chapter" xalign 0.1 yalign 0.1:
        font gui.interface_text_font
        color '#f224e8'
        size 80
    
    text "Select the Chapter you want to play at that scenario" xalign 0.1 xoffset 50 yalign 0.2:
        font gui.interface_text_font
        color '#ffffff'
        size 40
    
    hbox:
        style "chapter_pos"

        grid 5 1:
        
            spacing 100
            vbox:
                imagebutton action Start('start'):
                    idle chap_button_idle
                    hover chap_button_hover
                text "Chapter 1" style "chapter_text_pos"

            vbox:
                imagebutton action Start('chapter2'):
                    idle chap_button_idle
                    hover chap_button_hover
                text "Chapter 2" style "chapter_text_pos"
            
            vbox:
                imagebutton action Start('chapter3'):
                    idle chap_button_idle
                    hover chap_button_hover
                text "Chapter 3" style "chapter_text_pos"
            
            vbox:
                imagebutton action Start('chapter4'):
                    idle chap_button_idle
                    hover chap_button_hover
                text "Chapter 4" style "chapter_text_pos"
            
            vbox:
                imagebutton action Start('chapter5'):
                    idle chap_button_idle
                    hover chap_button_hover
                text "Chapter 5" style "chapter_text_pos"

    # if chapter are not unlocked, the pop up message should appear that player required to unlock (or nah...)

    textbutton _("Return"):
        xalign 0.1
        yalign 0.9
        yoffset 25
        action Return()
        

style chapter_pos is default:
    xalign 0.5
    yalign 0.6

style chapter_text_pos is text_pos # 
    