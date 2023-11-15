import os
import glob
import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import openpyxl

# URL da página da ssp:
url = "https://www.ssp.sp.gov.br/transparenciassp/Consulta2023.aspx"

# Configurando o serviço do ChromeDriver:
chrome_driver_path = "/chromedriver.exe" # Aplicar o caminho onde está o chromedriver na máquina (exemplo: "F:/Users/xxx/AppData/Local/Microsoft/WindowsApps/chromedriver.exe")
service = Service(executable_path=chrome_driver_path)

# Criar o driver com as opções e o serviço
driver = webdriver.Chrome(service=service)

driver.get(url)  # Aqui ele acessa o URL.

# Define o nome do arquivo de backup com a data atual
data_atual = datetime.datetime.now()
nome_backup = f"SPDadosCriminais_2023_backup_{data_atual.strftime('%d-%m-%y')}.xlsx"

# Caminho para a pasta de downloads padrão do navegador
arquivo_baixado = "/SPDadosCriminais_2023.xlsx" # Aplicar o caminho onde está o arquivo baixado (padrao) na máquina (exemplo: "F:/Users/xxx/Downloads/SPDadosCriminais_2023.xlsx")

# Caminho para a pasta de backup
backup_folder = '/backup' # Aplicar o caminho onde está o arquivo backup na máquina (exemplo: "D:/projetos/bot_tcc_data_caption/backup")

# Caminho completo do arquivo de backup
backup_file_path = os.path.join(backup_folder, nome_backup)

try:
    # Localizar e clicar no botão usando XPath
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="frmMain"]/div[4]/div/div[2]/div[2]'))
    )
    button.click()

    # Aguardando um tempo para que o download seja concluído
    time.sleep(60)

    # Fecha o navegador
    driver.quit()

    # Verificando se o arquivo baixado existe
    if os.path.exists(arquivo_baixado):
        # Lê os dados do arquivo baixado
        dados_captados = pd.read_excel(arquivo_baixado)

        # Verifica se o arquivo de backup existe
        if os.path.exists(backup_file_path):
            # Lê os dados do arquivo de backup
            dados_backup = pd.read_excel(backup_file_path)

            # Verificando se há novos dados no arquivo baixado
            novos_dados = dados_captados[~dados_captados.isin(dados_backup)].dropna()

            # Se houver novos dados, atualizar o arquivo de backup e excluir o mais antigo
            if not novos_dados.empty:
                # Lista todos os arquivos de backup na pasta
                backup_files = glob.glob(os.path.join(backup_folder, "SPDadosCriminais_2023_backup_*.xlsx"))

                # Verifica se existem arquivos de backup antigos para excluir
                if len(backup_files) > 0:
                    # Identifica o arquivo de backup mais antigo
                    oldest_backup = min(backup_files, key=os.path.getctime)

                    # Exclui o arquivo de backup mais antigo
                    os.remove(oldest_backup)
                    print("Arquivo de backup mais antigo excluído:", oldest_backup)

                # Salva o novo backup com o nome formatado
                dados_captados.to_excel(backup_file_path, index=False)
                print("Novos dados encontrados e atualizados no arquivo de backup:", backup_file_path)

                # Exclui o arquivo baixado
                os.remove(arquivo_baixado)
                print("Arquivo baixado excluído:", arquivo_baixado)
            else:
                print("Nenhum novo dado foi encontrado no arquivo baixado.")
                # Exclui o arquivo baixado
                os.remove(arquivo_baixado)
                print("Arquivo baixado excluído:", arquivo_baixado)
        else:
            # Se o arquivo de backup não existe, criar
            dados_captados.to_excel(backup_file_path, index=False)
            print("Arquivo de backup criado:", backup_file_path)

            # Exclui o arquivo baixado
            os.remove(arquivo_baixado)
            print("Arquivo baixado excluído:", arquivo_baixado)
    else:
        print("O arquivo baixado não foi encontrado.")

except TimeoutException:
    print("Elemento não encontrado ou não clicável.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")