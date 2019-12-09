#!/usr/bin/python3.7

# nulsws_msgtype_register.py
# must register before other stuff

'''
by Nancy Schorr for Nuls, December 2, 2019
'''
import json
from nulsws_library import prep_TOP_SECTION

# this can be a list once other versions are supported


# ------ msg_type --------------------
#  Message Type - string

# ----- host ----------------------------------------------
proto_ver = "0.1"
compatible_proto_versions = [proto_ver]
ip = "127.0.0.1"
special_port = "7775"
compress_type = "zlib"
mod_v = "0.1.0"
compress_rate_r = 0
subscriptionRange = 0
request_int = 1
sub_event_ct = 0
sub_period_int = 1
sub_range = ""
res_max_size = 0
zero = "0"

msgtype= "Request"
q1= "Query information about CPU"
q2= "Query information about RAM memory"
role_stats_mgr = "0.1"
sub_rng = ""
get_ram_info = "GetRAMInfo"
get_cpu_info = "GetCPUInfo"
# -----------------------------------------------------------------------------------

def make_nulsws_REGISTER_method(mindex):
    top_sec = prep_TOP_SECTION(3, mindex)
    #
    # jdd = {
    #     "MessageData": {
    #         "RequestAck": zero,
    #         "RequestMethods": {
    #             "RegisterAPI": {
    #                 "GetBalance": 0}
    #             }}}

    nulsws_register_j = {
        "MessageData": {
            "RequestAck": zero,
            "RequestMethods": {
                "RegisterAPI": {
                    "Abbreviation": "NSTM",
                    "ConnectionInformation": {
                        "IP": ip,
                        "Port": special_port
                    },
                    "Dependencies": {},
                    "Methods": [
                        {
                            "MethodDescription": q1,   # first method
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
                            "MethodDescription": q2,   #second method
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
        } }

    top_sec.update(nulsws_register_j)
    nulsws_register = json.dumps(top_sec)

    return nulsws_register


