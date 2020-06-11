# importação do given, when e then do behave
from behave import given, when, then

# variável que irá receber a URL do site que iremos interagir
base_url = 'http://globoesporte.globo.com/'

# variável que irá receber o elemento do menu-button que iremos interagir
element_menu = 'menu-button'

# variável que irá receber o elemento das tabelas que iremos interagir
element_link_tabelas = 'menu-1-tabelas'

# variável que irá receber o elemento das tabelas dos campeonatos nacionais que iremos interagir
element_link_nacionais = 'menu-2-nacionais'

# variável que irá receber o elemento da tabela do brasileirão série a que iremos interagir
element_link_brasileirao_a = 'menu-3-brasileirao-serie-a'

# variável que irá receber o elemento do primeiro colocado da tabela
get_primeiro = '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr[1]/td[2]/strong'

# configuração do step given
@given(u'acesso a página inicial do Globoesporte')
def step_impl(context):
	# irá acessar a página que escolhemos
	context.web.get(base_url)
	# raise NotImplementedError(u'STEP: Given acesso a página inicial do Globoesporte')

# configuração do primeiro step when
@when(u'clico no menu do brasileirão')
def step_impl(context):
	# irá procurar no código da página o elemento com o class name necessário para acessar o menu
	context.element_menu = context.web.find_element_by_class_name(element_menu)
	# irá realizar o clique do menu
	context.element_menu.click()

	# irá procurar no código da página o elemento com o id necessário para acessar as tabelas
	context.element_link_tabelas = context.web.find_element_by_id(element_link_tabelas)
	# irá realizar o clique das tabelas
	context.element_link_tabelas.click()

	# irá procurar no código da página o elemento com o id necessário para acessar as tabelas nacionais
	context.element_link_nacionais = context.web.find_element_by_id(element_link_nacionais)
	# irá realizar o clique das tabelas nacionais
	context.element_link_nacionais.click()

	# irá procurar no código da página o elemento com o id necessário para acessar a tabela do brasileirão série a
	context.element_link_brasileirao_a = context.web.find_element_by_id(element_link_brasileirao_a)
	# irá realizar o clique da tabela do brasileirão série a
	context.element_link_brasileirao_a.click()
	# raise NotImplementedError(u'STEP: When clico no menu do brasileirão')

# configuração do segundo step when
@when(u'classificação é exibida')
def step_impl(context):
	# irá procurar no código da página o elemento com o xpath necessário para pegar o primeiro colocado
	context.get_primeiro = context.web.find_element_by_xpath(get_primeiro)
	# raise NotImplementedError(u'STEP: When classificação é exibida')

# configuração do step then
@then(u'devo saber quem é o primeiro colocado')
def step_impl(context):
	# irá receber o texto do primeiro colocado
	primeiro = context.get_primeiro.text

	# imprime o primeiro colocado
	print(primeiro)

	# irá abrir o arquivo results.txt para leitura
	file = open('R:\\Documentos\\projetos\\brasileirao\\features\\results\\results.txt', 'r')
	# irá ler as linhas do arquivo
	content = file.readlines()
	# irá incluir um \n e depois o primeiro colocado
	content.append('\n' + primeiro)
	# irá abrir o arquivo results.txt para escrita
	file = open('R:\\Documentos\\projetos\\brasileirao\\features\\results\\results.txt', 'w')
	# irá escrever o content no arquivo results.txt
	file.writelines(content)
	# raise NotImplementedError(u'STEP: Then devo saber quem é o primeiro colocado')
