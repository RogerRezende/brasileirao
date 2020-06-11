# importação do given, when e then do behave
from behave import given, when, then

# variável que irá receber a URL do site que iremos interagir
base_url = 'http://globoesporte.globo.com/'

# configuração do step given
@given(u'acesso a página inicial do Globoesporte')
def step_impl(context):
	# irá acessar a página que escolhemos
	context.web.get(base_url)
	# raise NotImplementedError(u'STEP: Given acesso a página inicial do Globoesporte')

# configuração do primeiro step when
@when(u'clico no menu do alemão')
def step_impl(context):
	raise NotImplementedError(u'STEP: When clico no menu do brasileirão')

# configuração do segundo step when
@when(u'classificação é exibida')
def step_impl(context):
	raise NotImplementedError(u'STEP: When classificação é exibida')

# configuração do step then
@then(u'devo saber quem é o último colocado')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then devo saber quem é o primeiro colocado')
