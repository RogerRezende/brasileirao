#language: pt
Funcionalidade: Consultar Classificação do Alemão

	'''Eu como usuário quero acessar a página de classificação
	do Campeonato Alemão no Globoesporte para consultar o
	último colocado.'''

	Cenário: Consultar Último Colocado no Alemão
	Dado acesso a página inicial do Globoesporte
	Quando clico no menu do alemão
	E classificação é exibida
	Então devo saber quem é o último colocado