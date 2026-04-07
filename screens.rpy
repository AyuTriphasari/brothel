################################################################################
## screens.rpy — Cyberpunk Neon Custom Screens for Brothel Connection
################################################################################
##
## All default Ren'Py screens rebuilt with cyberpunk neon dark-mode aesthetics.
## Uses Ren'Py Screen Language with custom styles for every element.
##

init offset = -1

################################################################################
## Styles — Cyberpunk Foundation
################################################################################

style default:
    font gui.text_font
    size gui.text_size
    color gui.text_color
    outlines [(1, "#0a0a0f80", 0, 0)]

style input:
    color gui.neon_cyan
    adjust_spacing False

style hyperlink_text:
    color gui.neon_cyan
    hover_color gui.neon_magenta
    hover_underline True

style gui_text:
    font gui.interface_text_font
    color gui.interface_text_color
    size gui.interface_text_size

style button:
    padding (6, 6, 6, 6)

style button_text is gui_text:
    idle_color gui.idle_color
    hover_color gui.neon_cyan
    selected_color gui.neon_magenta
    insensitive_color gui.insensitive_color
    yalign 0.5

style label_text is gui_text:
    color gui.neon_cyan
    size gui.label_text_size
    font "fonts/Orbitron-Variable.ttf"

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable gui.unscrollable

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable gui.unscrollable

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## Say Screen — Dialogue Display
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background "gui/textbox.png"

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    padding gui.namebox_borders.padding

style say_label:
    color gui.neon_cyan
    font gui.name_text_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    bold True
    outlines [(2, "#00f0ff40", 0, 0), (1, "#00000080", 1, 1)]

style say_dialogue:
    xpos gui.dialogue_xpos
    xanchor 0
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

################################################################################
## Input Screen
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    color gui.neon_cyan

style input:
    color gui.neon_cyan
    caret Solid(gui.neon_magenta, xsize=2)

################################################################################
## Choice Screen — Cyberpunk Styled
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 16

        for i in items:
            textbutton i.caption:
                action i.action
                at choice_hover

transform choice_hover:
    on idle:
        alpha 0.85
    on hover:
        alpha 1.0
        linear 0.15 alpha 1.0

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    yanchor 0.5
    spacing 16

style choice_button is default:
    xsize gui.choice_button_width
    padding (30, 12, 30, 12)
    background Frame("gui/button/choice_[prefix_]background.png", gui.choice_button_borders, tile=gui.choice_button_tile)

style choice_button_text is default:
    font gui.choice_button_text_font
    size gui.choice_button_text_size
    xalign gui.choice_button_text_xalign
    idle_color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    insensitive_color gui.choice_button_text_insensitive_color
    outlines [(1, "#00000080", 1, 1)]

################################################################################
## Quick Menu
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -8

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    padding (18, 6, 18, 0)

style quick_button_text:
    size gui.quick_button_text_size
    idle_color gui.quick_button_text_idle_color
    hover_color gui.quick_button_text_hover_color
    selected_color gui.quick_button_text_selected_color
    font "fonts/ShareTechMono-Regular.ttf"
    outlines [(1, "#00000080", 1, 1)]

################################################################################
## Main Menu — Cyberpunk Neon
################################################################################

screen main_menu():
    tag menu

    add gui.main_menu_background

    ## Dark overlay gradient for readability
    add "gui/overlay/main_menu.png"

    frame:
        style "main_menu_frame"

    vbox:
        style_prefix "main_menu"

        ## Game title with neon glow
        text "{font=fonts/Orbitron-Variable.ttf}{size=72}{color=#00f0ff}BROTHEL{/color} {color=#ff00a0}CONNECTION{/color}{/size}{/font}":
            xalign 0.0
            outlines [(4, "#00f0ff30", 0, 0), (2, "#ff00a020", 0, 0)]
            xpos 120
            ypos 120

        ## Tagline
        text "{font=fonts/ShareTechMono-Regular.ttf}{size=24}{color=#666680}// SYSTEM INITIALIZED — v[config.version]{/color}{/size}{/font}":
            xpos 124
            ypos 145

    ## Navigation
    use navigation

    key "game_menu" action ShowMenu("main_menu")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text

