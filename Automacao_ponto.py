import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os
from datetime import datetime


url = 'https://dtfaceum.com/pentare'

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
cpf = os.getenv('CPF')



#service = Service("/usr/bin/chromedriver")
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)

driver.get(url)

wait = WebDriverWait(driver,10)

try:

    email_field = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="login_email"]')))
    password_field = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="login_password"]')))
    login_button = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div/div/div/form/div[3]/div/div/span/button/span[2]')



    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()

    

    pop_up_container = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.ant-modal-wrap"))
    )
    
    # Executa o comando JavaScript para remover o elemento.
    # 'arguments[0].remove()' é o comando para remover o elemento que foi passado.
    driver.execute_script("arguments[0].remove()", pop_up_container)
    #close_popup = wait.until(EC.element_to_be_clickable((By.XPATH,r'/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div')))
    #//span[contains(.,'FECHAR')]
    #/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span
    #/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span
    #/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span
    #/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span/span/svg
    #close_popup.click()

    cpf_field = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[2]/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/button')))
    cpf_field.click()
    cpf_field_input= wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[2]/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/input')))
    cpf_field_input.send_keys(cpf)

    #Falta apertar tecla enter ou clicar em bater
 
   
    confirmed_field= wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[2]/div[2]/main/div/div/div/div/div/div[2]/div/div[1]/div[2]/button[2]/span')))
    confirmed_field.click()

    #/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span/span/svg
    #/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span/span/svg/path[1]
    

except :

    # Configuração do e-mail
    email_send = os.getenv('EMAIL_SEND')
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    subject = 'Falha ao bater o ponto'

    data = datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
    body = f'Falha ao bater o ponto: {data}'

    #COnfig servidor
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    #Montar email
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server.sendmail(email_user, email_send, msg.as_string())

    server.quit()


