from flask import Blueprint, jsonify, request
from datetime import datetime

from src.blueprints.classes.snmp_class import SwitchData

json = Blueprint(name="json", import_name=__name__)

import asyncio

@json.route("", methods=['GET'])
# Точка для получения данных диагностики в формате JSON, 
# запросы от приложения приходят ну эту точку
async def getJsonDataIPPort():
    """
    ---
    get:
      parameters:
            - in: query
              name: id
              required: true
              schema:
                type: string
                example: 127.0.0.1
              allowReserved: true 
            - in: query
              name: port
              required: true
              schema:
                type: string
                example: 1
      title: Data acquisition functions
      description: Port diagnostic data
      responses:
        '200':
          description: Port diagnostic data
          content:
            application/json:
                example:
                    ip: 127.0.0.1
                    port: 1
                    date: 2020-04-22 16:32:00

                    port_state:
                        errorIndication : none
                        errorStatus : none
                        errorIndex : 0
                        port_state_values:
                            link_state : other
                            port_speed : nway-enabled
                            enabled_speed : enabled

                    cable_diag_action:
                        errorIndication : none
                        errorStatus : none
                        errorIndex : 0
                        diag_action_value:
                            action: processing

                    pairs_state:
                        errorIndication : none
                        errorStatus : none
                        errorIndex : 0
                        pairs_values: 
                            pair1_status: open
                            pair1_length: 5
                            pair2_status: open
                            pair2_length: 3

      tags:
          - Get Port Diagnostic Data
    """
    # Сверху - документация Swagger для точки

    ip = request.args.get('ip')
    port = request.args.get('port')

    tasks = [SwitchData(ip).snmp_check_port_json(port)] 
    results = await asyncio.gather(*tasks)
    print(results[0])

    return jsonify(results[0])
