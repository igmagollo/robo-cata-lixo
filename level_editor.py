import sys, os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from State import State

map_size = input()
x, y = map_size.split()
x, y = int(x), int(y)
scale = 600 // max(x,y)
initial_state = State(scale=scale)
initial_state.setMapa(x,y)

pygame.init()
size = width, heith = scale * x, scale * y
screen = pygame.display.set_mode(size)

robo = pygame.image.load("robo.png")
sujeira = pygame.image.load("sujeira.png")
lixo = pygame.image.load("lixo.png")
elevador = pygame.image.load("elevador.png")
parede = pygame.image.load("parede.png")
fundo = pygame.image.load("fundo.png")
power = pygame.image.load("power.png")
robo = pygame.transform.scale(robo, (scale, scale))
sujeira = pygame.transform.scale(sujeira, (scale, scale))
lixo = pygame.transform.scale(lixo, (scale, scale))
elevador = pygame.transform.scale(elevador, (scale, scale))
parede = pygame.transform.scale(parede, (scale, scale))
fundo = pygame.transform.scale(fundo, (scale, scale))
power = pygame.transform.scale(power, (scale, scale))

atual = None
function = None
remove = None

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			print(initial_state.getState())
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				atual = parede
				function = initial_state.addParede
				remove = initial_state.removeParede

			elif event.key == pygame.K_e:
				atual = elevador
				function = initial_state.addElevador
				remove = initial_state.removeElevador

			elif event.key == pygame.K_l:
				atual = lixo
				function = initial_state.addLixo
				remove = initial_state.removeLixo

			elif event.key == pygame.K_s:
				atual = sujeira
				function = initial_state.addSujeira
				remove = initial_state.removeSujeira

			elif event.key == pygame.K_r:
				atual = robo
				function = initial_state.setRobo
				remove = None

			elif event.key == pygame.K_t:
				atual = power
				function = initial_state.setPowerStation
				remove = None

			elif event.key == pygame.K_RETURN:
				if function:
					function(mouse_x // scale, (heith - mouse_y - scale) // scale)
			elif event.key == pygame.K_BACKSPACE:
				if function:
					remove(mouse_x // scale, (heith - mouse_y - scale) // scale)

	initial_state.desenha(screen)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	mouse_x = (mouse_x // scale) * scale 
	mouse_y = (mouse_y // scale) * scale
	if atual:
		screen.blit(atual, pygame.Rect(mouse_x, mouse_y, scale, scale));
	
	pygame.display.flip()
	