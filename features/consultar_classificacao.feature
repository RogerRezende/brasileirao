#language: pt
Funcionalidade: Consultar Classificação do Brasileirão

	'''Eu como usuário quero acessar a página de classificação
	do Campeonato Brasileiro no Globoesporte para consultar o
	primeiro e último colocado.'''

	Cenário: Consultar Primeiro Colocado no Brasileirão
	Dado acesso a página inicial do Globoesporte
	Quando clico no menu do brasileirão
	E classificação é exibida
	Então devo saber quem é o primeiro colocado

	Cenário: Consultar Último Colocado no Brasileirão
	Quando classificação é exibida do último colocado
	Então devo saber quem é o último colocado