################################################################################
## screens_custom/map_screen.rpy — City Map Navigation
################################################################################

screen map_screen():
    tag menu

    use game_menu(_("CITY MAP"), scroll="viewport"):
        style_prefix "map"

        vbox:
            spacing 20

            text "Select a destination:" style "map_prompt"

            ## ── Location Grid ──
            grid 2 3:
                spacing 16
                xalign 0.5

                # The Venue
                frame:
                    style "map_location_card"
                    background "#0a150fee"
                    vbox:
                        spacing 6
                        text "◈ THE NEXUS" style "map_loc_name" color gui.neon_cyan
                        text "Your establishment" style "map_loc_desc"
                        text "Status: Open" style "map_loc_status" color gui.neon_green
                        textbutton "▶ MANAGE":
                            style "map_loc_btn"
                            action Return("venue")

                # Downtown District
                frame:
                    style "map_location_card"
                    vbox:
                        spacing 6
                        text "★ DOWNTOWN" style "map_loc_name" color gui.neon_purple
                        text "Shopping & services" style "map_loc_desc"
                        text "Buy supplies & equipment" style "map_loc_status"
                        textbutton "▶ VISIT":
                            style "map_loc_btn"
                            action Return("downtown")

                # Recruitment Agency
                frame:
                    style "map_location_card"
                    vbox:
                        spacing 6
                        text "● TALENT AGENCY" style "map_loc_name" color gui.neon_magenta
                        text "Find new staff" style "map_loc_desc"
                        $ avail = len(staff_manager.available_hires)
                        text "[avail] candidates available" style "map_loc_status" color gui.neon_green
                        textbutton "▶ BROWSE":
                            style "map_loc_btn"
                            action ShowMenu("staff_screen")

                # Black Market
                frame:
                    style "map_location_card"
                    vbox:
                        spacing 6
                        text "▲ BLACK MARKET" style "map_loc_name" color gui.neon_red
                        text "High risk, high reward" style "map_loc_desc"
                        text "Danger: [reputation.danger]%" style "map_loc_status" color gui.neon_yellow
                        textbutton "▶ ENTER":
                            style "map_loc_btn"
                            action Return("black_market")
                            sensitive (clock.time_of_day == "Night")

                # Rival Clubs
                frame:
                    style "map_location_card"
                    vbox:
                        spacing 6
                        text "✕ RIVAL DISTRICT" style "map_loc_name" color gui.neon_yellow
                        text "Scout the competition" style "map_loc_desc"
                        text "Know your enemies" style "map_loc_status"
                        textbutton "▶ SCOUT":
                            style "map_loc_btn"
                            action Return("rivals")

                # Rest
                frame:
                    style "map_location_card"
                    background "#12120a20"
                    vbox:
                        spacing 6
                        text "☾ HOME" style "map_loc_name" color gui.idle_color
                        text "Rest and recover" style "map_loc_desc"
                        text "Advance to next day" style "map_loc_status"
                        textbutton "▶ SLEEP":
                            style "map_loc_btn"
                            action Return("sleep")

################################################################################
## Map Screen Styles
################################################################################

style map_prompt:
    font "fonts/ShareTechMono-Regular.ttf"
    size 22
    color gui.idle_color

style map_location_card:
    xsize 480
    ysize 180
    padding (24, 20, 24, 20)
    background "#12121aee"

style map_loc_name:
    font "fonts/Orbitron-Variable.ttf"
    size 22
    kerning 2.0

style map_loc_desc:
    font "fonts/Rajdhani-Regular.ttf"
    size 20
    color gui.idle_color

style map_loc_status:
    font "fonts/ShareTechMono-Regular.ttf"
    size 16
    color gui.idle_small_color

style map_loc_btn:
    padding (16, 6, 16, 6)

style map_loc_btn_text:
    font "fonts/Rajdhani-Bold.ttf"
    size 20
    color gui.idle_color
    hover_color gui.neon_cyan
    kerning 2.0
