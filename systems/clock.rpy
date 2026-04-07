################################################################################
## systems/clock.rpy — Day/Night Cycle & Time Management
################################################################################

init python:
    class GameClock:
        """Manages the flow of time in Brothel Connection."""

        PERIODS = ["Morning", "Afternoon", "Evening", "Night"]
        PERIOD_ICONS = {
            "Morning": "☀",
            "Afternoon": "◑",
            "Evening": "☾",
            "Night": "★"
        }

        def __init__(self, day=1, period_index=0):
            self.day = day
            self.period_index = period_index
            self.week = 1

        @property
        def time_of_day(self):
            return self.PERIODS[self.period_index]

        @property
        def icon(self):
            return self.PERIOD_ICONS[self.time_of_day]

        @property
        def day_of_week(self):
            days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"]
            return days[(self.day - 1) % 7]

        @property
        def is_weekend(self):
            return self.day_of_week in ("Saturday", "Sunday")

        @property
        def is_business_hours(self):
            return self.time_of_day in ("Evening", "Night")

        @property
        def is_night(self):
            return self.time_of_day == "Night"

        def advance(self):
            """Advance to the next time period. Returns True if a new day starts."""
            self.period_index += 1
            if self.period_index >= len(self.PERIODS):
                self.period_index = 0
                self.day += 1
                self.week = (self.day - 1) // 7 + 1
                return True
            return False

        def advance_to_evening(self):
            """Skip ahead to Evening (business start)."""
            self.period_index = 2  # Evening

        def advance_to_morning(self):
            """Skip to next Morning (new day)."""
            self.period_index = 0
            self.day += 1
            self.week = (self.day - 1) // 7 + 1

        def get_display(self):
            return "{} {} — Day {} ({})".format(
                self.icon, self.time_of_day, self.day, self.day_of_week
            )

        def get_short_display(self):
            return "Day {} {} {}".format(self.day, self.icon, self.time_of_day)
