################################################################################
## variables.rpy — Global Variables & Defaults for Brothel Connection
################################################################################

## ─── Player ───
default player_name = "V"

## ─── Economy ───
default money = 5000
default daily_revenue = 0
default daily_expenses = 0
default total_earned = 0
default total_spent = 0

## ─── Time ───
default clock = None   # Initialized in script.rpy via GameClock()

## ─── Reputation ───
default reputation = None  # Initialized in script.rpy via Reputation()

## ─── Staff ───
default staff_manager = None  # Initialized via StaffManager()

## ─── Upgrades ───
default upgrade_manager = None  # Initialized via UpgradeManager()

## ─── Events ───
default event_manager = None  # Initialized via EventManager()

## ─── Venue ───
default venue_level = 1
default venue_name = "The Nexus"
default venue_upgrades = {}

## ─── Game State Flags ───
default tutorial_complete = False
default day_phase_active = False
default current_event = None
default game_over = False

## ─── Stats Tracking ───
default days_survived = 0
default customers_served = 0
default events_resolved = 0

## ─── Difficulty ───
default difficulty = "normal"  # "easy", "normal", "hard"

## ─── Persistent Data (survives across saves) ───
default persistent.achievements = []
default persistent.best_score = 0
default persistent.total_playtime = 0
default persistent.endings_seen = []
