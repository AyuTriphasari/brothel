# Brothel Connection — Implementation Walkthrough

## Summary

Built a complete Ren'Py management simulation game with a **cyberpunk neon dark-mode GUI theme**. The game features a full day/night cycle, staff management, venue upgrades, reputation system, random events, and a story-driven prologue.

## Project Structure (65+ files)

```
game/
├── fonts/                     # 5 Google Fonts (Orbitron, Rajdhani, ShareTechMono)
├── gui/                       # 38 generated cyberpunk GUI assets
│   ├── main_menu.png          # AI-generated cyberpunk cityscape
│   ├── game_menu.png          # AI-generated club interior
│   ├── textbox.png            # Neon-bordered dialogue box
│   ├── frame.png              # Confirm dialog frame
│   ├── bar/                   # Progress bar assets
│   ├── button/                # Choice, slot, radio, check buttons
│   ├── overlay/               # Dark overlays for menus
│   ├── scrollbar/             # Scrollbar assets
│   └── slider/                # Slider assets
├── options.rpy                # Game config (1920x1080, title, transitions)
├── gui.rpy                    # Full cyberpunk color palette & theme vars
├── screens.rpy                # ALL default screens rebuilt with neon styling
├── characters.rpy             # 8 characters with neon-colored definitions
├── variables.rpy              # All game state defaults
├── script.rpy                 # Main game loop & entry point
├── systems/
│   ├── clock.rpy              # GameClock — day/night, weekdays, periods
│   ├── economy.rpy            # Economy — earn/spend, nightly revenue
│   ├── staff.rpy              # Staff & StaffManager — stats, training, roster
│   ├── reputation.rpy         # Reputation — fame tiers, quality, danger
│   ├── upgrades.rpy           # Upgrade & UpgradeManager — 12 upgrades in 4 categories
│   └── events.rpy             # EventManager — 10 events with multi-choice outcomes
├── screens_custom/
│   ├── hud.rpy                # Persistent top-bar (money, time, rep, staff)
│   ├── dashboard.rpy          # Main command center with stats cards
│   ├── staff_screen.rpy       # Staff roster with stat bars & actions
│   ├── venue_screen.rpy       # Upgrade tree with categories
│   └── map_screen.rpy         # 6 city locations
├── story/
│   └── prologue.rpy           # Opening cinematic + tutorial + event handler
└── scripts/
    └── generate_gui_assets.py # Asset generator (rerunnable)
```

## Key Architecture Decisions

### Cyberpunk GUI Theme
- **Color Palette**: Deep blacks (`#0a0a0f`), neon cyan (`#00f0ff`), magenta (`#ff00a0`), purple (`#b000ff`), green (`#39ff14`)
- **Fonts**: Orbitron (headings), Rajdhani (body), ShareTechMono (data/system)
- **Every default screen** fully rebuilt — main menu, game menu, save/load, preferences, history, confirm, etc.
- All GUI image assets generated programmatically via Python script

### Game Systems (Python Classes)
- **GameClock**: 4 time periods per day, weekday tracking, business hours logic
- **Economy**: Revenue calculations based on staff performance + reputation + venue level + weekend bonuses
- **Staff**: Individual stats (charisma, skill, stamina, mood), training, leveling, mood/affinity system
- **Reputation**: 7 fame tiers from "Unknown" to "Neon Empire", quality/danger/satisfaction tracking
- **Upgrades**: 12 upgrades across 4 categories with prerequisite trees and bonus stacking
- **Events**: 10 pre-built events (positive/negative/neutral) with conditional triggers and multi-choice outcomes

### Game Loop
```
Start → Prologue/Tutorial → Dashboard (command center)
  → Player chooses action (manage staff, upgrade, map, advance time, open business)
  → Process results → Check for random events → Loop back
  → End of day: expenses, staff rest, reputation decay, weekly refresh
```

## How to Run

1. Install [Ren'Py SDK](https://www.renpy.org/latest.html) (8.x recommended)
2. Point Ren'Py to the `/root/game/` directory as the project
3. Click "Launch Project" in the Ren'Py Launcher

## What's Next (Phase 5 — Future)

- Phone/messaging system for character interactions
- Additional story chapters and character arcs
- Character sprite art generation
- Audio/music integration
- More events and location-specific scenes
