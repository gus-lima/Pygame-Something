# Idle game
import configparser as cfgParser
from datetime import datetime, time
import pygame
from pygame.locals import *
import os
from pathlib import Path

FILE_DIR = Path(__file__).resolve().parent

# Configparser setup
config = cfgParser.ConfigParser()
config.read(f'{FILE_DIR}\\game_files\\game.ini')

def main():
	game_width = float(config['graphics']['resolution_width'])
	game_height = float(config['graphics']['resolution_height'])

	min_width = float(config['graphics']['resolution_width'])
	min_height = float(config['graphics']['resolution_height'])

	# Pygame setup
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((game_width, game_height), pygame.RESIZABLE)
	clock = pygame.time.Clock()
	running = True

	font = pygame.font.Font(None, 36)

	resources_manager = {}

	for idx, resource in enumerate(config['resources']):
		resources_manager[resource] = int(config['resources'][resource])

	while running:

		# Handles game quitting and resizing
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.VIDEORESIZE:
				# Enforce minimum width and height
				game_width = max(event.w, min_width)
				game_height = max(event.h, min_height)
				screen = pygame.display.set_mode((game_width, game_height), pygame.RESIZABLE)

			if event.type == pygame.KEYDOWN:
				if pygame.key.name(event.key) == "space":
					resources_manager['wood'] = int(resources_manager['wood']) + 1

		screen.fill("black")

		# Resources render
		for idx, resource in enumerate(resources_manager):
			text_surface = font.render(f'{resource} = {resources_manager[resource]}', True, (255, 255, 255))
			# Resources stays at 1% of the total width / height
			screen.blit(text_surface, (game_width * 0.01, (game_height * 0.01) + (idx * 25)))

		
		



		pygame.display.flip()

		clock.tick(60)


	pygame.quit()



if __name__ == "__main__":
	main()