################################################################################
## screens_custom/staff_screen.rpy — Staff Management Interface
################################################################################

screen staff_screen():
    tag menu

    use game_menu(_("STAFF"), scroll="viewport"):
        style_prefix "staff"

        vbox:
            spacing 20

            ## ── Roster Section ──
            label "ROSTER  ([staff_manager.roster.__len__]/[staff_manager.MAX_ROSTER])"

            if staff_manager.roster:
                for s in staff_manager.roster:
                    frame:
                        style "staff_card"
                        hbox:
                            spacing 20

                            ## Info Column
                            vbox:
                                xsize 200
                                spacing 4
                                text s.name style "staff_name_text"
                                text s.role style "staff_role_text"
                                text s.get_status_label() style "staff_status_text"
                                text "Lv.[s.level]  |  ¥[s.salary]/day" style "staff_sub_text"

                            ## Stats Column
                            vbox:
                                xsize 300
                                spacing 6

                                hbox:
                                    spacing 8
                                    text "CHA" style "staff_stat_label"
                                    bar:
                                        value s.charisma
                                        range 100
                                        style "staff_stat_bar"
                                    text "[s.charisma]" style "staff_stat_num"

                                hbox:
                                    spacing 8
                                    text "SKL" style "staff_stat_label"
                                    bar:
                                        value s.skill
                                        range 100
                                        style "staff_stat_bar"
                                    text "[s.skill]" style "staff_stat_num"

                                hbox:
                                    spacing 8
                                    text "STA" style "staff_stat_label"
                                    bar:
                                        value s.stamina
                                        range 100
                                        style "staff_stat_bar_stamina"
                                    text "[s.stamina]" style "staff_stat_num"

                                hbox:
                                    spacing 8
                                    text "MOD" style "staff_stat_label"
                                    bar:
                                        value s.mood
                                        range 100
                                        style "staff_stat_bar_mood"
                                    text s.get_mood_label() style "staff_stat_num"

                            ## Actions Column
                            vbox:
                                xsize 200
                                spacing 8

                                if not s.on_duty:
                                    textbutton "▶ Assign Duty":
                                        style "staff_action_btn"
                                        action Function(staff_manager.assign_duty, s)
                                else:
                                    textbutton "■ Remove":
                                        style "staff_action_btn"
                                        action Function(staff_manager.remove_from_duty, s)

                                if not s.on_duty and not s.is_tired:
                                    textbutton "◆ Train CHA":
                                        style "staff_action_btn"
                                        action Function(s.train, "charisma")
                                    textbutton "◆ Train SKL":
                                        style "staff_action_btn"
                                        action Function(s.train, "skill")

                                textbutton "✕ Fire":
                                    style "staff_fire_btn"
                                    action Confirm(
                                        "Fire {} from the roster?".format(s.name),
                                        Function(staff_manager.fire, s)
                                    )

            else:
                text "No staff hired yet." style "staff_empty_text"

            null height 20

            ## ── Available Hires Section ──
            label "AVAILABLE FOR HIRE"

            if staff_manager.available_hires:
                for s in staff_manager.available_hires:
                    frame:
                        style "staff_hire_card"
                        hbox:
                            spacing 20

                            vbox:
                                xsize 200
                                spacing 4
                                text s.name style "staff_name_text"
                                text s.role style "staff_role_text"
                                text "¥[s.salary]/day" style "staff_sub_text"
                                if s.traits:
                                    $ trait_text = ", ".join(s.traits)
                                    text "[trait_text]" style "staff_trait_text"

                            vbox:
                                xsize 260
                                spacing 6
                                hbox:
                                    spacing 8
                                    text "CHA [s.charisma]" style "staff_preview_stat"
                                    text "SKL [s.skill]" style "staff_preview_stat"
                                hbox:
                                    spacing 8
                                    text "STA [s.stamina]" style "staff_preview_stat"
                                    text "Total: [s.stat_total]" style "staff_preview_stat" color gui.neon_cyan

                            textbutton "HIRE":
                                style "staff_hire_btn"
                                action Function(staff_manager.hire, s)
            else:
                text "No one available right now." style "staff_empty_text"

################################################################################
## Staff Screen Styles
################################################################################

style staff_label_text:
    font "fonts/Orbitron-Variable.ttf"
    size 22
    color gui.neon_cyan
    kerning 3.0

style staff_card:
    xfill True
    padding (20, 16, 20, 16)
    background "#12121aee"

style staff_hire_card is staff_card:
    background "#0f0f18ee"

style staff_name_text:
    font "fonts/Orbitron-Variable.ttf"
    size 24
    color gui.text_color

style staff_role_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    color gui.neon_purple

style staff_status_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 16

style staff_sub_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 16
    color gui.idle_color

style staff_trait_text:
    font "fonts/Rajdhani-Regular.ttf"
    size 16
    color gui.neon_yellow

style staff_stat_label:
    font "fonts/ShareTechMono-Regular.ttf"
    size 16
    color gui.idle_color
    xsize 40
    yalign 0.5

style staff_stat_num:
    font "fonts/ShareTechMono-Regular.ttf"
    size 16
    color gui.text_color
    xsize 50
    yalign 0.5

style staff_stat_bar is bar:
    xsize 180
    ysize 12
    left_bar Solid(gui.neon_cyan)
    right_bar Solid("#1a1a2e")

style staff_stat_bar_stamina is staff_stat_bar:
    left_bar Solid(gui.neon_green)

style staff_stat_bar_mood is staff_stat_bar:
    left_bar Solid(gui.neon_yellow)

style staff_preview_stat:
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    color gui.idle_color

style staff_action_btn:
    padding (12, 6, 12, 6)

style staff_action_btn_text:
    font "fonts/Rajdhani-Medium.ttf"
    size 18
    color gui.idle_color
    hover_color gui.neon_cyan

style staff_fire_btn is staff_action_btn

style staff_fire_btn_text:
    font "fonts/Rajdhani-Medium.ttf"
    size 18
    color "#553340"
    hover_color gui.neon_red

style staff_hire_btn:
    padding (24, 10, 24, 10)
    yalign 0.5

style staff_hire_btn_text:
    font "fonts/Rajdhani-Bold.ttf"
    size 22
    color gui.neon_green
    hover_color "#ffffff"
    kerning 3.0

style staff_empty_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 20
    color gui.idle_color
