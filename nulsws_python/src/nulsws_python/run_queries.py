#!/usr/bin/python3.7

import json
from asyncio import sleep as a_sleep

from tornado.websocket import websocket_connect  # WebSocketClosedError
import nulsws_python.src.nulsws_python.routines as routines
from nulsws_python.src.nulsws_python.request_prep import RequestPrep
from nulsws_python.src.nulsws_python.make_top import MakeTop
from nulsws_python.src.nulsws_python.regular_request import RegularRequest

from tornado.httpclient import AsyncHTTPClient


class RunQueries(object):

    async def run_queries_m(self, msg_type, run_list, conf_ini_d):
        debug = 0
        ws = True   # False is for http
        m_indx = 0
        connection = None
        pause_time = .7
        str_m1 = "* * * First message going out- NEGOTIATE: \n"
        str_m2 = "--------- ! ! ! NEGOTIATE response received: "
        str_m3 = "------end Negotiate----------------------------------------"

        rout_obj = routines.Routines()
        req_obj = RequestPrep()
        msg_type_negotiate = 1
        prep_request = req_obj.prep_request
        ws_port = conf_ini_d.get("ws_port")
        host_ip = conf_ini_d.get("host_ip")
        http1_port = conf_ini_d.get("http1_port")
        conn_m = conf_ini_d.get("connect_method")

        if int(conn_m) == 1:
            conn_method = 'ws'  # add wss later
            conn_port = ws_port
        else:
            conn_method = 'https'
            conn_port = http1_port

        conn_url = ''.join([conn_method, "://", host_ip, ":", str(conn_port)])

        if not debug:
            mt_obj = MakeTop()
            top_plus_mid_dict = mt_obj.make_top_m(msg_type_negotiate, m_indx, conf_ini_d)  # must be done

            print("Using this connection: ", conn_url)
            connection = await websocket_connect(conn_url)  # 1) CONNECT

            while not connection:
                await a_sleep(pause_time)
            top_plus_mid_dict_json = json.dumps(top_plus_mid_dict)
            rout_obj.print_json_request(top_plus_mid_dict, str_m1)

            await connection.write_message(top_plus_mid_dict_json)  # 2) WRITE
            # await a_sleep(self.s_time)
            negotiate_result = await connection.read_message()  # 3 READ
            await a_sleep(pause_time)
            rout_obj.print_json_request(negotiate_result, str_m2)
        rout_obj.myprint(str_m3)
        rr_obj = RegularRequest()

        for run_item in run_list:
            m_indx += 1

            if msg_type == 3:
                main_request = prep_request(msg_type, m_indx, run_item, conf_ini_d)

                if debug:
                    json_reg = json.dumps(main_request)
                    rout_obj.print_json_request(json_reg, " ")

                else:
                    await rr_obj.regular_request_m(connection, main_request)
