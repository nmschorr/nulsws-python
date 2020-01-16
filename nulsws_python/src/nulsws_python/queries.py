#!/usr/bin/python3.7

import json
from asyncio import sleep as a_sleep

from tornado.websocket import websocket_connect  # WebSocketClosedError
import nulsws_python.src.nulsws_python.routines as routines
from nulsws_python.src.nulsws_python.request_prep import RequestPrep
from nulsws_python.src.nulsws_python.make_top import MakeTop
from nulsws_python.src.nulsws_python.regular_request import RegularRequest


class RunQueries(object):

    async def run_queries(self, run_list, conf_ini_d):
        m_indx = 0
        pause_time = .7
        rout_obj = routines.Routines()
        req_obj = RequestPrep()
        prep_request = req_obj.prep_request

        connection = None
        conn_m = conf_ini_d.get("connect_method")
        host_r = conf_ini_d.get("host_req")
        port_r = conf_ini_d.get("port_req")
        websock_url = ''.join([conn_m, "://", host_r, ":", str(port_r)])
        debug = 1
        str_m1 = "* * * First message going out- NEGOTIATE: \n"
        str_m2 = "--------- ! ! ! NEGOTIATE response received: "
        str_m3 = "------end Negotiate----------------------------------------"

        if not debug:
            mt_obj = MakeTop()
            top_plus_mid_dict = mt_obj.make_top(m_indx, conf_ini_d)  # must be done

            connection = await websocket_connect(websock_url)  # 1) CONNECT
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

            if True:
                # if mtpe == 3:
                main_request = prep_request(m_indx, run_item, conf_ini_d)

                if debug:
                    json_reg = json.dumps(main_request)
                    rout_obj.print_json_request(json_reg, " ")

                else:
                    await rr_obj.regular_request(connection, main_request)
