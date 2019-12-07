#!/usr/bin/python3.7

m_dict: dict = {0: 'None', 1: 'NegotiateConnection',
                2: 'NegotiateConnectionResponse',
                3: 'Request', 4: 'Unsubscribe', 5: 'Response', 6: 'Ack',
                7: 'RegisterCompoundMethod', 8: 'UnregisterCompoundMethod'}


bigtest = {"MessageData": {
            "RequestAck": False,
            "RequestMethods": {
                "RegisterAPI":{
                    "Abbreviation":"NTS","ConnectionInformation": {
                        "IP":"127.0.0.1",
                        "Port":"7779"},
                    "Dependencies": {
                        "Role_ServiceManager":"0.1"},
                    "Methods":[],
                    "ModuleDomain":"Nulstar",
                    "ModuleName":"Tester",
                    "ModuleRoles":{
                        "Role_Tester[0.1]": ["0.1"]},
                        "ModuleVersion":"0.1.0"}},
                "ResponseMaxSize":"0",
                "SubscriptionEventCounter":"0",
                "SubscriptionPeriod":"0",
                "SubscriptionRange":"" },
             "MessageID":"1549960969557-3",
             "MessageType":"Request",
             "TimeZone":8,
             "Timestamp":1549960969664
             }

request_t_label = "RequestType"
subscrip_evnt_ct_label = "SubscriptionEventCounter"
subscrip_period_label = "SubscriptionPeriod"
sub_rg_label = "SubscriptionRange"
req_method_label = "RequestMethods"
get_bal_label = "GetBalance"
response_max_size_label = "ResponseMaxSize"
address_label = "Address"
get_height_label = "GetHeight"

