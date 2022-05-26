class Oid(object):
     # Класс для определения OID и их имен
    def __init__(self):

        self.link_state = '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.5' # link STATUS
        self.port_speed = '.1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6' # port speed
        self.enabled_port = '.1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4' # enabled port

        self.port_diag_action = '.1.3.6.1.4.1.171.12.58.1.1.1.12' # port diag action

        self.pair1_status = '.1.3.6.1.4.1.171.12.58.1.1.1.4' # pair 1 status
        self.pair1_length = '.1.3.6.1.4.1.171.12.58.1.1.1.8' # pair 1 lenght

        self.pair2_status = '.1.3.6.1.4.1.171.12.58.1.1.1.5' # pair 2 status
        self.pair2_length = '.1.3.6.1.4.1.171.12.58.1.1.1.9' # pair 2 lenght

        self.oid_name = {}

        self.oid_name['1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.5'] = 'link_state'
        self.oid_name['1.3.6.1.4.1.171.11.117.1.1.2.3.1.1.6'] = 'port_speed'
        self.oid_name['1.3.6.1.4.1.171.11.117.1.1.2.3.2.1.4'] = 'enabled_port'

        self.oid_name['1.3.6.1.4.1.171.12.58.1.1.1.12'] = 'port_diag_action'

        self.oid_name['1.3.6.1.4.1.171.12.58.1.1.1.4'] = 'pair1_status'
        self.oid_name['1.3.6.1.4.1.171.12.58.1.1.1.8'] = 'pair1_length'

        self.oid_name['1.3.6.1.4.1.171.12.58.1.1.1.5'] = 'pair2_status'
        self.oid_name['1.3.6.1.4.1.171.12.58.1.1.1.9'] = 'pair2_length'

        self.decode = {}

        self.decode['link_state'] = {"1" : "other", "2" : "link-pass", "3" : "link-fail"}

        self.decode['port_speed'] = {"1" : "other", "2" : "nway-enabled", 
            "3" : "nway-disabled-10Mbps-Half", "4" : "nway-disabled-10Mbps-Full", 
            "5" : "nway-disabled-100Mbps-Half", "6" : "nway-disabled-100Mbps-Full", 
            "7" : "nway-disabled-1Gigabps-Half", "8" : "nway-disabled-1Gigabps-Full",
            "9" : "nway-disabled-1Gigabps-Full-master", "10" : "nway-disabled-1Gigabps-Full-slave"}

        self.decode['enabled_port'] = {"1" : "other", "2" : "disabled", "3" : "enabled"}

        self.decode['port_diag_action'] = {"1" : "action", "2" : "processing", "3" : "other"}

        self.decode['pair1_status'] = {"0" : "ok", "1" : "open", "2" : "short", "3" : "open-short", "4" : "crosstalk",
    "5" : "unknown", "6" : "count", "7" : "no-cable", "8" : "other"}

        self.decode['pair2_status'] = {"0" : "ok", "1" : "open", "2" : "short", "3" : "open-short", "4" : "crosstalk",
    "5" : "unknown", "6" : "count", "7" : "no-cable", "8" : "other"}

        self.decode_title = {}

        self.decode_title['link_state'] = 'Link Status'
        self.decode_title['port_speed'] = 'Port Speed'
        self.decode_title['enabled_port'] = 'Enabled Port'

        self.decode_title['port_diag_action'] = 'Port Diagnostics'

        self.decode_title['pair1_status'] = 'Pair 1 Status'
        self.decode_title['pair2_status'] = 'Pair 2 Status'
        self.decode_title['pair1_length'] = 'Pair 1 Length'
        self.decode_title['pair2_length'] = 'Pair 2 Length'

        # Для тестирования
        self.sysname = '.1.3.6.1.2.1.1.5'
        self.test = '.1.3.6.1.2.1.2.2.1.7'
        self.test_int = '.1.3.6.1.2.1.4.1' 
        self.testsec = '.1.3.6.1.2.1.2.2.1.2'  
        self.set = '.1.3.6.1.2.1.1.5'

        self.oid_name['1.3.6.1.2.1.2.2.1.7'] = 'test'
        self.oid_name['1.3.6.1.2.1.1.5'] = 'sysname'

        self.decode['test'] = {"1" : "other", "2" : "link-pass", "3" : "link-fail"}

        self.decode_title['test'] = 'Link Status'
        self.decode_title['sysname'] = 'System Name'
