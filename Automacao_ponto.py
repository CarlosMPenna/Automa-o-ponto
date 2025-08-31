import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

email_field = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="login_email"]')))
password_field = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="login_password"]')))
login_button = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div/div/div/form/div[3]/div/div/span/button/span[2]')



email_field.send_keys(email)
password_field.send_keys(password)
login_button.click()
close_popup = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span')))
#/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span
#/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span/span/svg
close_popup.click()

cpf_field = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div[2]/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/button')))
cpf_field.send_keys(cpf)





