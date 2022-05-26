from pysnmp.hlapi import *
from ipaddress import *
from datetime import datetime
from flask import Blueprint, jsonify, request, make_response, render_template, current_app
from flask_login import login_required, current_user

from src.blueprints.classes.snmp_class import SwitchData
from src.blueprints.classes.themes import Themes

data = Blueprint(name="data", import_name=__name__)

import asyncio

filename = 'ip_data\checked_ip_list.txt'
theme = Themes()

def chek_adress(ip):
    # Проверка IP-адреса на валидность
    try:
        ip_address(ip)
    except ValueError:
        return False
    else:
        return True
    
def get_ips():
    # Сбор списка IP-адресов
    with open(filename) as file:
        ip_list = [row.strip() for row in file]
    for ip in ip_list:
        if not chek_adress(ip):
            ip_list.remove(ip)
    return ip_list

@data.route("/data",  methods=['GET'])
# Маршрут для главной страницы с данными коммутаторов
async def getAllData():

    if not current_user.is_authenticated:
        return current_app.login_manager.unauthorized()

    ip_list = get_ips() # Получение списка коммутаторов
    tasks = [SwitchData(ip_list[i]).snmp_get() for i in range(0, len(ip_list))] # Запросы к коммутаторам по SNMP
                                                                                # (рекомендуемая замена - запрос к БД MS SQL)
    results = await asyncio.gather(*tasks) # Получение результатов запроса по SNMP
    date = datetime.now().strftime("%d-%m-%y %H:%M") # Текущая дата и время
 
    return render_template('data.php', result=results, date = date, theme=theme)

@data.route("/data/<ip>")
# Маршрут для страницы с портами определенного коммутатора (коммутатор определяется по IP-адресу)
async def getDataIP(ip):
    if not current_user.is_authenticated:
        return current_app.login_manager.unauthorized()
    # Отображаются кнопки с портами коммутатора, по нажатию переход на страницу с результатами диагностики

    return render_template('ip_data.php', ports=26, ip=ip, theme=theme)

@data.route("/data/<ip>/<port>")
# Маршрут для страницы с результатами диагностики по IP-адресу(ip) коммутатора и порту(port)
async def getDataIPPort(ip, port):
    if not current_user.is_authenticated:
        return current_app.login_manager.unauthorized()

    tasks = [SwitchData(ip).snmp_check_port(port)] # Запрос к коммутатору по IP-адресу через SNMP
    results = await asyncio.gather(*tasks)
    date = datetime.now().strftime("%d-%m-%y %H:%M")

    return render_template('port_data.php', result=results, date = date, ip=ip, port=port, theme=theme)

@data.route("/theme")
# Кнопка смены темы
def change_theme():
    theme.change_mode()
    return '<script>document.location.href = document.referrer</script>'

# @data.route("/errors")
# Маршрут для ошибок с коммутаторов
# async def getErrors():
#     if not current_user.is_authenticated:
#         return current_app.login_manager.unauthorized()

#     ip_list = get_ips()
#     tasks = [SwitchData(ip_list[i]).snmp_get_next_err() for i in range(0, len(ip_list))]
#     results = await asyncio.gather(*tasks)
#     date = datetime.now().strftime("%d-%m-%y %H:%M")

#     return render_template('errors.php', title='Test', result=results, date = date)

# @data.route("/errors/<ip>")
# Маршрут для ошибок с коммутатора по IP
# async def getErrrsApi(ip):
#     if not current_user.is_authenticated:
#         return current_app.login_manager.unauthorized()

#     tasks = [SwitchData(ip).snmp_get_next_err()]
#     results = await asyncio.gather(*tasks)
#     date = datetime.now().strftime("%d-%m-%y %H:%M")

#     return render_template('ip_errors.php', title='Test', result=results, date = date, ip=ip)