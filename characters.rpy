################################################################################
## characters.rpy — Character Definitions for Brothel Connection
################################################################################

## ─── Player Character ───
define pc = Character("[player_name]",
    color="#00f0ff",
    who_font="fonts/Orbitron-Variable.ttf",
    who_size=30,
    who_outlines=[(2, "#00f0ff40", 0, 0), (1, "#00000080", 1, 1)],
    what_font="fonts/Rajdhani-Regular.ttf",
)

## ─── Narrator ───
define narrator = Character(None,
    what_font="fonts/Rajdhani-Regular.ttf",
    what_color="#bbbbcc",
    what_outlines=[(1, "#00000060", 1, 1)],
)

## ─── System Messages ───
define system = Character("{font=fonts/ShareTechMono-Regular.ttf}{size=22}{color=#666680}[SYSTEM]{/color}{/size}{/font}",
    what_font="fonts/ShareTechMono-Regular.ttf",
    what_size=24,
    what_color="#888899",
)

## ─── Key NPCs ───

# Mentor / Ally
define maya = Character("MAYA",
    color="#39ff14",
    who_font="fonts/Orbitron-Variable.ttf",
    who_size=30,
    who_outlines=[(2, "#39ff1440", 0, 0)],
    what_font="fonts/Rajdhani-Regular.ttf",
)

# Rival 1
define vex = Character("VEX",
    color="#ff1744",
    who_font="fonts/Orbitron-Variable.ttf",
    who_size=30,
    who_outlines=[(2, "#ff174440", 0, 0)],
    what_font="fonts/Rajdhani-Regular.ttf",
)

# Rival 2
define serin = Character("SERIN",
    color="#ffe600",
    who_font="fonts/Orbitron-Variable.ttf",
    who_size=30,
    who_outlines=[(2, "#ffe60040", 0, 0)],
    what_font="fonts/Rajdhani-Regular.ttf",
)

# Informant/Fixer
define ghost = Character("GHOST",
    color="#b000ff",
    who_font="fonts/Orbitron-Variable.ttf",
    who_size=30,
    who_outlines=[(2, "#b000ff40", 0, 0)],
    what_font="fonts/Rajdhani-Regular.ttf",
)

# Police Contact
define officer_chen = Character("OFFICER CHEN",
    color="#aaaacc",
    who_font="fonts/Orbitron-Variable.ttf",
    who_size=28,
    who_outlines=[(2, "#aaaacc40", 0, 0)],
    what_font="fonts/Rajdhani-Regular.ttf",
)

## ─── Staff Characters (used in dialogue scenes) ───
define nyx_char = Character("NYX",
    color="#ff00a0",
    who_font="fonts/Orbitron-Variable.ttf",
    who_size=28,
    what_font="fonts/Rajdhani-Regular.ttf",
)

define kai_char = Character("KAI",
    color="#00f0ff",
    who_font="fonts/Orbitron-Variable.ttf",
    who_size=28,
    what_font="fonts/Rajdhani-Regular.ttf",
)
