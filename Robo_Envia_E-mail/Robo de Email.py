#Importando as Bibliotecas

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

print('Enviando e-mail...\n')

#criando 2 várias de quem vai enviar o e-mail e de quem vai receber o e-mail

de ='projetospython1@gmail.com' #Quem vai enviar o e-mail
para = 'projetospython1@gmail.com' #Quem vai receber o e-mail
msg= MIMEMultipart() #Função para validar os e-mails

msg ['from'] = de #Criando um laço com a função "from" aonde ele vai buscar o e-mail de quem vai enviar
msg ['To'] = para #Criando um laço com a função "To" aonde ele vai buscar o e-mail de quem vai receber
msg ['Subject']='Teste de envio com HTML' #Criando o Assunto do E-mail ( Título)


#Para Mandar arquivos ou Texto usamos esse Modulo
''' 

body = """Teste de e-mail automatico pelo Robo De e-mail. 
Aula em que faço o teste para verificar se da certo. 
""" #Corpo do Texto, aonde coloca o que você deseja no texto

msg.attach(MIMEText(body,'plain')) #Função para mandar o e-mail aonde ele faz o anexo do corpo do texto

############################################# Anexando o Arquivo #######################################################

nome_arquivo = 'panfleto.pdf' #variavel que vai o nome do arquivo

anexo=open('panfleto.pdf','rb') #Variavel para abril o arquivo

p = MIMEBase('application','octet-stream') #Chamando a função para anexar o arquivo

p.set_payload((anexo).read()) #Anexando e leando o arquivo

encoders.encode_base64(p) #Convertendo o arquivo em Base64 para poder enviar

p.add_header('content-Disposition',"attachment; filename = %s" %nome_arquivo) #indentificando o Arquivo no anexo

msg.attach(p) #Mandando o arquivo e anexando no e-mail



'''

#Para Mandar Link em HTML usamos esse outro

link= '''
<html>
	<body>
		<body bgcolor = #2E2E2E> </body bgcolor>
		<title> Bolsa de valores </title>
		<h3> Bom dia. No e-mail contém as informações atualizadas da atual bolsa de valores 
			Link na descrição 
		<h3>
		
		<p><a href = "<div class="row">  <div class="col-lg-8 col-md-8 col-sm-8 col-xs-8"><h3 class="data-table no-gutter">Maiores altas</h3><table class="data-table"><tbody>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/goau4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">GOAU4.SA</a></td><td class="up"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/goau4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">+3,36%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/goau4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 11,68</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/suzb3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">SUZB3.SA</a></td><td class="up"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/suzb3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">+2,59%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/suzb3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 52,70</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ggbr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">GGBR4.SA</a></td><td class="up"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ggbr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">+2,08%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ggbr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 27,98</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/klbn11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">KLBN11.SA</a></td><td class="up"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/klbn11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">+0,81%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/klbn11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 22,42</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">PETR4.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-0,06%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-altas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 32,05</a></td></tr>  </tbody></table></div>   <div class="col-lg-8 col-md-8 col-sm-8 col-xs-8"><h3 class="data-table no-gutter">Maiores baixas</h3><table class="data-table"><tbody>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/tots3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">TOTS3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/tots3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-10,97%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/tots3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 28,65</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">MGLU3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-10,71%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 4,42</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">BIDI11.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,85%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi11-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 14,22</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">CIEL3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,48%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 3,13</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">BIDI4.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,22%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bidi4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-baixas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 4,80</a></td></tr>  </tbody></table></div>   <div class="col-lg-8 col-md-8 col-sm-8 col-xs-8"><h3 class="data-table no-gutter">Mais negociadas</h3><table class="data-table"><tbody>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">MGLU3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-10,71%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/mglu3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 4,42</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">PETR4.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-0,06%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/petr4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 32,05</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">CIEL3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,48%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/ciel3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 3,13</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/hapv3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">HAPV3.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/hapv3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-8,04%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/hapv3-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 8,12</a></td></tr>  <tr class="dadosRankings"><td class="title" uolbpack-initialized="true"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bbdc4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">BBDC4.SA</a></td><td class="down"><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bbdc4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">-3,06%</a></td><td><a href="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/bbdc4-sa/" data-audience-click="{&quot;reference&quot;:&quot;abrir-acao-negociadas&quot;,&quot;component&quot;:&quot;stock-rankings&quot;}">R$ 17,77</a></td></tr>  </tbody></table></div> </a href>
		
		<p>
		
			<font color = #0101DF> <a href ="https://economia.uol.com.br/cotacoes/bolsas/acoes/bvsp-bovespa/goau4-sa/"> Clique Aqui </ a href> </font color>
		</P>
	<body>
</html>
'''

html = MIMEText(link, "html")

msg.attach(html)

s = smtplib.SMTP('smtp.gmail.com',587) #Função para defenir a porta do servidor(google.com porta 587), outros dominios outras portas

s.starttls() #Função para inciar o envio

s.login(de,'20252520') #Função para colcoar login e senha de quem vai mandar o e-mail usando a váriavel criada na parte de cima

text = msg.as_string() #Função para fazer todo o e-mail virar texto

s.sendmail(de,para,text) #Anexando as função de quem envia,de quem recebe e o corpo do e-mail convertido em texto

s.quit() #fecha o e-mail

print('E-mail enviado !!')