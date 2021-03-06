class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings"""
		# screen settings
		self.screen_width = 640
		self.screen_height = 480
		self.bg_color = (200,20,210)
		# Ship settings
		self.ship_speed_factor = 1.5
		# Bullet Settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60

	