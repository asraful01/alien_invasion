class Settings:
    """A class to store all settings for the game"""


    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width= 1200
        self.screen_height= 800
        self.bg_color= (230,230,230)

        #Ship settings
        self.ship_speed=1.5

        #bullet settings
        self.bullet_speed = 1.5
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed= 3
        #Alien Settings
        self.alien_speed= 1.0
        self.fleet_drop_speed=10
        #fleet_directoin of 1 represents right; -1 represent left
        self.fleet_direction = 1


