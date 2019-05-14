import pygame

class State:
	def __init__(self, scale, state=None):
		if state:
			self.robo = state[0]
			self.acumulado = state[1]
			self.sujeiras = state[2]
			self.contador = state[3]
			self.mapa = state[4]
			self.lixos = state[5]
			self.paredes = state[6]
			self.elevadores = state[7]
			self.power_station = state[8]
		else:
			self.robo = []
			self.acumulado = 0
			self.sujeiras = []
			self.contador = 0
			self.mapa = []
			self.lixos = []
			self.paredes = []
			self.elevadores = []
			self.power_station = []
		self.scale = scale

	def desenha(self, screen):
		robo = pygame.image.load("robo.png")
		sujeira = pygame.image.load("sujeira.png")
		lixo = pygame.image.load("lixo.png")
		elevador = pygame.image.load("elevador.png")
		parede = pygame.image.load("parede.png")
		fundo = pygame.image.load("fundo.png")
		power = pygame.image.load("power.png")
		robo = pygame.transform.scale(robo, (self.scale, self.scale))
		sujeira = pygame.transform.scale(sujeira, (self.scale, self.scale))
		lixo = pygame.transform.scale(lixo, (self.scale, self.scale))
		elevador = pygame.transform.scale(elevador, (self.scale, self.scale))
		parede = pygame.transform.scale(parede, (self.scale, self.scale))
		fundo = pygame.transform.scale(fundo, (self.scale, self.scale))
		power = pygame.transform.scale(power, (self.scale, self.scale))
		for i in  range(self.mapa[0]):
			for j in range(self.mapa[1]):
				screen.blit(fundo, pygame.Rect(i*self.scale, (self.mapa[1] - j - 1)*self.scale, self.scale, self.scale))
		for e in self.elevadores:
			screen.blit(elevador, pygame.Rect(e[0]*self.scale, (self.mapa[1] - e[1] - 1)*self.scale, self.scale, self.scale))
		for p in self.paredes:
			screen.blit(parede, pygame.Rect(p[0]*self.scale, (self.mapa[1] - p[1] - 1)*self.scale, self.scale, self.scale))
		if len(self.power_station) > 0:	
			screen.blit(power, pygame.Rect(self.power_station[0]*self.scale, (self.mapa[1] - self.power_station[1] - 1)*self.scale, self.scale, self.scale))
		for l in self.lixos:
			screen.blit(lixo, pygame.Rect(l[0]*self.scale, (self.mapa[1] - l[1] - 1)*self.scale, self.scale, self.scale))
		for s in self.sujeiras:
			screen.blit(sujeira, pygame.Rect(s[0]*self.scale, (self.mapa[1] - s[1] - 1)*self.scale, self.scale, self.scale))
		if len(self.robo) > 0:	
			screen.blit(robo, pygame.Rect(self.robo[0]*self.scale, (self.mapa[1] - self.robo[1] - 1)*self.scale, self.scale, self.scale))

	def getState(self):
		state = []
		state.append(self.robo)
		state.append(self.acumulado)
		state.append(self.sujeiras)
		state.append(self.contador)
		state.append(self.mapa)
		state.append(self.lixos)
		state.append(self.paredes)
		state.append(self.elevadores)
		state.append(self.power_station)
		return state

	def setRobo(self,x,y):
		self.robo = [x, y]

	def addSujeira(self,x,y):
		self.sujeiras.append([x,y])
		self.contador = self.contador + 1

	def removeSujeira(self,x,y):
		self.sujeiras.remove([x,y])
		self.contador = self.contador - 1

	def setMapa(self,x,y):
		self.mapa = [x,y]

	def addLixo(self,x,y):
		self.lixos.append([x,y])

	def removeLixo(self,x,y):
		self.lixos.remove([x,y])

	def addParede(self,x,y):
		self.paredes.append([x,y])

	def removeParede(self,x,y):
		self.paredes.remove([x,y])

	def addElevador(self,x,y):
		self.elevadores.append([x,y])

	def removeElevador(self,x,y):
		self.elevadores.remove([x,y])

	def setPowerStation(self,x,y):
		self.power_station = [x,y]

