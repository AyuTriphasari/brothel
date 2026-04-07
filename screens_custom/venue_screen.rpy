################################################################################
## screens_custom/venue_screen.rpy — Venue Upgrades Interface
################################################################################

screen venue_screen():
    tag menu

    use game_menu(_("VENUE"), scroll="viewport"):
        style_prefix "venue"

        vbox:
            spacing 24

            ## ── Venue Header ──
            frame:
                style "venue_header"
                hbox:
                    spacing 30
                    vbox:
                        spacing 6
                        text "[venue_name]" style "venue_title"
                        text "Level [upgrade_manager.get_venue_level]  |  [upgrade_manager.purchased_ids.__len__] upgrades" style "venue_sub"
                    null
                    vbox:
                        xalign 1.0
                        spacing 4
                        text "Available: ¥[economy.money:,]" style "venue_funds"

            ## ── Upgrade Categories ──
            for cat_id, cat_info in upgrade_manager.CATEGORIES.items():
                vbox:
                    spacing 12

                    text "{} {}".format("▸", cat_info["label"]):
                        style "venue_cat_label"
                        color cat_info["color"]

                    for u in upgrade_manager.get_by_category(cat_id):
                        frame:
                            style "venue_upgrade_card"
                            if u.purchased:
                                background "#0a1a0fee"

                            hbox:
                                spacing 16

                                ## Icon & Name
                                vbox:
                                    xsize 280
                                    spacing 4
                                    text "{} {}".format(u.icon, u.name):
                                        style "venue_upgrade_name"
                                        if u.purchased:
                                            color gui.neon_green
                                    text u.description style "venue_upgrade_desc"

                                ## Bonuses
                                vbox:
                                    xsize 250
                                    spacing 4
                                    text "BONUSES" style "venue_bonus_header"
                                    text u.get_bonus_text() style "venue_bonus_text"

                                ## Price & Action
                                vbox:
                                    xsize 180
                                    yalign 0.5
                                    spacing 8

                                    if u.purchased:
                                        text "✓ INSTALLED" style "venue_installed"
                                    elif u.can_purchase(economy, upgrade_manager.purchased_ids):
                                        text "¥[u.cost:,]" style "venue_price"
                                        textbutton "PURCHASE":
                                            style "venue_buy_btn"
                                            action Function(upgrade_manager.purchase, u.uid, economy)
                                    else:
                                        text "¥[u.cost:,]" style "venue_price_locked"
                                        if u.prereqs:
                                            $ missing = [p for p in u.prereqs if p not in upgrade_manager.purchased_ids]
                                            if missing:
                                                text "Requires prerequisite" style "venue_locked_text"
                                        if not economy.can_afford(u.cost):
                                            text "Insufficient funds" style "venue_locked_text"

################################################################################
## Venue Screen Styles
################################################################################

style venue_header:
    xfill True
    padding (24, 20, 24, 20)
    background "#12121aee"

style venue_title:
    font "fonts/Orbitron-Variable.ttf"
    size 32
    color gui.neon_cyan

style venue_sub:
    font "fonts/ShareTechMono-Regular.ttf"
    size 20
    color gui.idle_color

style venue_funds:
    font "fonts/Orbitron-Variable.ttf"
    size 24
    color gui.neon_green

style venue_cat_label:
    font "fonts/Orbitron-Variable.ttf"
    size 22
    kerning 3.0

style venue_upgrade_card:
    xfill True
    padding (20, 14, 20, 14)
    background "#12121acc"

style venue_upgrade_name:
    font "fonts/Rajdhani-Bold.ttf"
    size 22
    color gui.text_color

style venue_upgrade_desc:
    font "fonts/Rajdhani-Regular.ttf"
    size 18
    color gui.idle_color

style venue_bonus_header:
    font "fonts/ShareTechMono-Regular.ttf"
    size 14
    color gui.idle_small_color
    kerning 2.0

style venue_bonus_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 16
    color gui.neon_yellow

style venue_installed:
    font "fonts/Orbitron-Variable.ttf"
    size 18
    color gui.neon_green

style venue_price:
    font "fonts/Orbitron-Variable.ttf"
    size 22
    color gui.neon_green

style venue_price_locked:
    font "fonts/Orbitron-Variable.ttf"
    size 22
    color gui.insensitive_color

style venue_locked_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 14
    color gui.neon_red

style venue_buy_btn:
    padding (18, 8, 18, 8)

style venue_buy_btn_text:
    font "fonts/Rajdhani-Bold.ttf"
    size 20
    color gui.neon_cyan
    hover_color gui.neon_magenta
    kerning 3.0
