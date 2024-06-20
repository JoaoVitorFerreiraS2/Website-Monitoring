import tkinter.messagebox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

#Se for preciso uma e-mail e senha
usuario = 'seuemail@meuemail.com'
senha = 'sua senha'
texto_procurado = "<Coloque um texto do que você deseja buscar na página>"

#Status <deixe comentado se não tiver>
texto_status = "<Se tiver um status, coloque aqui o nome do status que você procura>"

navegador.get("coloque seu site")

#Colocando a o usuário e senha
navegador.find_element('xpath', '//*[@id="email"]').send_keys(usuario)
navegador.find_element('xpath', '//*[@id="password"]').send_keys(senha)
time.sleep(1)

navegador.find_element('xpath', '<Coloque o Xpath> de clique de entrada').click()
time.sleep(2)
navegador.find_element('xpath', '<O mesmo propósito>').click()

texto_encontrado = False  # Variável para controlar se o texto foi encontrado

try:
    while True:

        elemento = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '<Localize o bloco ou div que vai ter que ser monitorado>'))
        )
        elemento = navegador.find_element(By.XPATH, 'Coloque o mesmo que o de cima')
        html_div = elemento.get_attribute('innerHTML')
        
        # Variável para verificar se o texto esperado foi encontrado em algum lugar

        # Aqui é preciso verificar, pois precisa se adaptar ao seu código, no meu por exemplo eu buscava tr, ou seja, ele buscaria em todas as <tr> o que eu quero
        elementos_tr = navegador.find_elements(By.XPATH, '<Exemplo: /html/body/div[1]/div/div/div/section[2]/div/div[2]/div/div/table/tbody/tr>')

        for tr_elemento in elementos_tr:
            #Adapte ao seu sistema
            td_texto = tr_elemento.find_element(By.XPATH, './td[2]').text
            if texto_procurado in td_texto:
                
                #Aqui é referente ao status, adapte da forma que achar melhor
                print(f'Encontrei o "{texto_procurado}"')
                html_tr = tr_elemento.get_attribute('innerHTML')
                if texto_status in html_tr:
                    print(f'O {texto_procurado} está {texto_status}')
                    message = tkinter.messagebox.showwarning(title=f'!!!{texto_procurado}!!!', message=f'{texto_procurado} está {texto_status}', icon='warning')
                    message.attributes('-topmost', True)
                    message.withdraw()
                break  # Sai do loop assim que encontrar um resultado válido
            

        time.sleep(10)  # Intervalo de verificação em segundos

except Exception as e:
    print(f"Erro durante o processo: {e}")

finally:
    navegador.quit()
