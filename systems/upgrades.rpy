################################################################################
## systems/upgrades.rpy — Venue Upgrade System
################################################################################

init python:
    class Upgrade:
        """Represents a single venue upgrade."""

        def __init__(self, uid, name, description, cost, category,
                     prereqs=None, bonuses=None, icon="◆"):
            self.uid = uid
            self.name = name
            self.description = description
            self.cost = cost
            self.category = category  # "decor", "security", "entertainment", "vip"
            self.prereqs = prereqs or []  # list of upgrade uids required
            self.bonuses = bonuses or {}  # {"fame": 10, "quality": 5, ...}
            self.purchased = False
            self.icon = icon

        def can_purchase(self, economy, purchased_ids):
            """Check if this upgrade can be bought."""
            if self.purchased:
                return False
            if not economy.can_afford(self.cost):
                return False
            for req in self.prereqs:
                if req not in purchased_ids:
                    return False
            return True

        def get_bonus_text(self):
            parts = []
            labels = {
                "fame": "Fame",
                "quality": "Quality",
                "revenue_mult": "Revenue",
                "max_staff": "Staff Slots",
                "danger_reduction": "Heat Reduction"
            }
            for key, val in self.bonuses.items():
                name = labels.get(key, key)
                if key == "revenue_mult":
                    parts.append("+{}% {}".format(int(val * 100), name))
                else:
                    parts.append("+{} {}".format(val, name))
            return ", ".join(parts) if parts else "Cosmetic"


    class UpgradeManager:
        """Manages all venue upgrades."""

        CATEGORIES = {
            "decor": {"label": "Décor", "color": "#b000ff"},
            "security": {"label": "Security", "color": "#ff1744"},
            "entertainment": {"label": "Entertainment", "color": "#00f0ff"},
            "vip": {"label": "VIP", "color": "#ffe600"},
        }

        def __init__(self):
            self.upgrades = self._create_upgrade_tree()
            self.purchased_ids = []

        def _create_upgrade_tree(self):
            return [
                # ── Décor ──
                Upgrade("neon_signs", "Neon Signage", "Eye-catching neon signs attract passersby.",
                        500, "decor", bonuses={"fame": 15, "quality": 5}, icon="💡"),
                Upgrade("ambient_lighting", "Ambient Lighting", "Mood lighting with color-shifting LEDs.",
                        800, "decor", prereqs=["neon_signs"],
                        bonuses={"quality": 10, "fame": 5}, icon="✨"),
                Upgrade("holo_decor", "Holographic Décor", "Projection-mapped walls and floating displays.",
                        2000, "decor", prereqs=["ambient_lighting"],
                        bonuses={"fame": 25, "quality": 15}, icon="🌀"),

                # ── Security ──
                Upgrade("bouncers", "Door Security", "Professional bouncers maintain order.",
                        600, "security", bonuses={"danger_reduction": 10, "quality": 5}, icon="🛡"),
                Upgrade("cameras", "Surveillance System", "Cameras covering all areas.",
                        1200, "security", prereqs=["bouncers"],
                        bonuses={"danger_reduction": 15}, icon="📹"),
                Upgrade("cyber_defense", "Cyber Defense Net", "Anti-intrusion countermeasures.",
                        3000, "security", prereqs=["cameras"],
                        bonuses={"danger_reduction": 25, "fame": 10}, icon="🔒"),

                # ── Entertainment ──
                Upgrade("sound_system", "Sound System", "Premium speakers and bass rigs.",
                        700, "entertainment", bonuses={"quality": 10, "fame": 5}, icon="🔊"),
                Upgrade("dance_floor", "Light-Up Dance Floor", "Interactive LED dance floor.",
                        1500, "entertainment", prereqs=["sound_system"],
                        bonuses={"quality": 15, "fame": 15, "revenue_mult": 0.1}, icon="💃"),
                Upgrade("live_stage", "Live Performance Stage", "A stage for live acts and shows.",
                        3500, "entertainment", prereqs=["dance_floor"],
                        bonuses={"fame": 30, "revenue_mult": 0.2}, icon="🎤"),

                # ── VIP ──
                Upgrade("vip_lounge", "VIP Lounge", "An exclusive area for high-paying clients.",
                        2000, "vip", bonuses={"revenue_mult": 0.15, "fame": 10}, icon="👑"),
                Upgrade("private_rooms", "Private Rooms", "Discreet private entertainment suites.",
                        4000, "vip", prereqs=["vip_lounge"],
                        bonuses={"revenue_mult": 0.25, "fame": 20}, icon="🚪"),
                Upgrade("penthouse", "Penthouse Suite", "The ultimate VIP experience.",
                        8000, "vip", prereqs=["private_rooms"],
                        bonuses={"revenue_mult": 0.4, "fame": 50, "quality": 20}, icon="🏆"),
            ]

        def purchase(self, uid, economy):
            """Buy an upgrade. Returns True on success."""
            upgrade = self.get_by_id(uid)
            if not upgrade:
                return False
            if not upgrade.can_purchase(economy, self.purchased_ids):
                return False
            if economy.spend(upgrade.cost, "Upgrade: " + upgrade.name):
                upgrade.purchased = True
                self.purchased_ids.append(uid)
                return True
            return False

        def get_by_id(self, uid):
            for u in self.upgrades:
                if u.uid == uid:
                    return u
            return None

        def get_by_category(self, category):
            return [u for u in self.upgrades if u.category == category]

        def get_purchased(self):
            return [u for u in self.upgrades if u.purchased]

        def get_available(self, economy):
            return [u for u in self.upgrades
                    if u.can_purchase(economy, self.purchased_ids)]

        def get_total_bonuses(self):
            """Sum all bonuses from purchased upgrades."""
            totals = {}
            for u in self.get_purchased():
                for key, val in u.bonuses.items():
                    totals[key] = totals.get(key, 0) + val
            return totals

        def get_revenue_multiplier(self):
            bonuses = self.get_total_bonuses()
            return 1.0 + bonuses.get("revenue_mult", 0)

        def get_venue_level(self):
            """Calculate venue level from number of purchased upgrades."""
            count = len(self.purchased_ids)
            if count >= 10:
                return 5
            elif count >= 7:
                return 4
            elif count >= 4:
                return 3
            elif count >= 2:
                return 2
            return 1
