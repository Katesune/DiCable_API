from flask import jsonify
from src.blueprints.classes.oids import Oid

oid = Oid()
 # Класс ответа на SNMP запрос

class Answer(object):
    def __init__(self):
        self.errorIndication = None
        self.errorStatus = None
        self.errorIndex = 0
        self.varBinds = []
        self.names = []
        self.final_answers = {}

    def save_answer(self, errorIndication, errorStatus, errorIndex, varBinds):
        if errorIndication:
                self.errorIndication = errorIndication
        elif errorStatus:
                self.errorStatus = errorStatus
                self.errorIndex = errorIndex
        else:
            for name, val in varBinds:
                self.varBinds.append(val.prettyPrint())
                self.names.append(str(name))

    def data_exists(self, errorIndication, errorStatus, errorIndex):
        # Проверка на ошибки
        if errorIndication:
                self.errorIndication = errorIndication
        elif errorStatus:
                self.errorStatus = errorStatus
                self.errorIndex = errorIndex
        else:
            return True

    def compile_answer(self, varBinds):
        # Сохранение ответов и OID запроса
        for name, val in varBinds:
                self.varBinds.append(val.prettyPrint())
                n = str(name)
                self.names.append(n[0:len(n)-2])

    def decode_web(self):
        # Сохранение ответов в виде словаря с ключом(названием OID) и ответом
        for i in range(0, len(self.varBinds)):
            param = oid.oid_name[self.names[i]]

            if param in oid.decode_title:
                self.decode_title(param, i)
            else:
                self.decode_value(param, i)

    def decode_title(self, param, i):
        if param in oid.decode and self.varBinds[i] in oid.decode[param]:
            self.final_answers[oid.decode_title[param]] = oid.decode[param][self.varBinds[i]]
        else:
            self.final_answers[oid.decode_title[param]] = self.varBinds[i]

    def decode_value(self, param, i):
        if param in oid.decode and self.varBinds[i] in oid.decode[param]:
            self.final_answers[param] = oid.decode[param][self.varBinds[i]]
        else:
            self.final_answers[param] = self.varBinds[i]

    def decode(self):
        # Сохранение ответов в виде словаря с ключом(названием OID) и ответом
        for i in range(0, len(self.varBinds)):
            param = oid.oid_name[self.names[i]]
            self.decode_value(param, i)


    def return_errors_json(self):
        # Возврат ошибок для JSON ответа
        errors = {"errorIndication":self.errorIndication, 
            "errorStatus": self.errorStatus, 
            "errorIndex": self.errorIndex}
        return errors

    def save_errors(self, errorIndication, errorStatus, errorIndex):
        if errorIndication:
                self.errorIndication = errorIndication
        elif errorStatus:
                self.errorStatus = errorStatus
                self.errorIndex = errorIndex

    def get_array_result(self):
        return {"errorIndication":self.errorIndication, "errorStatus": self.errorStatus, "errorIndex": self.errorIndex, "varBinds": self.varBinds}

    # def compile_answer_table(self, varBinds, port):
    #     # Сохранение ответов и OID запроса с учетом порта
    #     for name, val in varBinds:
    #         if (str(port) == str(name[-1])):
    #                 self.varBinds.append(val.prettyPrint())
    #                 n = str(name)
    #                 self.names.append(n[0:len(n)-2])
    #                 # self.names.append(str(name)[0:len(name)-2])
