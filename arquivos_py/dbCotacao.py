import psycopg2
from selenium.webdriver.chrome.options import Options
from selenium import webdriver as wd
from datetime import datetime

try:
    # Configurando opções do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = wd.Chrome(options=chrome_options)

    # Acessando a página com as cotações
    driver.get("https://www.google.com/search?q=pre%C3%A7o+dolar")

    # Acessando o elemento (dólar) da página
    dolar = driver.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')

    # Obtendo a data e hora atual
    data_atual_str = datetime.today().strftime('%Y-%m-%d')
    hora_atual_str = datetime.today().strftime('%H:%M:%S')
    preco_dolar = float(dolar.get_attribute("data-value"))

    print(f'Data: {data_atual_str} Hora: {hora_atual_str}\nPreço: ${preco_dolar}')

    # Convertendo as strings para tipos de dados adequados
    data_atual = datetime.strptime(data_atual_str, '%Y-%m-%d').date()
    hora_atual = datetime.strptime(hora_atual_str, '%H:%M:%S').time()

    # Conectando ao PostgreSQL
    conn = psycopg2.connect(
        dbname="dbcotacao",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Inserindo dados no PostgreSQL
    cursor.execute('''
    CALL inserir_cotacao_dolar (%s, %s, %s)
    ''', (data_atual, hora_atual, preco_dolar))

    # Confirmando a transação
    conn.commit()

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fechando a conexão
    if cursor:
        cursor.close()
    if conn:
        conn.close()

    # Fechando o navegador
    driver.quit()