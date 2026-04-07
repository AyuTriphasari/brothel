################################################################################
## systems/reputation.rpy — Fame & Reputation System
################################################################################

init python:
    class Reputation(object):
        """Tracks the venue's public reputation and standing."""

        TIERS = [
            (0, "Unknown"),
            (100, "Hole in the Wall"),
            (250, "Local Spot"),
            (400, "Rising Star"),
            (600, "City Hotspot"),
            (800, "Underground Legend"),
            (950, "Neon Empire"),
        ]

        def __init__(self):
            self.fame = 0          # 0-1000: public awareness
            self.quality = 50      # 0-100: service quality
            self.danger = 0        # 0-100: heat from rivals/police
            self.customer_satisfaction = 70  # 0-100
            self.style_rating = 50  # 0-100: venue aesthetics

        @property
        def tier(self):
            """Get current reputation tier name."""
            result = "Unknown"
            for threshold, name in self.TIERS:
                if self.fame >= threshold:
                    result = name
            return result

        @property
        def tier_index(self):
            idx = 0
            for i, (threshold, _) in enumerate(self.TIERS):
                if self.fame >= threshold:
                    idx = i
            return idx

        @property
        def next_tier_threshold(self):
            """Fame needed for next tier."""
            current_idx = self.tier_index
            if current_idx < len(self.TIERS) - 1:
                return self.TIERS[current_idx + 1][0]
            return 1000

        @property
        def tier_progress(self):
            """Progress toward next tier (0.0 - 1.0)."""
            current_threshold = self.TIERS[self.tier_index][0]
            next_threshold = self.next_tier_threshold
            if next_threshold == current_threshold:
                return 1.0
            return (self.fame - current_threshold) / (next_threshold - current_threshold)

        def adjust_fame(self, amount):
            self.fame = min(1000, max(0, self.fame + amount))

        def adjust_quality(self, amount):
            self.quality = min(100, max(0, self.quality + amount))

        def adjust_danger(self, amount):
            self.danger = min(100, max(0, self.danger + amount))

        def process_nightly(self, staff_performance, venue_level):
            """Update reputation after a night of business."""
            # Fame grows based on quality and staff performance
            fame_gain = int((staff_performance / 100) * 5)
            fame_gain += venue_level * 2
            if self.quality > 70:
                fame_gain += 3

            self.adjust_fame(fame_gain)

            # Quality adjusts toward staff performance
            quality_delta = (staff_performance - self.quality) // 10
            self.adjust_quality(quality_delta)

            # Danger slowly decays
            if self.danger > 0:
                self.adjust_danger(-2)

            # Customer satisfaction
            sat_delta = (self.quality - 50) // 10
            self.customer_satisfaction = min(100, max(0,
                self.customer_satisfaction + sat_delta
            ))

        def get_fame_color(self):
            """Return neon color based on tier."""
            colors = [
                "#666680",  # Unknown
                "#888899",  # Hole in the Wall  
                "#aaaacc",  # Local Spot
                "#00f0ff",  # Rising Star
                "#b000ff",  # City Hotspot
                "#ff00a0",  # Underground Legend
                "#ffe600",  # Neon Empire
            ]
            return colors[min(self.tier_index, len(colors) - 1)]

        def get_danger_label(self):
            if self.danger >= 80:
                return "{color=#ff1744}CRITICAL{/color}"
            elif self.danger >= 60:
                return "{color=#ff00a0}HIGH{/color}"
            elif self.danger >= 40:
                return "{color=#ffe600}MODERATE{/color}"
            elif self.danger >= 20:
                return "{color=#00f0ff}LOW{/color}"
            else:
                return "{color=#39ff14}SAFE{/color}"
