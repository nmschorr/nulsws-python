#!/usr/bin/python3.7

# nulsws_msgtype_register.py

'''
by Nancy Schorr for Nuls, December 2, 2019
'''


proto_ver = "0.1"

# this can be a list once other versions are supported
compatible_proto_versions = [proto_ver]

# ------ msg_type --------------------
#  Message Type - string
msg_type = "r"
from time import time, timezone
t_stamp = int(time() * 1000)  # change float to int
tzone = int(timezone / 3600)  # change float to int to str
msg_index = 1
m_id = str(t_stamp) + "-" + str(msg_index)
# ----- host ----------------------------------------------

ip = "127.0.0.1"
connect_method_r= "ws://"
port_r = "7775"
websock_url: str = ''.join([connect_method_r, ip, ":", port_r])
compress_type= "zlib"
mod_v = "0.1.0"
compress_rate_r = 0
subscriptionRange = 0
request_int = 1
sub_event_ct = 0
sub_period_int = 1
sub_range = ""
res_max_size = 0
zero = "0"
address_val = "NULSd6Hggvrij3MPW9QTHJGBv7uiyMKw41i7t"  ##
msgtype= "Request"
q1= "Query information about CPU"
q2= "Query information about RAM memory"
role_stats_mgr = "0.1"
sub_rng = ""
get_ram_info = "GetRAMInfo"
get_cpu_info = "GetCPUInfo"
# -----------------------------------------------------------------------------------

nulsws_register = {
    "MessageData": {
        "RequestAck": zero,
        "RequestMethods": {
            "RegisterAPI": {
                "Abbreviation": "NSTM",
                "ConnectionInformation": {
                    "IP": ip,
                    "Port": port_r
                },
                "Dependencies": {},
                "Methods": [
                    {
                        "MethodDescription": q1,
                        "MethodMinEvent": zero,
                        "MethodMinPeriod": zero,
                        "MethodName": get_cpu_info,
                        "MethodScope": "admin",
                        "Parameters": [
                            {
                                "ParameterName": "lMaxCPUs",
                                "ParameterType": "int"
                            }
                        ]
                    },
                    {
                        "MethodDescription": q2,
                        "MethodMinEvent": zero,
                        "MethodMinPeriod": zero,
                        "MethodName": get_ram_info,
                        "MethodScope": "admin",
                        "Parameters": []
                    }
                ],
                "ModuleDomain": "Nulstar",
                "ModuleName": "StatsManager",
                "ModuleRoles": {
                    "Role_StatsManager": [
                        role_stats_mgr
                    ]
                },
                "ModuleVersion": mod_v
            }
        },
        "ResponseMaxSize": zero,
        "SubscriptionEventCounter": zero,
        "SubscriptionPeriod": zero,
        "SubscriptionRange": sub_rng
    },
    "MessageID": m_id,
    "MessageType": msgtype,
    "TimeZone": tzone,
    "Timestamp": t_stamp
}
