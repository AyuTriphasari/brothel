################################################################################
## story/prologue.rpy — Opening Sequence
################################################################################

label prologue:

    scene black with fade

    system "NEURAL LINK ESTABLISHED..."
    system "DATE: 2087.03.15 // LOCATION: NEO-TOKYO DISTRICT 9"
    system "INITIALIZING MEMORY SEQUENCE..."

    scene black with dissolve

    "{i}Rain hammers the neon-lit streets. The city never sleeps — it just changes shifts.{/i}"

    "{i}You step out of the mag-lev station, data-pad clutched in one hand, a set of old-fashioned keys in the other.{/i}"

    "{i}The keys belong to a place called 'The Nexus' — a run-down entertainment venue in the lower district.{/i}"

    "{i}Your uncle left it to you. Along with his debts.{/i}"

    pc "So this is it..."

    "{i}The building looms ahead. Dark. Quiet. A dead neon sign flickers once, twice, then dies.{/i}"

    pc "A real fixer-upper."

    "{i}Your phone buzzes. A message from someone named Maya — your uncle's old business partner.{/i}"

    maya "Hey, you made it. I know it doesn't look like much right now."

    maya "But your uncle... he saw something in this place. And in you, apparently."

    maya "Come inside. We've got work to do."

    "{i}You push through the heavy door. The interior is dusty but the bones are good — high ceilings, a long bar, space for a stage.{/i}"

    maya "First things first — we need someone to actually work here. I've got contacts at a talent agency downtown."

    maya "I also balanced the books. You've got ¥5,000 to start with. Spend it wisely."

    system "TUTORIAL: Welcome to Brothel Connection"

    maya "Let me show you how things work around here."

    maya "The {color=#00f0ff}DASHBOARD{/color} is your command center. You can manage staff, upgrade the venue, and navigate the city."

    maya "Hire your first couple of staff members. Assign them to duty before evening hits."

    maya "When you're ready, open for business. The city's nightlife waits for no one."

    maya "Oh, and one more thing — watch your {color=#ff1744}heat level{/color}. This district has eyes everywhere."

    maya "Keep a low profile until you're big enough to handle the attention."

    system "Tutorial complete. The city is yours."

    $ tutorial_complete = True

    jump main_loop


################################################################################
## Event Scene Labels — Called by the Event System
################################################################################

label event_scene:
    ## Generic event display using the active event
    $ ev = event_manager.active_event

    if ev is None:
        jump main_loop

    scene black with dissolve

    system "[ev.title]"

    "[ev.description]"

    ## Build menu from event choices
    $ choice_items = []
    $ i = 0
    python:
        for text, effects in ev.choices:
            choice_items.append((text, i))
            i += 1

    menu:
        "[ev.choices[0][0]]" if len(ev.choices) > 0:
            $ chosen = 0
        "[ev.choices[1][0]]" if len(ev.choices) > 1:
            $ chosen = 1
        "[ev.choices[2][0]]" if len(ev.choices) > 2:
            $ chosen = 2

    $ effects = event_manager.resolve_event(chosen)
    $ event_manager.apply_effects(effects, economy, reputation, staff_manager)

    ## Show effects feedback
    python:
        feedback_lines = []
        if "money" in effects:
            amt = effects["money"]
            if amt > 0:
                feedback_lines.append("{color=#39ff14}+¥" + str(amt) + "{/color}")
            else:
                feedback_lines.append("{color=#ff1744}¥" + str(amt) + "{/color}")
        if "fame" in effects:
            f = effects["fame"]
            if f > 0:
                feedback_lines.append("{color=#ff00a0}+" + str(f) + " Fame{/color}")
            else:
                feedback_lines.append("{color=#ff1744}" + str(f) + " Fame{/color}")
        if "danger" in effects:
            d = effects["danger"]
            if d > 0:
                feedback_lines.append("{color=#ffe600}+" + str(d) + " Heat{/color}")
            else:
                feedback_lines.append("{color=#39ff14}" + str(d) + " Heat{/color}")
        if "quality" in effects:
            q = effects["quality"]
            if q > 0:
                feedback_lines.append("{color=#00f0ff}+" + str(q) + " Quality{/color}")
            else:
                feedback_lines.append("{color=#ff1744}" + str(q) + " Quality{/color}")
        result_text = "  |  ".join(feedback_lines) if feedback_lines else "No significant changes."

    system "[result_text]"

    jump main_loop
