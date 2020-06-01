import pygame

pygame.init()#иницилизация

win = pygame.display.set_mode((600, 600))#создания окна

pygame.display.set_caption(' NCoH ')#заголовок к окну

x = 60
y = 500
widht = 40#ширина
height = 60#высота
speed = 10


run = True
while run:
	
	pygame.time.delay(100)#задержка

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ran = False
			exit()

	keys = pygame.key.get_pressed()#все нажание клавиш
	if keys[pygame.K_LEFT] or keys[pygame.K_a] and x > 10:
		x -= speed
	if keys[pygame.K_RIGHT] or keys[pygame.K_d] and x < 540:
		x += speed
	if keys[pygame.K_UP] or keys[pygame.K_w] and y > 10:
		y -= speed
	if keys[pygame.K_DOWN] or keys[pygame.K_s] and y < 500:
		y +=speed

	win.fill((0, 0, 0))#зарисовка экрана
	pygame.draw.rect(win, (255, 0, 0), (x, y, widht, height))#рисоване перса

	pygame.display.update()#обновление экрана
