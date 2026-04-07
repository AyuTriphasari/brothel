## options.rpy — Game Configuration for Brothel Connection

define config.name = _("Brothel Connection")
define config.version = "0.1.0"

define gui.show_name = True
define config.window_title = "Brothel Connection"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_game_transition = dissolve
define config.game_main_transition = dissolve
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve

define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7

define config.save_directory = "BrothelConnection-1698273645"

define config.window_icon = None

init python:
    if renpy.variant("pc") or renpy.variant("web"):
        config.screen_width = 1920
        config.screen_height = 1080

    if renpy.variant("mobile"):
        config.screen_width = 1280
        config.screen_height = 720

    config.thumbnail_width = 384
    config.thumbnail_height = 216

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpyc', 'archive')
    build.classify('**.png', 'archive')
    build.classify('**.jpg', 'archive')
    build.classify('**.mp3', 'archive')
    build.classify('**.ogg', 'archive')
    build.classify('**.ttf', 'archive')

    build.name = "BrothelConnection"
