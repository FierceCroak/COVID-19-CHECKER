import requests 
import json
import telepot
import time
from time import sleep
estado = input("DIGITE A SIGLA DO ESTADO -> ")

api = f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{estado}'

api2 = requests.get(api)
api3 = api2.json()

id = api3['uid']
uf = api3['uf']
cidade = api3['state']
casos = api3['cases']
mortes = api3['deaths']
suspeitos = api3['suspects']
recuperados = api3['refuses']

print(f"DADOS SOBRE COVID-19 DO ESTADO {cidade}.")
time.sleep(3)
print(f" \n ID = {id} \n UF = {uf} \n ESTADO = {cidade} \n CASOS = {casos} \n MORTES = {mortes} \n SUSPEITOS = {suspeitos} \n RECUPERADOS = {recuperados} \n \n feito pelo 𝙁𝙞𝙚𝙧𝙘𝙚𝘾𝙧𝙤𝙖𝙠 ;-; ")
