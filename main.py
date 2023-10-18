import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)

#intervalo = 2

#Entrando no LINKEDIN
url = 'https://www.linkedin.com/home?original_referer=https%3A%2F%2Fwww.linkedin.com%2Fnotifications%2F%3Ffilter%3Dall'
browser.get(url)
browser.maximize_window()
time.sleep(10)

#Logando
email_input = browser.find_element(By.ID,'session_key')
senha_input = browser.find_element(By.ID, 'session_password')
login_button = browser.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

email_input.send_keys('')
senha_input.send_keys('')
login_button.click()

browser.implicitly_wait(300)

#Pesquisando por "programador"
input_pesquisar = browser.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
input_pesquisar.send_keys('programador java')
input_pesquisar.send_keys(Keys.ENTER)
time.sleep(5)

#Clicando em pessoas
input_pessoas = browser.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul/li[3]/button')
input_pessoas.click()
time.sleep(3)

#Encontrando todos os botoções "Conectar" na página
botao_conectar = browser.find_elements(By.XPATH,"//button/span[text()='Conectar']")
#elementos_li = browser.find_elements(By.XPATH, "//li")

#Iterar sobre os botões e clicar em cada um
for botao in botao_conectar:
    try:
        botao.click()
        time.sleep(3)
    except Exception as e:
        pass
#Clicando em "Adicionar nota"
    add_nota = browser.find_element(By.XPATH,"//button/span[text()='Adicionar nota']")
    add_nota.click()
    time.sleep(2)
#Escrevendo a nota
    escrever_nota = browser.find_element(By.XPATH,'//*[@id="custom-message"]')
    escrever_nota.send_keys('Olá, se você recebeu essa mensagem é porque estou tentando um bot de automação :)')
    time.sleep(3)

#Clicando em "ENVIAR
    botao_enviar = browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]/span')
    botao_enviar.click()
    time.sleep(2)