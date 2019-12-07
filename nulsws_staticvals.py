#!/usr/bin/python3.7

m_dict: dict = {0: 'None', 1: 'NegotiateConnection',
                2: 'NegotiateConnectionResponse',
                3: 'Request', 4: 'Unsubscribe', 5: 'Response', 6: 'Ack',
                7: 'RegisterCompoundMethod', 8: 'UnregisterCompoundMethod'}



mid = "1549960969557-4"

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
             "MessageID":mid,
             "MessageType":"Request",
             "TimeZone":8,
             "Timestamp":1549960969664
             }

compress_type_label = "CompressionAlgorithm"
compress_rate_label = "CompressionRate"
msg_data_label = "MessageData"
msg_id_label = "MessageID"
msg_type_label = "MessageType"
negotiate_conn_label = "NegotiateConnection"
negotiate_stat_label = 'NegotiationStatus'
negotiate_conn_resp_label = "NegotiateConnectionResponse"
proto_label = "ProtocolVersion"
tmstmp_label = "Timestamp"
tmzone_label = "TimeZone"
request_label = "Request"
request_internalid_label = "RequestInternalID"
request_date_label = "RequestDate"
request_time_label = "RequestTime"
json_seps = (',', ':')

request_t_label = "RequestType"
subscrip_evnt_ct_label = "SubscriptionEventCounter"
subscrip_period_label = "SubscriptionPeriod"
sub_rg_label = "SubscriptionRange"
req_method_label = "RequestMethods"
get_bal_label = "GetBalance"
response_max_size_label = "ResponseMaxSize"
address_label = "Address"
get_height_label = "GetHeight"



