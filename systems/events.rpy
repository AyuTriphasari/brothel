################################################################################
## systems/events.rpy — Event System & Random Events
################################################################################

init python:
    import random as _random

    class GameEvent(object):
        """Represents a single game event."""

        def __init__(self, eid, title, description, event_type="random",
                     condition=None, choices=None, effects=None):
            self.eid = eid
            self.title = title
            self.description = description
            self.event_type = event_type  # "random", "story", "crisis"
            self.condition = condition    # string condition e.g. "fame >= 100"
            self.choices = choices or []  # list of (text, effects_dict)
            self.effects = effects or {}  # auto-applied effects
            self.seen = False

        def can_trigger(self, clock, reputation, economy):
            if self.condition:
                return _eval_event_condition(self.condition, clock, reputation, economy)
            return True


    def _eval_event_condition(cond, clock, reputation, economy):
        """Evaluate a string-based event condition safely."""
        try:
            return eval(cond, {"__builtins__": {}}, {
                "fame": reputation.fame,
                "quality": reputation.quality,
                "danger": reputation.danger,
                "money": economy.money,
                "day": clock.day,
                "is_weekend": clock.is_weekend,
                "time_of_day": clock.time_of_day,
            })
        except Exception:
            return False


    class EventManager(object):
        """Dispatches events based on game state."""

        def __init__(self):
            self.event_pool = self._create_events()
            self.active_event = None
            self.event_history = []
            self.events_this_day = 0

        def _create_events(self):
            return [
                # ── Positive Events ──
                GameEvent(
                    "rich_patron", "VIP Visitor",
                    "A wealthy corporate exec stumbles into your establishment, impressed by the ambiance.",
                    "random",
                    condition="fame >= 100",
                    choices=[
                        ("Roll out the red carpet", {"money": 500, "fame": 15}),
                        ("Treat them like anyone else", {"money": 200, "quality": 5}),
                    ]
                ),
                GameEvent(
                    "media_buzz", "Media Attention",
                    "A popular net-blogger wants to feature your venue on their channel.",
                    "random",
                    condition="fame >= 200",
                    choices=[
                        ("Welcome them in", {"fame": 40, "danger": 5}),
                        ("Politely decline — stay underground", {"fame": 5, "danger": -5}),
                    ]
                ),
                GameEvent(
                    "lucky_night", "Lucky Night",
                    "Something's in the air tonight — the venue is packed beyond capacity.",
                    "random",
                    choices=[
                        ("Enjoy the rush", {"money": 800}),
                    ]
                ),
                GameEvent(
                    "staff_bonding", "Staff Bonding",
                    "Your staff is in unusually high spirits tonight. Morale is infectious.",
                    "random",
                    choices=[
                        ("Join in the fun", {"staff_mood": 15, "quality": 5}),
                        ("Keep things professional", {"quality": 10}),
                    ]
                ),

                # ── Negative Events ──
                GameEvent(
                    "police_raid", "Police Inspection",
                    "Officers at the door. They want to 'inspect' the premises.",
                    "crisis",
                    condition="danger >= 30",
                    choices=[
                        ("Cooperate fully", {"money": -300, "danger": -20}),
                        ("Bribe them", {"money": -800, "danger": -10}),
                        ("Refuse entry (risky)", {"danger": 25, "fame": 10}),
                    ]
                ),
                GameEvent(
                    "rival_sabotage", "Rival Sabotage",
                    "Someone's been spreading rumors about your venue. A rival's handiwork.",
                    "crisis",
                    condition="fame >= 300",
                    choices=[
                        ("Ignore it and let quality speak", {"fame": -15, "quality": 5}),
                        ("Launch a counter-campaign", {"money": -500, "fame": 10}),
                        ("Investigate the source", {"danger": 10, "fame": 5}),
                    ]
                ),
                GameEvent(
                    "equipment_failure", "Equipment Malfunction",
                    "The main sound system blew out mid-night. Customers aren't happy.",
                    "random",
                    choices=[
                        ("Emergency repair (expensive)", {"money": -400, "quality": -5}),
                        ("Close early tonight", {"money": -200, "fame": -10}),
                    ]
                ),
                GameEvent(
                    "staff_conflict", "Staff Conflict",
                    "Two of your staff got into a heated argument in front of customers.",
                    "random",
                    choices=[
                        ("Mediate the conflict", {"staff_mood": -5, "quality": 5}),
                        ("Discipline both", {"staff_mood": -15, "quality": 10}),
                        ("Let them work it out", {"quality": -10}),
                    ]
                ),

                # ── Neutral Events ──
                GameEvent(
                    "new_trend", "New Trend",
                    "A new entertainment trend is sweeping the district. Adapt or fall behind.",
                    "random",
                    choices=[
                        ("Invest in the new trend", {"money": -600, "fame": 20, "quality": 10}),
                        ("Stick to what works", {"quality": 5}),
                    ]
                ),
                GameEvent(
                    "mysterious_offer", "Mysterious Offer",
                    "A shadowy figure approaches with a business proposition. Lucrative but risky.",
                    "random",
                    condition="day >= 7",
                    choices=[
                        ("Accept the deal", {"money": 1000, "danger": 20}),
                        ("Decline politely", {"danger": -5}),
                        ("Report to authorities", {"danger": -15, "fame": 5}),
                    ]
                ),
            ]

        def check_events(self, clock, reputation, economy):
            """Check if any event should trigger this period."""
            if self.events_this_day >= 2:
                return None

            eligible = [e for e in self.event_pool
                        if e.can_trigger(clock, reputation, economy)]

            if not eligible:
                return None

            # 40% chance of an event per time period
            if _random.random() > 0.4:
                return None

            event = _random.choice(eligible)
            self.active_event = event
            self.events_this_day += 1
            return event

        def resolve_event(self, choice_index):
            """Apply the effects of a choice. Returns the effects dict."""
            if not self.active_event or not self.active_event.choices:
                return {}

            if choice_index >= len(self.active_event.choices):
                return {}

            _, effects = self.active_event.choices[choice_index]

            self.active_event.seen = True
            self.event_history.append({
                "eid": self.active_event.eid,
                "title": self.active_event.title,
                "choice": choice_index,
                "effects": effects
            })
            self.active_event = None
            return effects

        def apply_effects(self, effects, economy, reputation, staff_manager):
            """Apply effect dict to game systems."""
            if "money" in effects:
                amt = effects["money"]
                if amt > 0:
                    economy.earn(amt, "Event bonus")
                else:
                    economy.spend(abs(amt), "Event cost")

            if "fame" in effects:
                reputation.adjust_fame(effects["fame"])

            if "quality" in effects:
                reputation.adjust_quality(effects["quality"])

            if "danger" in effects:
                reputation.adjust_danger(effects["danger"])

            if "staff_mood" in effects:
                for s in staff_manager.roster:
                    s.adjust_mood(effects["staff_mood"])

        def reset_daily(self):
            self.events_this_day = 0
