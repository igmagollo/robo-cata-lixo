import sys, os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from State import State
import ast

tamanho = [int(a) for a in input("Tamanho: ").split()]
initial_state = ast.literal_eval(input("Estado inicial: "))
scale = 600 // max(tamanho)
pygame.init()
size = width, heith = tamanho[0] * scale, tamanho[1] * scale
screen = pygame.display.set_mode(size)
delay = 30

bashCommand = "swipl -s robo_data_base.pl -g 'solucao(" + str(initial_state) + ", X), write(X),halt' > result.txt"
os.system(bashCommand)
f = open("./result.txt","r")
solution = ast.literal_eval(f.read())
f.close()
initial_state = State(scale, initial_state)
states = []
try:
	states = [State(scale, a) for a in solution]
except:
	print("error")
show_solution = False


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				show_solution = True
	if show_solution:
		if len(states):
			current = states.pop()
			current.desenha(screen)
			pygame.time.wait(delay)
	else:
		initial_state.desenha(screen)
	pygame.display.flip()
