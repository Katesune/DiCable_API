# -*- coding: utf-8 -*-

from src.blueprints.classes.snmp_answer import Answer
from src.blueprints.classes.oids import Oid
from flask import jsonify

from telnetlib import STATUS
from turtle import speed
from pysnmp.hlapi import *
from ipaddress import *
from datetime import datetime
import asyncio
import random
import json

oid = Oid()

settings_file = "settings.txt"
community = 'derfnutfo'  
channel = 161

link_state_oid = '1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.5' # link STATUS
port_speed_oid = '1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6' # port speed
enabled_port_oid = '1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4' # enabled port

port_diag_action_oid = '1.3.6.1.4.1.171.12.58.1.1.1.12' # port diag action

pair_1_status_oid = '1.3.6.1.4.1.171.12.58.1.1.1.4' # pair 1 status
pair_1_length_oid = '1.3.6.1.4.1.171.12.58.1.1.1.8' # pair 1 lenght

pair_2_status_oid = '1.3.6.1.4.1.171.12.58.1.1.1.5' # pair 2 status
pair_2_length_oid = '1.3.6.1.4.1.171.12.58.1.1.1.9' # pair 2 lenght

OIDmany = '1.3.6.1.2.1.1.9.1.2'
OIDtest = '1.3.6.1.2.1.2.1' 
OIDtestsec = '1.3.6.1.2.1.2.2.1.2'  
OIDset = '1.3.6.1.2.1.1.5'

