# Importando Todas as Bibliotecas

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlrd
#################################################################################################################################

print('Iniciando o Robô...\n')

##################################################################################################################################

# Criando um arquivo para Salvar o resultado

arq = open('resultado.txt', 'w')
##################################################################################################################################

# Abrindo a Planilha do Excel
'''
funções que não pode mudar o nome: (open_worbook, shett_by_name, nrows, ncols)
.'''

# Mostrando o Caminho do Excel
planilha = xlrd.open_workbook(
    r'C:\Users\Paulo Ricardo\Desktop\GIT\Python BOT\Robo Consulta Dominio\excel.xls')
# Criando uma váriavel para selecionar a folha aonde está os dados
folha = planilha.sheet_by_name('Plan1')
linha = folha.nrows  # Váriavel para contar as linhas da planilha
coluna = folha.ncols  # Váravel para contar as colunas da Planilha

##################################################################################################################################

# Chamando o Web Driver para abrir o Chrome

# Mostrando o Caminho do WebDriver
driver = webdriver.Chrome(
    'C:/Users/Paulo Ricardo/Desktop/GIT/Python BOT/Robo Consulta Dominio/chromedriver')
driver.get('https://registro.br/')  # Escolhendo o Site para ele abrir

###################################################################################################################################

# Criando um Laço de Repetição

'''
Esse laço conta o número de linhas da planilha, dentro do Range.
Aonde a função do range é sair do 0 e fazer a contagem pela váriavel que foi criada para a contagem das linhas
'''

for conta_linha in range(0, linha):  # Criando Condição
    # Criando a váriavel para guarda a contagem
    x = folha.cell_value(conta_linha, 0)
    # Mandando o WebDriver selecionar aonde ele vai digitar as informações
    pesquisa = driver.find_element(By.ID, 'is-avail-field')
    time.sleep(1)  # Tempo de Espera
    pesquisa.clear()  # Limpando a lacuna para ser digitalizado
    time.sleep(1)  # Tempo de Espera
    # Chamando a váriavel da contagem para escrever na lacuna
    pesquisa.send_keys(x)
    time.sleep(1)  # Tempo de Espera
    pesquisa.send_keys(Keys.RETURN)  # WebDriver da Enter para pesquisar
    time.sleep(1)  # Tempo de Espera
    # Selecionando a resposta para mostrar no Terminal
    driver.find_element(
        By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)  # Tempo de Espera
    texto = "Donínio %s %s\n" % (x, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text)  # Criando umaváriavel para guarda a resposta
    arq.write(texto)  # Escrevendo a
arq.close()
driver.close()  # fecha o WebDriver
