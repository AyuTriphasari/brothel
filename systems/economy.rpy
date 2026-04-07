################################################################################
## systems/economy.rpy — Financial System
################################################################################

init python:
    class Economy(object):
        """Manages all finances for Brothel Connection."""

        def __init__(self, starting_money=5000):
            self.money = starting_money
            self.daily_revenue = 0
            self.daily_expenses = 0
            self.total_earned = 0
            self.total_spent = 0
            self.transaction_log = []
            self.nightly_reports = []

        def earn(self, amount, source="Unknown"):
            """Add money from a revenue source."""
            self.money += amount
            self.daily_revenue += amount
            self.total_earned += amount
            self.transaction_log.append({
                "type": "income",
                "amount": amount,
                "source": source
            })
            return True

        def spend(self, amount, reason="Unknown"):
            """Spend money. Returns True if transaction succeeds."""
            if amount > self.money:
                return False
            self.money -= amount
            self.daily_expenses += amount
            self.total_spent += amount
            self.transaction_log.append({
                "type": "expense",
                "amount": amount,
                "reason": reason
            })
            return True

        def can_afford(self, amount):
            return self.money >= amount

        def calculate_nightly_revenue(self, staff_manager, reputation, clock):
            """Calculate revenue from a night of business."""
            base_revenue = 0

            # Revenue from active staff
            for s in staff_manager.get_on_duty():
                performance = (s.charisma + s.skill) / 2
                mood_multiplier = s.mood / 100.0
                base_revenue += int(performance * mood_multiplier * 2)

            # Weekend bonus (30%)
            if clock.is_weekend:
                base_revenue = int(base_revenue * 1.3)

            # Reputation multiplier
            rep_mult = 1.0 + (reputation.fame / 1000.0)
            quality_mult = 1.0 + (reputation.quality / 200.0)
            base_revenue = int(base_revenue * rep_mult * quality_mult)

            return max(base_revenue, 0)

        def calculate_daily_expenses(self, staff_manager, venue_level):
            """Calculate fixed daily costs."""
            # Base rent scales with venue level
            rent = 200 + (venue_level * 100)

            # Staff salaries
            salaries = sum(s.salary for s in staff_manager.roster)

            # Supplies/maintenance
            supplies = 50 + (venue_level * 25)

            return rent + salaries + supplies

        def process_end_of_day(self, staff_manager, reputation, venue_level, clock):
            """Process all end-of-day finances."""
            revenue = self.calculate_nightly_revenue(
                staff_manager, reputation, clock
            )
            expenses = self.calculate_daily_expenses(
                staff_manager, venue_level
            )

            self.earn(revenue, "Nightly business")
            self.spend(expenses, "Daily expenses")

            profit = revenue - expenses
            report = {
                "day": clock.day,
                "revenue": revenue,
                "expenses": expenses,
                "profit": profit,
                "balance": self.money
            }
            self.nightly_reports.append(report)

            # Reset daily counters
            self.daily_revenue = 0
            self.daily_expenses = 0

            return report

        def get_formatted_money(self):
            """Return money as formatted string with currency symbol."""
            return "¥{:,}".format(self.money)

        def get_last_report(self):
            if self.nightly_reports:
                return self.nightly_reports[-1]
            return None