style main_menu_frame:
    xsize 520
    yfill True
    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.0
    xoffset 120
    xmaximum 460
    yalign 0.5
    yoffset -80
    spacing 8

style main_menu_text:
    xalign 0.0
    idle_color gui.idle_color
    hover_color gui.neon_cyan
    selected_color gui.neon_magenta
    size gui.interface_text_size

################################################################################
## Navigation
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos 120
        yalign 0.6

        spacing 8

        if main_menu:
            textbutton _("▶  START") action Start()
            textbutton _("◆  LOAD") action ShowMenu("load")
            textbutton _("◇  PREFERENCES") action ShowMenu("preferences")
            textbutton _("◈  ABOUT") action ShowMenu("about")
            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("✕  QUIT") action Quit(confirm=not main_menu)
        else:
            textbutton _("◇  HISTORY") action ShowMenu("history")
            textbutton _("◆  SAVE") action ShowMenu("save")
            textbutton _("◆  LOAD") action ShowMenu("load")
            textbutton _("◇  PREFERENCES") action ShowMenu("preferences")
            textbutton _("▶  MAIN MENU") action MainMenu()
            textbutton _("◈  ABOUT") action ShowMenu("about")
            if renpy.variant("pc"):
                textbutton _("✕  QUIT") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    padding (24, 6, 24, 6)

style navigation_button_text:
    font "fonts/Rajdhani-Bold.ttf"
    size 32
    idle_color "#888899"
    hover_color gui.neon_cyan
    selected_color gui.neon_magenta
    outlines [(1, "#00000060", 1, 1)]
    kerning 2.0

################################################################################
## Game Menu — Base Template
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Navigation column
            frame:
                style "game_menu_navigation_frame"

            ## Content column
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:
                    transclude

    use navigation

    ## Title with neon styling
    textbutton _("◀  Return"):
        style "return_button"
        action Return()

    label title:
        style "game_menu_label"

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_label is gui_label

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    font "fonts/Orbitron-Variable.ttf"
    size 48
    color gui.neon_cyan
    yalign 0.5
    outlines [(3, "#00f0ff25", 0, 0), (1, "#00000080", 1, 1)]
    text_align 0.0

style return_button is navigation_button
style return_button_text is navigation_button_text

style return_button:
    xpos 120
    yalign 1.0
    yoffset -45

################################################################################
## About Screen
################################################################################

screen about():
    tag menu

    use game_menu(_("ABOUT"), scroll="viewport"):

        style_prefix "about"

        vbox:
            spacing 12

            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            text _("{font=fonts/ShareTechMono-Regular.ttf}{size=22}{color=#666680}A cyberpunk management simulation.{/color}{/size}{/font}")

            if gui.about:
                text "[gui.about!t]\n"

define gui.about = ""

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size 42
    color gui.neon_magenta

################################################################################
## Save / Load Screens
################################################################################

screen save():
    tag menu

    use file_slots(_("SAVE"))

