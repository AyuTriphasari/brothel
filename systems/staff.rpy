################################################################################
## systems/staff.rpy — Staff Management System
################################################################################

init python:
    import random as _random

    class Staff:
        """Represents an individual staff member."""

        ROLES = ["Hostess", "Bartender", "Dancer", "Security", "Manager"]

        def __init__(self, name, role="Hostess", portrait=None,
                     charisma=50, skill=50, stamina=80, salary=100):
            self.name = name
            self.role = role
            self.portrait = portrait or "images/characters/default.png"

            # Core stats (0-100)
            self.charisma = min(100, max(0, charisma))
            self.skill = min(100, max(0, skill))
            self.stamina = min(100, max(0, stamina))
            self.mood = 75  # starts neutral-positive

            # Employment
            self.salary = salary
            self.on_duty = False
            self.days_employed = 0

            # Progression
            self.experience = 0
            self.level = 1

            # Relationship with player
            self.affinity = 0  # -100 to 100

            # Personality traits (affect events/dialogue)
            self.traits = []

            # Status flags
            self.is_tired = False
            self.is_sick = False

        @property
        def performance(self):
            """Overall performance score for revenue calculations."""
            base = (self.charisma + self.skill) / 2
            mood_mod = self.mood / 100.0
            stamina_mod = self.stamina / 100.0
            return int(base * mood_mod * stamina_mod)

        @property
        def stat_total(self):
            return self.charisma + self.skill + self.stamina

        def train(self, stat, amount=5):
            """Train a specific stat. Costs stamina."""
            if self.stamina < 20:
                return False
            current = getattr(self, stat, None)
            if current is None:
                return False
            new_val = min(100, current + amount)
            setattr(self, stat, new_val)
            self.stamina = max(0, self.stamina - 15)
            self.experience += amount
            self._check_level_up()
            return True

        def rest(self):
            """Recover stamina and mood."""
            self.stamina = min(100, self.stamina + 30)
            self.mood = min(100, self.mood + 10)
            self.is_tired = False

        def work_shift(self):
            """Apply effects of working a shift."""
            stamina_cost = 20 + (5 if self.mood < 30 else 0)
            self.stamina = max(0, self.stamina - stamina_cost)
            self.days_employed += 1
            self.experience += 3

            if self.stamina < 20:
                self.is_tired = True
                self.mood = max(0, self.mood - 10)

            self._check_level_up()

        def adjust_mood(self, amount):
            self.mood = min(100, max(0, self.mood + amount))

        def adjust_affinity(self, amount):
            self.affinity = min(100, max(-100, self.affinity + amount))

        def _check_level_up(self):
            threshold = self.level * 50
            if self.experience >= threshold:
                self.level += 1
                self.experience -= threshold
                # Level up bonus
                self.charisma = min(100, self.charisma + 2)
                self.skill = min(100, self.skill + 2)

        def get_mood_label(self):
            if self.mood >= 80:
                return "{color=#39ff14}Excellent{/color}"
            elif self.mood >= 60:
                return "{color=#00f0ff}Good{/color}"
            elif self.mood >= 40:
                return "{color=#ffe600}Okay{/color}"
            elif self.mood >= 20:
                return "{color=#ff00a0}Poor{/color}"
            else:
                return "{color=#ff1744}Terrible{/color}"

        def get_status_label(self):
            if self.is_sick:
                return "{color=#ff1744}✕ Sick{/color}"
            elif self.is_tired:
                return "{color=#ffe600}▲ Tired{/color}"
            elif self.on_duty:
                return "{color=#39ff14}● On Duty{/color}"
            else:
                return "{color=#666680}○ Off Duty{/color}"


    class StaffManager:
        """Manages the entire roster of staff members."""

        MAX_ROSTER = 10

        def __init__(self):
            self.roster = []
            self.available_hires = []
            self._generate_initial_hires()

        def _generate_initial_hires(self):
            """Generate pool of staff available for hiring."""
            hire_pool = [
                Staff("Nyx", "Hostess", None, 65, 45, 80, 120),
                Staff("Zara", "Dancer", None, 55, 70, 75, 150),
                Staff("Kai", "Bartender", None, 50, 65, 85, 110),
                Staff("Raven", "Hostess", None, 75, 40, 70, 140),
                Staff("Echo", "Security", None, 35, 55, 90, 130),
                Staff("Luna", "Dancer", None, 70, 60, 65, 160),
                Staff("Blade", "Security", None, 30, 50, 95, 120),
                Staff("Mira", "Hostess", None, 80, 50, 60, 170),
            ]
            for s in hire_pool:
                s.traits = _random.sample(
                    ["Charming", "Tough", "Quick Learner", "Night Owl",
                     "Social", "Reserved", "Ambitious", "Loyal"],
                    k=2
                )
            self.available_hires = hire_pool

        def hire(self, staff):
            """Hire a staff member from the available pool."""
            if len(self.roster) >= self.MAX_ROSTER:
                return False
            if staff in self.available_hires:
                self.available_hires.remove(staff)
            self.roster.append(staff)
            return True

        def fire(self, staff):
            """Remove a staff member from the roster."""
            if staff in self.roster:
                self.roster.remove(staff)
                return True
            return False

        def assign_duty(self, staff):
            staff.on_duty = True

        def remove_from_duty(self, staff):
            staff.on_duty = False

        def get_on_duty(self):
            return [s for s in self.roster if s.on_duty and not s.is_sick]

        def get_available(self):
            return [s for s in self.roster
                    if not s.on_duty and not s.is_sick and not s.is_tired]

        def process_end_of_day(self):
            """Process end-of-day for all staff."""
            for s in self.roster:
                if s.on_duty:
                    s.work_shift()
                    s.on_duty = False
                else:
                    s.rest()

        def get_roster_count(self):
            return len(self.roster)

        def get_total_salaries(self):
            return sum(s.salary for s in self.roster)

        def refresh_hires(self):
            """Refresh available hires (costs money, happens weekly)."""
            new_names = ["Sable", "Cipher", "Neon", "Pixel", "Chrome",
                         "Ghost", "Jade", "Storm", "Blaze", "Iris"]
            roles = Staff.ROLES
            self.available_hires = []
            for i in range(4):
                name = _random.choice(new_names)
                role = _random.choice(roles)
                s = Staff(
                    name, role, None,
                    charisma=_random.randint(35, 80),
                    skill=_random.randint(35, 80),
                    stamina=_random.randint(60, 95),
                    salary=_random.randint(100, 200)
                )
                s.traits = _random.sample(
                    ["Charming", "Tough", "Quick Learner", "Night Owl",
                     "Social", "Reserved", "Ambitious", "Loyal"],
                    k=2
                )
                self.available_hires.append(s)
