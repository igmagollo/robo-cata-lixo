from pyswip import Prolog
import sys, os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from State import State
import ast

tamanho = input("Tamanho: ").split()
tamanho = [int(a) for a in tamanho]
tipo = input("Tipo de Busca: ")
initial_state = ast.literal_eval(input("Estado inicial: "))
scale = 600 // max(tamanho)
pygame.init()
size = width, heith = tamanho[0] * scale, tamanho[1] * scale
screen = pygame.display.set_mode(size)
black = 0, 0, 0
delay = 50


# prolog = Prolog()
# prolog.consult("robo_data_base.pl")

# [[2,4], 0, [[1,1], [3,2], [4,2], [1,4]], 4, [5,5], [[2,0]], [[2,1],[2,2],[2,3]], [[0,0], [0,1], [1,1], [1,2], [1,3], [1,4], [3,4], [3,3], [3,2]], [3,0]]
if tipo == "largura":
	# solution = prolog.query("solucao_bl(" + str(initial_state) + ", X)")
	bashCommand = "swipl -s robo_data_base.pl -g 'solucao_bl(" + str(initial_state) + ", X), write(X),halt' > result.txt"
else:
	# solution = prolog.query("solucao_bp(" + str(initial_state) + ", X)")
	bashCommand = "swipl -s robo_data_base.pl -g 'solucao_bp(" + str(initial_state) + ", X), write(X),halt' > result.txt"
os.system(bashCommand)
f = open("./result.txt","r")
solution = ast.literal_eval(f.read())
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