screen load():
    tag menu

    use file_slots(_("LOAD"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## Page selector
            order_reverse True

            ## File slot grid
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing 15

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y/%m/%d  %H:%M"), empty=_("▮▮▮  EMPTY SLOT")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Page navigation
            vbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5
                    spacing 12

                    textbutton _("◀  Prev") action FilePagePrevious()
                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")
                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _("Next  ▶") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color
    color gui.neon_cyan

style page_button:
    padding (15, 6, 15, 6)

style page_button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 22
    idle_color gui.idle_color
    hover_color gui.neon_cyan
    selected_color gui.neon_magenta

style slot_button:
    xsize gui.slot_button_width
    ysize gui.slot_button_height
    padding gui.slot_button_borders.padding
    background "gui/button/slot_[prefix_]background.png"

style slot_button_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size gui.slot_button_text_size
    color gui.slot_button_text_idle_color
    selected_idle_color gui.slot_button_text_selected_idle_color
    selected_hover_color gui.slot_button_text_selected_hover_color
    xalign gui.slot_button_text_xalign

style slot_time_text:
    size 18
    color gui.idle_small_color

style slot_name_text:
    size 18
    color gui.neon_cyan

################################################################################
## Preferences Screen — Cyberpunk Controls
################################################################################

screen preferences():
    tag menu

    use game_menu(_("PREFERENCES"), scroll="viewport"):

        vbox:
            xfill True
            spacing 24

            hbox:
                box_wrap True
                spacing 30

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "any window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height 15

            hbox:
                style_prefix "slider"
                box_wrap True
                spacing 20

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height 6
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text

style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    font "fonts/Orbitron-Variable.ttf"
    size 26
    color gui.neon_cyan
    yalign 1.0

style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_vbox is pref_vbox

style radio_button is gui_button
style radio_button_text is gui_button_text

style radio_button:
    padding (30, 6, 6, 6)
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    font gui.interface_text_font
    color gui.idle_color
    hover_color gui.neon_cyan
    selected_color gui.neon_magenta

style check_label is pref_label
style check_label_text is pref_label_text
style check_vbox is pref_vbox

style check_button is gui_button
style check_button_text is gui_button_text

style check_button:
    padding (30, 6, 6, 6)
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    font gui.interface_text_font
    color gui.idle_color
    hover_color gui.neon_cyan
    selected_color gui.neon_magenta

style slider_label is pref_label
style slider_label_text is pref_label_text

style slider_slider:
    xsize 525

style slider_button is gui_button
style slider_button_text is gui_button_text

style slider_pref_vbox:
    xsize 675

style mute_all_button is check_button
style mute_all_button_text is check_button_text

################################################################################
## History Screen
################################################################################

screen history():
    tag menu

    use game_menu(_("HISTORY"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:
            window:
                has hbox:
                    yfill True
                    spacing 30

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    font "fonts/Orbitron-Variable.ttf"
    size 22
    color gui.neon_cyan

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#bbbbcc"

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    color gui.idle_color

################################################################################
## Confirm Screen — Cyberpunk Modal
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                ## Neon-styled action buttons
                textbutton _("CONFIRM") action yes_action
                textbutton _("CANCEL") action no_action

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_button
style confirm_button_text is gui_button_text

style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign 0.5
    yalign 0.5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    font gui.interface_text_font
    color gui.text_color
    size 30

style confirm_button:
    padding (60, 12, 60, 12)

style confirm_button_text:
    font "fonts/Rajdhani-Bold.ttf"
    size 28
    idle_color gui.idle_color
    hover_color gui.neon_cyan
    selected_color gui.neon_magenta
    kerning 3.0

################################################################################
## Skip Indicator
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9
            text _("▶▶ SKIPPING")
            text "▮" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▮" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▮" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha 0.0
    pause delay
    block:
        linear (cycle * 0.5) alpha 1.0
        linear (cycle * 0.5) alpha 0.0
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos 15
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 20
    color gui.neon_cyan

style skip_triangle:
    font "fonts/ShareTechMono-Regular.ttf"
    color gui.neon_magenta

################################################################################
## Notify Screen
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos 68
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size gui.notify_text_size
    color gui.neon_green

################################################################################
## NVL Screen
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True

                for d in dialogue:
                    window:
                        id d.window_id
                        fixed:
                            yfit gui.nvl_height is None
                            if d.who is not None:
                                text d.who:
                                    id d.who_id
                            text d.what:
                                id d.what_id
        else:
            for d in dialogue:
                window:
                    id d.window_id
                    fixed:
                        yfit gui.nvl_height is None
                        if d.who is not None:
                            text d.who:
                                id d.who_id
                        text d.what:
                            id d.what_id

        if items:
            vbox:
                id "menu"
                for i in items:
                    textbutton i.caption:
                        action i.action
                        style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background "#0a0a0fe0"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign
    color gui.neon_cyan

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_thought_xalign else "tex")

style nvl_button:
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Small phone variants
style navigation_button:
    variant "small"
    size_group None

style quick_button:
    variant "small"
    padding (12, 4, 12, 0)

style quick_button_text:
    variant "small"
    size 18
