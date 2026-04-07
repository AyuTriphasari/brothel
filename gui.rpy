################################################################################
## gui.rpy — Cyberpunk Neon Theme for Brothel Connection
################################################################################
##
## A dark-mode, neon-accented cyberpunk GUI theme.
## Color palette: deep blacks, neon cyan, magenta, purple highlights.
##

init offset = -2

################################################################################
## Colors — Cyberpunk Neon Palette
################################################################################

## Primary neon colors
define gui.neon_cyan = "#00f0ff"
define gui.neon_magenta = "#ff00a0"
define gui.neon_purple = "#b000ff"
define gui.neon_green = "#39ff14"
define gui.neon_yellow = "#ffe600"
define gui.neon_red = "#ff1744"

## Background surfaces
define gui.dark_bg = "#0a0a0f"
define gui.dark_surface = "#12121a"
define gui.dark_elevated = "#1a1a2e"
define gui.dark_border = "#2a2a3e"

## Accent color (used by default Ren'Py systems)
define gui.accent_color = "#00f0ff"

## Text colors
define gui.text_color = "#d0d0e0"
define gui.interface_text_color = "#c0c0d0"
define gui.idle_color = "#666680"
define gui.idle_small_color = "#555570"
define gui.hover_color = "#00f0ff"
define gui.hover_sound = None
define gui.activate_sound = None
define gui.selected_color = "#ff00a0"
define gui.insensitive_color = "#33334a"
define gui.muted_color = "#444460"
define gui.hover_muted_color = "#555580"

################################################################################
## Fonts
################################################################################

define gui.text_font = "fonts/Rajdhani-Regular.ttf"
define gui.name_text_font = "fonts/Orbitron-Variable.ttf"
define gui.interface_text_font = "fonts/Rajdhani-Medium.ttf"
define gui.system_font = gui.text_font
define gui.monospace_font = "fonts/ShareTechMono-Regular.ttf"

################################################################################
## Font Sizes
################################################################################

define gui.text_size = 28
define gui.name_text_size = 30
define gui.interface_text_size = 28
define gui.label_text_size = 36
define gui.notify_text_size = 22
define gui.title_text_size = 64

################################################################################
## Main and Game Menus
################################################################################

define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

################################################################################
## Dialogue
################################################################################

define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 2
define gui.dialogue_width = 1116
define gui.dialogue_text_xalign = 0.0

################################################################################
## Textbox / Namebox  
################################################################################

define gui.textbox_height = 278
define gui.textbox_yalign = 1.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0

################################################################################
## Buttons
################################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

## Navigation button overrides
define gui.navigation_button_width = 360

## Choice buttons
define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(200, 10, 200, 10)
define gui.choice_button_text_font = gui.interface_text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#aaaacc"
define gui.choice_button_text_hover_color = gui.neon_cyan
define gui.choice_button_text_insensitive_color = "#444460"

## File slot buttons
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 18
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.neon_cyan
define gui.slot_button_text_selected_hover_color = gui.neon_magenta

################################################################################
## Bars, Scrollbars, and Sliders
################################################################################

define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38
define gui.thumb_size = 14

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

define gui.unscrollable = "hide"

################################################################################
## Frames / Panels
################################################################################

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False

################################################################################
## History
################################################################################

define config.history_length = 250
define gui.history_height = 210
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

################################################################################
## NVL Mode
################################################################################

define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_height = 173
define gui.nvl_spacing = 15
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

################################################################################
## Quick Menu
################################################################################

define gui.quick_button_text_size = 18
define gui.quick_button_text_idle_color = "#555570"
define gui.quick_button_text_hover_color = gui.neon_cyan
define gui.quick_button_text_selected_color = gui.neon_magenta

################################################################################
## Paging
################################################################################

define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.page_spacing = 0

################################################################################
## File Slots  
################################################################################

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

################################################################################
## Mobile Variants
################################################################################

init python:
    if renpy.variant("touch"):
        gui.text_size = 36
        gui.name_text_size = 40
        gui.interface_text_size = 36
        gui.quick_button_text_size = 24
        gui.label_text_size = 42
        gui.notify_text_size = 28

    if renpy.variant("small"):
        gui.text_size = 30
        gui.name_text_size = 36
        gui.interface_text_size = 30
        gui.quick_button_text_size = 22
        gui.label_text_size = 36
        gui.notify_text_size = 24

        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100

        gui.slot_button_width = 340
        gui.slot_button_height = 255

        gui.navigation_button_width = 300
        gui.choice_button_width = 1000
        gui.choice_button_text_size = 26

        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
