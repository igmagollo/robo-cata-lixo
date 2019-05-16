import sys, os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from State import State
import ast

def run(initial_state):
	bashCommand = "swipl -s robo_data_base.pl -g 'solucao(" + str(initial_state) + ", X), write(X),halt' > result.txt"
	os.system(bashCommand)
	f = open("./result.txt","r")
	try:
		solution = ast.literal_eval(f.read())
	except:
		print("error")
	f.close()
	return solution

x, y = input("X Y: ").split()
x, y = int(x), int(y)
scale = 600 // max(x,y)
initial_state = State(scale=scale)
initial_state.setMapa(x,y)
delay = 100

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
editable = True
compiled = False
running = False

states = []

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			print(initial_state.getState())
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p and editable:
				atual = parede
				function = initial_state.addParede
				remove = initial_state.removeParede

			elif event.key == pygame.K_e and editable:
				atual = elevador
				function = initial_state.addElevador
				remove = initial_state.removeElevador

			elif event.key == pygame.K_l and editable:
				atual = lixo
				function = initial_state.addLixo
				remove = initial_state.removeLixo

			elif event.key == pygame.K_s and editable:
				atual = sujeira
				function = initial_state.addSujeira
				remove = initial_state.removeSujeira

			elif event.key == pygame.K_r and editable:
				atual = robo
				function = initial_state.setRobo
				remove = None

			elif event.key == pygame.K_t and editable:
				atual = power
				function = initial_state.setPowerStation
				remove = None

			elif event.key == pygame.K_ESCAPE:
				atual = None
				function = None
				remove = None

			elif event.key == pygame.K_RETURN:
				if not atual and not function and not remove:
					if not compiled:
						editable = False
						try:
							solution = run(initial_state.getState())
							states = [State(scale, a) for a in solution]
						except:
							print("error")
							pygame.mixer.music.load("fail.mp3")
							pygame.mixer.music.play()
							ticks = pygame.time.get_ticks()
							x, y = width, heith
							pygame.time.wait(900)
							while pygame.time.get_ticks() - ticks < 8000: 
								x = x + 2
								y = y + 2
								screen.blit(pygame.transform.scale(robo,(x, y)), pygame.Rect(width//2 - x//2, heith//2 - y//2, x, y))
								pygame.display.flip()

							pygame.mixer.music.stop()
							sys.exit()
						compiled = True
					else:
						running = True


		elif event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				if function:
					function(mouse_x // scale, (heith - mouse_y - scale) // scale)
			elif pygame.mouse.get_pressed()[2]:
				if remove:
					remove(mouse_x // scale, (heith - mouse_y - scale) // scale)

	if not running:
		initial_state.desenha(screen)
		mouse_x, mouse_y = pygame.mouse.get_pos()
		mouse_x = (mouse_x // scale) * scale 
		mouse_y = (mouse_y // scale) * scale
		if atual:
			screen.blit(atual, pygame.Rect(mouse_x, mouse_y, scale, scale));
	else:
		if len(states) > 0:
			current = states.pop()
			current.desenha(screen)
			pygame.time.wait(delay)

	pygame.display.flip()
	