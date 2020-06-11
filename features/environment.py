# importação do webdriver do selenium
from selenium import webdriver

# função que irá criar uma instância webdriver
def before_all(context):
	context.web = webdriver.Chrome()

# função que irá imprimir sempre após algum step
def after_step(context, step):
	print()

# função que irá encerrar a instância após a execução
def after_all(context):
	context.web.quit()