class SwitchData(object):
    def __init__(self, ip):
        self.ip = ip
        self.results = {"ip": ip, "answers" :[]}

    async def snmp_get(self):

        await asyncio.sleep(random.randint(0, 2) * 0.001)
        for (errorIndication,errorStatus,errorIndex,varBinds) in getCmd(SnmpEngine(), 
            CommunityData('public'), UdpTransportTarget((self.ip, 161)), ContextData(), 
            ObjectType(ObjectIdentity(oid.sysname+'.0')), 
            lexicographicMode=False):

            answer = Answer()
            if answer.data_exists(errorIndication, errorStatus, errorIndex):
                answer.compile_answer(varBinds)

            answer.decode_web()

            self.results["answers"].append(answer)

        return self.results

    async def snmp_check_port(self, port):

        # await self.snmp_check_state(port)
        await self.snmp_set_diag(port)
        await self.snmp_get_diag_pairs(port)

        return self.results

    async def snmp_check_state(self, port):
        # Отправка запроса для получения инф. о статусе линка, скорости порта, доступности порта 

        await asyncio.sleep(random.randint(0, 2) * 0.001)
        for (errorIndication,errorStatus,errorIndex,varBinds) in getCmd(SnmpEngine(), 
            CommunityData('public'), UdpTransportTarget((self.ip, 161)), ContextData(), 
            ObjectType(ObjectIdentity(oid.link_state + '.'+ str(port) + '.1')),
            ObjectType(ObjectIdentity(oid.port_speed + '.'+ str(port) + '.1')),
            ObjectType(ObjectIdentity(oid.enabled_port + '.'+ str(port) + '.1')),
            lexicographicMode=False):

            answer = Answer()
            if answer.data_exists(errorIndication, errorStatus, errorIndex):
                answer.compile_answer(varBinds)

            answer.decode_web()

            self.results["answers"].append(answer)

        return self.results

    async def snmp_set_diag(self, port):
        # Запрос для запуска диагностики порта

        await asyncio.sleep(random.randint(0, 2) * 0.001)
        for (errorIndication,errorStatus,errorIndex,varBinds) in setCmd(SnmpEngine(), 
            CommunityData('private'), UdpTransportTarget((self.ip, 161)), ContextData(), 
            ObjectType(ObjectIdentity(oid.port_diag_action+'.'+str(port)), Integer(2)),
            lexicographicMode=False):

            answer = Answer()

            if answer.data_exists(errorIndication, errorStatus, errorIndex):
                answer.compile_answer(varBinds)

            answer.decode_web()

            self.results["answers"].append(answer)


    async def snmp_get_diag_pairs(self, port):
        # Запрос для получения диагностики 1 и 2 пары

        await asyncio.sleep(random.randint(0, 2) * 0.001)
        for (errorIndication,errorStatus,errorIndex,varBinds) in getCmd(SnmpEngine(), 
            CommunityData('public'), UdpTransportTarget((self.ip, 161)), ContextData(),
            ObjectType(ObjectIdentity(oid.pair1_status +'.'+str(port))),
            ObjectType(ObjectIdentity(oid.pair2_status +'.'+str(port))),
            ObjectType(ObjectIdentity(oid.pair1_length +'.'+str(port))),
            ObjectType(ObjectIdentity(oid.pair2_length +'.'+str(port))),
            lexicographicMode=False):

            answer = Answer()
             
            if answer.data_exists(errorIndication, errorStatus, errorIndex):
                answer.compile_answer(varBinds)

            answer.decode_web()

            self.results["answers"].append(answer)


    async def snmp_check_port_json(self, port):
        # Запрос для получения json данных по порту
        date = datetime.now().strftime("%d-%m-%y %H:%M")

        result = {"ip":self.ip, "port":port, "date":date, "port_state" :{}, "cable_diag_action":{}, "pairs_state":{}}

        # ans_r = await self.check_state_json(port)
        # result["port_state"] = ans_r.return_errors_json()
        # result["port_state"]["port_state_values"] = ans_r.final_answers

        ans_r = await self.set_diag_json(port)
        result["cable_diag_action"] = ans_r.return_errors_json()
        result["cable_diag_action"]["diag_action_values"] = ans_r.final_answers

        ans_r2 = await self.diag_pairs_json(port)
        result["pairs_state"] = ans_r2.return_errors_json()
        result["pairs_state"]["pairs_state_values"] = ans_r2.final_answers

        # Если нужны тестовые данные
        # result ["port_state"] = {"errorIndication":None, "errorStatus": None, "errorIndex": 0} 
        # result ["port_state"]["port_state_values"] = {"link_state":"link-pass", "port_speed":"nway-enabled", "enabled_port":"enabled"}

        # result ["cable_diag_action"] = {"errorIndication":None, "errorStatus": None, "errorIndex": 0} 
        # result["cable_diag_action"]["diag_action_values"] = {"port_diag_action":"processing"}

        # result ["pairs_state"] = {"errorIndication":None, "errorStatus": None, "errorIndex": 0} 
        # result["pairs_state"]["pairs_state_values"] = {"pair1_status":"ok","pair2_status":"ok", "pair1_length":"10", "pair2_length":"6" }

        return result

    async def check_state_json(self, port):
        await asyncio.sleep(random.randint(0, 2) * 0.001)
        for (errorIndication,errorStatus,errorIndex,varBinds) in getCmd(SnmpEngine(), 
            CommunityData('public'), UdpTransportTarget((self.ip, 161)), ContextData(),  
            ObjectType(ObjectIdentity(link_state_oid + '.'+ str(port) + '.1')),
            ObjectType(ObjectIdentity(port_speed_oid + '.'+ str(port) + '.1')),
            ObjectType(ObjectIdentity(enabled_port_oid + '.'+ str(port) + '.1')),
            lexicographicMode=False):

            answer = Answer()
            if answer.data_exists(errorIndication, errorStatus, errorIndex):
                answer.compile_answer(varBinds)

            answer.decode()

            return answer

    async def set_diag_json(self, port):
        await asyncio.sleep(random.randint(0, 2) * 0.001)
        for (errorIndication,errorStatus,errorIndex,varBinds) in setCmd(SnmpEngine(), 
            CommunityData('private'), UdpTransportTarget((self.ip, 161)), ContextData(), 
            ObjectType(ObjectIdentity(oid.port_diag_action+'.'+str(port)), Integer(2)),
            lexicographicMode=False):

            answer = Answer()
            if answer.data_exists(errorIndication, errorStatus, errorIndex):
                answer.compile_answer(varBinds)

            answer.decode()

            return answer

    async def diag_pairs_json(self, port):
        await asyncio.sleep(random.randint(0, 2) * 0.001)
        for (errorIndication,errorStatus,errorIndex,varBinds) in getCmd(SnmpEngine(), 
            CommunityData('public'), UdpTransportTarget((self.ip, 161)), ContextData(),
            ObjectType(ObjectIdentity(oid.pair1_status +'.'+str(port))),
            ObjectType(ObjectIdentity(oid.pair2_status +'.'+str(port))),
            ObjectType(ObjectIdentity(oid.pair1_length +'.'+str(port))),
            ObjectType(ObjectIdentity(oid.pair2_length +'.'+str(port))), 
            lexicographicMode=False):

            answer = Answer()
            if answer.data_exists(errorIndication, errorStatus, errorIndex):
                answer.compile_answer(varBinds)

            answer.decode()

            return answer

    
    # async def snmp_get_next_err(self):
    #     # Запрос на ошибки

    #     await asyncio.sleep(random.randint(0, 2) * 0.001)
    #     for (errorIndication,errorStatus,errorIndex,varBinds) in nextCmd(SnmpEngine(), 
    #         CommunityData('public'), UdpTransportTarget((self.ip, 161)), ContextData(), 
    #         ObjectType(ObjectIdentity(OIDtest)), lexicographicMode=False):
            
    #         answer = Answer()
    #         answer.save_errors(errorIndication, errorStatus, errorIndex)
    #         self.results["answers"].append(answer)

    #     return self.results

    # def getError(self):
    #     return self.results
    
    # def getRespose(self):
    #     return self.varBinds
