# importação do given, when e then do behave
from behave import given, when, then

# variável que irá receber a URL do site que iremos interagir
base_url = 'http://globoesporte.globo.com/'

# configuração do step given
@given(u'acesso a página inicial do Globoesporte')
def step_impl(context):
	raise NotImplementedError(u'STEP: Given acesso a página inicial do Globoesporte')


