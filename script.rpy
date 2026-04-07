################################################################################
## script.rpy — Main Game Entry & Loop for Brothel Connection
################################################################################

## ─── Game Initialization ───
label start:

    ## Initialize all game systems
    $ clock = GameClock()
    $ economy = Economy(5000)
    $ reputation = Reputation()
    $ staff_manager = StaffManager()
    $ upgrade_manager = UpgradeManager()
    $ event_manager = EventManager()

    ## Start prologue
    jump prologue


## ─── Main Game Loop ───
label main_loop:

    ## Show HUD
    show screen hud

    ## Check for random events
    $ event = event_manager.check_events(clock, reputation, economy)

    if event is not None:
        jump event_scene

    ## Show dashboard and wait for player action
    call screen dashboard

    ## Process the returned action
    $ action = _return

    if action == "advance_time":
        jump advance_time

    elif action == "open_business":
        jump open_business

    elif action == "sleep":
        jump end_of_day

    ## Default: loop back
    jump main_loop


## ─── Advance Time ───
label advance_time:

    $ new_day = clock.advance()

    if new_day:
        jump end_of_day
    else:
        system "[clock.icon] Time advances to [clock.time_of_day]."
        jump main_loop


## ─── Open for Business ───
label open_business:

    $ on_duty_count = len(staff_manager.get_on_duty())

    if on_duty_count == 0:
        system "You need at least one staff member on duty to open!"
        jump main_loop

    scene black with dissolve

    system "◈ THE NEXUS — NOW OPEN"

    "{i}The doors open. Music pulses through the speakers. The neon signs flicker to life.{/i}"

    if on_duty_count == 1:
        "{i}With just one person working, it's going to be a quiet night.{/i}"
    elif on_duty_count <= 3:
        "{i}A decent crew tonight. Should be able to handle a moderate crowd.{/i}"
    else:
        "{i}Full staff on deck. Tonight should be profitable.{/i}"

    ## Calculate average performance
    python:
        total_perf = sum(s.performance for s in staff_manager.get_on_duty())
        avg_perf = total_perf // max(1, on_duty_count)

    if avg_perf >= 70:
        "{i}The staff moves like clockwork — drinks flow, conversations spark, the atmosphere is electric.{/i}"
    elif avg_perf >= 40:
        "{i}Decent service, if not spectacular. The regulars seem satisfied.{/i}"
    else:
        "{i}A few stumbles tonight. The new hires are still finding their rhythm.{/i}"

    ## Process reputation
    $ reputation.process_nightly(avg_perf, upgrade_manager.get_venue_level())

    ## Revenue calculation with upgrade multiplier
    python:
        nightly_rev = economy.calculate_nightly_revenue(staff_manager, reputation, clock)
        nightly_rev = int(nightly_rev * upgrade_manager.get_revenue_multiplier())
        economy.earn(nightly_rev, "Nightly business")

    system "Tonight's revenue: {color=#39ff14}+¥[nightly_rev:,]{/color}"

    ## Weekend bonus note
    if clock.is_weekend:
        system "{color=#ffe600}Weekend bonus applied!{/color}"

    ## Advance to night / next day
    $ clock.advance()

    ## Check for late-night event
    $ event = event_manager.check_events(clock, reputation, economy)
    if event is not None:
        jump event_scene

    jump end_of_day


## ─── End of Day Processing ───
label end_of_day:

    scene black with dissolve

    ## Process daily expenses
    $ expenses = economy.calculate_daily_expenses(staff_manager, upgrade_manager.get_venue_level())
    $ economy.spend(expenses, "Daily expenses")

    ## Staff end-of-day
    $ staff_manager.process_end_of_day()

    ## Reset events
    $ event_manager.reset_daily()

    ## Weekly refresh of hires
    if clock.day % 7 == 0:
        $ staff_manager.refresh_hires()
        system "New talent available at the agency!"

    ## Danger decay
    if reputation.danger > 0:
        $ reputation.adjust_danger(-2)

    ## Show nightly report
    system "═══ END OF DAY [clock.day - 1] REPORT ═══"

    python:
        last_rev = economy.total_earned  # simplified
        report_text = "Expenses: ¥{:,}  |  Balance: ¥{:,}".format(expenses, economy.money)

    system "[report_text]"

    $ days_survived += 1

    ## Check game over
    if economy.money < 0:
        jump game_over_broke

    ## Advance to morning
    if clock.time_of_day != "Morning":
        $ clock.advance_to_morning()

    system "[clock.icon] A new day dawns. Day [clock.day] — [clock.day_of_week]."

    jump main_loop


## ─── Game Over Screens ───
label game_over_broke:
    scene black with dissolve

    system "═══ GAME OVER ═══"

    "{i}The creditors came calling. The lights went dark. The Nexus goes silent for the last time.{/i}"

    "{i}In a city that never sleeps, your dream finally did.{/i}"

    system "You survived [days_survived] days."

    menu:
        "Try Again":
            jump start
        "Main Menu":
            return
