class Settings():
    """class to store the game's settings"""

    def __init__(self):
        # screen settings
        self.screen_width = 1024
        self.screen_height = 720
        self.bg_color = (41,41,61)
        
        # ship settings
        self.ship_speed_multiplier = 1.5

        # bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 244, 197, 67
        self.bullets_allowed = 3
