%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Códigos vistos em aula
%
% solucao por busca em largura (bl)
solucao_bl(Inicial,Solucao) :- bl([[Inicial]],Solucao).
% Se o primeiro estado de F for meta, então o retorna com o caminho
bl([[Estado|Caminho]|_],[Estado|Caminho]) :- meta(Estado).
% falha ao encontrar a meta, então estende o primeiro estado até seus sucessores e os coloca no final da lista de fronteira
bl([Primeiro|Outros], Solucao) :- estende(Primeiro,Sucessores),
								concatena(Outros,Sucessores,NovaFronteira),
								bl(NovaFronteira,Solucao).
% metodo que faz a extensao do caminho até os nós filhos do estado
estende([Estado|Caminho],ListaSucessores):- bagof(
 												[Sucessor,Estado|Caminho],
 												(s(Estado,Sucessor),not(pertence(Sucessor,[Estado|Caminho]))),
					 							ListaSucessores),!.
% se o estado não tiver sucessor, falha e não procura mais (corte)
estende( _ ,[]).
%solucao por busca em profundidade (bp)
solucao_bp(Inicial,Solucao) :- bp([],Inicial,Solucao).
%Se o primeiro estado da lista é meta, retorna a meta
bp(Caminho,Estado,[Estado|Caminho]) :- meta(Estado).
%se falha, coloca o no caminho e continua a busca
bp(Caminho,Estado,Solucao) :- s(Estado,Sucessor),
not(pertence(Sucessor,[Estado|Caminho])),
 bp([Estado|Caminho],Sucessor,Solucao).

concatena([ ],L,L).
concatena([Cab|Cauda],L2,[Cab|Resultado]) :- concatena(Cauda,L2,Resultado).
pertence(Elem,[Elem|_ ]).
pertence(Elem,[ _| Cauda]) :- pertence(Elem,Cauda).
retirar_elemento(Elem,[Elem|Cauda],Cauda).
retirar_elemento(Elem,[Cabeca|Cauda],[Cabeca|Resultado]) :- retirar_elemento(Elem,Cauda,Resultado).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% formatoe estado
% [R, N, S, C, M, L, P, E, Pw]
anda_lado(Rx, NRx, Max) :- NRx is (Rx + 1), NRx < Max.
anda_lado(Rx, NRx, _) :- NRx is (Rx - 1), NRx >= 0.

pega_sujeira(Robo, Sujeiras, Acumulo, Contador, NSujeiras, NAcumulo, NContador) :- 
	pertence(Robo, Sujeiras),
	Acumulo < 2,
	retirar_elemento(Robo, Sujeiras, NSujeiras),
	NContador is (Contador - 1), NAcumulo is (Acumulo + 1).

joga_sujeira_lixo(Robo, S_acumulada, Lixos, NS_acumulada) :- 
	pertence(Robo, Lixos), 
	S_acumulada > 0, 
	NS_acumulada is 0.

anda_vertical([X,Y], Elevadores, [X, Ny]) :- 
	pertence([X,Y], Elevadores), 
	(Ny is Y + 1; Ny is Y - 1), 
	pertence([X, Ny], Elevadores).


s([Robo, S_acumulada, Sujeiras, Contador | Cauda], 
	[Robo, NS_acumulada, NSujeiras, NContador | Cauda]) :- 
	pega_sujeira(Robo, Sujeiras, S_acumulada, Contador, NSujeiras, NS_acumulada, NContador),!.


s([Robo, S_acumulada, Sujeiras, Contador, Mapa, Lixos| Cauda], 
	[Robo, NS_acumulada, Sujeiras, Contador, Mapa, Lixos| Cauda]) :-
	joga_sujeira_lixo(Robo, S_acumulada, Lixos, NS_acumulada),!.

s([[X,Y], S_acumulada, Sujeiras, Contador, [Mx, My], Lixos, Paredes| Cauda], 
	[[NRx,Y], S_acumulada, Sujeiras, Contador, [Mx, My], Lixos, Paredes| Cauda]) :- 
	anda_lado(X, NRx, Mx),
	not(pertence([NRx, Y], Paredes)).

s([Robo, S_acumulada, Sujeiras, Contador, Mapa, Lixos, Paredes, Elevadores, Power], 
	[NRobo, S_acumulada, Sujeiras, Contador, Mapa, Lixos, Paredes, Elevadores, Power]) :-
	anda_vertical(Robo, Elevadores, NRobo).

meta([Robo, S_acumulada, _, Contador, _, _, _, _, Power]) :- 
	Robo = Power, Contador = 0, S_acumulada = 0.
