################################################################################
## screens_custom/dashboard.rpy — Main Management Dashboard
################################################################################

screen dashboard():
    tag menu
    modal True
    zorder 100

    add "gui/game_menu.png"
    add "gui/overlay/game_menu.png"

    ## ═══ Title Bar ═══
    frame:
        style "dash_title_bar"
        hbox:
            spacing 20
            text "◈ COMMAND CENTER" style "dash_title_text"
            null width 40
            text "[clock.icon] [clock.time_of_day] — Day [clock.day] ([clock.day_of_week])" style "dash_time_text"
            null
            text "¥[economy.money:,]" style "dash_money_text"

    ## ═══ Main Content Area ═══
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        ## ── Stats Overview Row ──
        hbox:
            xalign 0.5
            spacing 24

            # Money Card
            frame:
                style "dash_card"
                vbox:
                    spacing 6
                    text "FUNDS" style "dash_card_label"
                    text "¥[economy.money:,]" style "dash_card_value" color gui.neon_green
                    if economy.get_last_report():
                        $ lr = economy.get_last_report()
                        if lr["profit"] >= 0:
                            text "+¥[lr[profit]:,] last night" style "dash_card_sub" color gui.neon_green
                        else:
                            $ loss = abs(lr["profit"])
                            text "-¥[loss:,] last night" style "dash_card_sub" color gui.neon_red

            # Reputation Card
            frame:
                style "dash_card"
                vbox:
                    spacing 6
                    text "REPUTATION" style "dash_card_label"
                    text "[reputation.tier]" style "dash_card_value" color gui.neon_magenta
                    bar:
                        value reputation.tier_progress
                        range 1.0
                        style "dash_progress_bar"

            # Staff Card
            frame:
                style "dash_card"
                vbox:
                    spacing 6
                    text "STAFF" style "dash_card_label"
                    $ on_duty = len(staff_manager.get_on_duty())
                    $ total = staff_manager.get_roster_count()
                    text "[total] / [staff_manager.MAX_ROSTER]" style "dash_card_value" color gui.neon_cyan
                    text "[on_duty] on duty" style "dash_card_sub"

            # Danger Card
            frame:
                style "dash_card"
                vbox:
                    spacing 6
                    text "HEAT LEVEL" style "dash_card_label"
                    text "[reputation.danger]%" style "dash_card_value"
                    text reputation.get_danger_label() style "dash_card_sub"

        ## ── Action Buttons Row ──
        hbox:
            xalign 0.5
            spacing 20

            textbutton "  MANAGE STAFF  ":
                style "dash_action_btn"
                action ShowMenu("staff_screen")

            textbutton "  UPGRADE VENUE  ":
                style "dash_action_btn"
                action ShowMenu("venue_screen")

            textbutton "  CITY MAP  ":
                style "dash_action_btn"
                action ShowMenu("map_screen")

            if clock.is_business_hours:
                textbutton "  ▶ OPEN FOR BUSINESS  ":
                    style "dash_action_btn_primary"
                    action Return("open_business")
            else:
                textbutton "  ▶ ADVANCE TIME  ":
                    style "dash_action_btn_primary"
                    action Return("advance_time")

        ## ── Bottom Actions ──
        hbox:
            xalign 0.5
            spacing 20

            textbutton "◆ SAVE":
                style "dash_small_btn"
                action ShowMenu("save")

            textbutton "◆ LOAD":
                style "dash_small_btn"
                action ShowMenu("load")

            textbutton "◇ PREFERENCES":
                style "dash_small_btn"
                action ShowMenu("preferences")

            textbutton "✕ MAIN MENU":
                style "dash_small_btn"
                action MainMenu()

################################################################################
## Dashboard Styles
################################################################################

style dash_title_bar:
    xfill True
    ysize 60
    xpadding 30
    ypadding 12
    background "#0a0a0fee"
    yalign 0.0

style dash_title_text:
    font "fonts/Orbitron-Variable.ttf"
    size 28
    color gui.neon_cyan
    yalign 0.5

style dash_time_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 22
    color gui.text_color
    yalign 0.5

style dash_money_text:
    font "fonts/Orbitron-Variable.ttf"
    size 26
    color gui.neon_green
    yalign 0.5

style dash_card:
    xsize 350
    ysize 160
    padding (24, 20, 24, 20)
    background "#12121aee"

style dash_card_label:
    font "fonts/Orbitron-Variable.ttf"
    size 16
    color gui.idle_color
    kerning 3.0

style dash_card_value:
    font "fonts/Orbitron-Variable.ttf"
    size 32
    color gui.text_color

style dash_card_sub:
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    color gui.idle_color

style dash_progress_bar is bar:
    xfill True
    ysize 8
    left_bar Solid(gui.neon_magenta)
    right_bar Solid("#1a1a2e")

style dash_action_btn:
    padding (30, 14, 30, 14)
    background "#1a1a2eee"
    hover_background "#1a1a2e"

style dash_action_btn_text:
    font "fonts/Rajdhani-Bold.ttf"
    size 24
    color gui.idle_color
    hover_color gui.neon_cyan
    kerning 2.0

style dash_action_btn_primary is dash_action_btn:
    background "#12121a"

style dash_action_btn_primary_text is dash_action_btn_text:
    color gui.neon_cyan
    hover_color gui.neon_magenta

style dash_small_btn:
    padding (18, 8, 18, 8)

style dash_small_btn_text:
    font "fonts/Rajdhani-Medium.ttf"
    size 20
    color gui.idle_color
    hover_color gui.neon_cyan
