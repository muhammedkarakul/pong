import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PONG")

running = True

# Paddle properties
paddle_x = 50
paddle_y = 250
paddle_width = 15
paddle_height = 90
paddle_speed = 1

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((0, 0, 0)) 
	pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
	pygame.display.flip()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddle_y -= paddle_speed
	if keys[pygame.K_s]:
		paddle_y += paddle_speed
pygame.quit()
