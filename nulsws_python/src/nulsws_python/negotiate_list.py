#!/usr/bin/python3.7
import json
from asyncio import sleep as a_sleep
from tornado.websocket import websocket_connect  # WebSocketClosedError

from nulsws_python.src.nulsws_python.prep_request import PrepRequest

class NegotiateList(object):

    async def negotiate_list(self, top_plus_mid_dict, m_indx, run_list, conf_ini_d, mtpe=3):
        pause_time = .7
        prepr_obj = PrepRequest()
        prep_request = prepr_obj.prep_request

        conn_m = eval(conf_ini_d.get("connect_method"))
        host_r = eval(conf_ini_d.get("host_req"))
        port_r = eval(conf_ini_d.get("port_req"))
        websock_url = ''.join([conn_m, host_r, ":", port_r])
        debug = 1

        if not debug:
            connection = await websocket_connect(websock_url)  # 1) CONNECT
            # await a_sleep(pause_time)
            while not connection:
                await a_sleep(pause_time)
            jd = json.dumps(top_plus_mid_dict)
            self.json_prt(top_plus_mid_dict, "* * * First message going out- NEGOTIATE: \n")

            await connection.write_message(jd)  # 2) WRITE
            # await a_sleep(self.s_time)
            negotiate_result = await connection.read_message()  # 3 READ
            await a_sleep(pause_time)
            self.json_prt(negotiate_result, "--------- ! ! ! NEGOTIATE response received: ")
        self.myprint("------end Negotiate----------------------------------------")

        for run_item in run_list:
            m_indx += 1

            if mtpe == 3:
                main_request = prep_request(m_indx, run_item, conf_ini_d)

                if debug:
                    json_reg = json.dumps(main_request)
                    self.json_prt(json_reg, " ")

                else:
                    await self.regular_request(connection, main_request)
