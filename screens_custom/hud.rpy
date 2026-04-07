################################################################################
## screens_custom/hud.rpy — Persistent HUD Overlay
################################################################################

screen hud():
    zorder 50
    layer "overlay"

    ## Top bar — always visible during gameplay
    frame:
        style "hud_bar"

        hbox:
            spacing 40
            xfill True

            ## Money
            hbox:
                spacing 8
                text "¥" style "hud_icon_text" color gui.neon_green
                text "[economy.money:,]" style "hud_value_text" color gui.neon_green

            ## Day & Time
            hbox:
                spacing 8
                text "[clock.icon]" style "hud_icon_text"
                text "[clock.time_of_day]" style "hud_value_text"
                text "—" style "hud_value_text" color gui.idle_color
                text "Day [clock.day]" style "hud_value_text"

            ## Reputation Tier
            hbox:
                spacing 8
                text "◈" style "hud_icon_text" color gui.neon_magenta
                text "[reputation.tier]" style "hud_value_text" color gui.neon_magenta

            ## Staff Count
            hbox:
                spacing 8
                text "●" style "hud_icon_text" color gui.neon_cyan
                text "[staff_manager.roster.__len__] Staff" style "hud_value_text"

style hud_bar:
    xfill True
    ysize 48
    xpadding 30
    ypadding 8
    background "#0a0a0fdd"
    yalign 0.0

style hud_icon_text:
    font "fonts/Rajdhani-Bold.ttf"
    size 22
    yalign 0.5

style hud_value_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 20
    color gui.text_color
    yalign 0.5
