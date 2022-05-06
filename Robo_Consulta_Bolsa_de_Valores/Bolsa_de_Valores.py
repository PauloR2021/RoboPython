#Iniciando as Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import xlrd
import smtplib



# Iniciando Robo
print('Iniciando o Robo !!!')


#Primeira Fase
#Criando Arquivos XLS e TXT para salvar as informações

m_a = open('Maiores_Altas.xls', 'w')
m_b = open('Maiores_Baixa.xls','w')
m_n = open('Maiores_Negociaveis.xls','w')
m_todas = open('Bolsa de Valores.txt','w')

# Chamando o WebDrive para abrir site de cotações
driver =webdriver.Chrome('C:/Users/Paulo Ricardo/Desktop/GIT/Robo de Python/Robo_Consulta_Bolsa_de_Valores/chromedriver')
driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

#Pegando as informações do Site
bolsa_alta = driver.find_element(By.XPATH,"/html/body/div[5]/article/div[2]/div/div[1]/div/div/div[3]/section[1]/div/div[1]").text
bolsa_baixa = driver.find_element(By.XPATH,'/html/body/div[5]/article/div[2]/div/div[1]/div/div/div[3]/section[1]/div/div[2]').text
bolsa_mais_negocio = driver.find_element(By.XPATH,'/html/body/div[5]/article/div[2]/div/div[1]/div/div/div[3]/section[1]/div/div[3]').text

#Salvando as Informações em seus respectivos arquivos
m_a.write(bolsa_alta)
m_b.write(bolsa_baixa)
m_n.write(bolsa_mais_negocio)
m_todas.write(f'As Maiores são {bolsa_baixa}\n'
              f'\nAs Menores são {bolsa_baixa}\n'
              f'\nAs Mais Negociaveis são {bolsa_mais_negocio}')

#Tempo de 2 Segundo para o Robo começar a Segunda Fase
time.sleep(2)

#Segunda Fase
#Criando os dados para Mandar o E-mail
de = 'projetospython1@gmail.com'
para = 'projetospython1@gmail.com'
msg=MIMEMultipart()

msg['from'] = de
msg['To']=para
msg['Subject']='Cotação da Bolsa de Valores'

#Criando o E-mail em HTML
link='''
<html>
	<body>
		<body bgcolor = #2E2E2E> </body bgcolor>
		<title> Bolsa de valores </title>
		<h3> Bom dia. No e-mail contém as informações atualizadas da atual bolsa de valores,
			Link na descrição 
		<h3>
		
		<p><a href = "<div class="row">  <div class="col-lg-8 col-md-8 col-sm-8 col-xs-8"><h3 class="data-table no-gutter">Maiores altas</h3><table class="data-table"><tbody>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/goau4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">GOAU4.SA</a></td><td class="up"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/goau4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">+3,36%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/goau4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 11,68</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/suzb3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">SUZB3.SA</a></td><td class="up"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/suzb3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">+2,59%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/suzb3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 52,70</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ggbr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">GGBR4.SA</a></td><td class="up"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ggbr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">+2,08%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ggbr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 27,98</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/klbn11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">KLBN11.SA</a></td><td class="up"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/klbn11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">+0,81%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/klbn11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 22,42</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">PETR4.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-0,06%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 32,05</a></td></tr>  </tbody></table></div>   <div class="col-lg-8 col-md-8 col-sm-8 col-xs-8"><h3 class="data-table no-gutter">Maiores baixas</h3><table class="data-table"><tbody>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/tots3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">TOTS3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/tots3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-10,97%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/tots3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 28,65</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">MGLU3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-10,71%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 4,42</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">BIDI11.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,85%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 14,22</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">CIEL3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,48%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 3,13</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">BIDI4.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,22%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 4,80</a></td></tr>  </tbody></table></div>   <div class="col-lg-8 col-md-8 col-sm-8 col-xs-8"><h3 class="data-table no-gutter">Mais negociadas</h3><table class="data-table"><tbody>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">MGLU3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-10,71%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 4,42</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">PETR4.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-0,06%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 32,05</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">CIEL3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,48%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 3,13</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/hapv3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">HAPV3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/hapv3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,04%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/hapv3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 8,12</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bbdc4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">BBDC4.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bbdc4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-3,06%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bbdc4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 17,77</a></td></tr>  </tbody></table></div> </a href>
		
		<p>
		
			<font color = #0101DF> <a href ="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/goau4-sa/"> Link- Clique Aqui </ a href> </font color>
		</P>
	<body>
</html>
'''



html = MIMEText(link, "html")
msg.attach(html)

#Enviando E-mail
s= smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(de,"20252520")
text = msg.as_string()
s.sendmail(de,para,text)
s.quit()
print('E-mail enviado !!!')
driver.close()

print('Acesse o Gmail: projetospython1@gmail.com com a Senha = 20252520')

#Terceira Fase

#abrindo o E-mail'''

'''emails = webdriver.Chrome('C:/Users/Paulo Ricardo/Desktop/Projeto/chromedriver')
emails.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

campo = emails.find_element(By.XPATH, "//*[@id='identifierId']")

campo.clear()
digite ='projetospython1@gmail.com'
time.sleep(1)
campo.send_keys(digite)
campo.send_keys(Keys.ENTER)

senha = emails.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/div')
senha.click()
senha=emails.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/div').send_keys('20252520')'''





