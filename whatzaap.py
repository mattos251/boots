from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

#definir contatos e grupos e msg a ser enviadas

contatos = ['istin'] #se quiser manda msg pra uma pessoa de algum grupo e so colocar dois parametros. grupo, nome.
mensagem = 'Pão Pão Pão Pão Pão Pão de queeeeijo'
boa_noite = 'boa noite!!'

#buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(5)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#buscar a barra de msg e manda a msg

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

#chamada das funções 

for contato in contatos: 
    buscar_contato(contato)
    i = 1
    while (i <= 200):
        i = i + 1
        print (enviar_mensagem(mensagem))


#campo de pesquisa _2_1wd "copyable-text selectable-text"

#campo de pesquisa privada "copyable-text selectable-text"
